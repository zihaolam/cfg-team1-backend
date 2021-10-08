import pymongo
import time
import os
from dotenv import load_dotenv

load_dotenv()

DB_URI = os.getenv('DB_URI')


def mongo_connect():
    try:
        conn = pymongo.MongoClient(DB_URI)
        db = conn.myFirstDatabase
        print("connected to MongoDB")
        return db

    except pymongo.errors.ConnectionFailure as err:
        print("connection failed with err: " + err)
        return False


db = mongo_connect()
while not db:
    time.sleep(5)
    db = mongo_connect()
