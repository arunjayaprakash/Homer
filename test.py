from pymongo import MongoClient
client = MongoClient()
db = client.quiz

collection = db.Science

pipeline = [ { "$sample": { "size" : 1 } }]

global_answers = []
global_ans = "lorem ipsum"


def Q():
    result = collection.aggregate(pipeline)
    for x in list(result):
            print(x['Question'])
            global global_answers
            global_answers = x['Options']
            global global_ans
            global_ans = x['Answer']
            print('A) '+ x['Options'][0] + '\n' + 'B) '+ x['Options'][1] + '\n' + 'C) '+ x['Options'][2])
    return

    
Q()
print(global_answers)

print(global_ans)
print ('fn.')

def V():
    ans = input("Enter choice")
    if ans == '1' or ans == '2' or ans == '3':
        ans = int(ans)
        ans=ans-1
        if global_answers[ans] == global_ans:
            print ( 'yes')
        else:
            print ('no')
    else:
        if (ans.lower()).replace(" ","") == (global_ans.lower()).replace(" ",""):
            print ('yes')
        else:
            print ('no')
    return

V()







