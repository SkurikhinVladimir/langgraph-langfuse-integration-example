# 🚀 LangGraph + Langfuse Demo

Демонстрационный проект локальной интеграции **LangGraph**, **Langfuse** и кастомных MCP-сервисов.

---

## ⚡ Быстрый старт

### 1. Запуск Langfuse и зависимостей

Заполните файл `.env.demo` необходимыми переменными окружения, затем выполните:

```bash
docker-compose -f docker-compose.langfuse.yml --env-file .env.demo up -d
```

### 2. Запуск приложения (агент, клиент, weather)

```bash
docker-compose --env-file .env.demo up  --build -d
```

### 3. Открыть интерфейс Langfuse

- [🌐 Web интерфейс Langfuse](http://localhost:3000)
- [⚙️ SSE клиент (FastAPI)](http://localhost:8001/docs#/)
- [🔁 Документация LangGraph API](http://localhost:8000/docs#/)
- [🧠 LangSmith (через LangGraph endpoint)](https://smith.langchain.com/studio/?baseUrl=http://localhost:8000)

---

## Полезные ссылки

- [📘 Документация Langfuse](https://langfuse.com/docs)
- [📘 Документация LangGraph](https://langchain-ai.github.io/langgraph/)
