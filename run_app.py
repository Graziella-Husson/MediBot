from rasa_core.channels import HttpInputChannel
from rasa_core.channels.slack import SlackInput
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/test') #PATH TO NLU MODEL
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter) #PATH TO DIALOGUE MODEL

input_channel = SlackInput(
   slack_token="xoxb-341974864337-IhMUzjU1BTO05JITsTgy93X5",  # this is the `bot_user_o_auth_access_token`
   slack_channel=""  # the name of your channel to which the bot posts
)

agent.handle_channel(HttpInputChannel(5004, "/", input_channel))
