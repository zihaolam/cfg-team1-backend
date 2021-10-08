from fastapi import APIRouter, HTTPException
import pymongo

from models.user import User
from config.db import db
from utils.serializer import serialize_dict, serialize_list
import sys
from bson import ObjectId

router = APIRouter()


@router.get('/')
def find_all_users():
	return serialize_list(db.user.find())


@router.post('/')
def create_user(user: User):
    try:
        inserted_id = db.user.insert_one(dict(user)).inserted_id
        return serialize_dict(db.user.find_one({"_id": inserted_id}))
    except pymongo.errors.OperationFailure:
        raise HTTPException(status_code=400, detail="db error")


@router.put('/{id}')
def update_user(id, user: User):
    try:
        db.user.find_one_and_update({"_id": ObjectId(id)},
                                    {"$set": dict(user)})
        return serialize_dict(db.user.find_one({"_id": ObjectId(id)}))
    except pymongo.errors.OperationFailure:
        raise HTTPException(status_code=400, detail="db error")


@router.delete("/{id}")
def delete_user(id):
    try:
        db.user.find_one_and_delete({"_id": ObjectId(id)})
        return {"detail": "success"}
    except pymongo.errors.OperationFailure:
        raise HTTPException(status_code=400, detail="db error")
