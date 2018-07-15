from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

from pymongo import MongoClient
client = MongoClient()
db = client.quiz
    
class ActionListTopics(Action):
    def name(self):
        return 'action_listtopics'
    
    def run(self,dispatcher,tracker,domain):
        dispatcher.utter_message("Sports, Science Movie Trivia or random?")
        return

class ActionAskQuestion(Action):
    def name(self):
        return 'action_askquestion'
    def run(self, dispatcher, tracker, domain):
        topic = tracker.get_slot('topic')
        if topic == 'science' :
            collection = db.Science
        elif topic == 'sports':
            collection = db.Science
        elif topic == 'movies':
            collection = db.MovieTrivia
        else
            collection = db.quiz_corpus
        pipeline = [ { "$sample": { "size" : 1 } }]
        result = collection.aggregate(pipeline)
        for x in list(result):
            dispatcher.utter_message(x['Question'])
            dispatcher.utter_message('A) '+ x['Options'][0] + '\n' + 'B) '+ x['Options'][1] + '\n' + 'C) '+ x['Options'][2]  )
        return

class ActionValidate(Action):
    def name(self):
        return 'action_validate'
    def run(self,dispatcher,tracker,domain):
        pass


