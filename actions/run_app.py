from rasa_core.channels import HttpInputChannel
from rasa_core.channels.slack import SlackInput
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter

nlu_interpreter = RasaNLUInterpreter('../models/nlu_model_en/') #PATH TO NLU MODEL
agent = Agent.load('../models/dialogue_model', interpreter = nlu_interpreter) #PATH TO DIALOGUE MODEL

input_channel = SlackInput(
   slack_token="",  # this is the `bot_user_o_auth_access_token`
   slack_channel=""  # the name of your channel to which the bot posts
)

agent.handle_channel(HttpInputChannel(5003, "/", input_channel))
