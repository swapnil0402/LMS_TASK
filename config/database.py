from pymongo.mongo_client import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient


uri = "mongodb+srv://swapnil:sappu9999@cluster0.dh5au7f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

db = client.lms_db

myCol = db["lms_collection"]