from utils.mongomodel import MongoModel

class User(MongoModel):
	username: str
	password: str
	role: str