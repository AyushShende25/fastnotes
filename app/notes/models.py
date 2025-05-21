from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Text
from app.core.base import Base


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(Text)
