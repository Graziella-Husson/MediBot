"""
This module is used to regroup all ask what actions.\n
An ask what action is an action where the bot will ask with buttons
what's wrong with the infos it has collected\n
Created on Tue Jun 26 10:22:40 2018\n
@author: U{@Graziella-Husson<https://github.com/Graziella-Husson>}
"""
from rasa_core.actions.action import Action
from rasa_core.dispatcher import Button
from ressources import get_utterance

def get_buttons_simple(buttons, slot_name, tracker, language, intent_name, other_value=None, button_name=None):
    """@param buttons: list of buttons in which we have to append new ones
    @param slot_name: name of the slot we want to add a button for
    @param tracker: used to get all infos for 'slot_name' entity from the tracker
    @param language: language of the bot (for display the right name of button)
    @param intent_name: name of the intent linked to the slot
    @param other_value: unrequired, if the slot value is set to this value, do not add a button
    @param button_name: unrequired, name of the button if different to {slot_name}_button\n
    Add a button to the list of buttons to display, named after the slot name.
    If the button is clicked, set the slot value to None\n
    @return: list of buttons in which we appended new ones"""
    slot_value = tracker.get_slot(slot_name)
    if slot_value is not None:
        if button_name is not None:
            to_search_in_ressources = button_name
        else:
            to_search_in_ressources = slot_name+"_button"
        if other_value is None or (other_value is not None and slot_value != other_value):
            slot_button = get_utterance(to_search_in_ressources, language)
            buttons.append(Button(title=slot_button,
                                  payload="/"+intent_name+"{\""+slot_name+"\":null}"))
    return buttons

def get_buttons_multiple(buttons, slot_names, tracker, language, intent_name, to_check):
    """@param buttons: list of buttons in which we have to append new ones
    @param slot_names: list of names of the slots we want to add a button for
    @param tracker: used to get all infos for 'slot_name' entity from the tracker
    @param language: language of the bot (for display the right name of button)
    @param intent_name: name of the intent linked to the slot
    @param to_check: value to check, if not set, do not display the buttons\n
    Add multiple buttons to the list of buttons to display,
    named after the slot names.
    If the button is clicked, set the slot value to None
    If the button clicked is not named after to_check,
    set the slot value to "Incorrect"\n
    @return: list of buttons in which we appended new ones"""
    to_check_value = tracker.get_slot(to_check)
    if to_check_value is not None:
        for slot_name in slot_names:
            to_search_in_ressources = slot_name+"_button"
            slot_button = get_utterance(to_search_in_ressources, language)
            if slot_name != to_check:
                buttons.append(Button(title=slot_button,
                                      payload="/"+intent_name+"{\""+intent_name+"_"+slot_name+"\":\"Incorrect\"}"))
            else:
                buttons.append(Button(title=slot_button,
                                      payload="/"+intent_name+"{\""+slot_name+"\":null}"))
    return buttons

def get_buttons_boolean(buttons, slot_name, tracker, language, intent_name, button_name=None):
    """@param buttons: list of buttons in which we have to append new ones
    @param slot_name: name of the boolean slot we want to add a button for
    @param tracker: used to get all infos for 'slot_name' entity from the tracker
    @param language: language of the bot (for display the right name of button)
    @param intent_name: name of the intent linked to the slot
    @param button_name: unrequired, name of the button if different to {slot_name}_button\n
    Add a button to the list of buttons to display, named after the slot names.
    If the slot value is True, when the button is clicked, set the slot value to False
    If the slot value is False, when the button is clicked, set the slot value to True\n
    @return: list of buttons in which we appended new ones"""
    slot_value = tracker.get_slot(slot_name)
    if slot_value is not None:
        if button_name is not None:
            to_search_in_ressources = button_name
        else:
            to_search_in_ressources = slot_name+"_button"
        slot_button = get_utterance(to_search_in_ressources, language)
        if slot_value:
            buttons.append(Button(title=slot_button,
                                  payload="/"+intent_name+"{\""+slot_name+"\":false}"))
        else:
            buttons.append(Button(title=slot_button,
                                  payload="/"+intent_name+"{\""+slot_name+"\":true}"))
    return buttons


class AskWhatAction(Action):
    intent_name = ""
    simple_buttons = []
    boolean_buttons = []
    multiple_buttons = []

    def check(self):
        """Used to check if all proprieties has been set"""
        if self.intent_name == "" or (len(self.simple_buttons) == 0 and len(self.boolean_buttons) == 0 and len(self.multiple_buttons) == 0):
                raise NotImplementedError("""
                a AskAction action must implement a __init__ method
                with a intent_name and minimun one of simple_buttons,
                boolean_buttons and multiple_buttons list""")

    def name(self):
        """the name of the action to implement"""
        raise NotImplementedError("""a AskWhatAction action must
                                    implement a name method""")

    def run(self, dispatcher, tracker, domain):
        language = tracker.get_slot("language")
        buttons = []
        for button in self.simple_buttons:
            if type(button) == list:
                if len(button) == 3:
                    buttons = get_buttons_simple(buttons, button[0], tracker, language, self.intent_name, button[2])
                else:
                    buttons = get_buttons_simple(buttons, button[0], tracker, language, self.intent_name, button_name=button[1])
            else:
                buttons = get_buttons_simple(buttons, button, tracker, language, self.intent_name)
        for button in self.boolean_buttons:
            if type(button) == list:
                buttons = get_buttons_boolean(buttons, button[0], tracker, language, self.intent_name, button_name=button[1])
            else:
                buttons = get_buttons_boolean(buttons, button, tracker, language, self.intent_name)
        for button in self.multiple_buttons:
            buttons = get_buttons_multiple(buttons, button[0], tracker, language, self.intent_name, button[1])
        if len(buttons) > 0:
            message = get_utterance("ask_what", language)
            dispatcher.utter_button_message(message, buttons)


class AskWhatSport(AskWhatAction):
    """Ask what's wrong with the infos for the intent activity"""
    def name(self):
        """@return: the name of the action."""
        return 'ask_what_sport'

    def __init__(self):
        """Display a button for all infos the tracker have for the intent 'activity':
            - activity_period
            - activity_distance
            - sport
            - activity_duration
            - activity_hard
            - activity_time
        sport is linked to activity_level.
        If the sport is incorrect, activity_level too.
        When clicked, a button will reset the slot linked to it."""
        self.intent_name = "activity"
        self.simple_buttons = [["activity_duration", "duration_button"],
                               ["activity_distance", "distance_button"],
                               ["activity_period", "period_button"],
                               ["activity_time", "time_button"],
                               "activity_hard"]
        self.multiple_buttons = [[["sport", "level"], "sport"]]


class AskWhatPain(AskWhatAction):
    """Ask what's wrong with the infos for the intent pain"""
    def name(self):
        """@return: the name of the action."""
        return 'ask_what_pain'

    def __init__(self):
        """Display a button for all infos the tracker have for the intent 'pain':
            - pain_period
            - pain_desc
            - pain_body_part
            - pain_duration
            - pain_change
            - pain_time
        pain_desc is linked to pain_level. If the pain_desc is incorrect,
        pain_level too.
        When clicked, a button will reset the slot linked to it."""
        self.intent_name = "pain"
        self.simple_buttons = [["pain_change", "evolution_button"],
                               ["pain_duration", "duration_button"],
                               ["pain_body_part", "body_part_button"],
                               ["pain_period", "period_button"],
                               ["pain_time", "time_button"]]
        self.multiple_buttons = [[["pain_desc", "level"], "pain_desc"]]


class AskWhatPathology(AskWhatAction):
    """Ask what's wrong with the infos for the intent pathology"""
    def name(self):
        """@return: the name of the action."""
        return 'ask_what_pathology'

    def __init__(self):
        """Display a button for all infos the tracker have for the intent 'pathology':
            - pathology_body_part
            - symtoms
            - pathology_time
            - pathology_change (boolean)
            - pathology_period
            - pathology_treatment_linked (boolean)
        When clicked, a button will reset the slot linked to it."""
        self.intent_name = "pathology"
        self.simple_buttons = [["pathology_body_part", "body_part_button"],
                               ["pathology_time", "time_button"],
                               ["pathology_period", "period_button"],
                               "symtoms"]
        self.boolean_buttons = [["pathology_change", "evolution_button"],
                                "pathology_treatment_linked"]


class AskWhatTreatment(AskWhatAction):
    """Ask what's wrong with the infos for the intent treatment"""
    def name(self):
        """@return: the name of the action."""
        return 'ask_what_treatment'

    def __init__(self):
        """Display a button for all infos the tracker have for the intent 'treatment':
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
        If medicinal button is cliked,
        set the slot 'medicinal' to the opposite of its value.
        If medicinal button is cliked,
        set the slot 'treatment_prescripted' to the opposite of its value.
        If medicinal button is cliked,
        set the slot 'treatment_ok' to the opposite of its value.
        For others buttons, when clicked, will reset the slot linked to it."""
        self.intent_name = "treatment"
        self.simple_buttons = [["treatment_period", "period_button"],
                               ["treatment_time", "time_button"],
                               ["treatment_duration", "duration_button"],
                               ["treatment_overdosage", None, "no_drug"],
                               ["dosing", None, "no_drug"],
                               ["drug", None, "no_drug"],
                               ["treatment_being_taken", None, "no_drug"]]
        self.boolean_buttons = ["treatment_prescripted",
                                "medicinal",
                                "treatment_ok"]


class AskWhatInfoPatient(AskWhatAction):
    """Ask what's wrong with the infos for the intent infoPatient"""
    def name(self):
        """@return: the name of the action."""
        return 'ask_what_info_patient'

    def __init__(self):
        """Display a button for all infos the tracker
        have for the intent 'info_patient':
            - addiction
            - weight
            - infoPatient_distance
            - gender
            - infoPatient_temperature
            - heart_rate
            - blood_pressure
            - infoPatient_time
        When clicked, the button will reset the slot linked to it."""
        self.intent_name = "infoPatient"
        self.simple_buttons = [["infoPatient_distance", "size_button"],
                               ["infoPatient_temperature", "temperature_button"],
                               ["infoPatient_time", "date_check_up_button"],
                               "addiction",
                               "weight",
                               "gender",
                               "heart_rate",
                               "blood_pressure"]
