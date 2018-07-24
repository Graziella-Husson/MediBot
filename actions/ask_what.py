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
        if button_name is None:
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
        if button_name is None:
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

class AskWhatSport(Action):
    """Ask what's wrong with the infos for the intent activity"""
    def name(self):
        """@return: the name of the action."""
        return 'ask_what_sport'

    def run(self, dispatcher, tracker, domain):
        """@param tracker: used to get all infos for 'activity' intent from the tracker + language
        @param dispatcher: used to display buttons with dispatcher.utter_button_message
        Display a button for all infos the tracker have for the intent 'activity':
            - activity_period
            - activity_distance
            - sport
            - activity_duration
            - activity_hard
            - activity_time
        sport is linked to activity_level. If the sport is incorrect, activity_level too.
        When clicked, a button will reset the slot linked to it.            """
        language = tracker.get_slot("language")
        intent_name = "activity"
        buttons = []
        buttons = get_buttons_multiple(buttons, ["sport", "level"], tracker, language, intent_name, "sport")
        buttons = get_buttons_simple(buttons, "activity_duration", tracker, language, intent_name, button_name="duration_button")
        buttons = get_buttons_simple(buttons, "activity_distance", tracker, language, intent_name, button_name="distance_button")
        buttons = get_buttons_simple(buttons, "activity_period", tracker, language, intent_name, button_name="period_button")
        buttons = get_buttons_simple(buttons, "activity_hard", tracker, language, intent_name)
        buttons = get_buttons_simple(buttons, "activity_time", tracker, language, intent_name, button_name="time_button")
        message = get_utterance("ask_what", language)
        dispatcher.utter_button_message(message, buttons)

class AskWhatPain(Action):
    """Ask what's wrong with the infos for the intent pain"""
    def name(self):
        """@return: the name of the action."""
        return 'ask_what_pain'

    def run(self, dispatcher, tracker, domain):
        """@param tracker: used to get all infos for 'pain' intent from the tracker + language
        @param dispatcher: used to display buttons with dispatcher.utter_button_message(message, buttons)
        Display a button for all infos the tracker have for the intent 'pain':
            - pain_period
            - pain_desc
            - pain_body_part
            - pain_duration
            - pain_change
            - pain_time
        pain_desc is linked to pain_level. If the pain_desc is incorrect, pain_level too.
        When clicked, a button will reset the slot linked to it."""
        language = tracker.get_slot("language")
        intent_name = "pain"
        buttons = []
        buttons = get_buttons_multiple(buttons, ["pain_desc", "level"], tracker, language, intent_name, "pain_desc")
        buttons = get_buttons_simple(buttons, "pain_change", tracker, language, intent_name, button_name="evolution_button")
        buttons = get_buttons_simple(buttons, "pain_duration", tracker, language, intent_name, button_name="duration_button")
        buttons = get_buttons_simple(buttons, "pain_body_part", tracker, language, intent_name, button_name="body_part_button")
        buttons = get_buttons_simple(buttons, "pain_period", tracker, language, intent_name, button_name="period_button")
        buttons = get_buttons_simple(buttons, "pain_time", tracker, language, intent_name, button_name="time_button")
        message = get_utterance("ask_what", language)
        dispatcher.utter_button_message(message, buttons)

class AskWhatPathology(Action):
    """Ask what's wrong with the infos for the intent pathology"""
    def name(self):
        """@return: the name of the action."""
        return 'ask_what_pathology'

    def run(self, dispatcher, tracker, domain):
        """@param tracker: used to get all infos for 'pathology' intent from the tracker + language
        @param dispatcher: used to display buttons with dispatcher.utter_button_message(message, buttons)
        Display a button for all infos the tracker have for the intent 'pathology':
            - pathology_body_part
            - symtoms
            - pathology_time
            - pathology_change (boolean)
            - pathology_period
            - pathology_treatment_linked (boolean)
        When clicked, a button will reset the slot linked to it."""
        language = tracker.get_slot("language")
        intent_name = "pathology"
        buttons = []
        buttons = get_buttons_simple(buttons, "symtoms", tracker, language, intent_name)
        buttons = get_buttons_simple(buttons, "pathology_body_part", tracker, language, intent_name, button_name="body_part_button")
        buttons = get_buttons_simple(buttons, "pathology_time", tracker, language, intent_name, button_name="time_button")
        buttons = get_buttons_simple(buttons, "pathology_period", tracker, language, intent_name, button_name="period_button")
        buttons = get_buttons_boolean(buttons, "pathology_change", tracker, language, intent_name, button_name="evolution_button")
        buttons = get_buttons_boolean(buttons, "pathology_treatment_linked", tracker, language, intent_name)
        message = get_utterance("ask_what", language)
        dispatcher.utter_button_message(message, buttons)

class AskWhatTreatment(Action):
    """Ask what's wrong with the infos for the intent treatment"""
    def name(self):
        """@return: the name of the action."""
        return 'ask_what_treatment'

    def run(self, dispatcher, tracker, domain):
        """@param tracker: used to get all infos for 'treatment' intent from the tracker + language
        @param dispatcher: used to display buttons with dispatcher.utter_button_message(message, buttons)
        Display a button for all infos the tracker have for the intent 'treatment':
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
        If medicinal button is cliked, set the slot 'medicinal' to the opposite of its value.
        If medicinal button is cliked, set the slot 'treatment_prescripted' to the opposite of its value.
        If medicinal button is cliked, set the slot 'treatment_ok' to the opposite of its value.
        For others buttons, when clicked, will reset the slot linked to it."""
        language = tracker.get_slot("language")
        intent_name = "treatment"
        buttons = []
        buttons = get_buttons_boolean(buttons, "medicinal", tracker, language, intent_name)
        buttons = get_buttons_simple(buttons, "treatment_being_taken", tracker, language, intent_name, "no_drug")
        buttons = get_buttons_simple(buttons, "drug", tracker, language, intent_name, "no_drug")
        buttons = get_buttons_simple(buttons, "dosing", tracker, language, intent_name, "no_drug")
        buttons = get_buttons_simple(buttons, "treatment_period", tracker, language, intent_name, button_name="period_button")
        buttons = get_buttons_simple(buttons, "treatment_time", tracker, language, intent_name, button_name="time_button")
        buttons = get_buttons_simple(buttons, "treatment_overdosage", tracker, language, intent_name, "no_drug")
        buttons = get_buttons_simple(buttons, "treatment_duration", tracker, language, intent_name, button_name="duration_button")
        buttons = get_buttons_boolean(buttons, "treatment_prescripted", tracker, language, intent_name)
        buttons = get_buttons_boolean(buttons, "treatment_ok", tracker, language, intent_name)
        message = get_utterance("ask_what", language)
        dispatcher.utter_button_message(message, buttons)

class AskWhatInfoPatient(Action):
    """Ask what's wrong with the infos for the intent infoPatient"""
    def name(self):
        """@return: the name of the action."""
        return 'ask_what_info_patient'

    def run(self, dispatcher, tracker, domain):
        """@param tracker: used to get all infos for 'info_patient' intent from the tracker + language
        @param dispatcher: used to display buttons with dispatcher.utter_button_message(message, buttons)
        Display a button for all infos the tracker have for the intent 'info_patient':
            - addiction
            - weight
            - infoPatient_distance
            - gender
            - infoPatient_temperature
            - heart_rate
            - blood_pressure
            - infoPatient_time
        When clicked, the button will reset the slot linked to it."""
        language = tracker.get_slot("language")
        intent_name = "infoPatient"
        buttons = []
        buttons = get_buttons_simple(buttons, "addiction", tracker, language, intent_name)
        buttons = get_buttons_simple(buttons, "weight", tracker, language, intent_name)
        buttons = get_buttons_simple(buttons, "infoPatient_distance", tracker, language, intent_name, button_name="size_button")
        buttons = get_buttons_simple(buttons, "gender", tracker, language, intent_name)
        buttons = get_buttons_simple(buttons, "infoPatient_temperature", tracker, language, intent_name, button_name="temperature_button")
        buttons = get_buttons_simple(buttons, "heart_rate", tracker, language, intent_name)
        buttons = get_buttons_simple(buttons, "blood_pressure", tracker, language, intent_name)
        buttons = get_buttons_simple(buttons, "infoPatient_time", tracker, language, intent_name, button_name="date_check_up_button")
        message = get_utterance("ask_what", language)
        dispatcher.utter_button_message(message, buttons)
