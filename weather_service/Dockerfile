FROM python:3.12-slim
WORKDIR /app
COPY weather_service /app/weather_service
COPY weather_service/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt || true
ENV FASTMCP_HOST=0.0.0.0
ENV FASTMCP_PORT=8000
ENV PYTHONPATH=/app
CMD ["python", "-m", "weather_service.server"]
