from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

from pymongo import MongoClient
client = MongoClient()
db = client.quiz

import random

def get_random_Q(coll):
    # coll refers to your collection
    count = db.coll.count()
    return coll.find()[random.randrange(count)] #ensure Q doesnt repeat in sess?
    
class ActionListTopics(Action):
    def name(self):
        return 'action_listtopics'
    
    def run(self,dispatcher,tracker,domain):
        pass


class ActionAskQuestion(Action):
    def name(self):
        return 'action_askquestion'
    def run(self, dispatcher, tracker, domain):
        topic = tracker.get_slot('topic')
        Q = get_random_Q(topic)
        dispatcher.utter_message(Q["Question"])
        dispatcher.utter_message(Q["Options"])
        return

class ActionValidate(Action):
    def name(self):
        return 'action_validate'
    def run(self,dispatcher,tracker,domain):
        pass


