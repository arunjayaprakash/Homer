from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionAskQuestion(Action):
	def name(self):
		return 'action_askquestion'
		
	def run(self, dispatcher, tracker, domain):
		pass

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


