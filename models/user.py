from utils.mongomodel import MongoModel
from typing import List


class CourseHistory(MongoModel):
    progress: str
    courseId: str


class User(MongoModel):
    username: str
    password: str
    role: str
    courseHistory: List[CourseHistory] = []
    rating: float
