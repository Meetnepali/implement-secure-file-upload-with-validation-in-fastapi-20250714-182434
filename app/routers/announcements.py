from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, status
from sqlalchemy.orm import Session
from app import schemas, models
from app.database import SessionLocal
from datetime import datetime, timezone, timedelta
import logging
import asyncio
import json
from typing import List

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def simulate_delivery(announcement_id: int, emails: List[str]):
    for email in emails:
        logging.info(f"[SIMULATION] Delivered Announcement ID {announcement_id} to {email}")

async def schedule_announcement_delivery(announcement_id: int, scheduled_time: datetime, emails: List[str]):
    now = datetime.now(timezone.utc)
    delay = (scheduled_time - now).total_seconds()
    if delay > 0:
        await asyncio.sleep(delay)
    simulate_delivery(announcement_id, emails)

@router.post("/", response_model=schemas.AnnouncementResponse, status_code=201, summary="Schedule an announcement", response_description="Announcement successfully scheduled")
async def schedule_announcement(
    announcement: schemas.AnnouncementCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    # Check for duplicate announcement (title and scheduled time)
    existing = db.query(models.Announcement).filter_by(title=announcement.title, scheduled_time=announcement.scheduled_time).first()
    if existing:
        raise HTTPException(status_code=409, detail="Announcement with same title and scheduled time already exists.")
    try:
        # Serialize emails for storage
        emails_str = json.dumps(announcement.emails)
        db_announcement = models.Announcement(
            title=announcement.title,
            body=announcement.body,
            emails=emails_str,
            scheduled_time=announcement.scheduled_time,
            status="scheduled",
        )
        db.add(db_announcement)
        db.commit()
        db.refresh(db_announcement)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error saving announcement to database.")
    background_tasks.add_task(
        schedule_announcement_delivery, db_announcement.id, announcement.scheduled_time, announcement.emails
    )
    return schemas.AnnouncementResponse(id=db_announcement.id, message="Announcement scheduled and will be delivered at the specified time.")
