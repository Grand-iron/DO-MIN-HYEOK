from fastapi import APIRouter, HTTPException
from app.schema.chat import ChatInput, ChatOutput
from app.core.prompts import WORLD_PROMPT, CHARACTER_PROMPTS, build_prompt
from app.service.llm import generate_text, LLMError

router = APIRouter(tags=["chat"])

@router.post("/chat/{character_id}", response_model=ChatOutput)
async def chat_with_character(character_id: str, input: ChatInput):
    character_prompt = CHARACTER_PROMPTS.get(character_id.lower())
    if not character_prompt:
        raise HTTPException(status_code=404, detail=f"Unknown character: {character_id}")
    prompt = build_prompt(WORLD_PROMPT, character_prompt, None, input.message)
    try:
        reply = generate_text(prompt, temperature=input.temperature, top_p=input.top_p)
        return ChatOutput(reply=reply)
    except LLMError as e:
        raise HTTPException(status_code=500, detail=str(e))