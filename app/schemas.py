from typing import List
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, validator

class AnnouncementBase(BaseModel):
    title: str = Field(..., title="Announcement Title", max_length=120, example="Class Cancelled")
    body: str = Field(..., title="Announcement Body", example="Today's class is cancelled due to instructor illness.")
    emails: List[EmailStr] = Field(..., title="Recipient Emails", example=["student1@example.com", "student2@example.com"])
    scheduled_time: datetime = Field(..., title="Scheduled Time (UTC)", example="2024-06-09T18:00:00Z")

    @validator('scheduled_time')
    def scheduled_time_in_future(cls, v):
        from datetime import datetime, timezone
        if v <= datetime.now(timezone.utc):
            raise ValueError("scheduled_time must be in the future.")
        return v

class AnnouncementCreate(AnnouncementBase):
    pass

class AnnouncementResponse(BaseModel):
    id: int
    message: str

    class Config:
        orm_mode = True
