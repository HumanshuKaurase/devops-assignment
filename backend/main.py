import os
from celery import Celery
from celery.result import AsyncResult
from fastapi import FastAPI
from worker import write_log_celery

app = FastAPI()

# 🔑 Redis config via ENV variables
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")

CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"

celery_app = Celery(
    "worker",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

# ------------------------
# API ROUTES (IMPORTANT)
# ------------------------

@app.post("/notify/")
async def notify_user(email: str):
    """Trigger background task"""
    task = write_log_celery.delay(f"Notification sent to {email}")
    return {
        "message": f"Email will be sent to {email}",
        "task_id": task.id
    }


@app.get("/task_status/{task_id}")
async def get_task_status(task_id: str):
    """Check task status"""
    task_result = AsyncResult(task_id)

    if task_result.successful():
        return {
            "task_id": task_id,
            "status": "completed",
            "result": task_result.result
        }
    elif task_result.failed():
        return {
            "task_id": task_id,
            "status": "failed"
        }
    else:
        return {
            "task_id": task_id,
            "status": "in progress"
        }


@app.get("/health")
async def health():
    return {"status": "OK"}

