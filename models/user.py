from utils.mongomodel import MongoModel
from typing import List


class CourseHistory(MongoModel):
    progress: float
    courseId: str


class User(MongoModel):
    username: str
    password: str
    role: str = "Student"
    courseHistory: List[CourseHistory] = []
    rating: float = None
