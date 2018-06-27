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

global config,first,obligatories,reminder_patient,reminder_end_session,reminder_patient_little,last_session
config = yaml.load(open('config.yml'))
first = True
obligatories = dict()
reminder_patient=timedelta(seconds=0)
reminder_end_session=timedelta(seconds=0)
reminder_patient_little=timedelta(seconds=0)
date_end=timedelta(seconds=0)
last_session=False

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
        count_user_reminder_max = config['count_user_reminder_max']
        to_return.append(SlotSet("stopword",stopword))
        to_return.append(SlotSet("emergency",emergency))
        to_return.append(SlotSet("nickname",nickname))
        to_return.append(SlotSet("exitword",exitword))
        to_return.append(SlotSet("count_user_reminder_max",count_user_reminder_max))
        to_return.append(SlotSet("count_user_reminder",0))
        to_return.append(SlotSet("followed_intent",followed_intent))
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
        return to_return

class SaveConv(Action):
    def name(self):
        return 'save_conv'
        
    def run(self, dispatcher, tracker, domain):
        global first
        to_return = []
        if first:
            to_return = InitBot().run(dispatcher, tracker, domain)
            for i in to_return:
                tracker.update(i)
            nickname = tracker.get_slot("nickname")
            to_return = []
            #print("reminder change session scheduled at "+str(date_end))
            #to_return.append(ReminderScheduled("change_session_reminder", date_end, kill_on_user_message=False))  
            #print("reminder before change session scheduled at "+str(date_end - reminder_end_session))
            #to_return.append(ReminderScheduled("session_end_reminder", date_end - reminder_end_session, kill_on_user_message=False)) 
            dispatcher.utter_message("Nice to meet you! My name is "+nickname)
        nickname = tracker.get_slot("nickname")
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
                dispatcher.utter_message("It seems that you have an emeregency. I contacted someone.")
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
                dispatcher.utter_message("Talk to you later.")   
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
          sport = tracker.get_slot("sport")
          requested_slot = tracker.get_slot("requested_slot")
          sport_duration = tracker.get_slot("sport_duration")
          activity = tracker.get_slot("activity")
          pain = tracker.get_slot("pain")
          body_part = tracker.get_slot("body_part")
          pain_duration = tracker.get_slot("pain_duration")
          pain_desc = tracker.get_slot("pain_desc")
          pain_level = tracker.get_slot("pain_level")
          duration = tracker.get_slot("duration")
          pain_change = tracker.get_slot("pain_change")
          pain_time = tracker.get_slot("time")
          period = tracker.get_slot("period")
          distance = tracker.get_slot("distance")
          pain_period = tracker.get_slot("pain_period")
          sport_period = tracker.get_slot("sport_period")
          activity_hard = tracker.get_slot("activity_hard")
          emotional_sadness = tracker.get_slot("emotional_sadness")
          emotional_hapiness = tracker.get_slot("emotional_hapiness")
          social = tracker.get_slot("social")
          topic = tracker.get_slot("topic")
          response = ("""`\ttopic = {}, requested_slot = {},`
`\tactivity = {}, sport = {}, sport_duration = {}, sport_period = {}, activity_hard = {},`
`\tpain = {}, pain_duration = {}, pain_desc = {}, body_part = {}, pain_change = {}, pain_period = {}, pain_level = {}, pain_time = {}` 
`\tsadness = {},`
`\thappy = {},`
`\tsocial = {},`
`\tdistance = {}, period = {}, duration = {}`""").format(topic,requested_slot,
activity,sport, sport_duration, sport_period, activity_hard, pain, pain_duration, 
pain_desc, body_part, pain_change, pain_period, pain_level, pain_time,emotional_sadness,
emotional_hapiness,social,distance, period, duration)
          dispatcher.utter_message(response)
          conv.write("{ '"+str(date)+"' : [{'text': '"+response+"'}]},\n")
          conv.close() 