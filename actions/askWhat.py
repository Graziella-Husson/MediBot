from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.dispatcher import Button
from ressources import get_utterance
from initAndComplex import get_complex_entities

def get_buttons_simple(buttons, slot_name, tracker,language,intent_name,other_value=None):
    slot_value = tracker.get_slot(slot_name)
    to_search_in_ressources = ""
    every = get_complex_entities()
    for i in every:
        if i in slot_name:
            to_search_in_ressources = i+"_button"
    if to_search_in_ressources == "":
        to_search_in_ressources = slot_name+"_button"
    if slot_value != None :
        if other_value == None or (other_value != None and slot_value != other_value):
            slot_button = get_utterance(to_search_in_ressources,language)
            buttons.append(Button(title=slot_button, payload="/"+intent_name+"{\""+slot_name+"\":null}"))   
    return buttons

def get_buttons_boolean(buttons, slot_name, tracker,language,intent_name):
    slot_value = tracker.get_slot(slot_name)
    if slot_value != None:
            slot_button = get_utterance(slot_name+"_button",language)
            if slot_value:
                buttons.append(Button(title=slot_button, payload="/"+intent_name+"{\""+slot_name+"\":false}"))
            else:
                buttons.append(Button(title=slot_button, payload="/"+intent_name+"{\""+slot_name+"\":true}"))   
    return buttons

class AskWhatSport(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'ask_what_sport'
        
    def run(self, dispatcher, tracker, domain):  
        """
        @param tracker: used to get all infos for 'activity' intent from the tracker + language
        @param dispatcher: used to display buttons with dispatcher.utter_button_message
        
        Display a button for all infos the tracker have for the intent 'activity':
            - activity_period
            - activity_distance
            - sport
            - activity_duration
            - activity_hard
            - activity_time
            
        sport is linked to sport_level. If the sport is incorrect, sport_level too.
        When clicked, a button will reset the slot linked to it.            
        """      
        language = tracker.get_slot("language")
        intent_name = "activity"
        sport = tracker.get_slot("sport")
        buttons = []
        if sport != None:
            sport_button = get_utterance("sport_button",language)
            level_button = get_utterance("level_button",language)
            buttons.append(Button(title=sport_button, payload="/activity{\"sport\":null}"))
            buttons.append(Button(title=level_button, payload="/activity{\"sport_level\":\"Incorrect\"}"))
        buttons = get_buttons_simple(buttons, "activity_duration", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "activity_distance", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "activity_period", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "activity_hard", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "activity_time", tracker,language,intent_name)
        message = get_utterance("ask_what",language)
        dispatcher.utter_button_message(message, buttons)
        
class AskWhatPain(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'ask_what_pain'
        
    def run(self, dispatcher, tracker, domain):  
        """
        @param tracker: used to get all infos for 'pain' intent from the tracker + language
        @param dispatcher: used to display buttons with dispatcher.utter_button_message(message, buttons)
        
        Display a button for all infos the tracker have for the intent 'pain':
            - pain_period
            - pain_desc
            - pain_body_part
            - pain_duration
            - pain_change
            - pain_time
            
        pain_desc is linked to pain_level. If the pain_desc is incorrect, pain_level too.
        When clicked, a button will reset the slot linked to it.            
        """      
        language = tracker.get_slot("language")
        intent_name = "pain"
        desc = tracker.get_slot("pain_desc")
        evolution = tracker.get_slot("pain_change")
        buttons = []
        if desc != None:
            desc_button = get_utterance("desc_button",language)
            level_button = get_utterance("level_button",language)
            buttons.append(Button(title=desc_button, payload="/pain{\"pain_desc\":null}"))
            buttons.append(Button(title=level_button, payload="/pain{\"pain_level\":\"Incorrect\"}"))
        if evolution != None:
            evolution_button = get_utterance("evolution_button",language)
            buttons.append(Button(title=evolution_button, payload="/pain{\"pain_change\":null}"))
        buttons = get_buttons_simple(buttons, "pain_duration", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "pain_body_part", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "pain_period", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "pain_time", tracker,language,intent_name)
        message = get_utterance("ask_what",language)
        dispatcher.utter_button_message(message, buttons)
        
class AskWhatPathology(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'ask_what_pathology'
        
    def run(self, dispatcher, tracker, domain):  
        """
        @param tracker: used to get all infos for 'pathology' intent from the tracker + language
        @param dispatcher: used to display buttons with dispatcher.utter_button_message(message, buttons)
        
        Display a button for all infos the tracker have for the intent 'pathology':
            - pathology_body_part
            - symtoms
            - pathology_time
            - pathology_change (boolean)
            - pathology_period
            - pathology_treatment_linked (boolean)
            
        When clicked, a button will reset the slot linked to it.            
        """      
        language = tracker.get_slot("language")
        intent_name = "pathology"
        buttons = []
        buttons = get_buttons_simple(buttons, "symtoms", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "pathology_body_part", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "pathology_time", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "pathology_period", tracker,language,intent_name)
        buttons = get_buttons_boolean(buttons, "pathology_change", tracker,language,intent_name)
        buttons = get_buttons_boolean(buttons, "pathology_treatment_linked", tracker,language,intent_name)
        message = get_utterance("ask_what",language)
        dispatcher.utter_button_message(message, buttons)
               
class AskWhatTreatment(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'ask_what_treatment'
        
    def run(self, dispatcher, tracker, domain):  
        """
        @param tracker: used to get all infos for 'treatment' intent from the tracker + language
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
            
        If medicinal button is cliked, set the slot 'medicinal' to the opposite of its value.
        If medicinal button is cliked, set the slot 'treatment_prescripted' to the opposite of its value.
        If medicinal button is cliked, set the slot 'treatment_ok' to the opposite of its value.
        For others buttons, when clicked, will reset the slot linked to it.            
        """      
        language = tracker.get_slot("language")
        intent_name = "treatment"
        buttons = []
        buttons = get_buttons_boolean(buttons, "medicinal", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "treatment_being_taken", tracker,language,intent_name,"no_drug")
        buttons = get_buttons_simple(buttons, "drug", tracker,language,intent_name,"no_drug")
        buttons = get_buttons_simple(buttons, "dosing", tracker,language,intent_name,"no_drug")
        buttons = get_buttons_simple(buttons, "treatment_period", tracker,language,intent_name,"no_drug")
        buttons = get_buttons_simple(buttons, "treatment_time", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "treatment_overdosage", tracker,language,intent_name)
        buttons = get_buttons_boolean(buttons, "treatment_prescripted", tracker,language,intent_name)
        buttons = get_buttons_boolean(buttons, "treatment_ok", tracker,language,intent_name)
        message = get_utterance("ask_what",language)
        dispatcher.utter_button_message(message, buttons)
               
class AskWhatInfoPatient(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'ask_what_info_patient'
        
    def run(self, dispatcher, tracker, domain):  
        """
        @param tracker: used to get all infos for 'info_patient' intent from the tracker + language
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
            
        When clicked, the button will reset the slot linked to it.            
        """      
        language = tracker.get_slot("language")
        intent_name = "infoPatient"
        date_check_up = tracker.get_slot("infoPatient_time")
        buttons = []
        buttons = get_buttons_simple(buttons, "addiction", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "weight", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "infoPatient_distance", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "gender", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "infoPatient_temperature", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "heart_rate", tracker,language,intent_name)
        buttons = get_buttons_simple(buttons, "blood_pressure", tracker,language,intent_name)
        if date_check_up != None:
            date_check_up_button = get_utterance("date_check_up_button",language)
            buttons.append(Button(title=date_check_up_button, payload="/info_patient{\"infoPatient_time\":null}"))
        message = get_utterance("ask_what",language)
        dispatcher.utter_button_message(message, buttons)