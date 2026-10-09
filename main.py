
from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="DevOps Learning API",
    description="My first backend for learning Docker, AWS, Kubernetes, and CI/CD",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Hello from my DevOps API!",
        "status": "running",
        "next_step": "Docker"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get("/hello/{name}")
def say_hello(name: str):
    return {
        "message": f"Hello, {name}!",
        "served_by": "FastAPI"
    }
