from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ResetSportSlots(Action):
    def name(self):
        return 'reset_slots_sport'
    
    def run(self, dispatcher, tracker, domain):
        global_score = tracker.get_slot("global_score")
        dispatcher.utter_message("Saved!")
        # TODO: save to DB
        sport_level = tracker.get_slot("sport_level")
        if sport_level=='little':
            global_score+=1
            MET = "< 3 MET"
        elif sport_level=='moderate':
            global_score+=2
            MET = "3-6 MET"
        elif sport_level=='vigorous':
            global_score+=3
            MET = "> 6 MET"
        #TODO: save score and MET
        return[SlotSet("global_score",global_score),SlotSet("activity_hard",None), SlotSet("sport_duration",None), SlotSet("sport_level",None), SlotSet("sport",None), SlotSet("distance",None), SlotSet("sport_period", None), SlotSet("topic", None), SlotSet("requested_slot", None), SlotSet("activity",True)]

class ResetPainSlots(Action):
    def name(self):
        return 'reset_slots_pain'
    
    def run(self, dispatcher, tracker, domain):
        global_score = tracker.get_slot("global_score")
        dispatcher.utter_message("Saved!")
        # TODO: save to DB
        sport_level = tracker.get_slot("sport_level")
        if sport_level=='severe':
            global_score+=1
        elif sport_level=='moderate':
            global_score+=2
        elif sport_level=='mild':
            global_score+=3
        #TODO: save score
        return [SlotSet("global_score",global_score),SlotSet("pain_duration",None), SlotSet("pain_desc",None), SlotSet("body_part",None), SlotSet("pain_change",None), SlotSet("pain_period",None), SlotSet("topic", None), SlotSet("requested_slot", None),SlotSet("pain",True), SlotSet("pain_level",None)]
