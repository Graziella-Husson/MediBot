from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from ressources import get_utterance

class ResetSportSlots(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'reset_slots_sport'
    
    def run(self, dispatcher, tracker, domain):
        """
        @return: A list of SlotSet
        @param tracker: get all infos for intent 'activity'
        Set all slots for intent 'activity' to None : 
            - activity_period
            - activity_distance
            - sport
            - activity_duration
            - activity_hard
            - activity_time
        Set slot activity to True
        """  
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
        #TODO: save score and MET warning : save level in language of bot
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
        """
        @return: the name of the action.
        """
        return 'reset_slots_pain'
    
    def run(self, dispatcher, tracker, domain):  
        """
        @return: A list of SlotSet
        @param tracker: get all infos for intent 'pain'
        Set all slots for intent 'pain' to None:
            - pain_period
            - pain_desc
            - pain_body_part
            - pain_duration
            - pain_change
            - pain_time
        Set slot pain to True
        """  
        language = tracker.get_slot("language")
        global_score = tracker.get_slot("global_score")
        dispatcher.utter_message(get_utterance("saved",language))
        # TODO: save to DB warning : save level in language of bot
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
        """
        @return: the name of the action.
        """
        return 'reset_slots_pathology'
    
    def run(self, dispatcher, tracker, domain):  
        """
        @return: A list of SlotSet
        @param tracker: get all infos for intent 'pathology'
        Set all slots for intent 'pathology' to None:
            - pathology_body_part
            - symtoms
            - pathology_time
            - pathology_change (boolean)
            - pathology_period
            - pathology_treatment_linked (boolean)
        Set slot pathology to True
        """  
        language = tracker.get_slot("language")
        global_score = tracker.get_slot("global_score")
        global_score+=1        
        dispatcher.utter_message(get_utterance("saved",language))
        # TODO: save to DB
        return [SlotSet("global_score",global_score),
                SlotSet("symtoms",None),
                SlotSet("pathology_body_part",None),
                SlotSet("pathology_time",None),
                SlotSet("pathology_change",None),
                SlotSet("pathology_period",None),
                SlotSet("pathology_treatment_linked",None),
                SlotSet("topic", None), 
                SlotSet("requested_slot", None),
                SlotSet("pathology",True)]

class ResetTreatmentSlots(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'reset_slots_treatment'
    
    def run(self, dispatcher, tracker, domain):  
        """
        @return: A list of SlotSet
        @param tracker: get all infos for intent 'treatment'
        Set all slots for intent 'treatment' to None:
            - medicinal (boolean)
            - drug
        Set slot treatment to True
        """  
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
        """
        @return: the name of the action.
        """
        return 'reset_slots_info_patient'
    
    def run(self, dispatcher, tracker, domain):  
        """
        @return: A list of SlotSet
        @param tracker: get all infos for intent 'info_patient'
        Set all slots for intent 'info_patient' to None:
            - addiction
            - weight
            - infoPatient_distance
            - gender
            - infoPatient_temperature
            - heart_rate
            - blood_pressure
            - infoPatient_time
        Set slot info_patient to True
        """  
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