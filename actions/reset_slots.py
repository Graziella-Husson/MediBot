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


class ResetSlotsAction(Action):
    """Heritated from Action, used to reset given slots"""
    calculus = False
    intent_name = ""
    entities = []

    def check(self):
        """Used to check if all proprieties has been set"""
        if self.intent_name == "" or len(self.entities) == 0:
            raise NotImplementedError("""
            a ResetSlots action must implement a __init__ method
            with a intent_name and entities list""")

    def name(self):
        """the name of the action to implement"""
        raise NotImplementedError("""a ResetSlots action must
                                    implement a name method""")

    def run(self, dispatcher, tracker, domain):
        """Save infos and reset slots"""
        language = tracker.get_slot("language")
        global_score = tracker.get_slot("global_score")
        dispatcher.utter_message(get_utterance("saved", language))
        # TODO: save infos to DB, warning : save level in language of bot
        if self.calculus:
            global_score = self.calculus_action(tracker)
        to_return = self.core_action()
        to_return.append(SlotSet("global_score", global_score))
        #TODO: save score
        return to_return

    def core_action(self):
        """Set entities list, topic and requested_slot
        to None. Set intent_name to True"""
        to_return = []
        to_reset = ["topic", "requested_slot"]
        for entity in self.entities:
            to_return.append(SlotSet(entity, None))
        for reset in to_reset:
            to_return.append(SlotSet(reset, None))
        to_return.append(SlotSet(self.intent_name, True))
        return to_return

    def calculus_action(self, tracker):
        """In case of calculus action, save the score depending on level"""
        level = tracker.get_slot(self.intent_name+"_level")
        global_score = tracker.get_slot("global_score")
        if level == 'little' or level == 'severe':
            global_score += 1
            met = "< 3 MET"
        elif level == 'moderate':
            global_score += 2
            met = "3-6 MET"
        elif level == 'vigorous' or level == 'mild':
            global_score += 3
            met = "> 6 MET"
        #TODO: save met
        return global_score


class ResetSportSlots(ResetSlotsAction):
    """Reset slots linked to activity intent and save infos in DB"""
    def name(self):
        """
        @return: the name of the action.
        """
        return 'reset_slots_sport'

    def __init__(self):
        """Set all slots for intent 'activity' to None :
            - activity_hard
            - activity_duration
            - activity_level
            - sport
            - activity_distance
            - activity_period
            - activity_time
        Set slot activity to True"""
        self.calculus = True
        self.intent_name = "activity"
        self.entities = ["activity_hard",
                         "activity_duration",
                         "activity_level",
                         "sport",
                         "activity_distance",
                         "activity_period",
                         "activity_time"
                         ]


class ResetPainSlots(ResetSlotsAction):
    """Reset slots linked to pain intent and save infos in DB"""
    def name(self):
        """@return: the name of the action."""
        return 'reset_slots_pain'

    def __init__(self):
        """Set all slots for intent 'pain' to None:
            - pain_period
            - pain_desc
            - pain_body_part
            - pain_duration
            - pain_change
            - pain_time
            - pain_level
        Set slot pain to True"""
        self.calculus = True
        self.intent_name = "pain"
        self.entities = ["pain_period",
                         "pain_desc",
                         "pain_body_part",
                         "pain_duration",
                         "pain_change",
                         "pain_time",
                         "pain_level"
                         ]


class ResetPathologySlots(ResetSlotsAction):
    """Reset slots linked to pathology intent and save infos in DB"""
    def name(self):
        """@return: the name of the action."""
        return 'reset_slots_pathology'

    def __init__(self):
        """Set all slots for intent 'pathology' to None:
            - pathology_body_part
            - symtoms
            - pathology_time
            - pathology_change (boolean)
            - pathology_period
            - pathology_treatment_linked (boolean)
            - pathology_duration
        Set slot pathology to True"""
        self.intent_name = "pathology"
        self.entities = ["pathology_body_part",
                         "symtoms",
                         "pathology_time",
                         "pathology_change",
                         "pathology_period",
                         "pathology_treatment_linked",
                         "pathology_duration"
                         ]


class ResetTreatmentSlots(ResetSlotsAction):
    """Reset slots linked to treatment intent and save infos in DB"""
    def name(self):
        """@return: the name of the action."""
        return 'reset_slots_treatment'

    def __init__(self):
        """Set all slots for intent 'treatment' to None:
            - medicinal (boolean)
            - treatment_being_taken
            - drug
            - dosing
            - treatment_time
            - treatment_prescripted(boolean)
            - treatment_ok(boolean)
            - treatment_overdosage
            - treatment_period
            - treatment_duration
        Set slot treatment to True"""
        self.intent_name = "treatment"
        self.entities = ["medicinal",
                         "treatment_being_taken",
                         "drug",
                         "dosing",
                         "treatment_time",
                         "treatment_prescripted",
                         "treatment_ok",
                         "treatment_overdosage",
                         "treatment_period",
                         "treatment_duration"
                         ]


class ResetInfoPatientSlots(ResetSlotsAction):
    """Reset slots linked to infoPatient intent and save infos in DB"""
    def name(self):
        """@return: the name of the action."""
        return 'reset_slots_info_patient'

    def __init__(self):
        """Set all slots for intent 'infoPatient' to None:
            - addiction
            - weight
            - infoPatient_distance
            - gender
            - infoPatient_temperature
            - heart_rate
            - blood_pressure
            - infoPatient_time
        Set slot infoPatient to True"""
        self.intent_name = "infoPatient"
        self.entities = ["addiction",
                         "weight",
                         "infoPatient_distance",
                         "gender",
                         "infoPatient_temperature",
                         "heart_rate",
                         "blood_pressure",
                         "infoPatient_time"
                         ]
