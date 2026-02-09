from pymongo import MongoClient

client = MongoClient("mongodb+srv://vision:382AGNIRO@cluster0.t45opkp.mongodb.net/?appName=Cluster0", serverSelectionTimeoutMS=5000)
print(client.server_info())
