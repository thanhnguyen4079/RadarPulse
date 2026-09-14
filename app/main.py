from fastapi import fastapi
from app.config import get_settings

settings = get_settings()

app = FastAPI(
    title = settings.app_name,
    description = "",
    version = settings.app_version
)

@app.get("/health")
def health_check():
    return {"status": "ok", "version": settings.app_version}
    