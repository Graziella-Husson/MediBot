from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action, ActionListen
from rasa_core.events import SlotSet, AllSlotsReset, UserUtteranceReverted, ReminderScheduled, ConversationPaused
from datetime import datetime as dt
import dateutil
from datetime import timedelta

from rasa_core.actions.forms import (
EntityFormField
)

import yaml
import os

from simple_actions import Fallback
from duckling import DucklingWrapper
from ressources import get_utterance

global config,first,obligatories,reminder_patient,reminder_end_session,reminder_patient_little,last_session, d, begin_date, language_global,followed_intent,complex_entities
config = yaml.load(open('config.yml'))
begin_date = None
first = True
obligatories = dict()
reminder_patient=timedelta(seconds=0)
reminder_end_session=timedelta(seconds=0)
reminder_patient_little=timedelta(seconds=0)
date_end=timedelta(seconds=0)
last_session=False
d = DucklingWrapper()
language_global = None
followed_reminders=[]
follow_intent_trigger_date = timedelta(seconds=0)
complex_entities = ["time", "body_part","distance","duration","period", "temperature"]

def get_complex_entities():
    """
    Get complex_entities list
    """
    return complex_entities
    
def get_followed_reminders():
    """
    Get followed_reminders list
    """
    return followed_reminders

def set_followed_reminders(to_set):
    """
    Set followed_reminders list
    """
    global followed_reminders
    followed_reminders = to_set
    
def get_language():
    """
    Get language
    """
    return language_global
    
def get_obligatories():
    """
    Get mandatories dictionnary
    """
    return obligatories

def get_reminder_patient():
    """
    Get get_reminder_patient time
    """
    return reminder_patient
    
def get_date_end():
    """
    Get date of the ending current session
    """
    return date_end
    
def get_reminder_end_session():
    """
    Get reminder_end_session time
    """
    return reminder_end_session
    
def get_last_session():
    """
    Get last session boolean
    """
    return last_session

class InitBot(Action):
    def set_begin_date(self):
        """
        Set the global variable begin_date
        If the begin_date for this patient is in the DB, get it
        If not, set it to now
        """
        global begin_date
        # TODO: get in DB if exists
        # if not :
        begin_date = dt.now()
        # TODO: save in DB
    
    def loadConfig(self,current_session,to_return):
        """
        Get all requested slots, requested intents, followed intent and add them into a dictionary used by many other actions.
        Get all config texts:
            - stopword
            - emergency word
            - nickname of the bot
            - exit word
            - language
            - count_user_reminder_max
        """
        global obligatories, language_global
        obligatories = dict()
        r=config['sessions'][current_session]['requested_slot']
        if r!="None":
            for j in r :
                obligatories[j] = []
                for i in r[j].split(','):
                    obligatories[j].append(EntityFormField(i, i))
        r=config['sessions'][current_session]['requested_intent']
        if r!="None":
            obligatories['requested_intent']= []
            for i in r.split(','):
                obligatories['requested_intent'].append(EntityFormField(i, i))
        r=config['sessions'][current_session]['followed_intent']
        followed_intent = []
        if r!="None":
            for i in r.split(','):
                followed_intent.append(i)
        stopword=str(config['stopword'])
        emergency=str(config['emergency'])
        nickname=str(config['nickname'])
        exitword=str(config['exit'])
        language_global=str(config['language'])
        count_user_reminder_max = config['count_user_reminder_max']
        to_return.append(SlotSet("stopword",stopword))
        to_return.append(SlotSet("emergency",emergency))
        to_return.append(SlotSet("nickname",nickname))
        to_return.append(SlotSet("exitword",exitword))
        to_return.append(SlotSet("count_user_reminder_max",count_user_reminder_max))
        to_return.append(SlotSet("count_user_reminder",0))
        to_return.append(SlotSet("followed_intent",followed_intent))
        to_return.append(SlotSet("language",language_global))
        return to_return

    def get_current_session(self):
        """
        @return current session number using begin_date and current date
        """
        delta_time = dt.now() - begin_date
        duration_done = timedelta(seconds=0)
        for i in config['sessions']:
            session = config['sessions'][i]
            duration = session['duration']
            for k in duration.keys():
                j = duration[k]
                if k == 'minutes':
                    duration_done+=timedelta(minutes=int(j))
                if k == 'weeks':
                    duration_done+=timedelta(weeks=int(j))
                if k == 'days':
                    duration_done+=timedelta(days=int(j))
                if k == 'hours':
                    duration_done+=timedelta(hours=int(j)) 
                if duration_done > delta_time:
                    return (i)
                
    def last_session(self,current_session):
        """
        @return True if it's the last session, False otherwise
        """
        try:
            config['sessions'][int(current_session)+1]
            current_session=int(current_session)
            return False
        except:
            current_session=int(current_session)
            return True
            
    def get_current_reminder_times(self,current_session,to_return):
        """
        @return: List of SlotSet
        Get all reminders times in config file:
            - reminder_patient
            - reminder_end_session
            - reminder_patient_little
            - follow_intent_trigger_date (time = date of Xst next session beginning, with X follow_in_current_session_plus config parameter)
        """
        global reminder_patient,reminder_end_session,reminder_patient_little,date_end,follow_intent_trigger_date
        reminders = ['reminder_patient','reminder_end_session','reminder_patient_little'] 
        duration_session = timedelta(seconds=0)   
        session = config['sessions'][current_session]
        for i in session['duration'].keys():
            j = session['duration'][i]
            if i == 'minutes':
                duration_session+=timedelta(minutes=int(j))
            if i == 'weeks':
                duration_session+=timedelta(weeks=int(j))
            if i == 'days':
                duration_session+=timedelta(days=int(j))
            if i == 'hours':
                duration_session+=timedelta(hours=int(j)) 
        date_end = dt.now()+duration_session
        
        for reminder in reminders:
            reminder_config = config[reminder]
            reminder1 = timedelta(seconds=0)
            for i in reminder_config.keys():
                j = reminder_config[i]
                if i == 'minutes':
                    reminder1+=timedelta(minutes=int(j))
                if i == 'weeks':
                    reminder1+=timedelta(weeks=int(j))
                if i == 'days':
                    reminder1+=timedelta(days=int(j))
                if i == 'hours':
                    reminder1+=timedelta(hours=int(j)) 
            if reminder == 'reminder_patient':
                reminder_patient=reminder1
            elif reminder == 'reminder_end_session':
                reminder_end_session=reminder1  
            elif reminder == 'reminder_patient_little':
                reminder_patient_little=reminder1
                
        follow_in_current_session_plus = int(config['follow_in_current_session_plus'])
        time = timedelta(seconds=5)
        time = self.get_duration_until(1,current_session, time)
        time = self.get_duration_until(current_session,follow_in_current_session_plus+current_session, time)
        follow_intent_trigger_date = begin_date+time
        return to_return
    
    def get_duration_until(self,begin,end, time):
        """
        @param begin: number of begin session
        @param end: number of end session
        @param time: time (0 or duration already set)
        @return time past between begin session and end session, add it to time paramter
        @raise LastSessionException : if the number of session between begin and end includes a non existent session
        """
        for i in range(begin,end):
            try:
                config['sessions'][i+1]['duration']
                duration = config['sessions'][i]['duration']
                for k in duration.keys():
                    j = duration[k]
                    if k == 'minutes':
                        time+=timedelta(minutes=int(j))
                    if k == 'weeks':
                        time+=timedelta(weeks=int(j))
                    if k == 'days':
                        time+=timedelta(days=int(j))
                    if k == 'hours':
                        time+=timedelta(hours=int(j))
            except:
                print("This is the last session!")
        return time
    
    def name(self):
        """
        @return: the name of the action.
        """
        return 'init'
        
    def run(self, dispatcher, tracker, domain):
        """
        @return: List of SlotSet
        If it's the first time we talk, call method C{set_begin_date}
        Get the current session
        Check if it's the last session
        Set the reminders times
        Do the complex config calling C{loadConfig}
        Set global score to 0
        """
        global first,last_session        
        to_return = []
        if first :
            first = False
            self.set_begin_date()
        else:
            to_return.append(SlotSet("requested_slot",None))
            to_return.append(AllSlotsReset())
        current_session = self.get_current_session()
        print("Current session is : "+str(current_session))
        last_session = self.last_session(current_session)
        to_return = self.get_current_reminder_times(current_session,to_return)
        to_return = self.loadConfig(current_session,to_return)
        to_return.append(SlotSet("current_session",current_session))
        to_return.append(SlotSet("global_score",0))
        return to_return

class SaveConv(Action):
    def duckling_set_slots(self,data,to_return):
        """
        @return: List of SlotSet
        @param data: all entities detected
        Check all the complex entities detected with duckling to know what slot to set:
            - time
            - distance
            - duration
            - temperature
        If distance, duration or temperature have a unit, set them
        For every times founded, check if it's the traduction of others entiity and, if not set time
        If time has a 'to' and 'from' date, check the duration and set it.
        """
        try:
            to_set = {'time':[],'distance':None,'duration':None,'temperature':None}
            time = None
            for i in data:
                entity = i['entity']
                if entity in to_set.keys():
                    if i['extractor'] == 'ner_duckling':
                        if entity != 'time':
                            unit = i['additional_info']['unit']
                            if unit != None:
                                value = str(i['additional_info']['value'])+" "+str(i['additional_info']['unit'])
                                to_set[entity]=value
                        else:
                            value = str(i['additional_info']['value'])
                            to_set[entity].append(value)
                    else:
                        if i['entity']=='time':
                            time = i['value']
            print(to_set)
            count = 0
            for i in to_set.keys():
                if to_set[i] != None:
                    if i != 'time':
                        to_return.append(SlotSet(i,to_set[i]))
                        count += 1 
                else:
                    to_return.append(SlotSet(i,None))
                    
            if len(to_set['time']) > count:
                for i in to_set.keys():
                    if i != 'time' and to_set[i] != None:
                        print(to_set[i])
                        to_check=[]
                        to_check_list = d.parse_time(to_set[i])
                        for k in to_check_list:
                            for j in k['value']['others']:
                                to_check.append(j['value'])
                        for j in to_set['time']:
                            if j.startswith('{'):
                                dict_to_from = yaml.load(j)               
                                for to_from in dict_to_from:
                                    time = dict_to_from[to_from]
                                    if time != 'None':
                                        for check in to_check:
                                            year = int(time[:4])
                                            if time[:-1] in check or year < 2010:
                                                to_set['time'].remove(j)
                                                break
                            else:
                                for check in to_check:
                                    year = int(j[:4])
                                    if j[:-1] in check or year < 2010:
                                        to_set['time'].remove(j)
                                        break
                to_return.append(SlotSet('time',to_set['time']))
                for i in to_set['time']:
                    dict_to_from = yaml.load(i)    
                    if dict_to_from['to'] != None and dict_to_from['from'] != None:
                        from_date = dateutil.parser.parse(dict_to_from['from'])
                        to_date = dateutil.parser.parse(dict_to_from['to'])
                        duration = to_date-from_date
                        if to_set['duration'] == None:
                            to_return.append(SlotSet('duration',duration))
            else:
                to_return.append(SlotSet('time',None))
        except:
            pass
        return to_return
        
    def save(self,tracker,to_return):
        """
        @return: List of : 
            - intent detected
            - entities detected
            - a list of SlotSet
            - response of the user
        Save everything the user said in a file named after the current session number in a folder named after the ID of patient
        Call C{followed_intent_found} method if the intent is followed
        """
        current_session = tracker.get_slot("current_session")
        id_user = tracker.sender_id
        idy = "./saves/"+str(id_user)+"/"+str(current_session)
        try:
            conv = open(idy, 'a')
        except:
            try:
                os.mkdir("saves") 
                os.mkdir("saves/"+str(id_user)+"/") 
            except:
                os.mkdir("saves/"+str(id_user)+"/") 
            conv = open(idy, 'a')  
        date = dt.now()
        response = tracker.latest_message.text
        intent = tracker.latest_message.intent
        intent_name = intent['name']
        followed_intent = tracker.get_slot("followed_intent")
        if intent_name in followed_intent:
            self.followed_intent_found(to_return,intent_name,current_session,followed_intent)
        to_return.append(SlotSet("topic",intent_name))
        entities = tracker.latest_message.entities
        #nlu_infos = tracker.latest_message.parse_data
        conv.write("{ '"+str(date)+"' : [{'intent':"+str(intent)+"}, {'entities':"+str(entities)+"}, {'text':'"+str(response)+"'}]},\n")
        conv.close()
        return [intent, entities,to_return,response]
    
    def followed_intent_found(self, to_return, intent_name,current_session,followed_intent):
        """
        @return: List of SlotSet
        @param to_return: the list of SlotSet 
        @param intent_name: the name of the intent followed
        @param current_session: number of the current session
        @param followed_intent: list of followed intent
        Set mandatory for this session the intent and entities linked
        Send a followed_intent_reminder reminder at the begining of the Xst next session 
        """
        global followed_reminders
        found = False
        for i in obligatories['requested_intent']:
            if intent_name in i.entity_name:
                found = True
        if not found:
            obligatories['requested_intent'].append(EntityFormField(intent_name, intent_name))
        entities = ""
        for entity in obligatories[intent_name]:
            entities += entity.entity_name+"."
        entities = entities[:-1]
#        name = intent_name+"-"+entities+"*"+str(current_session)
#        print("Reminder scheduled at "+str(follow_intent_trigger_date)+" for following intent: "+intent_name)
#        reminder = ReminderScheduled("followed_intent_reminder", follow_intent_trigger_date, name, kill_on_user_message=False)
#        #TODO : add reminder in DB using reminder.as_dict()
#        followed_reminders.append(reminder)
#        to_return.append(reminder)
        followed_intent.remove(intent_name)
        to_return.append(SlotSet("followed_intent",followed_intent))
    
    def check(self,to_return,intent,entities,tracker,dispatcher,response,domain):
        """
        @return: List of SlotSet
        @param to_return: the list of SlotSet 
        @param intent: intent detected 
        @param entities: entities detected
        @param response: response of the user
        Check the response of the user :
            - if the confidence of intent detection is under 50%, call C{Fallback} action
            - if one of specific word is detected:
                - emergency: send an alert
                - stopword: tell the bot that he made a mistake
                - exitword: do not send the reminder_user_little reminder
            - if none of the above is detected :
                - Send user_reminder_little and user_reminder
        """
        language = tracker.get_slot("language")
        response1 = ("""`\tIntent : {}`
`\tEntities : {}`""").format(intent, entities)
        dispatcher.utter_message(response1)
        if intent['confidence']<0.5:
            action = Fallback()
            tracker.trigger_follow_up_action(action)
            return to_return
        else:
            emergency = tracker.get_slot("emergency")
            stopword = tracker.get_slot("stopword")
            exitword = tracker.get_slot("exitword")
            if response == emergency:
                #TODO : send a notification instead
                dispatcher.utter_message(get_utterance("emergency",language))
                SumUpSLots().run(dispatcher, tracker, domain)            
                action = ActionListen()
                tracker.trigger_follow_up_action(action)
                return to_return
            elif response == stopword and not first:
                for i in range (0,2):
                    if not (tracker.latest_action_name == None or tracker.latest_action_name == 'init'):
                        #print(tracker.latest_action_name)
                        to_return.append(UserUtteranceReverted())
                        if not (tracker.latest_action_name == None or tracker.latest_action_name == 'init'):
                            to_return.append(UserUtteranceReverted())
                        return to_return
            elif response == exitword:
                dispatcher.utter_message(get_utterance("exit",language))
                SumUpSLots().run(dispatcher, tracker, domain)   
                action = ActionListen()
                tracker.trigger_follow_up_action(action)
                count_user_reminder = 0
                to_return.append(SlotSet("count_user_reminder",count_user_reminder))
#                print("reminder user scheduled at "+str(dt.now() + reminder_patient))
#                to_return.append(ReminderScheduled("user_reminder", dt.now() + reminder_patient, kill_on_user_message=True))
                return to_return
            
            else:
                count_user_reminder = 0
#                to_return.append(SlotSet("count_user_reminder",count_user_reminder))
#                print("reminder user little scheduled at "+str(dt.now() + reminder_patient_little))
#                to_return.append(ReminderScheduled("user_reminder_little", dt.now() + reminder_patient_little,kill_on_user_message=True))
#                print("reminder user scheduled at "+str(dt.now() + reminder_patient))
#                to_return.append(ReminderScheduled("user_reminder", dt.now() + reminder_patient, kill_on_user_message=True))
                return to_return
        
    def name(self):
        """
        @return: the name of the action.
        """
        return 'save_conv'
        
    def run(self, dispatcher, tracker, domain):
        """
        @return: List of SlotSet
        If it's the first time we talk, call the method C{InitBot().run} and send reminders
        Save conversation
        Set slots checking complex entities with duckling
        Check if there's no noticeable word or low confidence
        """
        global first        
        language = tracker.get_slot("language")
        to_return = []
        if first:
            to_return = InitBot().run(dispatcher, tracker, domain)
            for i in to_return:
                tracker.update(i)
            nickname = tracker.get_slot("nickname")
            language = tracker.get_slot("language")
            print(language)
            to_return = []
#            print("reminder change session scheduled at "+str(date_end))
#            to_return.append(ReminderScheduled("change_session_reminder", date_end, kill_on_user_message=False))  
#            print("reminder before change session scheduled at "+str(date_end - reminder_end_session))
#            to_return.append(ReminderScheduled("session_end_reminder", date_end - reminder_end_session, kill_on_user_message=False)) 
            dispatcher.utter_message(get_utterance("welcome",language)+" "+nickname)
        [intent, entities,to_return,response] = self.save(tracker,to_return)
        to_return = self.duckling_set_slots(entities,to_return)
        to_return = self.check(to_return,intent,entities,tracker,dispatcher,response,domain)
        return to_return
            
class SumUpSLots(Action):
    def name(self):
        """
        @return: the name of the action.
        """
        return 'sum_up_slots'
        
    def run(self, dispatcher, tracker, domain):
          """
          Sum up slots from the tracker (for debug)
          Save bot utterances in conversation save file
          """
          id_user = tracker.sender_id
          current_session = tracker.get_slot("current_session")
          idy = "./saves/"+str(id_user)+"/"+str(current_session)
          try:
              conv = open(idy, 'a')
          except:
              os.mkdir("saves") 
              os.mkdir("saves/"+str(id_user)+"/") 
              conv = open(idy, 'a')
          date = dt.now()
          response = tracker.latest_bot_utterance.text
          if not response == None:
              conv.write("{ '"+str(date)+"' : [{'text': '"+response+"'}]],\n")
          response = ("""`\ttopic = {}, requested_slot = {},`
`\tactivity = {}, sport = {}, activity_level = {}, activity_duration = {}, activity_period = {}, activity_hard = {}, activity_time = {}, activity_distance = {},`
`\tpain = {}, pain_duration = {}, pain_desc = {}, pain_body_part = {}, pain_change = {}, pain_period = {}, pain_level = {}, pain_time = {},` 
`\tpathology = {}, symtoms = {}, pathology_body_part = {}, pathology_time = {}, pathology_change = {}, pathology_period = {}, pathology_treatment_linked = {},`
`\ttreatment = {}, medicinal = {}, treatment_being_taken = {}, drug = {}, dosing = {}, treatment_time = {}, treatment_prescripted = {}, treatment_ok = {}, treatment_overdosage = {}, treatment_period = {}, treatment_duration = {}`
`\tinfoPatient = {}, addiction = {}, weight = {}, infoPatient_distance = {}, gender = {}, infoPatient_temperature = {}, heart_rate = {}, blood_pressure = {}, infoPatient_time= {},`
`\tsadness = {},`
`\thappy = {},`
`\tsocial = {},`
`\trisk = {},`
`\tdistance = {}, period = {}, duration = {}, time = {}, body_part = {},temperature = {}`""").format(
tracker.get_slot("topic"), tracker.get_slot("requested_slot"),
tracker.get_slot("activity"), tracker.get_slot("sport"), tracker.get_slot("activity_level"), tracker.get_slot("activity_duration"), tracker.get_slot("activity_period"), tracker.get_slot("activity_hard"), tracker.get_slot("activity_time"),tracker.get_slot("activity_distance"),
tracker.get_slot("pain"), tracker.get_slot("pain_duration"), tracker.get_slot("pain_desc"), tracker.get_slot("pain_body_part"), tracker.get_slot("pain_change"), tracker.get_slot("pain_period"), tracker.get_slot("pain_level"), tracker.get_slot("pain_time"),
tracker.get_slot("pathology"), tracker.get_slot("symtoms"),tracker.get_slot("pathology_body_part"),tracker.get_slot("pathology_time"),tracker.get_slot("pathology_change"),tracker.get_slot("pathology_period"),tracker.get_slot("pathology_treatment_linked"),
tracker.get_slot("treatment"), tracker.get_slot("medicinal"), tracker.get_slot("treatment_being_taken"),tracker.get_slot("drug"),tracker.get_slot("dosing"),tracker.get_slot("treatment_time"),tracker.get_slot("treatment_prescripted"),tracker.get_slot("treatment_ok"),tracker.get_slot("treatment_overdosage"),tracker.get_slot("treatment_period"),tracker.get_slot("treatment_duration"),
tracker.get_slot("infoPatient"), tracker.get_slot("addiction"), tracker.get_slot("weight"), tracker.get_slot("infoPatient_distance"), tracker.get_slot("gender"), tracker.get_slot("infoPatient_temperature"), tracker.get_slot("heart_rate"), tracker.get_slot("blood_pressure"), tracker.get_slot("infoPatient_time"),
tracker.get_slot("emotional_sadness"),
tracker.get_slot("emotional_hapiness"),
tracker.get_slot("social"),
tracker.get_slot("risk"),
tracker.get_slot("distance"), tracker.get_slot("period"), tracker.get_slot("duration"), tracker.get_slot("time"), tracker.get_slot("body_part"), tracker.get_slot("temperature"))
          dispatcher.utter_message(response)
          conv.write("{ '"+str(date)+"' : [{'text': '"+response+"'}]},\n")
          conv.close() 