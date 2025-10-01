import json, re
from typing import List, Tuple
from app.schemas.eval import Rubric, EvalItem, EvalResult, JudgeScore
from app.services.gemini import gen_text, judge_text

JUDGE_SCHEMA = """
너는 게임 상황극 대화의 심판이다.
아래 루브릭에 따라 각 항목 0~4점(정수)으로 채점하고, 한 문장 이유를 제공한다.
출력은 반드시 JSON으로만 하라. 추가 텍스트 금지.

JSON 스키마:
{
  "per_dim": {"immersion": 0-4, "consistency": 0-4, "impact": 0-4, ...},
  "reason": "한 줄 이유",
  "hard_rule_violations": ["위반한 규칙 문자열 목록"]
}
"""

def build_generation_prompt(system_prompt: str, item: EvalItem) -> str:
    parts = []
    if system_prompt:
        parts.append(f"[System]\n{system_prompt}")
    if item.context:
        parts.append(f"[Context]\n{item.context}")
    parts.append(f"[User]\n{item.input}")
    return "\n\n".join(parts)

def build_judge_prompt(rubric: Rubric, item: EvalItem, output_text: str) -> str:
    rubric_json = json.dumps(rubric.dict(), ensure_ascii=False)
    expected = json.dumps(item.expected_keywords or [], ensure_ascii=False)
    return f"""{JUDGE_SCHEMA}

[Rubric]
{rubric_json}

[Hard-rule reference: expected_keywords]
모델 출력에 아래 키워드가 '적절히' 포함/반영되었는지 참고용으로 확인한다(강제 포함 아님).
{expected}

[Candidate Output]
{output_text}
"""

def safe_json_extract(s: str):
    # 출력에 불필요한 문장이 섞였을 때 대비
    match = re.search(r"\{.*\}\s*$", s.strip(), re.S)
    if not match:
        return None
    try:
        return json.loads(match.group(0))
    except Exception:
        return None

def weighted_total(per_dim: dict, rubric: Rubric) -> float:
    weights = {d.name: d.weight for d in rubric.dimensions}
    total_w = sum(weights.values()) or 1.0
    score = 0.0
    for name, val in per_dim.items():
        w = weights.get(name, 0.0)
        score += (val * w)
    return score / total_w

def evaluate_items(items: List[EvalItem], rubric: Rubric, system_prompt: str, max_items: int = None) -> Tuple[List[EvalResult], float]:
    use_items = items[:max_items] if max_items else items
    results: List[EvalResult] = []

    for it in use_items:
        # 1) 생성
        gen_prompt = build_generation_prompt(system_prompt, it)
        out = gen_text(gen_prompt)

        # 2) 심판
        jp = build_judge_prompt(rubric, it, out)
        j_raw = judge_text(jp)
        j = safe_json_extract(j_raw) or {"per_dim": {}, "reason": "parse_failed", "hard_rule_violations": []}

        # 3) 총점
        total = weighted_total(j.get("per_dim", {}), rubric)
        result = EvalResult(
            input=it.input,
            output=out,
            score=JudgeScore(
                per_dim=j.get("per_dim", {}),
                reason=j.get("reason", ""),
                hard_rule_violations=j.get("hard_rule_violations", []),
                weighted_total=total
            )
        )
        results.append(result)

    avg = sum(r.score.weighted_total for r in results) / max(1, len(results))
    return results, avg
