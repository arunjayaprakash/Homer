from pymongo import MongoClient
client = MongoClient()
db = client.quiz

collection = db.quiz_corpus
topics = ["Movie Trivia","Science","Sports"]

''' to remove null documents '''
'''
for x in topics:
    y = x.replace(" ","")
    pipeline = {"Question":null}
    result = collection.delete_many(pipeline)


for x in topics:
    y = x.replace(" ","")
    pipeline = [ { "$match": { "Category": x } }, { "$out": y } ]
    result = collection.aggregate(pipeline)
'''
# db.quiz_corpus.aggregate({$match:{"Category":"Science"}},{$sample:{size:1}})

x = "Science"
pipeline = [ {"$match":{"Category":"Science"}},{"$sample":{"size":1}}]
        
result = collection.aggregate(pipeline)
for x in list(result):
    print(x)

