import google.generativeai as genai
from app.core import config as cfg

if cfg.GEMINI_API_KEY:
    genai.configure(api_key=cfg.GEMINI_API_KEY)

class LLMError(Exception):
    pass

def generate_text(prompt: str, *, temperature: float | None = None, top_p: float | None = None) -> str:
    try:
        model = genai.GenerativeModel(
            cfg.MODEL_NAME,
            generation_config={
                "temperature": temperature if temperature is not None else cfg.DEFAULT_TEMPERATURE,
                "top_p": top_p if top_p is not None else cfg.DEFAULT_TOP_P,
                "max_output_tokens": cfg.MAX_OUTPUT_TOKENS,
            },
        )
        resp = model.generate_content(prompt)
        text = (resp.text or "").strip()
        # 세계관 규칙 상 180자 제한
        return text[:180]
    except Exception as e:
        raise LLMError(str(e))
