from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet, AllSlotsReset, ReminderScheduled, UserUtteranceReverted
from rasa_core.dispatcher import Button
from datetime import datetime as dt
from datetime import timedelta

from rasa_core.actions.forms import (
EntityFormField,
FormAction
)

import yaml
import os

global config, obligatory_sport, obligatory_pain, reminder_time, current_session, first, reminder_patient
obligatory_pain=[]
obligatory_sport=[]
reminder_time = timedelta(seconds=0)
reminder_patient = timedelta(seconds=0)
reminder_end_session = timedelta(seconds=0)
first = True
config = yaml.load(open('config.yml'))
current_session = "test"

########################################################
###########          INIT & CONFIG           ###########
########################################################
class InitBot(Action):

    def loadConfig(self):
        global obligatory_sport, obligatory_pain
        obligatory_pain=[]
        obligatory_sport=[]
        r=config['sessions'][current_session]['requested_slot']
        for i in r['pain'].split(','):
            obligatory_pain.append(EntityFormField(i, i))
        for i in r['sport'].split(','):
            obligatory_sport.append(EntityFormField(i, i))

    def get_current_session(self):
        global current_session
        old = current_session
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
        if current_session == old:
            print("DEAD")

    def get_current_reminder_times(self):
        global reminder_time, reminder_patient, reminder_end_session
        reminder = config['sessions'][current_session]['reminder_time']
        for i in reminder.keys():
            j = reminder[i]
            if i == 'minutes':
                reminder_time+=timedelta(minutes=int(j))
            if i == 'weeks':
                reminder_time+=timedelta(weeks=int(j))
            if i == 'days':
                reminder_time+=timedelta(days=int(j))
            if i == 'hours':
                reminder_time+=timedelta(hours=int(j))
        
        reminder_patient_config = config['reminder_patient']
        reminder_patient = timedelta(seconds=0)
        for i in reminder_patient_config.keys():
            j = reminder_patient_config[i]
            if i == 'minutes':
                reminder_patient+=timedelta(minutes=int(j))
            if i == 'weeks':
                reminder_patient+=timedelta(weeks=int(j))
            if i == 'days':
                reminder_patient+=timedelta(days=int(j))
            if i == 'hours':
                reminder_patient+=timedelta(hours=int(j)) 
                
        reminder_end_session_config = config['reminder_patient']
        reminder_end_session = timedelta(seconds=0)
        for i in reminder_end_session_config.keys():
            j = reminder_end_session_config[i]
            if i == 'minutes':
                reminder_end_session+=timedelta(minutes=int(j))
            if i == 'weeks':
                reminder_end_session+=timedelta(weeks=int(j))
            if i == 'days':
                reminder_end_session+=timedelta(days=int(j))
            if i == 'hours':
                reminder_end_session+=timedelta(hours=int(j))   
    
    def name(self):
        return 'init'
        
    def run(self, dispatcher, tracker, domain):
        self.get_current_session()
        self.get_current_reminder_times()
        self.loadConfig()
        print("Current session is : "+current_session)
        #print(reminder_time)
        end = config['sessions'][current_session]['end']
        date_el = end.split(',')
        date=dt(int(date_el[0]), int(date_el[1]),int(date_el[2]),
                                  int(date_el[3]),int(date_el[4]), int(date_el[5]))
        print("reminder change session scheduled at "+str(date))
        print("reminder before change session scheduled at "+str(date - reminder_end_session))
        return [AllSlotsReset(), 
                ReminderScheduled("change_session_reminder", date, kill_on_user_message=False),
                ReminderScheduled("session_end_reminder", date - reminder_end_session, kill_on_user_message=False)]

########################################################
###########         COMPLEX ACTIONS          ###########
########################################################
        
class SaveConv(Action):
    def name(self):
        return 'save_conv'
        
    def run(self, dispatcher, tracker, domain):
        global first
        if first == True:
            action = InitBot()
            tracker.follow_up_action = action
            first = False
        id_user = tracker.sender_id
        idy = "./saves/"+str(id_user)+"/"+current_session
        try:
            conv = open(idy, 'a')
        except:
            os.mkdir("saves") 
            os.mkdir("saves/"+str(id_user)+"/") 
            conv = open(idy, 'a')  
        date = dt.now()
        response = tracker.latest_message.text
        intent = tracker.latest_message.intent
        entities = tracker.latest_message.entities
        #nlu_infos = tracker.latest_message.parse_data
        conv.write("{ '"+str(date)+"' : [{'intent':"+str(intent)+"}, {'entities':"+str(entities)+"}, {'text':"+str(response)+"}]},\n")
        conv.close()
        response1 = ("""`\tIntent : {}`
`\tEntities : {}`""").format(intent, entities)
        dispatcher.utter_message(response1)
        if response == "stop" and not first:
            for i in range (0,2):
                if not (tracker.latest_action_name == None or tracker.latest_action_name == 'init'):
                    #print(tracker.latest_action_name)
                    tracker.update(UserUtteranceReverted())
        #return [ReminderScheduled("user_reminder", dt.now() + reminder_patient, kill_on_user_message=True)]
            
class SumUpSLots(Action):
    def name(self):
        return 'sum_up_slots'
        
    def run(self, dispatcher, tracker, domain):
          id_user = tracker.sender_id
          idy = "./saves/"+str(id_user)+"/"+current_session
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
          body_part = tracker.get_slot("body_part")
          pain_duration = tracker.get_slot("pain_duration")
          pain_level = tracker.get_slot("pain_level")
          duration = tracker.get_slot("duration")
          pain_change = tracker.get_slot("pain_change")
          period = tracker.get_slot("period")
          distance = tracker.get_slot("distance")
          pain_period = tracker.get_slot("pain_period")
          sport_period = tracker.get_slot("sport_period")
          topic = tracker.get_slot("topic")
          response = ("""`\ttopic = {}, requested_slot = {},`
`\tsport = {}, sport_duration = {}, sport_period = {},`
`\tpain_duration = {}, pain_level = {}, body_part = {}, pain_change = {}, pain_period = {}, `
`\tdistance = {}, period = {}, duration = {}`""").format(topic,requested_slot,sport, sport_duration, sport_period, pain_duration, pain_level, body_part, pain_change, pain_period, distance, period, duration)
          dispatcher.utter_message(response)
          conv.write("{ '"+str(date)+"' : [{'text': '"+response+"'}]},\n")
          conv.close()      
             
########################################################
###########             REMINDERS            ###########
########################################################
class ChangeSessionReminder(Action):
    def name(self):
        return 'change_session_reminder'
        
    def run(self, dispatcher, tracker, domain):
          action = InitBot()
          tracker.trigger_follow_up_action(action)
          response = ("We just changed session! :smile:")
          dispatcher.utter_message(response)
          
class UserReminder(Action):
    def name(self):
        return 'user_reminder'
        
    def run(self, dispatcher, tracker, domain):
        #TODO : Send a notif instead
          response = ("Hey! It's been a while! We have to talk about you :smile:")
          dispatcher.utter_message(response)      
          
class SessionEndReminder(Action):
    def name(self):
        return 'session_end_reminder'
        
    def run(self, dispatcher, tracker, domain):
        #TODO : Send a notif instead
          response = ("Hey! We have to talk about you :smile:")
          dispatcher.utter_message(response)

########################################################
###########            FORM ACTIONS          ###########
########################################################
class ActionFillSlotsPain(FormAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields():
        return obligatory_pain
    
    def name(self):
        return 'action_check_slots_pain'
    
    def submit(self, dispatcher, tracker, domain):
        # TODO: get pain level
        pain_duration = tracker.get_slot("pain_duration")
        pain_level = tracker.get_slot("pain_level")
        body_part = tracker.get_slot("body_part")
        pain_change = tracker.get_slot("pain_change")
        pain_period = tracker.get_slot("pain_period")
        response = "To sum up,"
        something = False
        if pain_level != None:
            response += " you have some {} pain".format(pain_level)
            something = True
        if body_part != None:
            response += " it's localized at {}".format(body_part)
            something = True
        if pain_duration != None:
            response += " the duration of this pain is {}".format(pain_duration)
            something = True
        if pain_period != None:
            response += " the period/recurrence is {}".format(pain_period)
            something = True
        if pain_change != None:
            response += " the pain seems to be {}".format(pain_change)
            something = True
        if not something:
            response += " you feel some pain."
            # TODO: add to database 
            tracker.update(SlotSet("topic",None))
            tracker.update(SlotSet("requested_slot",None))
        else:
            response += ". Is it right?"
        dispatcher.utter_message(response)
        
class ActionFillSlotsSport(FormAction):
    RANDOMIZE = True

    @staticmethod
    def required_fields():
        return obligatory_sport
        
    
    def name(self):
        return 'action_check_slots_sport'
    
    def submit(self, dispatcher, tracker, domain):
        # TODO: get sport level
        tracker.update(SlotSet("sport_level","medium"))
        
        sport_duration = tracker.get_slot("sport_duration")
        sport_level = tracker.get_slot("sport_level")
        sport = tracker.get_slot("sport")
        sport_period = tracker.get_slot("sport_period")
        distance = tracker.get_slot("distance")
        something= False
        response = "To sum up,"
        if sport_level != None:
            response += " you did some {} physical activity".format(sport_level)
            something = True
        if sport != None:
            response += " the sport detected is {}".format(sport)
            something = True
        if sport_duration != None:
            response += " the duration is of {}".format(sport_duration)
            something = True
        if distance != None:
            response += " the distance you did is of {}".format(distance)
            something = True
        if sport_period != None:
            response +=" the period/recurrence detected is {}".format(sport_period)
            something = True
        if not something:
            response+= " you did some physical activities."
            # TODO: save in database
            tracker.update(SlotSet("topic",None))
            tracker.update(SlotSet("requested_slot",None))
        else:
            response += ". Is it right?"
        dispatcher.utter_message(response)

########################################################
###########            RESET SLOTS           ###########
########################################################        
class ResetSportSlots(Action):
    def name(self):
        return 'reset_slots_sport'
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Saved!")
        # TODO: save to DB
        return[SlotSet("sport_duration",None), SlotSet("sport_level",None), SlotSet("sport",None), SlotSet("distance",None), SlotSet("sport_period", None), SlotSet("topic", None), SlotSet("requested_slot", None)]

class ResetPainSlots(Action):
    def name(self):
        return 'reset_slots_pain'
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Saved!")
        # TODO: save to DB
        return [SlotSet("pain_duration",None), SlotSet("pain_level",None), SlotSet("body_part",None), SlotSet("pain_change",None), SlotSet("pain_period",None), SlotSet("topic", None), SlotSet("requested_slot", None)]

########################################################
###########           COMPLEX SETS           ###########
########################################################        
class SetPeriod(Action):
    def name(self):
        return 'action_period'
    
    def run(self, dispatcher, tracker, domain):
        requested_slot = tracker.get_slot("requested_slot")
        topic = tracker.get_slot("topic")
        period = tracker.get_slot("period")
        action = None
        if requested_slot=="pain_period":
            tracker.update(SlotSet("pain_period",period))
            action = ActionFillSlotsPain()
        elif requested_slot=="sport_period":
            tracker.update(SlotSet("sport_period",period))
            action = ActionFillSlotsSport()
        else:
            if topic=="pain":
                tracker.update(SlotSet("pain_period",period))
                action = ActionFillSlotsPain()
            elif topic=="sport":
                tracker.update(SlotSet("sport_period",period))
                action = ActionFillSlotsSport()
        tracker.trigger_follow_up_action(action)
        tracker.update(SlotSet("duration",None))

class SetDuration(Action):
    def name(self):
        return 'action_duration'
    
    def run(self, dispatcher, tracker, domain):
        requested_slot = tracker.get_slot("requested_slot")
        topic = tracker.get_slot("topic")
        duration = tracker.get_slot("duration")
        action = None
        if requested_slot=="pain_duration":
            tracker.update(SlotSet("pain_duration",duration))
            action = ActionFillSlotsPain()
        elif requested_slot=="sport_duration":
            tracker.update(SlotSet("sport_duration",duration))
            action = ActionFillSlotsSport()
        else:
            if topic=="pain":
                tracker.update(SlotSet("pain_duration",duration))
                action = ActionFillSlotsPain()
            elif topic=="sport":
                tracker.update(SlotSet("sport_duration",duration))
                action = ActionFillSlotsSport()
        #print(action)
        tracker.trigger_follow_up_action(action)
        tracker.update(SlotSet("duration",None))

########################################################
###########              TOPICS              ###########
######################################################## 
class SportTopic(Action):
    def name(self):
        return 'set_topic_sport'
        
    def run(self, dispatcher, tracker, domain):
        return [SlotSet("topic","sport")]
        
class PainTopic(Action):
    def name(self):
        return 'set_topic_pain'
        
    def run(self, dispatcher, tracker, domain):
        return [SlotSet("topic","pain")]
        
########################################################
###########             ASK WHAT             ###########
######################################################## 
class AskWhatSport(Action):
    def name(self):
        return 'ask_what_sport'
        
    def run(self, dispatcher, tracker, domain):
        sport_period = tracker.get_slot("sport_period")
        distance = tracker.get_slot("distance")
        buttons = [
                    Button(title="Sport", payload="/activity{\"sport\":null}"),
                    Button(title="Duration", payload="/activity{\"sport_duration\":null}")
                ]
        if distance != None:
            buttons.append(Button(title="Distance", payload="/activity{\"distance\":null}"))
        if sport_period != None:
            buttons.append(Button(title="Period", payload="/activity{\"sport_period\":null}"))
        dispatcher.utter_button_message("Ok. So, tell me what's wrong? Click on a button or tell me above!", buttons)
        
class AskWhatPain(Action):
    def name(self):
        return 'ask_what_pain'
        
    def run(self, dispatcher, tracker, domain):
        pain_period = tracker.get_slot("pain_period")
        buttons = [
                    Button(title="Level", payload="/pain{\"pain_level\":null}"),
                    Button(title="Duration", payload="/pain{\"pain_duration\":null}"),
                    Button(title="Body part", payload="/pain{\"body_part\":null}"),
                    Button(title="Evolution", payload="/pain{\"pain_change\":null}")
                ]
        if pain_period != None:
            buttons.append(Button(title="Period", payload="/pain{\"pain_period\":null}"))
        dispatcher.utter_button_message("Ok. So, tell me what's wrong? Click on a button or tell me above!", buttons)