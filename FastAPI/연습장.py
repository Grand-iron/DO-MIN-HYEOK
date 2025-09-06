from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()

class ChatInput(BaseModel):
    message: str

# 캐릭터별 설정 프롬프트
CHARACTER_PROMPTS = {
    "lee": "너는 '이이름'이라는 캐릭터야. 똑똑하고 날카로운 인물.",
    "jina": "너는 '지나'라는 캐릭터야. 겁이 많고 부끄러움이 많아.",
}

# 공통 세계관 설정
WORLD_PROMPT = "세계는 2040년, 3차대전 이후의 잿더미가 되었고, 당신은 검문소의 시민이다."

@app.post("/chat/{character_id}")
async def chat_with_character(character_id: str, input: ChatInput):
    character_prompt = CHARACTER_PROMPTS.get(character_id.lower(), "")
    prompt = f"{WORLD_PROMPT}\n\n{character_prompt}"
    
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": input.message}
    ]

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:11434/v1/chat/completions",
            json={
                "model": "openchat",
                "messages": messages
            }
        )
    
    reply = response.json()["choices"][0]["message"]["content"]
    return {"reply": reply}
