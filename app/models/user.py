from models.db.db_setup import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import (Integer, String, Boolean)
from models.profile import Profile, Skill


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    is_recruiter: Mapped[bool] = mapped_column(Boolean, default=False)

    profile: Mapped["Profile"] = relationship("Profile", back_populates="user")


