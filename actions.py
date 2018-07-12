from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

from pymongo import MongoClient
client = MongoClient()
db = client.homer_db1


class ActionAskQuestion(Action):
    def name(self):
        return 'action_askquestion'
    def run(self, dispatcher, tracker, domain):
        topic = tracker.get_slot('topic')
        doc=db.topic.aggregate({$sample:{size:1}})
        dispatcher.utter_message(doc["Question"])
        dispatcher.utter_message(doc["Options"])
        return



    
class ActionListTopics(Action):
    def name(self):
        return 'action_listtopics'
    
    def run(self,dispatcher,tracker,domain):
        pass

class ActionValidate(Action):
    def name(self):
        return 'action_validate'
    def run(self,dispatcher,tracker,domain):
        pass


