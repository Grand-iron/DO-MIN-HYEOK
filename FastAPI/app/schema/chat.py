from pydantic import BaseModel, Field
from typing import Optional

class ChatInput(BaseModel):
    message: str
    temperature: Optional[float] = Field(None, ge=0, le=2)
    top_p: Optional[float] = Field(None, ge=0, le=1)

class ChatOutput(BaseModel):
    reply: str
