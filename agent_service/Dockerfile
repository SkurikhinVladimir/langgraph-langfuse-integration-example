FROM python:3.12-slim
WORKDIR /app
COPY agent_service /app/agent_service
COPY agent_service/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONPATH=/app
CMD ["langgraph", "dev", "--host", "0.0.0.0", "--port", "8000", "--config", "agent_service/langgraph.json"]
