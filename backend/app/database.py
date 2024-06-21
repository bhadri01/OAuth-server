from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS")
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

try:
    client = MongoClient(f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_DETAILS}", serverSelectionTimeoutMS=5000)
    db = client.OAuth
    users_collection = db.users
    # Attempt a simple operation to verify connection
    client.admin.command('ping')
    print("Database connected successfully.")
except (errors.ServerSelectionTimeoutError, errors.ConnectionFailure) as e:
    print("Database not connected.")
    print(e)
