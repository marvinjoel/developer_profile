import os
import bcrypt
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controller.exceptions import BadRequestException
from controller.schemas.user import UserInput
from models.db.db_setup import db_session
from models.user import User

authRouter = APIRouter(
    prefix=os.getenv('API_PREFIX'),
    tags=['auth']
)


@authRouter.post("/auth/users")
async def create_user(input: UserInput, db: Session = Depends(db_session)) -> UserInput:
    exist = db.query(User).filter(User.email == input.email).first()
    if exist:
        raise BadRequestException("Email ya existe")

    password = bytes(input.hashed_password, 'utf-8')
    input.hashed_password = str(bcrypt.hashpw(password, bcrypt.gensalt(rounds=10)), 'utf-8')
    item = User(**input.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item