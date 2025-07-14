from sqlalchemy import Column, Integer, String, DateTime, Text
from app.database import Base

class Announcement(Base):
    __tablename__ = "announcements"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(120), nullable=False)
    body = Column(Text, nullable=False)
    emails = Column(Text, nullable=False)  # Comma-separated list
    scheduled_time = Column(DateTime, nullable=False)
    status = Column(String(50), default="scheduled")
