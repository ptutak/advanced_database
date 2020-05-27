from pprint import pformat
from pymongo import MongoClient
from bson.code import Code


client = MongoClient(
    "mongodb+srv://zabd2020:aggregations@db2020-aggregations-2sawx.mongodb.net"
)

db = client.get_database(name="db-aggregations")

# Zad 1
movies = db.movies.aggregate(
    [
        {"$match": {"languages": {"$elemMatch": {"$in": ["English", "German"]}}}},
        {"$project": {"imdb.rating": True, "title": True}},
        {"$limit": 5},
    ]
)

print("\nZad1\n")
for movie in movies:
    print(pformat(movie))


# Zad 2
movies = db.movies.aggregate(
    [
        {"$match": {"$and": [{"imdb.rating": {"$gt": 5.0}}, {"year": {"$gt": 1960}}]}},
        {"$unwind": {"path": "$directors"}},
        {"$unwind": {"path": "$cast"}},
        {"$addFields": {"director_is_cast": {"$cmp": ["$directors", "$cast"]}}},
        {"$match": {"director_is_cast": {"$eq": 0}}},
        {"$count": "number_of_movies"},
        {"$limit": 5},
    ]
)
print("\nZad2\n")
for movie in movies:
    print(pformat(movie))


# Zad 3
movies = db.movies.aggregate(
    [
        {"$match": {"imdb.rating": {"$gt": 0.0}}},
        {"$sort": {"imdb.rating": -1}},
        {"$limit": 100},
        {"$unwind": {"path": "$cast"}},
        {"$group": {"_id": "$cast"}},
        {"$limit": 10},
    ]
)

print("\nZad3\n")
for movie in movies:
    print(pformat(movie))
