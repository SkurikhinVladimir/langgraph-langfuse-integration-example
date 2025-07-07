from fastapi import FastAPI
from pydantic import BaseModel, Field
from langgraph.pregel.remote import RemoteGraph
from starlette.responses import StreamingResponse
from agent_client.config import settings
import json

app = FastAPI()

remote_graph = RemoteGraph(settings.graph_name, url=settings.graph_url)


class ChatRequest(BaseModel):
    messages: list[dict] = Field(
        ...,
        json_schema_extra={
            "example": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Привет! Какая погода в Лос-Анджелесе?"},
            ]
        },
    )


@app.post("/chat/sse")
async def chat_sse(request: ChatRequest):
    async def event_generator():
        async for chunk in remote_graph.astream({"messages": request.messages}):
            yield f"data: {json.dumps(chunk, ensure_ascii=False)}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")


# Локальный запуск
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("client:app", host="0.0.0.0", port=8000)
