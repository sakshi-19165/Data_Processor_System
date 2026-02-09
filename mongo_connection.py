import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_collection():
    uri = os.getenv("MONGO_URI")
    client = MongoClient(uri)

    db = client["data_processing_db"]
    collection = db["cleaned_records"]

    return collection
