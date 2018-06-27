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
            body_part = tracker.get_slot("body_part")
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
                if body_part != None:
                    response += "\tThe pain is localized at {}.\n".format(body_part)
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
            sport_duration = tracker.get_slot("sport_duration")
            sport = tracker.get_slot("sport")
            sport_period = tracker.get_slot("sport_period")
            distance = tracker.get_slot("distance")
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