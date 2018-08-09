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
from insertfonction import insert_to_answer
from init_and_complex import get_session_id


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
        slack_id = tracker.sender_id
        global_score = tracker.get_slot("global_score")
        dispatcher.utter_message(get_utterance("saved", language, slack_id))
        for e in self.entities:
            slot_value = tracker.get_slot(e)
            if slot_value is not None:
                session_id = get_session_id()
                insert_to_answer(slot_value, session_id, e, tracker.sender_id)
#                insert_to_answer(value,session,entity,slack_id)
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


class ResetActivitySlots(ResetSlotsAction):
    """Reset slots linked to activity intent and save infos in DB"""
    def name(self):
        """
        @return: the name of the action.
        """
        return 'reset_slots_activity'

    def __init__(self):
        """Set all slots for intent 'activity' to None :
            - activity_hard
            - activity_duration
            - activity_level
            - activity_sport
            - activity_distance
            - activity_period
            - activity_time
        Set slot activity to True"""
        self.calculus = True
        self.intent_name = "activity"
        self.entities = ["activity_hard",
                         "activity_duration",
                         "activity_level",
                         "activity_sport",
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
            - pathology_symptom
            - pathology_time
            - pathology_change (boolean)
            - pathology_period
            - pathology_treatment_linked (boolean)
            - pathology_duration
        Set slot pathology to True"""
        self.intent_name = "pathology"
        self.entities = ["pathology_body_part",
                         "pathology_symptom",
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
            - treatment_medicinal (boolean)
            - treatment_being_taken
            - treatment_drug
            - treatment_dosing
            - treatment_time
            - treatment_prescripted(boolean)
            - treatment_ok(boolean)
            - treatment_overdosage
            - treatment_period
            - treatment_duration
        Set slot treatment to True"""
        self.intent_name = "treatment"
        self.entities = ["treatment_medicinal",
                         "treatment_being_taken",
                         "treatment_drug",
                         "treatment_dosing",
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
            - infoPatient_addiction
            - infoPatient_weight
            - infoPatient_distance
            - infoPatient_gender
            - infoPatient_temperature
            - infoPatient_heart_rate
            - infoPatient_blood_pressure
            - infoPatient_time
        Set slot infoPatient to True"""
        self.intent_name = "infoPatient"
        self.entities = ["infoPatient_addiction",
                         "infoPatient_weight",
                         "infoPatient_distance",
                         "infoPatient_gender",
                         "infoPatient_temperature",
                         "infoPatient_heart_rate",
                         "infoPatient_blood_pressure",
                         "infoPatient_time"
                         ]


class ResetSleepSlots(ResetSlotsAction):
    """Reset slots linked to sleep intent and save infos in DB"""
    def name(self):
        """@return: the name of the action."""
        return 'reset_slots_sleep'

    def __init__(self):
        """Set all slots for intent 'sleep' to None:
            - sleep_duration
            - sleep_quality
        Set slot sleep to True"""
        self.intent_name = "sleep"
        self.entities = ["sleep_duration",
                         "sleep_quality"
                         ]


class ResetEatingDisordersSlots(ResetSlotsAction):
    """Reset slots linked to eatingDisorders intent and save infos in DB"""
    def name(self):
        """@return: the name of the action."""
        return 'reset_slots_eatingDisorders'

    def __init__(self):
        """Set all slots for intent 'eatingDisorders' to None:
            - eatingDisorders_duration
            - eatingDisorders_time
        Set slot eatingDisorders to True"""
        self.intent_name = "eatingDisorders"
        self.entities = ["eatingDisorders_duration",
                         "eatingDisorders_time"
                         ]


class ResetDrugAddictionSlots(ResetSlotsAction):
    """Reset slots linked to drugAddiction intent and save infos in DB"""
    def name(self):
        """@return: the name of the action."""
        return 'reset_slots_drugAddiction'

    def __init__(self):
        """Set all slots for intent 'drugAddiction' to None:
            - drugAddiction_period
            - drugAddiction_drug
            - drugAddiction_dosing
            - drugAddiction_duration
            - drugAddiction_time
        Set slot drugAddiction to True"""
        self.intent_name = "drugAddiction"
        self.entities = ["drugAddiction_period",
                         "drugAddiction_drug",
                         "drugAddiction_dosing",
                         "drugAddiction_duration",
                         "drugAddiction_time"
                         ]


class ResetSmokingSlots(ResetSlotsAction):
    """Reset slots linked to smoking intent and save infos in DB"""
    def name(self):
        """@return: the name of the action."""
        return 'reset_slots_smoking'

    def __init__(self):
        """Set all slots for intent 'smoking' to None:
            - smoking_period
            - smoking_dosing
            - smoking_duration
            - smoking_time
        Set slot smoking to True"""
        self.intent_name = "smoking"
        self.entities = ["smoking_period",
                         "smoking_dosing",
                         "smoking_duration",
                         "smoking_time"
                         ]


class ResetAlcoholSlots(ResetSlotsAction):
    """Reset slots linked to smoking intent and save infos in DB"""
    def name(self):
        """@return: the name of the action."""
        return 'reset_slots_alcohol'

    def __init__(self):
        """Set all slots for intent 'alcohol' to None:
            - alcohol_period
            - alcohol_dosing
            - alcohol_duration
            - alcohol_time
        Set slot smoking to True"""
        self.intent_name = "alcohol"
        self.entities = ["alcohol_period",
                         "alcohol_dosing",
                         "alcohol_duration",
                         "alcohol_time"
                         ]
