from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.dispatcher import Button

class AskWhatSport(Action):
    def name(self):
        return 'ask_what_sport'
        
    def run(self, dispatcher, tracker, domain):
        sport_period = tracker.get_slot("sport_period")
        distance = tracker.get_slot("distance")
        sport = tracker.get_slot("sport")
        duration = tracker.get_slot("sport_duration")
        activity_hard = tracker.get_slot("activity_hard")
        buttons = []
        if sport != None:
            buttons.append(Button(title="Sport", payload="/activity{\"sport\":null}"))
            buttons.append(Button(title="Level", payload="/activity{\"sport_level\":\"Incorrect\"}"))
        if duration != None:
            buttons.append(Button(title="Duration", payload="/activity{\"sport_duration\":null}"))
        if distance != None:
            buttons.append(Button(title="Distance", payload="/activity{\"distance\":null}"))
        if sport_period != None:
            buttons.append(Button(title="Period", payload="/activity{\"sport_period\":null}"))
        if activity_hard != None:
            buttons.append(Button(title="Hardness", payload="/activity{\"activity_hard\":null}"))            
        dispatcher.utter_button_message("Ok. So, tell me what's wrong? Click on a button or tell me above!", buttons)
        
class AskWhatPain(Action):
    def name(self):
        return 'ask_what_pain'
        
    def run(self, dispatcher, tracker, domain):
        pain_period = tracker.get_slot("pain_period")
        desc = tracker.get_slot("pain_desc")
        duration = tracker.get_slot("pain_duration")
        body_part = tracker.get_slot("body_part")
        evolution = tracker.get_slot("pain_change")
        buttons = []
        if desc != None:
            buttons.append(Button(title="Description", payload="/pain{\"pain_desc\":null}"))
            buttons.append(Button(title="Level", payload="/pain{\"pain_level\":\"Incorrect\"}"))
        if duration != None:
            buttons.append(Button(title="Duration", payload="/pain{\"pain_duration\":null}"))
        if body_part != None:
            buttons.append(Button(title="Body part", payload="/pain{\"body_part\":null}"))
        if evolution != None:
            buttons.append(Button(title="Evolution", payload="/pain{\"pain_change\":null}"))
        if pain_period != None:
            buttons.append(Button(title="Period", payload="/pain{\"pain_period\":null}"))
        dispatcher.utter_button_message("Ok. So, tell me what's wrong? Click on a button or tell me above!", buttons)
