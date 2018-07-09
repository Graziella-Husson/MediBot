from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action, ActionListen
from rasa_core.events import SlotSet, AllSlotsReset, UserUtteranceReverted, ReminderScheduled, ConversationPaused
from datetime import datetime as dt
from datetime import timedelta

from rasa_core.actions.forms import (
EntityFormField
)

import yaml
import os

from simpleActions import Fallback
from duckling import DucklingWrapper
from ressources import get_utterance

global config,first,obligatories,reminder_patient,reminder_end_session,reminder_patient_little,last_session, d
config = yaml.load(open('config.yml'))
first = True
obligatories = dict()
reminder_patient=timedelta(seconds=0)
reminder_end_session=timedelta(seconds=0)
reminder_patient_little=timedelta(seconds=0)
date_end=timedelta(seconds=0)
last_session=False
d = DucklingWrapper()
print(d)

def get_obligatories():
    return obligatories

def get_reminder_patient():
    return reminder_patient
    
def get_date_end():
    return date_end
    
def get_reminder_end_session():
    return reminder_end_session
    
def get_last_session():
    return last_session

class InitBot(Action):

    def loadConfig(self,current_session,to_return):
        global obligatories
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
        followed_intent=[]
        r=config['sessions'][current_session]['followed_intent']
        if r!="None":
            for i in r.split(','):
                followed_intent.append(i)
        stopword=str(config['stopword'])
        emergency=str(config['emergency'])
        nickname=str(config['nickname'])
        exitword=str(config['exit'])
        language=str(config['language'])
        count_user_reminder_max = config['count_user_reminder_max']
        to_return.append(SlotSet("stopword",stopword))
        to_return.append(SlotSet("emergency",emergency))
        to_return.append(SlotSet("nickname",nickname))
        to_return.append(SlotSet("exitword",exitword))
        to_return.append(SlotSet("count_user_reminder_max",count_user_reminder_max))
        to_return.append(SlotSet("count_user_reminder",0))
        to_return.append(SlotSet("followed_intent",followed_intent))
        to_return.append(SlotSet("language",language))
        return to_return

    def get_current_session(self):
        now = dt.now()
        inter = abs(now-dt(2011, 1, 1))
        my_date= now
        begins = dict()
        for i in config['sessions']:
            for j in config['sessions'][i]:
                if j == "begin":
                    begins[i] = config['sessions'][i][j]
        for i in begins.values():
            date_el = i.split(',')
            date=dt(int(date_el[0]), int(date_el[1]),int(date_el[2]),
                                      int(date_el[3]),int(date_el[4]), int(date_el[5]))
            this_inter = abs(now - date)
            if  this_inter < inter:
                inter = this_inter
                my_date=date
        
        for i in begins.keys():
            date_el = begins[i].split(',')
            date=dt(int(date_el[0]), int(date_el[1]),int(date_el[2]),
                                      int(date_el[3]),int(date_el[4]), int(date_el[5]))
            if str(date)== str(my_date):
                current_session = i
        current_session=int(current_session)
        return current_session
                
    def last_session(self,tracker,current_session):
        try:
            config['sessions'][int(current_session)+1]
            current_session=int(current_session)
            return False
        except:
            current_session=int(current_session)
            return True
            
    def get_current_reminder_times(self,current_session,to_return):
        global reminder_patient,reminder_end_session,reminder_patient_little,date_end
        reminders = ['reminder_patient','reminder_end_session','reminder_patient_little'] 
        end = config['sessions'][current_session]['end']
        date_el = end.split(',')
        date_end=dt(int(date_el[0]), int(date_el[1]),int(date_el[2]),
                                  int(date_el[3]),int(date_el[4]), int(date_el[5]))
        print(current_session)
        print(date_end)
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
        to_return.append(SlotSet("follow_in_current_session_plus",follow_in_current_session_plus))   
        return to_return
    
    def name(self):
        return 'init'
        
    def run(self, dispatcher, tracker, domain):
        global first,last_session
        to_return = []
        current_session = self.get_current_session()
        print("Current session is : "+str(current_session))
        last_session = self.last_session(tracker,current_session)
        if first :
            first = False
        else:
            to_return.append(SlotSet("requested_slot",None))
            to_return.append(AllSlotsReset())
        to_return = self.get_current_reminder_times(current_session,to_return)
        to_return = self.loadConfig(current_session,to_return)
        to_return.append(SlotSet("current_session",current_session))
        to_return.append(SlotSet("global_score",0))
        return to_return

class SaveConv(Action):
    def duckling_set_slots(self,data,to_return):
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
            else:
                to_return.append(SlotSet('time',None))
        except:
            pass
        return to_return
        
    def save(self,tracker,to_return):
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
        follow_in_current_session_plus=tracker.get_slot("follow_in_current_session_plus")
        followed_intent = tracker.get_slot("followed_intent")
        if intent_name in followed_intent:
            new_session = int(current_session)+follow_in_current_session_plus
            try:
                old = config['sessions'][new_session]['requested_intent']
                if intent_name not in old:
                    config['sessions'][new_session]['requested_intent'] = old+","+intent_name
                with open('config.yml', 'w') as outfile:
                    yaml.dump(config, outfile, default_flow_style=False)
            except:
                print("last session!")
        to_return.append(SlotSet("topic",intent_name))
        entities = tracker.latest_message.entities
        #nlu_infos = tracker.latest_message.parse_data
        conv.write("{ '"+str(date)+"' : [{'intent':"+str(intent)+"}, {'entities':"+str(entities)+"}, {'text':'"+str(response)+"'}]},\n")
        conv.close()
        return [intent, entities,to_return,response]
    
    def check(self,to_return,intent,entities,tracker,dispatcher,response,domain):
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
        return 'save_conv'
        
    def run(self, dispatcher, tracker, domain):
        global first        
        language = tracker.get_slot("language")
        to_return = []
        if first:
            to_return = InitBot().run(dispatcher, tracker, domain)
            for i in to_return:
                tracker.update(i)
            nickname = tracker.get_slot("nickname")
            language = tracker.get_slot("language")
            to_return = []
            #print("reminder change session scheduled at "+str(date_end))
            #to_return.append(ReminderScheduled("change_session_reminder", date_end, kill_on_user_message=False))  
            #print("reminder before change session scheduled at "+str(date_end - reminder_end_session))
            #to_return.append(ReminderScheduled("session_end_reminder", date_end - reminder_end_session, kill_on_user_message=False)) 
            dispatcher.utter_message(get_utterance("welcome",language)+" "+nickname)
        [intent, entities,to_return,response] = self.save(tracker,to_return)
        to_return = self.duckling_set_slots(entities,to_return)
        to_return = self.check(to_return,intent,entities,tracker,dispatcher,response,domain)
        return to_return
            
class SumUpSLots(Action):
    def name(self):
        return 'sum_up_slots'
        
    def run(self, dispatcher, tracker, domain):
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
`\tactivity = {}, sport = {}, activity_duration = {}, activity_period = {}, activity_hard = {}, activity_time = {}, activity_distance = {},`
`\tpain = {}, pain_duration = {}, pain_desc = {}, pain_body_part = {}, pain_change = {}, pain_period = {}, pain_level = {}, pain_time = {},` 
`\tpathology = {}, symtoms = {}, pathology_body_part = {},`
`\ttreatment = {}, medicinal = {}, drug = {},`
`\tinfoPatient = {}, addiction = {}, weight = {}, infoPatient_distance = {}, gender = {}, infoPatient_temperature = {}, heart_rate = {}, blood_pressure = {}, infoPatient_time= {},`
`\tsadness = {},`
`\thappy = {},`
`\tsocial = {},`
`\tdistance = {}, period = {}, duration = {}, time = {}, body_part = {},temperature = {}`""").format(
tracker.get_slot("topic"), tracker.get_slot("requested_slot"),
tracker.get_slot("activity"), tracker.get_slot("sport"), tracker.get_slot("activity_duration"), tracker.get_slot("activity_period"), tracker.get_slot("activity_hard"), tracker.get_slot("activity_time"),tracker.get_slot("activity_distance"),
tracker.get_slot("pain"), tracker.get_slot("pain_duration"), tracker.get_slot("pain_desc"), tracker.get_slot("pain_body_part"), tracker.get_slot("pain_change"), tracker.get_slot("pain_period"), tracker.get_slot("pain_level"), tracker.get_slot("pain_time"),
tracker.get_slot("pathology"), tracker.get_slot("symtoms"),tracker.get_slot("pathology_body_part"),
tracker.get_slot("treatment"), tracker.get_slot("medicinal"), tracker.get_slot("drug"),
tracker.get_slot("infoPatient"), tracker.get_slot("addiction"), tracker.get_slot("weight"), tracker.get_slot("infoPatient_distance"), tracker.get_slot("gender"), tracker.get_slot("infoPatient_temperature"), tracker.get_slot("heart_rate"), tracker.get_slot("blood_pressure"), tracker.get_slot("infoPatient_time"),
tracker.get_slot("emotional_sadness"),
tracker.get_slot("emotional_hapiness"),
tracker.get_slot("social"),
tracker.get_slot("distance"), tracker.get_slot("period"), tracker.get_slot("duration"), tracker.get_slot("time"), tracker.get_slot("body_part"), tracker.get_slot("temperature"))
          dispatcher.utter_message(response)
          conv.write("{ '"+str(date)+"' : [{'text': '"+response+"'}]},\n")
          conv.close() 