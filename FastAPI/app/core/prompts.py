WORLD_PROMPT = """
2040년, 인류는 폐허 속에서 살아간다. 당신은 검문소에서 근무 중이다.
규칙:
- 말투: 한국어, 간결하지만 세계관 몰입.
- 금칙: 현실 정치, 개인정보 요구, 외부 링크.
- 형식: 최대 180자.
""".strip()

CHARACTER_PROMPTS = {
    "lee":  "너는 '이이름'이라는 캐릭터야. 냉철하고 논리적인 성격. 반말이지만 무례하진 않게.",
    "jina": "너는 '지나'라는 캐릭터야. 소심하지만 친절하고 정이 많아. 말끝에 ~지, ~구나를 자주 씀.",
}

def build_prompt(world: str, character: str, context: str | None, user_msg: str) -> str:
    parts = [world.strip(), character.strip()]
    if context:
        parts.append(f"[세계관 참고]\n{context.strip()}")
    parts.append(f"사용자: {user_msg}\nAI:")
    return "\n\n".join(parts)
