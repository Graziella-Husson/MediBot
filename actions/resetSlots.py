from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from ressources import get_utterance

class ResetSportSlots(Action):
    def name(self):
        return 'reset_slots_sport'
    
    def run(self, dispatcher, tracker, domain):  
        language = tracker.get_slot("language")
        global_score = tracker.get_slot("global_score")
        dispatcher.utter_message(get_utterance("saved",language))
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
        return[SlotSet("global_score",global_score),
               SlotSet("activity_hard",None), 
                SlotSet("activity_duration",None), 
                SlotSet("sport_level",None), 
                SlotSet("sport",None), 
                SlotSet("activity_distance",None), 
                SlotSet("activity_period", None), 
                SlotSet("activity_time", None), 
                SlotSet("topic", None), 
                SlotSet("requested_slot", None), 
                SlotSet("activity",True)]

class ResetPainSlots(Action):
    def name(self):
        return 'reset_slots_pain'
    
    def run(self, dispatcher, tracker, domain):  
        language = tracker.get_slot("language")
        global_score = tracker.get_slot("global_score")
        dispatcher.utter_message(get_utterance("saved",language))
        # TODO: save to DB
        pain_level = tracker.get_slot("pain_level")
        if pain_level=='severe':
            global_score+=1
        elif pain_level=='moderate':
            global_score+=2
        elif pain_level=='mild':
            global_score+=3
        #TODO: save score
        return [SlotSet("global_score",global_score),
                SlotSet("pain_duration",None), 
                SlotSet("pain_desc",None), 
                SlotSet("pain_body_part",None),
                SlotSet("pain_change",None),
                SlotSet("pain_period",None),
                SlotSet("pain_time",None),
                SlotSet("topic", None), 
                SlotSet("requested_slot", None),
                SlotSet("pain",True), 
                SlotSet("pain_level",None)]

class ResetPathologySlots(Action):
    def name(self):
        return 'reset_slots_pathology'
    
    def run(self, dispatcher, tracker, domain):  
        language = tracker.get_slot("language")
        global_score = tracker.get_slot("global_score")
        global_score+=1        
        dispatcher.utter_message(get_utterance("saved",language))
        # TODO: save to DB
        return [SlotSet("global_score",global_score),
                SlotSet("symtoms",None),
                SlotSet("pathology_body_part",None),
                SlotSet("topic", None), 
                SlotSet("requested_slot", None),
                SlotSet("pathology",True)]

class ResetTreatmentSlots(Action):
    def name(self):
        return 'reset_slots_treatment'
    
    def run(self, dispatcher, tracker, domain):  
        language = tracker.get_slot("language")
        global_score = tracker.get_slot("global_score")
        global_score+=2
        dispatcher.utter_message(get_utterance("saved",language))
        # TODO: save to DB
        return [SlotSet("global_score",global_score),
                SlotSet("medicinal",None),
                SlotSet("drug",None),
                SlotSet("topic", None), 
                SlotSet("requested_slot", None),
                SlotSet("treatment",True)]

class ResetInfoPatientSlots(Action):
    def name(self):
        return 'reset_slots_info_patient'
    
    def run(self, dispatcher, tracker, domain):  
        language = tracker.get_slot("language")
        dispatcher.utter_message(get_utterance("saved",language))
        # TODO: save to DB
        return [SlotSet("addiction",None),
                SlotSet("weight",None),
                SlotSet("infoPatient_distance",None),
                SlotSet("gender",None),
                SlotSet("infoPatient_temperature",None),
                SlotSet("heart_rate",None),
                SlotSet("blood_pressure",None),
                SlotSet("infoPatient_time",None),
                SlotSet("topic", None), 
                SlotSet("requested_slot", None),
                SlotSet("infoPatient",True)]