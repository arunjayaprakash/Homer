from pymongo import MongoClient
import json

client = MongoClient()

db = client.homer_db1

movies = db.movies
sports = db.sports
science = db.science


with open("sports_trivia.json","r") as readfile:
    raw_json = json.load(readfile)
    for x in raw_json:
        sports.insert_one(
            {
                "Question": x["Question"],
                "Options": x["Options"],
                "Answer": x["Answer"]
            }
        )

