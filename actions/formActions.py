from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.events import SlotSet
from rasa_core.dispatcher import Button
from level_classifiers import get_pain_level, get_physical_activity_level

from rasa_core.actions.forms import (
EntityFormField,
FormAction,
BooleanFormField
)

from initAndComplex import get_obligatories
from ressources import get_utterance

class FormActionTriggerAction(FormAction):
        """
        A custom class heritating from FormAction. The main difference is in what we use to ask requested_slots.
        In RASA we use the domain templates. Here, we use a custom action named utter_ask_{entity_name}.
        """
        def run(self, dispatcher, tracker, domain):
            """
           Trigger a custom action to ask the requested_slot.
            """
            events = self.get_requested_slot(tracker) + self.get_other_slots(tracker)
            temp_tracker = tracker.copy()
            for e in events:
                temp_tracker.update(e)
            for field in self.required_fields():
                if self.should_request_slot(temp_tracker, field.slot_name):
                    action = domain.action_for_name("utter_ask_{}".format(field.slot_name))
                    tracker.trigger_follow_up_action(action)
                    events.append(SlotSet("requested_slot", field.slot_name))
                    return events
            events_from_submit = self.submit(dispatcher, temp_tracker, domain) or []
            return events + events_from_submit

class ActionFillSlotsPain(FormActionTriggerAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields():
        """
        @return: if the dict C{obligatories} from the C{init} class contains a list a the requested slot for the intent 'pain',
        return it. If not, return an empty list.
        """
        obligatories = get_obligatories()
        try:
            return obligatories['pain']
        except:
            return []
    
    def name(self):
        """
        @return: the name of the action.
        """
        return 'action_check_slots_pain'
    
    def submit(self, dispatcher, tracker, domain):  
        """
        @param tracker: used to get the language of the bot and get and set global score
        @param dispatcher: used to tell the patient that he talked about the intent 'pain'.
        The entitities linked to this intent are:
            - pain_level
            - pain_duration
            - pain_desc
            - pain_body_part
            - pain_change
            - pain_period
        This action will sum up these infos. If they're all set to None (no mandatory entity), just say that we talked about a pain
        Ask if the informations are correct.
        If the pain level is 'Incorrect', that mean the user said that it was incorrect before. If so, display buttons to allow user to tell the level of his pain
        The pain level is calculated with the method C{get_pain_level(pain_desc)}
        If we want the pain level, we have to have the pain_desc slot mandatory.
        """
        language = tracker.get_slot("language")
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
                response = get_utterance("sum_up",language)
                if pain_desc != None:
                    if level == None:
                        #get pain level
                        level = get_pain_level(pain_desc)                
                        tracker.update(SlotSet("pain_level",level))
                    level = get_utterance(level,language)
                    response += get_utterance("pain_desc",language).format(pain_desc, level)
                if pain_body_part != None:
                    response += get_utterance("pain_body_part",language).format(pain_body_part)
                if pain_duration != None:
                    response += get_utterance("pain_duration",language).format(pain_duration)
                if pain_period != None:
                    response += get_utterance("pain_period",language).format(pain_period)
                if pain_change != None:
                    response += get_utterance("pain_change",language).format(pain_change)
                response += get_utterance("right",language)
            except:
                response = get_utterance("pain_no_entity",language)
                # TODO: add to database
            tracker.update(SlotSet("topic",None))
            tracker.update(SlotSet("requested_slot",None))
            dispatcher.utter_message(response)
        else:
            mild = get_utterance("mild",language)
            moderate = get_utterance("moderate",language)
            severe = get_utterance("severe",language)
            buttons = [Button(title=mild, payload="/pain{\"pain_level\":\"mild\"}"),
                       Button(title=moderate, payload="/pain{\"pain_level\":\"moderate\"}"),
                       Button(title=severe, payload="/pain{\"pain_level\":\"severe\"}")]
            message = get_utterance("ask_level_pain",language)
            dispatcher.utter_button_message(message, buttons)
        
        
class ActionFillSlotsSport(FormActionTriggerAction):
    RANDOMIZE = True

    @staticmethod
    def required_fields():
        """
        @return: if the dict C{obligatories} from the C{init} class contains a list a the requested slot for the intent 'activity',
        return it. If not, return an empty list.
        """
        obligatories = get_obligatories()
        try:
            return obligatories['activity']    
        except:
            return []    
    
    def name(self):
        """
        @return: the name of the action.
        """
        return 'action_check_slots_sport'
    
    def submit(self, dispatcher, tracker, domain):  
        """
        @param tracker: used to get the language of the bot and get and set global score
        @param dispatcher: used to tell the patient that he talked about the intent 'activity'.
        The entitities linked to this intent are:
            - sport_level
            - activity_duration
            - sport
            - activity_period
            - activity_distance
            - activity_hard (boolean)
        This action will sum up these infos. If they're all set to None (no mandatory entity), just say that we talked about an activity
        Ask if the informations are correct.
        If the sport level is 'Incorrect', that mean the user said that it was incorrect before. If so, display buttons to allow user to tell the level of his activity
        The sport level is calculated with the method C{get_physical_activity_level(sport)}
        If we want the sport level, we have to have the sport slot mandatory.
        """
        language = tracker.get_slot("language")
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
                response = get_utterance("sum_up",language)
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
                    sport_level = get_utterance(sport_level,language)
                    response += get_utterance("sport",language).format(sport_level, MET, sport)
                if sport_duration != None:
                    response += get_utterance("activity_duration",language).format(sport_duration)
                if distance != None:
                    response += get_utterance("activity_distance",language).format(distance)
                if sport_period != None:
                    response += get_utterance("activity_period",language).format(sport_period)
                if activity_hard != None:
                    if activity_hard:
                        response += get_utterance("activity_hard_true",language)
                    else:
                        response += get_utterance("activity_hard_false",language)
                response += get_utterance("right",language)
            except:
                response = get_utterance("activity_no_entity",language)
                # TODO: save in database
            tracker.update(SlotSet("topic",None))
            tracker.update(SlotSet("requested_slot",None))
            dispatcher.utter_message(response)
        else:
            little = get_utterance("little",language)
            moderate = get_utterance("moderate",language)
            vigorous = get_utterance("vigorous",language)
            buttons = [Button(title=little, payload="/pain{\"sport_level\":\"little\"}"),
                       Button(title=moderate, payload="/pain{\"sport_level\":\"moderate\"}"),
                       Button(title=vigorous, payload="/pain{\"sport_level\":\"vigorous\"}")]
            message = get_utterance("ask_level_activity",language)
            dispatcher.utter_button_message(message, buttons)  

class CheckRequestedIntents(FormActionTriggerAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields():
        """
        @return: if the dict C{obligatories} from the C{init} class contains a list a the requested slot for 'requested_intent',
        return it. If not, return an empty list.
        """
        obligatories = get_obligatories() 
        try:
            return obligatories['requested_intent']
        except:
            return []
    
    def name(self):
        """
        @return: the name of the action.
        """
        return 'action_check_intents'
    
    def submit(self, dispatcher, tracker, domain):  
        """
        @param tracker: used to get the language of the bot
        @param dispatcher: used to tell the patient that he talked about all the intents he had to.
        """
        language = tracker.get_slot("language")
        dispatcher.utter_message(get_utterance("requested_intent",language))

class Sadness(FormActionTriggerAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields():
        """
        @return: if the dict C{obligatories} from the C{init} class contains a list a the requested slot for the intent 'emotional_sadness',
        return it. If not, return an empty list.
        """
        obligatories = get_obligatories()
        try:
            return obligatories['emotional_sadness']
        except:
            return []

    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_emotionnal_sadness'
        
    def submit(self, dispatcher, tracker, domain):  
        """
        @param tracker: used to get the language of the bot and get and set global score
        @param dispatcher: used to tell the patient that he talked about the intent 'emotional_sadness'.
        No entities for this intent for now.
        """
        language = tracker.get_slot("language")
        global_score = tracker.get_slot('global_score')
        global_score+=1
        #TODO: save score        
        dispatcher.utter_message(get_utterance("sum_up_sadness",language))
        tracker.update(SlotSet("global_score",global_score))
      
class Happy(FormActionTriggerAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields():
        """
        @return: if the dict C{obligatories} from the C{init} class contains a list a the requested slot for the intent 'emotional_hapiness',
        return it. If not, return an empty list.
        """
        obligatories = get_obligatories()
        try:
            return obligatories['emotional_hapiness']
        except:
            return []
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_emotional_hapiness'
        
    def submit(self, dispatcher, tracker, domain):  
        """
        @param tracker: used to get the language of the bot and get and set global score
        @param dispatcher: used to tell the patient that he talked about the intent 'emotional_hapiness'.
        No entities for this intent for now.
        """
        language = tracker.get_slot("language")
        global_score = tracker.get_slot('global_score')
        global_score+=3
        #TODO: save score
        dispatcher.utter_message(get_utterance("sum_up_happiness",language))
        tracker.update(SlotSet("global_score",global_score))

class Social(FormActionTriggerAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields():
        """
        @return: if the dict C{obligatories} from the C{init} class contains a list a the requested slot for the intent 'social',
        return it. If not, return an empty list.
        """
        obligatories = get_obligatories()
        try:
            return obligatories['social']
        except:
            return []
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_social'
        
    def submit(self, dispatcher, tracker, domain):  
        """
        @param tracker: used to get the language of the bot and get and set global score
        @param dispatcher: used to tell the patient that he talked about the intent 'social'.
        No entities for this intent for now.
        """
        language = tracker.get_slot("language")
        global_score = tracker.get_slot('global_score')
        global_score+=2
        #TODO: save score
        dispatcher.utter_message(get_utterance("sum_up_social",language))
        tracker.update(SlotSet("social",True))
        tracker.update(SlotSet("global_score",global_score))
        
class Pathology(FormActionTriggerAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields():
        """
        @return: if the dict C{obligatories} from the C{init} class contains a list a the requested slot for the intent 'pathology',
        return it. If not, return an empty list.
        """
        obligatories = get_obligatories()
        try:
            return obligatories['pathology']
        except:
            return []
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_pathology'
        
    def submit(self, dispatcher, tracker, domain):  
        """
        @param tracker: used to get the language of the bot and get and set global score
        @param dispatcher: used to tell the patient that he talked about the intent 'social'.
        The entitities linked to this intent are:
            - pathology_body_part
            - sum_up
        This action will sum up these infos. If they're all set to None (no mandatory entity), just say that we talked about a pathology
        Ask if the informations are correct.
        """
        language = tracker.get_slot("language")
        global_score = tracker.get_slot('global_score')
        global_score+=2
        #TODO: save score
        symtoms = tracker.get_slot("symtoms")
        pathology_body_part = tracker.get_slot("pathology_body_part")
        try:
            obligatories = get_obligatories()
            len(obligatories['pathology'])>0
            response = get_utterance("sum_up",language)
            if symtoms != None:
                response += get_utterance("symtoms",language).format(symtoms)
            if pathology_body_part != None:
                response += get_utterance("pathology_body_part",language).format(pathology_body_part)
            response += get_utterance("right",language)
        except:
            response = get_utterance("sum_up_pathology",language)
        dispatcher.utter_message(response)
        tracker.update(SlotSet("global_score",global_score))
        
class Treatment(FormActionTriggerAction):
    RANDOMIZE = False
    
    @staticmethod
    def required_fields():
        """
        @return: if the dict C{obligatories} from the C{init} class contains a list a the requested slot for the intent 'treatment',
        return it. If not, return an empty list.
        """
        obligatories = get_obligatories()
        try:
            return obligatories['treatment']
        except:
            return []
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_treatment'
        
    def submit(self, dispatcher, tracker, domain):  
        """
        @param tracker: used to get the language of the bot and get and set global score
        @param dispatcher: used to tell the patient that he talked about the intent 'treatment'.
        The entitities linked to this intent are:
            - medicinal (boolean)
            - drug
        This action will sum up these infos. If they're all set to None (no mandatory entity), just say that we talked about a treatment
        Ask if the informations are correct.
        """
        language = tracker.get_slot("language")
        global_score = tracker.get_slot('global_score')
        global_score+=2
        #TODO: save score
        medicinal = tracker.get_slot("medicinal")
        drug = tracker.get_slot("drug")
        try:
            obligatories = get_obligatories()
            len(obligatories['treatment'])>0
            response = get_utterance("sum_up",language)
            if medicinal != None:
                if medicinal :
                    response += get_utterance("medicinal_true",language)
                else:
                    response += get_utterance("medicinal_false",language)
            if drug != None and drug != "no_drug":
                response += get_utterance("drug",language).format(drug)
            response += get_utterance("right",language)
        except:
            response = get_utterance("sum_up_treatment",language)      
        dispatcher.utter_message(response)
        tracker.update(SlotSet("global_score",global_score))
        
class InfoPatient(FormActionTriggerAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields():
        """
        @return: if the dict C{obligatories} from the C{init} class contains a list a the requested slot for the intent 'infoPatient',
        return it. If not, return an empty list.
        """
        obligatories = get_obligatories()
        try:
            return obligatories['infoPatient']
        except:
            return []
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_info_patient'
        
    def submit(self, dispatcher, tracker, domain):  
        """
        @param tracker: used to get the language of the bot and get and set global score
        @param dispatcher: used to tell the patient that he talked about the intent 'info_patient'.
        The entitities linked to this intent are:
            - addiction
            - weight
            - infoPatient_distance
            - gender
            - infoPatient_temperature
            - heart_rate
            - blood_pressure
            - infoPatient_time
        This action will sum up these infos. If they're all set to None (no mandatory entity), just say that we talked about a personal info
        Ask if the informations are correct.
        """
        language = tracker.get_slot("language")
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
            response = get_utterance("sum_up",language)
            if addiction != None:
                response += get_utterance("addiction",language).format(addiction)
            if weight != None:
                response += get_utterance("weight",language).format(weight)
            if size != None:
                response += get_utterance("size",language).format(size)
            if gender != None:
                response += get_utterance("gender",language).format(gender)
            if temperature != None:
                response += get_utterance("infoPatient_temperature",language).format(temperature)
            if heart_rate != None:
                response += get_utterance("heart_rate",language).format(heart_rate)
            if blood_pressure != None:
                response += get_utterance("blood_pressure",language).format(blood_pressure)
            if date_check_up != None:
                response += get_utterance("infoPatient_time",language).format(date_check_up)
            response += get_utterance("right",language)
        except:
            response = get_utterance("sum_up_info_patient",language)
        dispatcher.utter_message(response)