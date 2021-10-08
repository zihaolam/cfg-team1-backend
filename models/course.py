from typing import List, Dict
from utils.mongomodel import MongoModel


class Question(MongoModel):
    question: str
    answer: str


class Translation(MongoModel):
    language: str
    text: str


class Comment(MongoModel):
    username: str
    text: str


class Module(MongoModel):
    name: str
    description: str
    videoLink: str
    views: int = 0
    questions: List[Question] = []
    transcript: str = ""
    translation: List[Translation] = []
    comments: List[Comment] = []
    duration: float


class Course(MongoModel):
    name: str
    description: str
    modules: List[Module]
    price: float
    rating: float
    type: str
    userId: str
    cumulativeRating: float
    thumbnailUrl: str = ""
    category: str
