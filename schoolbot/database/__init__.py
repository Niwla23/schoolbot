import pymongo
from schoolbot.helpers import config

client = pymongo.MongoClient(config["mongodb"])

db = client["discord_schoolbot"]
tests_collection = db["tests"]
