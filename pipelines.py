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


# Zad 4

alliances = db.air_alliances.aggregate(
    [
        {"$unwind": {"path": "$airlines"}},
        {
            "$lookup": {
                "from": "air_routes",
                "let": {"airline_name": "$airlines"},
                "pipeline": [
                    {
                        "$match": {
                            "$expr": {
                                "$and": [
                                    {"$eq": ["$airline.name", "$$airline_name"]},
                                    {"$eq": ["$dst_airport", "BCN"]},
                                ]
                            }
                        }
                    },
                ],
                "as": "routes",
            }
        },
        {"$unwind": {"path": "$routes"}},
        {"$group": {"_id": "$name", "count": {"$sum": 1}}},
    ]
)

print("\nZad4\n")
for alliance in alliances:
    print(pformat(alliance))


# Zad 5

routes = db.air_routes.aggregate(
    [
        {
            "$graphLookup": {
                "from": "air_routes",
                "startWith": "$dst_airport",
                "connectFromField": "dst_airport",
                "connectToField": "src_airport",
                "maxDepth": 1,
                "depthField": "numRoutes",
                "as": "routes_to",
            }
        },
        {"$unwind": {"path": "$routes_to"}},
        {"$match": {"src_airport": {"$eq": "COO"}}},
        {"$match": {"routes_to.dst_airport": {"$eq": "LFW"}}},
        {"$count": "routes_num"},
    ]
)

print("\nZad5\n")
for route in routes:
    print(pformat(route))


# Zad 9

routes = db.air_routes.aggregate(
    [
        {
            "$facet": {
                "categorizeByDest": [
                    {"$group": {"_id": "$dst_airport", "count": {"$sum": 1},}},
                    {"$sort": {"count": -1}},
                ],
                "categorizeBySrc": [
                    {"$group": {"_id": "$src_airport", "count": {"$sum": 1},}},
                    {"$sort": {"count": -1}},
                ],
            }
        }
    ]
)

print("\nZad9\n")
for route in routes:
    print(pformat(route))
    break
