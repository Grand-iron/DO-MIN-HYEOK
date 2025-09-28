from pathlib import Path
from dotenv import load_dotenv
import os

# 프로젝트 루트(FastAPI/.env)
ROOT = Path(__file__).resolve().parent.parent.parent
load_dotenv(ROOT / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash-lite")
JUDGE_MODEL = os.getenv("JUDGE_MODEL", "gemini-2.5-flash-lite")
DEFAULT_TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
DEFAULT_TOP_P = float(os.getenv("TOP_P", "0.95"))
MAX_OUTPUT_TOKENS = int(os.getenv("MAX_OUTPUT_TOKENS", "256"))
