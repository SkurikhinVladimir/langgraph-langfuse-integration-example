import asyncio
from typing import Optional
from langchain_openai import ChatOpenAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langfuse.callback import CallbackHandler
from agent_service.config import settings


def init_langfuse() -> Optional[CallbackHandler]:
    """Инициализация Langfuse callback handler из переменных окружения"""
    handler = CallbackHandler(
        host=settings.langfuse_url,
        public_key=settings.langfuse_init_project_public_key,
        secret_key=settings.langfuse_init_project_secret_key,
    )
    return handler


def get_llm() -> ChatOpenAI:
    """Инициализация LLM из переменных окружения или конфиг-файла."""
    return ChatOpenAI(
        base_url=settings.openai_base_url,
        api_key=settings.openai_api_key,
        model=settings.openai_model,
    )


def get_mcp_client() -> MultiServerMCPClient:
    """Инициализация MCP клиента из переменных окружения или конфиг-файла."""
    return MultiServerMCPClient(
        {
            "weather": {
                "transport": "streamable_http",
                "url": settings.mcp_url,
            }
        }
    )


async def get_agent():
    """Создание LangGraph агента с тулзами MCP."""
    langfuse_handler = init_langfuse()
    config = {"callbacks": [langfuse_handler]} if langfuse_handler else {}
    llm = get_llm()
    client = get_mcp_client()
    tools = await client.get_tools()
    return create_react_agent(
        model=llm,
        tools=tools,
        prompt="Ты полезный ассистент. Отвечай на вопросы пользователя.",
    ).with_config(config)


# Для теста: запуск агента и вывод сообщения об инициализации
if __name__ == "__main__":

    async def main():
        agent = await get_agent()
        print("Агент успешно инициализирован:", agent)

    asyncio.run(main())
