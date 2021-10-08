from fastapi import APIRouter, HTTPException
import pymongo

from models.user import User
from config.db import db
from utils.serializer import serialize_dict, serialize_list
from bson import ObjectId

router = APIRouter()


@router.get('/')
def find_all_users():
	return serialize_list(db.user.find())

@router.get('/{id}')
def find_user_by_id(id):
	return serialize_dict(db.user.find_one({"_id": ObjectId(id)}))

@router.post('/create')
def create_user(userRequest:dict):
    try:
        userRequest["rating"] = 50
        userRequest["courseHistory"] = [] 
        inserted_id = db.user.insert_one(dict(userRequest)).inserted_id
        return serialize_dict(db.user.find_one({"_id": inserted_id}))
    except pymongo.errors.OperationFailure:
        raise HTTPException(status_code=400, detail="db error")


@router.put('/{id}')
def update_user(id, userRequest:dict):
    try:
        originData = serialize_dict(db.user.find_one({"_id": ObjectId(id)}, {'_id': False}))
        for key,value in userRequest.items():
            if key in originData:
                originData[key] = value
        db.user.find_one_and_update({"_id": ObjectId(id)},
                                    {"$set": originData})
        return serialize_dict(db.user.find_one({"_id": ObjectId(id)}))
    except pymongo.errors.OperationFailure:
        raise HTTPException(status_code=400, detail="db error")

@router.delete("/{id}")
def delete_user(id):
    try:
        db.user.find_one_and_delete({"_id": ObjectId(id)})
        return {"status": "Success"}
    except pymongo.errors.OperationFailure:
        raise HTTPException(status_code=400, detail="db error")
