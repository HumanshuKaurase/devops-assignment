import os
from celery import Celery

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")

broker_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
result_backend = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"

celery_app = Celery(
    "worker",
    broker=broker_url,
    backend=result_backend
)

@celery_app.task
def write_log_celery(message: str):
    return f"Processed message: {message}"

