from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.events import SlotSet
from rasa_core.dispatcher import Button
from pain_classifier import get_pain_level
from physical_activity_classifier import get_physical_activity_level

from rasa_core.actions.forms import (
EntityFormField,
FormAction,
BooleanFormField
)

from initAndComplex import get_obligatories

class ActionFillSlotsPain(FormAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields():
        obligatories = get_obligatories()
        try:
            return obligatories['pain']
        except:
            return []
    
    def name(self):
        return 'action_check_slots_pain'
    
    def submit(self, dispatcher, tracker, domain):
        level = tracker.get_slot("pain_level")
        if not level == "Incorrect":
            pain_duration = tracker.get_slot("pain_duration")
            pain_desc = tracker.get_slot("pain_desc")
            pain_body_part = tracker.get_slot("pain_body_part")
            pain_change = tracker.get_slot("pain_change")
            pain_period = tracker.get_slot("pain_period")
            obligatories = get_obligatories()
            try:
                len(obligatories['pain'])
                response = "To sum up:\n"
                if pain_desc != None:
                    if level == None:
                        #get pain level
                        level = get_pain_level(pain_desc)                
                        tracker.update(SlotSet("pain_level",level))
                        #TODO : do something if None
                    response += "\tYou have some {} pain (it's considered has a {} pain).\n".format(pain_desc, level)
                if pain_body_part != None:
                    response += "\tThe pain is localized at {}.\n".format(pain_body_part)
                if pain_duration != None:
                    response += "\tThe duration of this pain is of {}.\n".format(pain_duration)
                if pain_period != None:
                    response += "\tThe period/recurrence is {}.\n".format(pain_period)
                if pain_change != None:
                    response += "\tThe pain seems to be {}.\n".format(pain_change)
                response += "Is it right?"
            except:
                response= "So, you feel some pain."
                # TODO: add to database
            tracker.update(SlotSet("topic",None))
            tracker.update(SlotSet("requested_slot",None))
            dispatcher.utter_message(response)
        else:
            buttons = [Button(title="Mild", payload="/pain{\"pain_level\":\"mild\"}"),
                       Button(title="Moderate", payload="/pain{\"pain_level\":\"moderate\"}"),
                       Button(title="Severe", payload="/pain{\"pain_level\":\"severe\"}")]
            dispatcher.utter_button_message("I failed to calculate your pain level. Can you tell me it? Click on one of the buttons above.", buttons)
        
        
class ActionFillSlotsSport(FormAction):
    RANDOMIZE = True

    @staticmethod
    def required_fields():
        obligatories = get_obligatories()
        try:
            return obligatories['activity']    
        except:
            return []    
    
    def name(self):
        return 'action_check_slots_sport'
    
    def submit(self, dispatcher, tracker, domain):
        sport_level = tracker.get_slot("sport_level")
        if not sport_level == "Incorrect":
            sport_duration = tracker.get_slot("activity_duration")
            sport = tracker.get_slot("sport")
            sport_period = tracker.get_slot("activity_period")
            distance = tracker.get_slot("activity_distance")
            activity_hard = tracker.get_slot("activity_hard")
            try:
                obligatories = get_obligatories()
                len(obligatories['activity'])>0
                response = "To sum up:\n"
                if sport != None:
                    if sport_level == None:
                        #get sport level
                        sport_level = get_physical_activity_level(sport)
                        tracker.update(SlotSet("sport_level",sport_level))
                        #TODO: do something if None
                        if sport_level=='little':
                            MET = "< 3 MET"
                        elif sport_level=='moderate':
                            MET = "3-6 MET"
                        elif sport_level=='vigorous':
                            MET = "> 6 MET"
                    response += "\tYou did some {} physical activity ({}). The sport detected is {}.\n".format(sport_level, MET, sport)
                if sport_duration != None:
                    response += "\tThe duration is of {}.\n".format(sport_duration)
                if distance != None:
                    response += "\tThe distance you did is of {}.\n".format(distance)
                if sport_period != None:
                    response +="\tThe period/recurrence detected is {}.\n".format(sport_period)
                if activity_hard != None:
                    if activity_hard:
                        response +="\tYour activity was hard because of your general health.\n"
                    else:
                        response +="\tYour general health did not make your activity harder.\n"
                response += "Is it right?"
            except:
                response= "So, you did some physical activities."
                # TODO: save in database
            tracker.update(SlotSet("topic",None))
            tracker.update(SlotSet("requested_slot",None))
            dispatcher.utter_message(response)
        else:
            buttons = [Button(title="Little", payload="/pain{\"sport_level\":\"little\"}"),
                       Button(title="Moderate", payload="/pain{\"sport_level\":\"moderate\"}"),
                       Button(title="Vigorous", payload="/pain{\"sport_level\":\"vigorous\"}")]
            dispatcher.utter_button_message("I failed to calculate your physical activity level. Can you tell me it? Click on one of the buttons above.", buttons)
        

class CheckRequestedIntents(FormAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields():
        obligatories = get_obligatories() 
        try:
            return obligatories['requested_intent']
        except:
            return []
    
    def name(self):
        return 'action_check_intents'
    
    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_message("We talked about everything we had to! But feel free to talk to me about avrything else!")

class Sadness(FormAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields():
        obligatories = get_obligatories()
        try:
            return obligatories['emotional_sadness']
        except:
            return []

    def name(self):
        return 'sum_up_emotionnal_sadness'
        
    def submit(self, dispatcher, tracker, domain):
        global_score = tracker.get_slot('global_score')
        global_score+=1
        #TODO: save score
        response = "It seems that you are in a bad mood... Do you want to talk about it in details?"
        dispatcher.utter_message(response)
        tracker.update(SlotSet("emotional_sadness",True))
        tracker.update(SlotSet("global_score",global_score))
      
class Happy(FormAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields():
        obligatories = get_obligatories()
        try:
            return obligatories['emotional_hapiness']
        except:
            return []
        
    def name(self):
        return 'sum_up_emotional_hapiness'
        
    def submit(self, dispatcher, tracker, domain):
        global_score = tracker.get_slot('global_score')
        global_score+=3
        #TODO: save score
        response = "Great! You are in a good mood!"
        dispatcher.utter_message(response)
        tracker.update(SlotSet("emotional_hapiness",True))
        tracker.update(SlotSet("global_score",global_score))

class Social(FormAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields():
        obligatories = get_obligatories()
        try:
            return obligatories['social']
        except:
            return []
        
    def name(self):
        return 'sum_up_social'
        
    def submit(self, dispatcher, tracker, domain):
        global_score = tracker.get_slot('global_score')
        global_score+=2
        #TODO: save score
        response = "It seems that you talked about a social thing."
        dispatcher.utter_message(response)
        tracker.update(SlotSet("social",True))
        tracker.update(SlotSet("global_score",global_score))
        
class Pathology(FormAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields():
        obligatories = get_obligatories()
        try:
            return obligatories['pathology']
        except:
            return []
        
    def name(self):
        return 'sum_up_pathology'
        
    def submit(self, dispatcher, tracker, domain):
        global_score = tracker.get_slot('global_score')
        global_score+=2
        #TODO: save score
        symtoms = tracker.get_slot("symtoms")
        pathology_body_part = tracker.get_slot("pathology_body_part")
        try:
            obligatories = get_obligatories()
            len(obligatories['pathology'])>0
            response = "To sum up,"
            if symtoms != None:
                response += "\n\tYou have some symptoms : {}".format(symtoms)
            if pathology_body_part != None:
                response += "\n\tThis symptom is localized at {}".format(pathology_body_part)
            response+="\nIs it right?"
        except:
            response = "It seems that you talked about a pathology."
        dispatcher.utter_message(response)
        tracker.update(SlotSet("pathology",True))
        tracker.update(SlotSet("global_score",global_score))
        
class Treatment(FormAction):
    RANDOMIZE = False
    
    @staticmethod
    def required_fields():
        obligatories = get_obligatories()
        try:
            return obligatories['treatment']
        except:
            return []
        
    def name(self):
        return 'sum_up_treatment'
        
    def submit(self, dispatcher, tracker, domain):
        global_score = tracker.get_slot('global_score')
        global_score+=2
        #TODO: save score
        medicinal = tracker.get_slot("medicinal")
        drug = tracker.get_slot("drug")
        try:
            obligatories = get_obligatories()
            len(obligatories['treatment'])>0
            response = "To sum up,"        
            if medicinal != None:
                if medicinal :
                    response += "\n\tYour traitment is medicinal"
                else:
                    response += "\n\tYour traitment is not medicinal"
            if drug != None and drug != "no_drug":
                response += "\n\tYou take: {}".format(drug)
            response+="\nIs it right?"
        except:
            response = "It seems that you talked about a treatment."        
        dispatcher.utter_message(response)
        tracker.update(SlotSet("treatment",True))
        tracker.update(SlotSet("global_score",global_score))
        
class InfoPatient(FormAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields():
        obligatories = get_obligatories()
        try:
            return obligatories['infoPatient']
        except:
            return []
        
    def name(self):
        return 'sum_up_info_patient'
        
    def submit(self, dispatcher, tracker, domain):
        #TODO: save score
        addiction = tracker.get_slot("addiction")
        weight = tracker.get_slot("weight")
        size = tracker.get_slot("infoPatient_distance")
        gender = tracker.get_slot("gender")
        temperature = tracker.get_slot("infoPatient_temperature")
        heart_rate = tracker.get_slot("heart_rate")
        blood_pressure = tracker.get_slot("blood_pressure")
        date_check_up = tracker.get_slot("infoPatient_time")
        try:
            obligatories = get_obligatories()
            len(obligatories['infoPatient'])>0
            response = "To sum up,"        
            if addiction != None:
                response+= "\n\tYou have some addiction: {}".format(addiction)
            if weight != None:
                response+= "\n\tYour weight is of {}".format(weight)
            if size != None:
                response+= "\n\tYou're {} tall".format(size)
            if gender != None:
                response+= "\n\tYou're a {}".format(gender)
            if temperature != None:
                response+= "\n\tYour temperature is of {}".format(temperature)
            if heart_rate != None:
                response+= "\n\tYour heart rate is of {}".format(heart_rate)
            if blood_pressure != None:
                response+= "\n\tYour blood pressure is of {}".format(blood_pressure)
            if date_check_up != None:
                response+= "\n\tYou saw some caregivers on : {}".format(date_check_up)
            response+= "\nIs it right?"
        except:
            response = "It seems that you talked about some personal informations."
        dispatcher.utter_message(response)
        tracker.update(SlotSet("infoPatient",True))