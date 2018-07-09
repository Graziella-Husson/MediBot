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
        return 'sum_up_fallback'
        
    def run(self, dispatcher, tracker, domain):  
        language = tracker.get_slot("language")
        response = get_utterance("fallback",language)
        dispatcher.utter_message(response)

class AskActivityHard(Action):
    def name(self):
        return 'utter_ask_activity_hard'
        
    def run(self, dispatcher, tracker, domain):  
        language = tracker.get_slot("language")
        message = get_utterance("ask_activity_hard",language)
        yes_button = get_utterance("yes",language)
        no_button = get_utterance("no",language)
        buttons = [Button(title=yes_button, payload="/activity{\"activity_hard\":true}"),       
                   Button(title=no_button, payload="/activity{\"activity_hard\":false}")] 
        dispatcher.utter_button_message(message, buttons)

class AskSport(Action):
    def name(self):
        return 'utter_ask_sport'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_sport",language)
        dispatcher.utter_message(response)
        
class AskActivityDuration(Action):
    def name(self):
        return 'utter_ask_activity_duration'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_activity_duration",language)
        dispatcher.utter_message(response)

class AskPainBodyPart(Action):
    def name(self):
        return 'utter_ask_pain_body_part'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_pain_body_part",language)
        dispatcher.utter_message(response)

class AskPathologyBodyPart(Action):
    def name(self):
        return 'utter_ask_pathology_body_part'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_pathology_body_part",language)
        dispatcher.utter_message(response)

class AskPainDuration(Action):
    def name(self):
        return 'utter_ask_pain_duration'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_pain_duration",language)
        dispatcher.utter_message(response)
        
class AskPainChange(Action):
    def name(self):
        return 'utter_ask_pain_change'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        message = get_utterance("ask_pain_change",language)
        continuous_button = get_utterance("continuous_button",language)
        intermittent_button = get_utterance("intermittent_button",language)
        brief_button = get_utterance("brief_button",language)
        buttons = [Button(title=continuous_button, payload="/pain{\"pain_change\":\"continuous\"}"),       
                   Button(title=intermittent_button, payload="/pain{\"pain_change\":\"intermittent\"}"),       
                   Button(title=brief_button, payload="/pain{\"pain_change\":\"brief\"}")] 
        dispatcher.utter_button_message(message, buttons)
 
class AskPainPeriod(Action):
    def name(self):
        return 'utter_ask_pain_period'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_pain_period",language)
        dispatcher.utter_message(response)

class AskActivityPeriod(Action):
    def name(self):
        return 'utter_ask_activity_period'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_activity_period",language)
        dispatcher.utter_message(response)

class AskPain(Action):
    def name(self):
        return 'utter_ask_pain'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_pain",language)
        dispatcher.utter_message(response)

class AskActivity(Action):
    def name(self):
        return 'utter_ask_activity'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_activity",language)
        dispatcher.utter_message(response)
        
class AskSocial(Action):
    def name(self):
        return 'utter_ask_social'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_social",language)
        dispatcher.utter_message(response)

class AskHappiness(Action):
    def name(self):
        return 'utter_ask_emotionnal_hapiness'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_happiness",language)
        dispatcher.utter_message(response)

class AskSadness(Action):
    def name(self):
        return 'utter_ask_emotionnal_sadness'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_sadness",language)
        dispatcher.utter_message(response)
       
class AskPainDesc(Action):
    def name(self):
        return 'utter_ask_pain_desc'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_pain_desc",language)
        dispatcher.utter_message(response)
       
class Agree(Action):
    def name(self):
        return 'sum_up_agree'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("agree",language)
        dispatcher.utter_message(response)
      
class Disagree(Action):
    def name(self):
        return 'sum_up_disagree'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("disagree",language)
        dispatcher.utter_message(response)
      
class AskWhy(Action):
    def name(self):
        return 'ask_why'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_why",language)
        dispatcher.utter_message(response)
      
class Bye(Action):
    def name(self):
        return 'sum_up_bye'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("bye",language)
        dispatcher.utter_message(response)
             
class Hello(Action):
    def name(self):
        return 'sum_up_hello'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("hello",language)
        dispatcher.utter_message(response)
             
class AskSymptoms(Action):
    def name(self):
        return 'utter_ask_symtoms'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_symtoms",language)
        dispatcher.utter_message(response)         

class AskMedicinal(Action):
    def name(self):
        return 'utter_ask_medicinal'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        message = get_utterance("ask_medicinal",language)
        
        yes_button = get_utterance("yes_button",language)
        no_button = get_utterance("no_button",language)
        buttons = [Button(title=yes_button, payload="/treatment{\"medicinal\":true}"),       
                   Button(title=no_button, payload="/treatment{\"medicinal\":false, \"drug\":\"no_drug\"}")] 
        dispatcher.utter_button_message(message, buttons)

class AskDrug(Action):
    def name(self):
        return 'utter_ask_drug'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_drug",language)
        dispatcher.utter_message(response)         

class AskPainTime(Action):
    def name(self):
        return 'utter_ask_pain_time'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_pain_time",language)
        dispatcher.utter_message(response)     

class AskActivityTime(Action):
    def name(self):
        return 'utter_ask_activity_time'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_activity_time",language)
        dispatcher.utter_message(response)     

class AskActivityDistance(Action):
    def name(self):
        return 'utter_ask_activity_distance'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_activity_distance",language)
        dispatcher.utter_message(response) 
        
class AskWeight(Action):
    def name(self):
        return 'utter_ask_weight'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_weight",language)
        dispatcher.utter_message(response) 
        
class AskInfoPatientDistance(Action):
    def name(self):
        return 'utter_ask_infoPatient_distance'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_infoPatient_distance",language)
        dispatcher.utter_message(response) 
        
class AskHeartRate(Action):
    def name(self):
        return 'utter_ask_heart_rate'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_heart_rate",language)
        dispatcher.utter_message(response) 
   
class AskInfoPatientTemperature(Action):
    def name(self):
        return 'utter_ask_infoPatient_temperature'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_infoPatient_temperature",language)
        dispatcher.utter_message(response) 
   
class AskGender(Action):
    def name(self):
        return 'utter_ask_gender'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_gender",language)
        dispatcher.utter_message(response) 

class AskBloodPressure(Action):
    def name(self):
        return 'utter_ask_blood_pressure'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_blood_pressure",language)
        dispatcher.utter_message(response) 
   
class AskAddiction(Action):
    def name(self):
        return 'utter_ask_addiction'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_addiction",language)
        dispatcher.utter_message(response) 
   
class AskInfoPatientTime(Action):
    def name(self):
        return 'utter_ask_infoPatient_time'
        
    def run(self, dispatcher, tracker, domain): 
        language = tracker.get_slot("language")
        response = get_utterance("ask_infoPatient_time",language)
        dispatcher.utter_message(response) 
        
if __name__ == '__main__':
    config = yaml.load(open('config.yml'))
    language=str(config['language'])
    print(get_utterance("fallback",language))