from fastapi import APIRouter, HTTPException
import pymongo

from config.db import db

from models.user import User

router = APIRouter()


@router.post("/login")
def login_handler(user: User):
    user = dict(user)
    try:
        credentials = db.user.find_one({"username": user["username"]})
        if not credentials:
            raise HTTPException(status_code=400, detail="user not found")

        if credentials["password"] == user["password"]:
            return {"status": "Success"}

        else:
            return {"status": "Failed"}

    except pymongo.errors.OperationFailure:
        raise HTTPException(status_code=400, detail="db error")
