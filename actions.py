from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

from pymongo import MongoClient
client = MongoClient()
db = client.test
collection = db.docs

global_answers = []
global_ans = "Lorem Ipsum"

class ActionListTopics(Action):
    def name(self):
        return 'action_listtopics'
    
    def run(self,dispatcher,tracker,domain):
        dispatcher.utter_message("Sports, Science, Movie Trivia or random?")
        return

class ActionAskQuestion(Action):
    def name(self):
        return 'action_askquestion'
    def run(self, dispatcher, tracker, domain):
        topic = tracker.get_slot('topic')
        if topic == 'science' :
            pipeline = [
                { "$match": { "Category": "Science"}},
                { "$sample": {"size": 1 }}
            ]
        elif topic == 'sports':
            pipeline = [
                { "$match": { "Category": "Sports"}},
                { "$sample": {"size": 1 }}
            ]
        elif topic == 'movie':
            pipeline = [
                { "$match": { "Category": "Movie Trivia"}},
                { "$sample": {"size": 1 }}
            ]
        else:
            pipeline = [ { "$sample": { "size" : 1 } }]
        
        result = collection.aggregate(pipeline)
        '''while (list(result)[0] == None):
            result = collection.aggregate(pipeline)'''

            
        for x in list(result):
            curr = tracker.get_slot('topic')
            try:
                dispatcher.utter_message('Asking from ' + curr)
            except TypeError:
                dispatcher.utter_message('Asking from random category')
            dispatcher.utter_message(x['Question'])
            global global_answers
            global_answers = x['Options']
            global global_ans
            global_ans = x['Answer']
            dispatcher.utter_message('A) '+ x['Options'][0] + '\n' + 'B) '+ x['Options'][1] + '\n' + 'C) '+ x['Options'][2])
        return

class ActionValidate(Action):
    def name(self):
        return 'action_validate'
    def run(self,dispatcher,tracker,domain):
        ans = tracker.get_slot('answer')
        if ans == '0' or ans == '1' or ans == '2':
            ans = int(ans)
            #ans=ans-1
            if global_answers[ans] == global_ans:
                dispatcher.utter_message('yes')
            else:
                dispatcher.utter_message('no its actually '+global_ans)
        else:

            if (ans.lower()).replace(" ","") in (global_ans.lower()).replace(" ",""):
                dispatcher.utter_message('yes')
            else:
                dispatcher.utter_message('no its actually '+global_ans)
        return [SlotSet('answer',None)]


