from models.db.db_setup import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import (Column, Integer, String, ForeignKey, Table)


profiles_skills = Table(
    'profiles_skill', Base.metadata,
    Column('profile_id', Integer, ForeignKey('profiles.id'), primary_key=True),
    Column("skill_id", Integer, ForeignKey('skills.id'), primary_key=True)
)


class Skill(Base):
    __tablename__ = 'skills'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, index=True)
    profiles: Mapped[list["Profile"]] = relationship("Profile", secondary=profiles_skills, back_populates="skills")


class Profile(Base):
    __tablename__ = 'profiles'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    full_name: Mapped[str] = mapped_column(String, index=True)
    bio: Mapped[str] = mapped_column(String, index=True)
    github_url: Mapped[str] = mapped_column(String)
    portfolio_url: Mapped[str] = mapped_column(String)
    twitter_url: Mapped[str] = mapped_column(String)
    instagram_url: Mapped[str] = mapped_column(String)

    user: Mapped["User"] = relationship("User", back_populates="profile")
    skills: Mapped[list["Skill"]] = relationship('Skill', secondary=profiles_skills, back_populates="profiles")



