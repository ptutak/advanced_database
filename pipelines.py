from pprint import pformat
from pymongo import MongoClient


client = MongoClient(
    host="db2020-aggregations-2sawx.mongodb.net",
    port=27017,
    username="zabd2020",
    password="aggregations",
)

db = client.get_database(name="db-aggregations")

one = db.movies.find_one()

print(pformat(one))
