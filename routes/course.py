from fastapi import APIRouter, HTTPException, File, UploadFile
from numpy import mod
import pymongo
import json
from models.course import Course
from config.db import db
from utils.serializer import serialize_dict, serialize_list
import sys
from bson import ObjectId
from ML import ML
import aiofiles
from utils.file_upload import upload_file
import uuid
from moviepy.editor import VideoFileClip

router = APIRouter()

ml = ML()

@router.get('/')
def find_all_course():
    return serialize_list(db.course.find())


@router.get('/{id}')
def find_course(id):
    return serialize_dict(db.course.find_one({"_id": ObjectId(id)}))


@router.post('/')
async def create_course(courseRequest:dict):

    try:
        courseRequest["cumulativeRating"] = 3
        for module in courseRequest['modules']:
            module["views"] = 0
            module["rating"] = 3
            module["comments"] = []
        inserted_id = db.course.insert_one(courseRequest).inserted_id
        return serialize_dict(db.course.find_one({"_id": inserted_id}))
    except pymongo.errors.OperationFailure as e:
        print(e)
        raise HTTPException(status_code=400, detail="db error")


@router.put('/{id}')
def update_course(id, courseRequest:dict):
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
        return {"detail": "success"}
    except pymongo.errors.OperationFailure:
        raise HTTPException(status_code=400, detail="db error")


@router.post('/file-upload')
async def handler(file: UploadFile = File(...)):
    filename = str(uuid.uuid4()) + file.filename
    response = {}
    try:
        async with aiofiles.open('tempfile.mp4', 'wb') as out_file:
            while content := await file.read(1024):  # async read chunk
                await out_file.write(content)
            
            success = upload_file('./tempfile.mp4', filename)
            if success:
                response['url'] = f"https://cfg-team1.s3.ap-southeast-1.amazonaws.com/{filename}"
                response["detail"] = "upload succeed"
                clip = VideoFileClip("./tempfile.mp4")
                response["duration"] = clip.duration
            else:
                raise HTTPException(status_code=400, detail="upload failed")
    finally:
        english_text, duration = ml.convert_audio_to_original_text(
            './tempfile.mp4', src_lang="en-GB")
        hindhi_text = ml.convert_original_text_to_specific_lang(
            english_text, 'hi')
        ms_text = ml.convert_original_text_to_specific_lang(
            english_text, 'ms')
        questions = []
        # questions = ml.generate_questions(english_text)
        response["questions"] = questions
        response["transcript"] = {
            "english": english_text,
            "hindhi": hindhi_text,
            "malay": ms_text,
        }
        print(response)
        return response
