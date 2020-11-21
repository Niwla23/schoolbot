import pymongo

client = pymongo.MongoClient('localhost', 27017)

db = client["discord_schoolbot"]
tests_collection = db["tests"]
