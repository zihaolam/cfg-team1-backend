from pydantic import BaseModel, BaseConfig
from bson import ObjectId

class MongoModel(BaseModel):
    class Config(BaseConfig):
        json_encoders = {
            ObjectId: lambda oid: str(oid),
        }