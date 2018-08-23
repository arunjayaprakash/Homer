from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/Homer_nlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-386245034688-386713966068-403921128039-7348725ccf93b61f0cdba01020f13243', #app verification token
							'xoxb-386245034688-402641770532-yhoMSVcvSVfXiDnpwmm5blcd', # bot verification token
							'hhEnwW7vArgjJoiChqXeCHD0', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5005, '/', input_channel))