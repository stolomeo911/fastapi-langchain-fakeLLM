from fastapi import APIRouter, HTTPException, Response
from fastapi_app.api.models import Message, ModelResponse
from langchain_core.prompts import ChatPromptTemplate
from fastapi_app.llm.offline_llm import llm
from langchain.memory import ConversationBufferMemory
import json

router = APIRouter()

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/chat")
async def chat(message: Message) -> ModelResponse:
    try:
        # Create the chat prompt template
        prompt_template = ChatPromptTemplate.from_template("Answer to the user's question: {q}")

        # Retrieve the chat history from the message object
        chat_history = message.conversation_history

        # Store the conversation history in memory
        memory.save_context({"input": chat_history}, {"output": message.user_input})

        print(memory.chat_memory)
        # Generate the model's response
        chain = prompt_template | llm
        response = chain.invoke({"q": message.user_input})

        # Parse the response to update the sources
        response_data = json.loads(response)
        if "sources" in response_data:
            response_data["sources"] = [f"http://{source}" if not source.startswith("http") else source for source in
                                        response_data["sources"]]

        # Convert the updated response back to a JSON string
        updated_response = json.dumps(response_data)

        model_response = ModelResponse(user_input=message.user_input, response=updated_response)
        return model_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# You can use this debug method to check how the (raw) output of the model looks like
@router.get("/debug")
async def debug():
    prompt = ChatPromptTemplate.from_template("Answer to the user's question: {q}")
    chain = prompt | llm
    return chain.invoke({"q": "dummy question"})