from fastapi import APIRouter, HTTPException
import pymongo
import json
from models.course import Course
from config.db import db
from utils.serializer import serialize_dict, serialize_list
import sys
from bson import ObjectId
from ML import ML
import aiofiles

router = APIRouter()

ml = ML()


@router.get('/')
def find_all_course():
    return serialize_list(db.course.find())


@router.get('/{id}')
def find_course_by_id(id):
    return serialize_dict(db.course.find_one({"_id": ObjectId(id)}))


@router.post('/create')
async def create_course(course: Course):
    try:
        course = dict(course)
        course['modules'] = [dict(module) for module in course['modules']]
        # translations = []
        # try:
        #     async with aiofiles.open('tempfile.mp4', 'wb') as out_file:
        #         while content := await file.read(1024):  # async read chunk
        #             await out_file.write(content)

        # finally:
        #     langs = ["en-GB", "ms", "hi"]
        #     for lang in langs:
        #         translations.append({"text": ml.convert_audio_to_original_text(
        #             './tempfile.mp4', src_lang=lang),
        #             "language": lang
        #         })

        # for module in course['modules']:
        inserted_id = db.course.insert_one(dict(course)).inserted_id
        return serialize_dict(db.course.find_one({"_id": inserted_id}))
    except pymongo.errors.OperationFailure:
        raise HTTPException(status_code=400, status="db error")


@router.put('/{id}')
def update_course(id, courseRequest):
    try:
        originData = serialize_dict(db.user.find_one({"_id": ObjectId(id)}, {'_id': False}))
        for key,value in courseRequest.items():
            if key in originData:
                originData[key] = value
        db.user.find_one_and_update({"_id": ObjectId(id)},
                                    {"$set": originData})
        return serialize_dict(db.user.find_one({"_id": ObjectId(id)}))
    except pymongo.errors.OperationFailure:
        raise HTTPException(status_code=400, status="db error")


@router.delete("/{id}")
def delete_course(id):
    try:
        db.course.find_one_and_delete({"_id": ObjectId(id)})
        return {"status": "Success"}
    except pymongo.errors.OperationFailure:
        raise HTTPException(status_code=400, status="db error")
