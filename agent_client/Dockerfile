FROM python:3.11-slim
WORKDIR /app
COPY agent_client /app/agent_client
COPY agent_client/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENV PYTHONPATH=/app
CMD ["uvicorn", "agent_client.client:app", "--host", "0.0.0.0", "--port", "8000"]
