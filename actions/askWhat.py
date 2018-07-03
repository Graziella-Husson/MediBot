from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.dispatcher import Button

class AskWhatSport(Action):
    def name(self):
        return 'ask_what_sport'
        
    def run(self, dispatcher, tracker, domain):
        sport_period = tracker.get_slot("activity_period")
        distance = tracker.get_slot("activity_distance")
        sport = tracker.get_slot("sport")
        duration = tracker.get_slot("activity_duration")
        activity_hard = tracker.get_slot("activity_hard")
        activity_time = tracker.get_slot("activity_time")
        buttons = []
        if sport != None:
            buttons.append(Button(title="Sport", payload="/activity{\"sport\":null}"))
            buttons.append(Button(title="Level", payload="/activity{\"sport_level\":\"Incorrect\"}"))
        if duration != None:
            buttons.append(Button(title="Duration", payload="/activity{\"activity_duration\":null}"))
        if distance != None:
            buttons.append(Button(title="Distance", payload="/activity{\"activity_distance\":null}"))
        if sport_period != None:
            buttons.append(Button(title="Period", payload="/activity{\"activity_period\":null}"))
        if activity_hard != None:
            buttons.append(Button(title="Hardness", payload="/activity{\"activity_hard\":null}"))   
        if activity_time != None:
            buttons.append(Button(title="Begin date", payload="/activity{\"activity_time\":null}"))            
        dispatcher.utter_button_message("Ok. So, tell me what's wrong? Click on a button or tell me above!", buttons)
        
class AskWhatPain(Action):
    def name(self):
        return 'ask_what_pain'
        
    def run(self, dispatcher, tracker, domain):
        pain_period = tracker.get_slot("pain_period")
        desc = tracker.get_slot("pain_desc")
        duration = tracker.get_slot("pain_duration")
        pain_body_part = tracker.get_slot("pain_body_part")
        evolution = tracker.get_slot("pain_change")
        time = tracker.get_slot("pain_time")
        buttons = []
        if desc != None:
            buttons.append(Button(title="Description", payload="/pain{\"pain_desc\":null}"))
            buttons.append(Button(title="Level", payload="/pain{\"pain_level\":\"Incorrect\"}"))
        if duration != None:
            buttons.append(Button(title="Duration", payload="/pain{\"pain_duration\":null}"))
        if pain_body_part != None:
            buttons.append(Button(title="Body part", payload="/pain{\"pain_body_part\":null}"))
        if evolution != None:
            buttons.append(Button(title="Evolution", payload="/pain{\"pain_change\":null}"))
        if pain_period != None:
            buttons.append(Button(title="Period", payload="/pain{\"pain_period\":null}"))
        if time != None:
            buttons.append(Button(title="Begin date", payload="/pain{\"pain_time\":null}"))
        dispatcher.utter_button_message("Ok. So, tell me what's wrong? Click on a button or tell me above!", buttons)

class AskWhatPathology(Action):
    def name(self):
        return 'ask_what_pathology'
        
    def run(self, dispatcher, tracker, domain):
        symtoms = tracker.get_slot("symtoms")
        pathology_body_part = tracker.get_slot("pathology_body_part")
        buttons = []
        if symtoms != None:
            buttons.append(Button(title="Symtoms", payload="/pathology{\"symtoms\":null}"))
        if pathology_body_part != None:
            buttons.append(Button(title="Body part", payload="/pathology{\"pathology_body_part\":null}"))
        dispatcher.utter_button_message("Ok. So, tell me what's wrong? Click on a button or tell me above!", buttons)

class AskWhatTreatment(Action):
    def name(self):
        return 'ask_what_treatment'
        
    def run(self, dispatcher, tracker, domain):
        medicinal = tracker.get_slot("medicinal")
        drug = tracker.get_slot("drug")
        buttons = []
        if medicinal != None:
            if medicinal:
                buttons.append(Button(title="Medicinal", payload="/treatment{\"medicinal\":false, \"drug\":\"no_drug\"}"))
            else:
                buttons.append(Button(title="Medicinal", payload="/treatment{\"medicinal\":true}"))                
        if drug != None:
            buttons.append(Button(title="Drug", payload="/treatment{\"drug\":null}"))
        dispatcher.utter_button_message("Ok. So, tell me what's wrong? Click on a button or tell me above!", buttons)

class AskWhatInfoPatient(Action):
    def name(self):
        return 'ask_what_info_patient'
        
    def run(self, dispatcher, tracker, domain):
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
            buttons.append(Button(title="Addiction", payload="/info_patient{\"addiction\":null}"))
        if weight != None:
            buttons.append(Button(title="Weight", payload="/info_patient{\"weight\":null}"))
        if size != None:
            buttons.append(Button(title="Size", payload="/info_patient{\"infoPatient_distance\":null}"))
        if gender != None:
            buttons.append(Button(title="Gender", payload="/info_patient{\"gender\":null}"))
        if temperature != None:
            buttons.append(Button(title="Temperature", payload="/info_patient{\"infoPatient_temperature\":null}"))
        if heart_rate != None:
            buttons.append(Button(title="Heart rate", payload="/info_patient{\"heart_rate\":null}"))
        if blood_pressure != None:
            buttons.append(Button(title="Blood pressure", payload="/info_patient{\"blood_pressure\":null}"))
        if date_check_up != None:
            buttons.append(Button(title="Date last check up", payload="/info_patient{\"infoPatient_time\":null}"))
        dispatcher.utter_button_message("Ok. So, tell me what's wrong? Click on a button or tell me above!", buttons)
