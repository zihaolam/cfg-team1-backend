from fastapi import FastAPI, Form, UploadFile, File
from routes.user import router as user_router
from routes.auth import router as auth_router
from routes.course import router as course_router
from ML import ML
import aiofiles
import os

from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/user")
app.include_router(auth_router, prefix="/auth")
app.include_router(course_router, prefix="/course")

ml = ML()


@app.post("/test")
async def handler(file: UploadFile = File(...)):
    try:
        async with aiofiles.open('tempfile.mp4', 'wb') as out_file:
            while content := await file.read(1024):  # async read chunk
                await out_file.write(content)

    finally:
        english_text = ml.convert_audio_to_original_text(
            './tempfile.mp4', src_lang="en-GB")
        # ms_text = ml.convert_original_text_to_specific_lang(
        #     english_text, tgt_lang="ms")
        # hi_text = ml.convert_original_text_to_specific_lang(
        #     english_text, tgt_lang="hi")
        # questions = ml.generate_questions(english_text)
        print(english_text)
        # print("questions", questions)
