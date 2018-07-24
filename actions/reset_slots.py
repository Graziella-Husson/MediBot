"""
This module is used to regroup all reset slots actions.\n
A reset slots action is an action where the bot will reset all given slots\n
If the intent linked has a calculus, save him in the DB too\n
Created on Tue Jun 26 10:22:40 2018\n
@author: U{@Graziella-Husson<https://github.com/Graziella-Husson>}
"""
from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from ressources import get_utterance

class ResetSportSlots(Action):
    """Reset slots linked to activity intent and save infos in DB"""
    def name(self):
        """
        @return: the name of the action.
        """
        return 'reset_slots_sport'

    def run(self, dispatcher, tracker, domain):
        """@return: A list of SlotSet
        @param tracker: get all infos for intent 'activity'
        Set all slots for intent 'activity' to None :
            - activity_period
            - activity_distance
            - sport
            - activity_duration
            - activity_hard
            - activity_time
        Set slot activity to True"""
        language = tracker.get_slot("language")
        global_score = tracker.get_slot("global_score")
        dispatcher.utter_message(get_utterance("saved", language))
        # TODO: save to DB
        activity_level = tracker.get_slot("activity_level")
        if activity_level == 'little':
            global_score += 1
            met = "< 3 MET"
        elif activity_level == 'moderate':
            global_score += 2
            met = "3-6 MET"
        elif activity_level == 'vigorous':
            global_score += 3
            met = "> 6 MET"
        #TODO: save score and met warning : save level in language of bot
        return[SlotSet("global_score", global_score),
               SlotSet("activity_hard", None),
               SlotSet("activity_duration", None),
               SlotSet("activity_level", None),
               SlotSet("sport", None),
               SlotSet("activity_distance", None),
               SlotSet("activity_period", None),
               SlotSet("activity_time", None),
               SlotSet("topic", None),
               SlotSet("requested_slot", None),
               SlotSet("activity", True)]

class ResetPainSlots(Action):
    """Reset slots linked to pain intent and save infos in DB"""
    def name(self):
        """@return: the name of the action."""
        return 'reset_slots_pain'

    def run(self, dispatcher, tracker, domain):
        """@return: A list of SlotSet
        @param tracker: get all infos for intent 'pain'
        Set all slots for intent 'pain' to None:
            - pain_period
            - pain_desc
            - pain_body_part
            - pain_duration
            - pain_change
            - pain_time
        Set slot pain to True"""
        language = tracker.get_slot("language")
        global_score = tracker.get_slot("global_score")
        dispatcher.utter_message(get_utterance("saved", language))
        # TODO: save to DB warning : save level in language of bot
        pain_level = tracker.get_slot("pain_level")
        if pain_level == 'severe':
            global_score += 1
        elif pain_level == 'moderate':
            global_score += 2
        elif pain_level == 'mild':
            global_score += 3
        #TODO: save score
        return [SlotSet("global_score", global_score),
                SlotSet("pain_duration", None),
                SlotSet("pain_desc", None),
                SlotSet("pain_body_part", None),
                SlotSet("pain_change", None),
                SlotSet("pain_period", None),
                SlotSet("pain_time", None),
                SlotSet("topic", None),
                SlotSet("requested_slot", None),
                SlotSet("pain", True),
                SlotSet("pain_level", None)]

class ResetPathologySlots(Action):
    """Reset slots linked to pathology intent and save infos in DB"""
    def name(self):
        """@return: the name of the action."""
        return 'reset_slots_pathology'

    def run(self, dispatcher, tracker, domain):
        """@return: A list of SlotSet
        @param tracker: get all infos for intent 'pathology'
        Set all slots for intent 'pathology' to None:
            - pathology_body_part
            - symtoms
            - pathology_time
            - pathology_change (boolean)
            - pathology_period
            - pathology_treatment_linked (boolean)
        Set slot pathology to True"""
        language = tracker.get_slot("language")
        global_score = tracker.get_slot("global_score")
        global_score += 1
        dispatcher.utter_message(get_utterance("saved", language))
        # TODO: save to DB
        return [SlotSet("global_score", global_score),
                SlotSet("symtoms", None),
                SlotSet("pathology_body_part", None),
                SlotSet("pathology_time", None),
                SlotSet("pathology_change", None),
                SlotSet("pathology_period", None),
                SlotSet("pathology_treatment_linked", None),
                SlotSet("topic", None),
                SlotSet("requested_slot", None),
                SlotSet("pathology", True)]

class ResetTreatmentSlots(Action):
    """Reset slots linked to treatment intent and save infos in DB"""
    def name(self):
        """@return: the name of the action."""
        return 'reset_slots_treatment'

    def run(self, dispatcher, tracker, domain):
        """@return: A list of SlotSet
        @param tracker: get all infos for intent 'treatment'
        Set all slots for intent 'treatment' to None:
            - medicinal (boolean)
            - treatment_being_taken
            - drug
            - dosing
            - treatment_time
            - treatment_prescripted(boolean)
            - treatment_ok(boolean)
            - treatment_overdosage
            - treatment_period
        Set slot treatment to True"""
        language = tracker.get_slot("language")
        global_score = tracker.get_slot("global_score")
        global_score += 2
        response = get_utterance("saved", language)
        response += get_utterance("more_treatment", language)
        dispatcher.utter_message(response)
        # TODO: save to DB
        return [SlotSet("global_score", global_score),
                SlotSet("medicinal", None),
                SlotSet("drug", None),
                SlotSet("treatment_being_taken", None),
                SlotSet("dosing", None),
                SlotSet("treatment_time", None),
                SlotSet("treatment_prescripted", None),
                SlotSet("treatment_ok", None),
                SlotSet("treatment_overdosage", None),
                SlotSet("treatment_period", None),
                SlotSet("treatment_duration", None),
                SlotSet("topic", None),
                SlotSet("requested_slot", None),
                SlotSet("treatment", True)]

class ResetInfoPatientSlots(Action):
    """Reset slots linked to infoPatient intent and save infos in DB"""
    def name(self):
        """@return: the name of the action."""
        return 'reset_slots_info_patient'

    def run(self, dispatcher, tracker, domain):
        """@return: A list of SlotSet
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
        Set slot info_patient to True"""
        language = tracker.get_slot("language")
        dispatcher.utter_message(get_utterance("saved", language))
        # TODO: save to DB
        return [SlotSet("addiction", None),
                SlotSet("weight", None),
                SlotSet("infoPatient_distance", None),
                SlotSet("gender", None),
                SlotSet("infoPatient_temperature", None),
                SlotSet("heart_rate", None),
                SlotSet("blood_pressure", None),
                SlotSet("infoPatient_time", None),
                SlotSet("topic", None),
                SlotSet("requested_slot", None),
                SlotSet("infoPatient", True)]