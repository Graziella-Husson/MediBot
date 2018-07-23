from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.dispatcher import Button
from ressources import get_utterance

class AskAction(Action):
    """
    Used to say something to the user
    
    If self.SIMPLE is set, use its value for search utterance in ressources
    """
    SIMPLE = False
    
    def init(self):
        #self.entityName = ""
        raise NotImplementedError("a AskAction action must implement a init method")
    
    def run(self, dispatcher, tracker, domain):
        """
        Print something for the user 
        
        If self.SIMPLE is set, use its value for search utterance in ressources
        """
        self.init()
        language = tracker.get_slot("language")
        if not self.SIMPLE:
            to_search_in_ressources = "ask_"+self.entityName
        else:
            to_search_in_ressources = self.entityName
        response = get_utterance(to_search_in_ressources,language)
        dispatcher.utter_message(response)

class AskBooleanAction(Action):
    """
    Used to say something to the user using two buttons (yes and no)
    
    If payloadNo is set, a custom payload for 'No' will be used
    """
    payloadNo = None
    def init(self):
        #self.entityName = ""
        #self.intentName = ""
        raise NotImplementedError("a AskBooleanAction action must implement a init method")

    def run(self, dispatcher, tracker, domain):
        """
        Show two buttons (one for yes and one for no)
        
        If payloadNo is set, a custom payload for 'No' will be used
        """
        self.init()
        language = tracker.get_slot("language")
        message = get_utterance("ask_"+self.entityName,language)
        yes_button = get_utterance("yes",language)
        no_button = get_utterance("no",language)
        buttons = []
        buttons.append(Button(title=yes_button, payload="/"+self.intentName+"{\""+self.entityName+"\":true}"))
        if self.payloadNo == None:
            buttons.append(Button(title=no_button, payload="/"+self.intentName+"{\""+self.entityName+"\":false}"))
        else:
            buttons.append(Button(title=no_button, payload=self.payloadNo))
        dispatcher.utter_button_message(message, buttons)

class AskButtonsAction(Action):
    """
    Used to say something to the user using predefined buttons 
    """
    def init(self):
        #self.entityName = ""
        #self.intentName = ""
        #self.buttons = []
        raise NotImplementedError("a AskButtonsAction action must implement a init method")
    
    def run(self, dispatcher, tracker, domain):
        """
        For each button is self.buttons, make a button after the name button
        """
        self.init()
        language = tracker.get_slot("language")
        message = get_utterance("ask_"+self.entityName,language)
        buttons_to_show = []
        for button in self.buttons:
            name_button = get_utterance(button+"_button",language)
            buttons_to_show.append(Button(title=name_button, payload="/"+self.intentName+"{\""+self.entityName+"\":\""+name_button.lower()+"\"}"))
        dispatcher.utter_button_message(message, buttons_to_show)

class AskMedicinal(AskBooleanAction):
    """
    Say something to the user : display buttons to tell if the treatment is medicinal or not
    When the "no" button is clicked, we have to set :
        - drug 
        - dosing
        - treatment_being_taken
        - treatment_period
        - treatment_overdosage
    to something, saying that we won't ask anything about it for this treatment.
    """ 
    
    def init(self):
        """
        Set the name of the intent
        
        Set the name of the entity to ask
        """
        self.entityName = "medicinal"
        self.intentName = "treatment"
        self.payloadNo = "/treatment{\"medicinal\":false, \"drug\":\"no_drug\", \"dosing\":\"no_drug\", \"treatment_being_taken\":\"no_drug\", \"treatment_overdosage\":\"no_drug\"}"
    
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_medicinal'

class AskActivityHard(AskBooleanAction):
    """
    Say something to the user : ask if the activity was hard to perform because of the general health
    """  
    def init(self):
        """
        Set the name of the intent
        
        Set the name of the entity to ask
        """
        self.entityName = "activity_hard"
        self.intentName = "activity"
    
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_activity_hard'

class AskSport(AskAction):
    """
    Say something to the user : ask the activity the user did
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "sport"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_sport'
                
class AskActivityDuration(AskAction):
    """
    Say something to the user : ask the duration of the activity
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "activity_duration"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_activity_duration'

class AskPainBodyPart(AskAction):
    """
    Say something to the user : ask the part of the body where the pain is
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "pain_body_part"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pain_body_part'

class AskPathologyBodyPart(AskAction):
    """
    Say something to the user : ask the body part where the pathology is
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "pathology_body_part"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pathology_body_part'

class AskPainDuration(AskAction):
    """
    Say something to the user : ask the duration of the pain
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "pain_duration"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pain_duration'
        
class AskPainChange(AskButtonsAction):
    """
    Say something to the user : display buttons asking the evolution of the pain (brief, continuous, intermittent)
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        
        Set the name of the intent
        
        Set the list of available buttons to show to the user
        """
        self.entityName = "pain_change"
        self.intentName = "pain"
        self.buttons = ["continuous","intermittent","brief"]
    
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pain_change'
 
class AskPainPeriod(AskAction):
    """
    Say something to the user : ask the period of the pain
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "pain_period"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pain_period'
        
class AskActivityPeriod(AskAction):
    """
    Say something to the user : ask the period of the activity
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "activity_period"
    
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_activity_period'

class AskActivity(AskAction):
    """
    Say something to the user :  ask the user to talk about his activity
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "activity"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_activity'
        
class AskSocial(AskAction):
    """
    Say something to the user :  ask the user to talk about his social activity
    """
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "social"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_social'

class AskHappiness(AskAction):
    """
    Say something to the user :  ask the user to talk about his happiness
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "happiness"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_emotionnal_hapiness'

class AskSadness(AskAction):
    """
    Say something to the user :  ask the user to talk about his sadness
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "sadness"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_emotionnal_sadness'
       
class AskPainDesc(AskAction):
    """
    Say something to the user :  ask the description of the pain
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "pain_desc"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pain_desc'
       
class AskSymptoms(AskAction):
    """
    Say something to the user : ask the symptoms
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "symtoms"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_symtoms'      

class AskDrug(AskAction):
    """
    Say something to the user : ask the drug of the treatment
    We have to talk about that only if the treatment is medicinal
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "drug"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_drug'     

class AskPainTime(AskAction):
    """
    Say something to the user : ask the begin date of the pain
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "pain_time"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pain_time' 

class AskActivityTime(AskAction):
    """
    Say something to the user : ask the begin date of the activity
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "activity_time"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_activity_time'     

class AskActivityDistance(AskAction):
    """
    Say something to the user : ask the distance of the activity
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "activity_distance"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_activity_distance'
        
class AskWeight(AskAction):
    """
    Say something to the user : ask the weight of the patient
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "weight"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_weight'
        
class AskInfoPatientDistance(AskAction):
    """
    Say something to the user : ask the size of the patients
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "infoPatient_distance"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_infoPatient_distance'
        
class AskHeartRate(AskAction):
    """
    Say something to the user : ask the heart rate of the patient
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "heart_rate"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_heart_rate'
   
class AskInfoPatientTemperature(AskAction):
    """
    Say something to the user : ask the temperature of the patient
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "infoPatient_temperature"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_infoPatient_temperature'
   
class AskGender(AskAction):
    """
    Say something to the user : ask the gender of the patient
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "gender"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_gender'

class AskBloodPressure(AskAction):
    """
    Say something to the user : ask the blood pressure of the patient
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "blood_pressure"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_blood_pressure'
        
class AskAddiction(AskAction):
    """
    Say something to the user : ask if the patient have an addicition
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "addiction"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_addiction'
           
class AskInfoPatientTime(AskAction):
    """
    Say something to the user : ask the last date of medical check up
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "infoPatient_time"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_infoPatient_time'
        
class AskPathologyTime(AskAction):
    """
    Say something to the user : ask the begin time of pathology/side effect/symptom
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "pathology_time"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pathology_time'

class AskPathologyPeriod(AskAction):
    """
    Say something to the user : ask the period of pathology/side effect/symptom
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "pathology_period"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pathology_period'

class AskPathologyChange(AskBooleanAction):
    """
    Say something to the user : display buttons to tell if the pathology is worst or not
    """ 
    def init(self):
        """
        Set the name of the intent
        
        Set the name of the entity to ask
        """
        self.entityName = "pathology_change"
        self.intentName = "pathology"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pathology_change'

class AskPathologyTreatmentLinked(AskBooleanAction):
    """
    Say something to the user : display buttons to tell if the pathology is linked to the treatment or not (according to patient)
    """ 
    def init(self):
        """
        Set the name of the intent
        
        Set the name of the entity to ask
        """
        self.intentName = "pathology"
        self.entityName = "pathology_treatment_linked"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pathology_treatment_linked'
        
class AskDosing(AskAction):
    """
    Say something to the user : ask the dose the patient is taking (not the one prescripted)
    We have to talk about that only if the treatment is medicinal
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "dosing"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_dosing'
        
class AskTreatmentTime(AskAction):
    """
    Say something to the user : ask the begin date of the treatment taken
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "treatment_time"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_treatment_time'
        
class AskTreatmentBeingTaken(AskButtonsAction):
    """
    Say something to the user : display buttons to tell if the treatment is being well taken or forgotten or stopped
    When the "stopped" button is clicked, we have to set :
        - dosing
    to something, saying that we won't ask anything about it for this treatment.        
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        
        Set the name of the intent
        
        Set the list of available buttons to show to the user
        """
        self.entityName = "treatment_being_taken"
        self.intentName = "treatment"
        self.buttons = ["taken","stopped","forgotten"]
    
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_treatment_being_taken'

class AskTreatmentOverdosage(AskButtonsAction):
    """
    Say something to the user : display buttons to tell if the treatment dose is well taken or overdose or under dose
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        
        Set the name of the intent
        
        Set the list of available buttons to show to the user
        """
        self.entityName = "treatment_overdosage"
        self.intentName = "treatment"
        self.buttons = ["welltaken","overdose","underdose"]
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_treatment_overdosage'
        
class AskTreatmentPeriod(AskAction):
    """
    Say something to the user : ask the period of the medicinal treatment 
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "treatment_period"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_treatment_period'

class AskTreatmentPrescripted(AskBooleanAction):
    """
    Say something to the user : display buttons to tell if the treatment is prescripted or not
    """ 
    def init(self):
        """
        Set the name of the intent
        
        Set the name of the entity to ask
        """
        self.intentName = "treatment"
        self.entityName = "treatment_prescripted"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_treatment_prescripted'

class AskTreatmentOk(AskBooleanAction):
    """
    Say something to the user : display buttons to tell if the patient feels ok about his treatment or not
    """ 
    def init(self):
        """
        Set the name of the intent
        
        Set the name of the entity to ask
        """
        self.intentName = "treatment"
        self.entityName = "treatment_ok"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_treatment_ok'
  
class AskRisk(AskAction):
    """
    Say something to the user : ask the user to talk about his risky behaviors
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "risk"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_risk'

class AskPain(AskAction):
    """
    Say something to the user : ask the user to talk about his pain
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "pain"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pain'
        
    def run(self, dispatcher, tracker, domain):
        language = tracker.get_slot("language")
        response = get_utterance("ask_pain",language)
        dispatcher.utter_message(response)
        
class Fallback(AskAction):
    """
    Say something to the user : fallback
    """
    SIMPLE = True
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "fallback"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_fallback'
        
class Agree(AskAction):
    """
    Say something to the user : tell that we understand the user agreed
    """ 
    SIMPLE = True
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "agree"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_agree'
      
class Disagree(AskAction):
    """
    Say something to the user : tell that we understand the user disagreed
    """ 
    SIMPLE = True
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "disagree"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_disagree'
      
class AskWhy(AskAction):
    """
    Say something to the user : asky why the user is sad
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "why"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'ask_why'
      
class Bye(AskAction):
    """
    Say something to the user : say bye
    """ 
    SIMPLE = True
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "bye"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_bye'
             
class Hello(AskAction):
    """
    Say something to the user : say hello
    """ 
    SIMPLE = True
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "hello"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_hello'

class AskTreatmentDuration(AskAction):
    """
    Say something to the user : ask the duration of the treatment 
    """ 
    def init(self):
        """        
        Set the name of the entity to ask
        """
        self.entityName = "treatment_duration"
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_treatment_duration'