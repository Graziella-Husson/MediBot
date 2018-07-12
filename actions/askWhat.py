from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.dispatcher import Button
from ressources import get_utterance

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
        sport_period = tracker.get_slot("activity_period")
        distance = tracker.get_slot("activity_distance")
        sport = tracker.get_slot("sport")
        duration = tracker.get_slot("activity_duration")
        activity_hard = tracker.get_slot("activity_hard")
        activity_time = tracker.get_slot("activity_time")
        buttons = []
        if sport != None:
            sport_button = get_utterance("sport_button",language)
            level_button = get_utterance("level_button",language)
            buttons.append(Button(title=sport_button, payload="/activity{\"sport\":null}"))
            buttons.append(Button(title=level_button, payload="/activity{\"sport_level\":\"Incorrect\"}"))
        if duration != None:
            duration_button = get_utterance("duration_button",language)
            buttons.append(Button(title=duration_button, payload="/activity{\"activity_duration\":null}"))
        if distance != None:
            distance_button = get_utterance("distance_button",language)
            buttons.append(Button(title=distance_button, payload="/activity{\"activity_distance\":null}"))
        if sport_period != None:
            period_button = get_utterance("period_button",language)
            buttons.append(Button(title=period_button, payload="/activity{\"activity_period\":null}"))
        if activity_hard != None:
            activity_hard_button = get_utterance("activity_hard_button",language)
            buttons.append(Button(title=activity_hard_button, payload="/activity{\"activity_hard\":null}"))   
        if activity_time != None:
            time_button = get_utterance("time_button",language)
            buttons.append(Button(title=time_button, payload="/activity{\"activity_time\":null}"))       
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
        pain_period = tracker.get_slot("pain_period")
        desc = tracker.get_slot("pain_desc")
        duration = tracker.get_slot("pain_duration")
        pain_body_part = tracker.get_slot("pain_body_part")
        evolution = tracker.get_slot("pain_change")
        time = tracker.get_slot("pain_time")
        buttons = []
        if desc != None:
            desc_button = get_utterance("desc_button",language)
            level_button = get_utterance("level_button",language)
            buttons.append(Button(title=desc_button, payload="/pain{\"pain_desc\":null}"))
            buttons.append(Button(title=level_button, payload="/pain{\"pain_level\":\"Incorrect\"}"))
        if duration != None:
            duration_button = get_utterance("duration_button",language)
            buttons.append(Button(title=duration_button, payload="/pain{\"pain_duration\":null}"))
        if pain_body_part != None:
            body_part_button = get_utterance("body_part_button",language)
            buttons.append(Button(title=body_part_button, payload="/pain{\"pain_body_part\":null}"))
        if evolution != None:
            evolution_button = get_utterance("evolution_button",language)
            buttons.append(Button(title=evolution_button, payload="/pain{\"pain_change\":null}"))
        if pain_period != None:
            period_button = get_utterance("period_button",language)
            buttons.append(Button(title=period_button, payload="/pain{\"pain_period\":null}"))
        if time != None:
            time_button = get_utterance("time_button",language)
            buttons.append(Button(title=time_button, payload="/pain{\"pain_time\":null}"))
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
            - symtoms
            - pathology_body_part
            
        When clicked, a button will reset the slot linked to it.            
        """      
        language = tracker.get_slot("language")
        symtoms = tracker.get_slot("symtoms")
        pathology_body_part = tracker.get_slot("pathology_body_part")
        buttons = []
        if symtoms != None:
            symtoms_button = get_utterance("symtoms_button",language)
            buttons.append(Button(title=symtoms_button, payload="/pathology{\"symtoms\":null}"))
        if pathology_body_part != None:
            body_part_button = get_utterance("body_part_button",language)
            buttons.append(Button(title=body_part_button, payload="/pathology{\"pathology_body_part\":null}"))
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
            - drug
            
        If medicinal button is cliked, set the slot 'medicinal' to the opposite of its value.
        For others buttons, when clicked, will reset the slot linked to it.            
        """      
        language = tracker.get_slot("language")
        medicinal = tracker.get_slot("medicinal")
        drug = tracker.get_slot("drug")
        buttons = []
        if medicinal != None:
            medicinal_button = get_utterance("medicinal_button",language)
            if medicinal:
                buttons.append(Button(title=medicinal_button, payload="/treatment{\"medicinal\":false, \"drug\":\"no_drug\"}"))
            else:
                buttons.append(Button(title=medicinal_button, payload="/treatment{\"medicinal\":true}"))                
        if drug != None:
            drug_button = get_utterance("drug_button",language)
            buttons.append(Button(title=drug_button, payload="/treatment{\"drug\":null}"))
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
        addiction = tracker.get_slot("addiction")
        weight = tracker.get_slot("weight")
        size = tracker.get_slot("infoPatient_distance")
        gender = tracker.get_slot("gender")
        temperature = tracker.get_slot("infoPatient_temperature")
        heart_rate = tracker.get_slot("heart_rate")
        blood_pressure = tracker.get_slot("blood_pressure")
        date_check_up = tracker.get_slot("infoPatient_time")
        buttons = []
        if addiction != None:
            addiction_button = get_utterance("addiction_button",language)
            buttons.append(Button(title=addiction_button, payload="/info_patient{\"addiction\":null}"))
        if weight != None:
            weight_button = get_utterance("weight_button",language)
            buttons.append(Button(title=weight_button, payload="/info_patient{\"weight\":null}"))
        if size != None:
            size_button = get_utterance("size_button",language)
            buttons.append(Button(title=size_button, payload="/info_patient{\"infoPatient_distance\":null}"))
        if gender != None:
            gender_button = get_utterance("gender_button",language)
            buttons.append(Button(title=gender_button, payload="/info_patient{\"gender\":null}"))
        if temperature != None:
            temperature_button = get_utterance("temperature_button",language)
            buttons.append(Button(title=temperature_button, payload="/info_patient{\"infoPatient_temperature\":null}"))
        if heart_rate != None:
            heart_rate_button = get_utterance("heart_rate_button",language)
            buttons.append(Button(title=heart_rate_button, payload="/info_patient{\"heart_rate\":null}"))
        if blood_pressure != None:
            blood_pressure_button = get_utterance("blood_pressure_button",language)
            buttons.append(Button(title=blood_pressure_button, payload="/info_patient{\"blood_pressure\":null}"))
        if date_check_up != None:
            date_check_up_button = get_utterance("date_check_up_button",language)
            buttons.append(Button(title=date_check_up_button, payload="/info_patient{\"infoPatient_time\":null}"))
        message = get_utterance("ask_what",language)
        dispatcher.utter_button_message(message, buttons)