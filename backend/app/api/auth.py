
from fastapi import APIRouter, Depends, HTTPException, status
from pymongo.database import Database

from app.db.session import get_db
from app.schemas.user import UserCreate, UserOut, Token
from app.services import auth as auth_service

router = APIRouter()


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Database = Depends(get_db)):
    existing = db.users.find_one({"email": user_in.email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = auth_service.create_user(db, user_in.email, user_in.password)
    # normalize output for UserOut schema
    return {"id": str(user["_id"]), "email": user["email"], "is_active": user.get("is_active", True)}


@router.post("/login", response_model=Token)
def login(user_in: UserCreate, db: Database = Depends(get_db)):
    user = auth_service.authenticate_user(db, user_in.email, user_in.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth_service.create_access_token(subject=user.get("email"))
    return {"access_token": token, "token_type": "bearer"}
