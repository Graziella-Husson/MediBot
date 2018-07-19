from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.events import SlotSet
from rasa_core.dispatcher import Button
from level_classifiers import get_pain_level, get_physical_activity_level

from rasa_core.actions.forms import FormAction

from initAndComplex import get_obligatories
from ressources import get_utterance

def get_response_simple(response, slot_name,tracker,language,other_value=None,utt_name=None):
    """
    @param response: string of the response the bot will say to the user
    @param slot_name: name of the slot we want to sum up
    @param tracker: used to get all infos for 'slot_name' entity from the tracker
    @param language: language of the bot (for display the right name of button)
    @param other_value: unrequired, if the slot value is set to this value, do not sum up it
    @param button_name: unrequired, name of the ressource in json if different to slot_name
    
    Add a part in the response of the bot with a sentence to sum up a given slot
    
    @return: string of the response the bot will say to the user
    """
    if utt_name!=None:
        to_search_in_ressources = utt_name
    else:
        to_search_in_ressources = slot_name
    slot_value = tracker.get_slot(slot_name)
    if slot_value != None:
        if other_value == None or (other_value != None and slot_value != other_value):
            response += get_utterance(to_search_in_ressources,language).format(slot_value)
    return response

def get_response_boolean(response, slot_name,tracker,language):
    """
    @param response: string of the response the bot will say to the user
    @param slot_name: name of the boolean slot we want to sum up
    @param tracker: used to get all infos for 'slot_name' entity from the tracker
    @param language: language of the bot (for display the right name of button)
    
    Add a part in the response of the bot with a sentence to sum up a given boolean slot, depending of its true or false value
    
    @return: string of the response the bot will say to the user
    """
    slot_value = tracker.get_slot(slot_name)
    if slot_value != None:
        if slot_value:
            response += get_utterance(slot_name+"_true",language)
        else:
            response += get_utterance(slot_name+"_false",language)
    return response        

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

class ActionWithCalculus(FormActionTriggerAction):
    """
    A custom class heritating from FormActionTriggerAction. 
    This type of action is used when the intent is containing a level calculated:
        - pain (mild, moderate,severe)
        - activity (little, moderate, vigorous)
    """    
    def init(self,intent_name,to_calculate_slot,levelsList,classifier_method):
        """
        @param intent_name: name of the intent
        @param to_calculate_slot: name of the slot used to calculate level
        @param levelsList: list of different levels
        @param classifier_method: method called to classify level with to_calculate_slot name
        Set all specific variables for one ActionWithCalculus action 
        """         
        self.intentName = intent_name
        self.mainSlot = to_calculate_slot
        self.levels = levelsList
        self.classifier = classifier_method
        
    def calculus_action(self, tracker, language, dispatcher): 
        """
        @param tracker: used to get the language of the bot and get and set global score
        @param language: language used by the bot 
        @param dispatcher: used to tell the patient that he talked about the intent 
        This action will sum up infos about the intent. If they're all set to None (no mandatory entity), just say that we talked about intent
        Ask if the informations are correct.
        If the level is 'Incorrect', that mean the user said that it was incorrect before. If so, display buttons to allow user to tell the level himself
        """         
        level = tracker.get_slot(self.intentName+"_level")
        if not level == "Incorrect":
            mainSlotValue = tracker.get_slot(self.mainSlot)
            obligatories = get_obligatories()
            try:
                len(obligatories[self.intentName])
                response = get_utterance("sum_up",language)
                if mainSlotValue != None:
                    if level == None:
                        #get calculated level
                        level = self.classifier(mainSlotValue)                
                        tracker.update(SlotSet(self.intentName+"_level",level))
                    level = get_utterance(level,language)
                    response += get_utterance(self.mainSlot,language).format(mainSlotValue, level)
                response = self.sum_up_setted_slots(response,tracker,language)
                response += get_utterance("right",language)
            except:
                response = get_utterance(self.intentName+"_no_entity",language)
                # TODO: add to database
            tracker.update(SlotSet("topic",None))
            tracker.update(SlotSet("requested_slot",None))
            dispatcher.utter_message(response)
        else:
            buttons = []
            for level in self.levels:
                level_title = get_utterance(level,language)
                buttons.append(Button(title=level_title, payload="/"+self.intentName+"{\""+self.intentName+"_level"+"\":\""+level+"\"}"))
            message = get_utterance("ask_level_"+self.intentName,language)
            dispatcher.utter_button_message(message, buttons)
                   
    def sum_up_setted_slots(self, response,tracker,language):
        raise NotImplementedError("a FormActionTriggerAction action must implement a sum_up_setted_slots method")

class ActionWithoutCalculus(FormActionTriggerAction):
    """
    A custom class heritating from FormActionTriggerAction. 
    This type of action is used when the intent is not containing a level calculated but containing entities
    """
        
    def action_core(self, tracker, language,dispatcher, intentName): 
        """
        @param tracker: used to get the language of the bot and get and set global score
        @param language: language used by the bot 
        @param dispatcher: used to tell the patient that he talked about the intent
        @intentName: name of the intent
        
        This action will sum up infos about the intent. If they're all set to None (no mandatory entity), just say that we talked about intent
        Ask if the informations are correct.
        """        
        global_score = tracker.get_slot('global_score')
        global_score+=2
        #TODO: save score
        try:
            obligatories = get_obligatories()
            len(obligatories[intentName])>0
            response = get_utterance("sum_up",language)
            self.sum_up_setted_slots(response,tracker,language)
            response += get_utterance("right",language)
        except:
            response = get_utterance("sum_up_"+intentName,language)
        dispatcher.utter_message(response)
        tracker.update(SlotSet("global_score",global_score))
                   
    def sum_up_setted_slots(self, response,tracker,language):
        raise NotImplementedError("a FormActionTriggerAction action must implement a sum_up_setted_slots method")

class ActionFillSlotsPain(ActionWithCalculus):
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
        The entities linked to the 'pain' intent are:
            - pain_level
            - pain_duration
            - pain_desc
            - pain_body_part
            - pain_change
            - pain_period
            - pain_time
        The pain level is calculated with the method C{get_pain_level(pain_desc)}
        If we want the pain level, we have to have the pain_desc slot mandatory.
        """         
        language = tracker.get_slot("language")        
        self.init("pain","pain_desc",["mild","moderate","severe"],get_pain_level)
        self.calculus_action(tracker, language,dispatcher)
        
    def sum_up_setted_slots(self, response,tracker,language):
        """
        @return: all infos sum up response
        """
        response = get_response_simple(response, "pain_body_part",tracker,language)
        response = get_response_simple(response, "pain_duration",tracker,language)
        response = get_response_simple(response, "pain_period",tracker,language)
        response = get_response_simple(response, "pain_change",tracker,language)
        response = get_response_simple(response, "pain_time",tracker,language)
        return response
                
class ActionFillSlotsSport(ActionWithCalculus):
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
        The entities linked to the 'activity' intent are:
            - activity_level
            - activity_duration
            - sport
            - activity_period
            - activity_distance
            - activity_hard (boolean)
            - activity_time
        The sport level is calculated with the method C{get_physical_activity_level(sport)}
        If we want the sport level, we have to have the sport slot mandatory.
        """
        language = tracker.get_slot("language")        
        self.init("activity","sport",["little","moderate","vigorous"],get_physical_activity_level)
        self.calculus_action(tracker, language,dispatcher)
        
    def sum_up_setted_slots(self, response,tracker,language):
        """
        @return: all infos sum up response
        """
        response = get_response_simple(response, "activity_duration",tracker,language)
        response = get_response_simple(response, "activity_distance",tracker,language)
        response = get_response_simple(response, "activity_period",tracker,language)
        response = get_response_simple(response, "activity_time",tracker,language)
        response = get_response_boolean(response, "activity_hard",tracker,language)
        return response
    
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
        
class Pathology(ActionWithoutCalculus):
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
            - symtoms
            - pathology_time
            - pathology_change (boolean)
            - pathology_period
            - pathology_treatment_linked (boolean)
        This action will sum up these infos. If they're all set to None (no mandatory entity), just say that we talked about a pathology
        Ask if the informations are correct.
        """
        language = tracker.get_slot("language")   
        intentName = "pathology"
        self.action_core(tracker, language,dispatcher, intentName)

    def sum_up_setted_slots(self, response,tracker,language):
        """
        @return: all infos sum up response
        """
        response = get_response_simple(response, "symtoms",tracker,language)
        response = get_response_simple(response, "pathology_body_part",tracker,language)
        response = get_response_simple(response, "pathology_time",tracker,language)
        response = get_response_boolean(response, "pathology_change",tracker,language)
        response = get_response_simple(response, "pathology_period",tracker,language)
        response = get_response_boolean(response, "pathology_treatment_linked",tracker,language)
        return response
        
class Treatment(ActionWithoutCalculus):
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
            - treatment_being_taken
            - drug
            - dosing	
            - treatment_time
            - treatment_prescripted(boolean)
            - treatment_ok(boolean)
            - treatment_overdosage
            - treatment_period

        This action will sum up these infos. If they're all set to None (no mandatory entity), just say that we talked about a treatment
        Ask if the informations are correct.
        """
        language = tracker.get_slot("language")   
        intentName = "treatment"
        self.action_core(tracker, language,dispatcher, intentName)

    def sum_up_setted_slots(self, response,tracker,language):
        """
        @return: all infos sum up response
        """
        response = get_response_boolean(response, "medicinal",tracker,language)
        response = get_response_simple(response, "treatment_being_taken",tracker,language,"no_drug")
        response = get_response_simple(response, "drug",tracker,language,"no_drug")
        response = get_response_simple(response, "dosing",tracker,language,"no_drug")
        response = get_response_simple(response, "treatment_period",tracker,language)
        response = get_response_simple(response, "treatment_time",tracker,language)
        response = get_response_simple(response, "treatment_overdosage",tracker,language,"no_drug")
        response = get_response_boolean(response, "treatment_prescripted",tracker,language)
        response = get_response_boolean(response, "treatment_ok",tracker,language)
        return response

class InfoPatient(ActionWithoutCalculus):
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
        intentName = "infoPatient"
        self.action_core(tracker, language,dispatcher, intentName)

    def sum_up_setted_slots(self, response,tracker,language):
        """
        @return: all infos sum up response
        """
        response = get_response_simple(response, "addiction",tracker,language)
        response = get_response_simple(response, "weight",tracker,language)
        response = get_response_simple(response, "infoPatient_distance",tracker,language,utt_name="size")
        response = get_response_simple(response, "gender",tracker,language)
        response = get_response_simple(response, "infoPatient_temperature",tracker,language)
        response = get_response_simple(response, "heart_rate",tracker,language)
        response = get_response_simple(response, "blood_pressure",tracker,language)
        response = get_response_simple(response, "infoPatient_time",tracker,language)
        return response