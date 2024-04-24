from pymongo import MongoClient

host = 'pymongo-mongodb-1'
port = 27017
db_name = 'temp_db'

mongo_uri = f'mongodb://{host}:{port}/{db_name}'  # Get MongoDB connection string from environment variable

client = MongoClient(mongo_uri)

print(client)

db = client[db_name]
collection = db['collection']