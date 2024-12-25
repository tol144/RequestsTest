from sqlalchemy import func, DateTime, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from datetime import datetime


class BaseModel(DeclarativeBase):
    pass


class RequestResults(BaseModel):
    __tablename__ = "t_request_results"

    id: Mapped[int] = mapped_column(primary_key=True)
    request_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    result: Mapped[str] = mapped_column(Text)
