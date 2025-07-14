from fastapi import FastAPI
from app.routers import announcements
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Scheduled Announcements API",
    description="API for scheduling course announcements for future delivery to enrolled students.",
    version="1.0.0",
)

app.include_router(announcements.router, prefix="/announcements", tags=["Announcements"])
