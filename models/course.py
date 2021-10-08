from typing import List, Dict
from utils.mongomodel import MongoModel

class Module(MongoModel):
	name: str
	description: str
	videoLink: str

class Course(MongoModel):
	name: str
	description: str
	modules: List[Module]
	price: float
	rating: float