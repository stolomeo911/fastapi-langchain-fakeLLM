from pydantic import BaseModel


class Message(BaseModel):
    user_input: str
    session_id: str
    #conversation_history: str


# Define the Response model
class ModelResponse(BaseModel):
    user_input: str
    response: str