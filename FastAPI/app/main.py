from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router.chat import router as chat_router

app = FastAPI(title="Nimbus LLM API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Godot에서 호출할 거면 편하게 와일드카드
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(chat_router, prefix="/api")
