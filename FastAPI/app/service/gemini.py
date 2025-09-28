from app.core.config import (
    GEMINI_API_KEY, GEN_MODEL, JUDGE_MODEL,
    DEFAULT_TEMPERATURE, DEFAULT_TOP_P, MAX_OUTPUT_TOKENS
)
import google.generativeai as genai

genai.configure(api_key=GEMINI_API_KEY)

def _params():
    return {
        "temperature": DEFAULT_TEMPERATURE,
        "top_p": DEFAULT_TOP_P,
        "max_output_tokens": MAX_OUTPUT_TOKENS,
    }

def gen_text(prompt: str) -> str:
    model = genai.GenerativeModel(GEN_MODEL)
    resp = model.generate_content(prompt, generation_config=_params())
    return resp.text or ""

def judge_text(judge_prompt: str) -> str:
    model = genai.GenerativeModel(JUDGE_MODEL)
    resp = model.generate_content(judge_prompt, generation_config=_params())
    return resp.text or ""
