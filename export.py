from pprint import pformat
from pymongo import MongoClient
from bson.code import Code


client = MongoClient("localhost")

db = client.get_database(name="local")

routes = db.air_routes.insert_many()
