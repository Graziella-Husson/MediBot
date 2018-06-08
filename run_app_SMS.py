from rasa_core.channels import HttpInputChannel
from rasa_core.channels.twilio import TwilioInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/current/') #PATH TO NLU MODEL
agent = Agent.load('./models/dialogue/', interpreter = nlu_interpreter) #PATH TO DIALOGUE MODEL

input_channel = TwilioInput(
  account_sid="", # you get this from your twilio account
  auth_token="", # also from your twilio account
  twilio_number="" # a number associated with your twilio account
)

agent.handle_channel(HttpInputChannel(5004, "/app", input_channel))
