from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.dispatcher import Button
from ressources import get_utterance
import yaml

class Fallback(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_fallback'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : fallback
        """
        language = tracker.get_slot("language")
        response = get_utterance("fallback",language)
        dispatcher.utter_message(response)

class AskActivityHard(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_activity_hard'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask if the activity was hard to perform because of the general health
        """  
        language = tracker.get_slot("language")
        message = get_utterance("ask_activity_hard",language)
        yes_button = get_utterance("yes",language)
        no_button = get_utterance("no",language)
        buttons = [Button(title=yes_button, payload="/activity{\"activity_hard\":true}"),       
                   Button(title=no_button, payload="/activity{\"activity_hard\":false}")] 
        dispatcher.utter_button_message(message, buttons)

class AskSport(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_sport'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the activity the user did
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_sport",language)
        dispatcher.utter_message(response)
        
class AskActivityDuration(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_activity_duration'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the duration of the activity
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_activity_duration",language)
        dispatcher.utter_message(response)

class AskPainBodyPart(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pain_body_part'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the part of the body where the pain is
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_pain_body_part",language)
        dispatcher.utter_message(response)

class AskPathologyBodyPart(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pathology_body_part'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the body part where the pathology is
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_pathology_body_part",language)
        dispatcher.utter_message(response)

class AskPainDuration(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pain_duration'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the duration of the pain
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_pain_duration",language)
        dispatcher.utter_message(response)
        
class AskPainChange(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pain_change'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : display buttons asking the evolution of the pain (brief, continuous, intermittent)
        """ 
        language = tracker.get_slot("language")
        message = get_utterance("ask_pain_change",language)
        continuous_button = get_utterance("continuous_button",language)
        intermittent_button = get_utterance("intermittent_button",language)
        brief_button = get_utterance("brief_button",language)
        buttons = [Button(title=continuous_button, payload="/pain{\"pain_change\":\""+continuous_button.lower()+"\"}"),       
                   Button(title=intermittent_button, payload="/pain{\"pain_change\":\""+intermittent_button.lower()+"\"}"),       
                   Button(title=brief_button, payload="/pain{\"pain_change\":\""+brief_button.lower()+"\"}")] 
        dispatcher.utter_button_message(message, buttons)
 
class AskPainPeriod(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pain_period'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the period of the pain
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_pain_period",language)
        dispatcher.utter_message(response)

class AskActivityPeriod(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_activity_period'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the period of the activity
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_activity_period",language)
        dispatcher.utter_message(response)

class AskPain(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pain'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the user to talk about his pain
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_pain",language)
        dispatcher.utter_message(response)

class AskActivity(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_activity'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user :  ask the user to talk about his activity
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_activity",language)
        dispatcher.utter_message(response)
        
class AskSocial(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_social'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user :  ask the user to talk about his social activity
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_social",language)
        dispatcher.utter_message(response)

class AskHappiness(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_emotionnal_hapiness'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user :  ask the user to talk about his happiness
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_happiness",language)
        dispatcher.utter_message(response)

class AskSadness(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_emotionnal_sadness'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user :  ask the user to talk about his sadness
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_sadness",language)
        dispatcher.utter_message(response)
       
class AskPainDesc(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pain_desc'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user :  ask the description of the pain
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_pain_desc",language)
        dispatcher.utter_message(response)
       
class Agree(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_agree'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : tell that we understand the user agreed
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("agree",language)
        dispatcher.utter_message(response)
      
class Disagree(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_disagree'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : tell that we understand the user disagreed
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("disagree",language)
        dispatcher.utter_message(response)
      
class AskWhy(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'ask_why'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : asky why the user is sad
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_why",language)
        dispatcher.utter_message(response)
      
class Bye(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_bye'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : say bye
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("bye",language)
        dispatcher.utter_message(response)
             
class Hello(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_hello'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : say hello
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("hello",language)
        dispatcher.utter_message(response)
             
class AskSymptoms(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_symtoms'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the symptoms
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_symtoms",language)
        dispatcher.utter_message(response)         

class AskMedicinal(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_medicinal'
        
    def run(self, dispatcher, tracker, domain):
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
        language = tracker.get_slot("language")
        message = get_utterance("ask_medicinal",language)
        
        yes_button = get_utterance("yes",language)
        no_button = get_utterance("no",language)
        buttons = [Button(title=yes_button, payload="/treatment{\"medicinal\":true}"),       
                   Button(title=no_button, payload="/treatment{\"medicinal\":false, \"drug\":\"no_drug\", \"dosing\":\"no_drug\", \"treatment_being_taken\":\"no_drug\", \"treatment_overdosage\":\"no_drug\"}")] 
        dispatcher.utter_button_message(message, buttons)

class AskDrug(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_drug'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the drug of the treatment
        We have to talk about that only if the treatment is medicinal
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_drug",language)
        dispatcher.utter_message(response)         

class AskPainTime(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pain_time'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the begin date of the pain
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_pain_time",language)
        dispatcher.utter_message(response)     

class AskActivityTime(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_activity_time'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the begin date of the activity
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_activity_time",language)
        dispatcher.utter_message(response)     

class AskActivityDistance(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_activity_distance'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the distance of the activity
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_activity_distance",language)
        dispatcher.utter_message(response) 
        
class AskWeight(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_weight'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the weight of the patient
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_weight",language)
        dispatcher.utter_message(response) 
        
class AskInfoPatientDistance(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_infoPatient_distance'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the size of the patients
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_infoPatient_distance",language)
        dispatcher.utter_message(response) 
        
class AskHeartRate(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_heart_rate'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the heart rate of the patient
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_heart_rate",language)
        dispatcher.utter_message(response) 
   
class AskInfoPatientTemperature(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_infoPatient_temperature'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the temperature of the patient
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_infoPatient_temperature",language)
        dispatcher.utter_message(response) 
   
class AskGender(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_gender'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the gender of the patient
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_gender",language)
        dispatcher.utter_message(response) 

class AskBloodPressure(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_blood_pressure'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the blood pressure of the patient
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_blood_pressure",language)
        dispatcher.utter_message(response) 
   
class AskAddiction(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_addiction'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask if the patient have an addicition
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_addiction",language)
        dispatcher.utter_message(response) 
   
class AskInfoPatientTime(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_infoPatient_time'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the last date of medical check up
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_infoPatient_time",language)
        dispatcher.utter_message(response) 
        
class AskPathologyTime(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pathology_time'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the begin time of pathology/side effect/symptom
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_pathology_time",language)
        dispatcher.utter_message(response) 

class AskPathologyPeriod(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pathology_period'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the period of pathology/side effect/symptom
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_pathology_period",language)
        dispatcher.utter_message(response)

class AskPathologyChange(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pathology_change'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : display buttons to tell if the pathology is worst or not
        """ 
        language = tracker.get_slot("language")
        message = get_utterance("ask_pathology_change",language)
        
        yes_button = get_utterance("yes",language)
        no_button = get_utterance("no",language)
        buttons = [Button(title=yes_button, payload="/pathology{\"pathology_change\":true}"),       
                   Button(title=no_button, payload="/pathology{\"pathology_change\":false}")] 
        dispatcher.utter_button_message(message, buttons)

class AskPathologyTreatmentLinked(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_pathology_treatment_linked'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : display buttons to tell if the pathology is linked to the treatment or not (according to patient)
        """ 
        language = tracker.get_slot("language")
        message = get_utterance("ask_pathology_treatment_linked",language)
        
        yes_button = get_utterance("yes",language)
        no_button = get_utterance("no",language)
        buttons = [Button(title=yes_button, payload="/pathology{\"pathology_treatment_linked\":true}"),       
                   Button(title=no_button, payload="/pathology{\"pathology_treatment_linked\":false}")] 
        dispatcher.utter_button_message(message, buttons)
        
class AskDosing(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_dosing'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the dose the patient is taking (not the one prescripted)
        We have to talk about that only if the treatment is medicinal
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_dosing",language)
        dispatcher.utter_message(response)
        
class AskTreatmentTime(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_treatment_time'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the begin date of the treatment taken
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_treatment_time",language)
        dispatcher.utter_message(response)
        
class AskTreatmentBeingTaken(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_treatment_being_taken'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : display buttons to tell if the treatment is being well taken or forgotten or stopped
        When the "stopped" button is clicked, we have to set :
            - dosing
        to something, saying that we won't ask anything about it for this treatment.        
        """ 
        language = tracker.get_slot("language")
        message = get_utterance("ask_treatment_being_taken",language)
        taken_button = get_utterance("taken",language)
        stopped_button = get_utterance("stopped",language)
        forgotten_button = get_utterance("forgotten",language)
        buttons = [Button(title=taken_button, payload="/treatment{\"treatment_being_taken\":\""+taken_button.lower()+"\"}"),       
                   Button(title=stopped_button, payload="/treatment{\"treatment_being_taken\":\""+stopped_button.lower()+"\", \"dosing\":\"no_drug\"}"),    
                   Button(title=forgotten_button, payload="/treatment{\"treatment_being_taken\":\""+forgotten_button.lower()+"\"}")] 
        dispatcher.utter_button_message(message, buttons)

class AskTreatmentOverdosage(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_treatment_overdosage'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : display buttons to tell if the treatment dose is well taken or overdose or under dose
        """ 
        language = tracker.get_slot("language")
        message = get_utterance("ask_treatment_overdosage",language)
        taken_button = get_utterance("welltaken",language)
        overdose_button = get_utterance("overdose",language)
        underdose_button = get_utterance("underdose",language)
        buttons = [Button(title=taken_button, payload="/treatment{\"treatment_overdosage\":\""+taken_button.lower()+"\"}"),       
                   Button(title=overdose_button, payload="/treatment{\"treatment_overdosage\":\""+overdose_button.lower()+"\"}"),    
                   Button(title=underdose_button, payload="/treatment{\"treatment_overdosage\":\""+underdose_button.lower()+"\"}")] 
        dispatcher.utter_button_message(message, buttons)
        
class AskTreatmentPeriod(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_treatment_period'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : ask the period of the medicinal treatment 
        """ 
        language = tracker.get_slot("language")
        response = get_utterance("ask_treatment_period",language)
        dispatcher.utter_message(response)

class AskTreatmentPrescripted(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_treatment_prescripted'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : display buttons to tell if the treatment is prescripted or not
        """ 
        language = tracker.get_slot("language")
        message = get_utterance("ask_treatment_prescripted",language)
        
        yes_button = get_utterance("yes",language)
        no_button = get_utterance("no",language)
        buttons = [Button(title=yes_button, payload="/treatment{\"treatment_prescripted\":true}"),       
                   Button(title=no_button, payload="/treatment{\"treatment_prescripted\":false}")] 
        dispatcher.utter_button_message(message, buttons)

class AskTreatmentOk(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'utter_ask_treatment_ok'
        
    def run(self, dispatcher, tracker, domain):
        """
        Say something to the user : display buttons to tell if the patient feels ok about his treatment or not
        """ 
        language = tracker.get_slot("language")
        message = get_utterance("ask_treatment_ok",language)
        
        yes_button = get_utterance("yes",language)
        no_button = get_utterance("no",language)
        buttons = [Button(title=yes_button, payload="/treatment{\"treatment_ok\":true}"),       
                   Button(title=no_button, payload="/treatment{\"treatment_ok\":false}")] 
        dispatcher.utter_button_message(message, buttons)
  