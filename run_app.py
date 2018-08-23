from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/Homer_nlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-421917054450-422953358791-421202004400-1ec96ad1e759d87e7d152b804b39d5a0',
                            'xoxb-421917054450-423260603894-E1wnmPf6kumKgC53RJxfzaXU',
                            'JqxU40rBlzRSjoqtjnyFDZib',
                            True)

agent.handle_channel(HttpInputChannel(5005, '/', input_channel))