from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet, AllSlotsReset, StoryExported, ReminderScheduled, TopicSet
from datetime import datetime as dt
from datetime import timedelta

from rasa_core.actions.forms import (
EntityFormField,
FormAction
)

import random
import yaml
import os

global config, obligatory_sport, obligatory_pain, reminder_time, current_session
obligatory_pain=[]
obligatory_sport=[]
reminder_time=30
config = yaml.load(open('config.yml'))
current_session = "session1"
r=config['sessions'][current_session]['requested_slot']
for i in r['pain'].split(','):
	obligatory_pain.append(EntityFormField(i, i))
for i in r['sport'].split(','):
	obligatory_sport.append(EntityFormField(i, i))
reminder_time = config['sessions'][current_session]['reminder_time']


class InitBot(Action):

    def loadConfig(self,current_session):
        global config, obligatory_sport, obligatory_pain, reminder_time
        begin = config['sessions'][current_session]['begin']
        r=config['sessions'][current_session]['requested_slot']
        for i in r['pain'].split(','):
            obligatory_pain.append(EntityFormField(i, i))
        for i in r['sport'].split(','):
            obligatory_sport.append(EntityFormField(i, i))
        reminder_time = config['sessions'][current_session]['reminder_time']

    def get_current_session(self):
        global config, obligatory_sport, obligatory_pain, reminder_time
        current_session = None
        now = dt.now()
        inter = now-dt(2011, 1, 1)
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
            this_inter = now - date
            if  this_inter < inter:
                inter = this_inter
                my_date=date
        
        for i in begins.keys():
            date_el = begins[i].split(',')
            date=dt(int(date_el[0]), int(date_el[1]),int(date_el[2]),
                                      int(date_el[3]),int(date_el[4]), int(date_el[5]))
            if str(date)== str(my_date):
                current_session = i
        return current_session    
    
    def name(self):
        return 'init'
        
    def run(self, dispatcher, tracker, domain):
        global config, obligatory_sport, obligatory_pain, reminder_time
        current_session = self.get_current_session()
        self.loadConfig(current_session)
        self.reminderNextSession()
        print("reminder in"+str(reminder_time)+"s")
        return ReminderScheduled("action_test_reminder", dt.now() + timedelta(seconds=int(reminder_time)), kill_on_user_message=False)

class PainTopic(Action):
    def name(self):
        return 'set_topic_pain'
        
    def run(self, dispatcher, tracker, domain):
        return [SlotSet("topic","pain")]
        
class SaveConv(Action):
    def name(self):
        return 'save_conv'
        
    def run(self, dispatcher, tracker, domain):
        global current_session
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
        conv.write(str(id_user)+" ["+str(date)+"]: "+response+"\n")
        conv.close()
        
class SportTopic(Action):
    def name(self):
        return 'set_topic_sport'
        
    def run(self, dispatcher, tracker, domain):
        return [SlotSet("topic","sport")]
    
class SetDuration(Action):
    def name(self):
        return 'action_duration'
    
    def run(self, dispatcher, tracker, domain):
        requested_slot = tracker.get_slot("requested_slot")
        topic = tracker.get_slot("topic")
        duration = tracker.get_slot("duration")
        if requested_slot=="pain_duration":
            tracker.update(SlotSet("pain_duration",duration))
        elif requested_slot=="sport_duration":
            tracker.update(SlotSet("sport_duration",duration))
        else:
            if topic=="pain":
                tracker.update(SlotSet("pain_duration",duration))
            elif topic=="sport":
                tracker.update(SlotSet("sport_duration",duration))
        return [SlotSet("duration",None)]

class SumUpSLots(Action):
    def name(self):
        return 'sum_up_slots'
        
    def run(self, dispatcher, tracker, domain):
          global current_session
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
              conv.write("BOT ["+str(date)+"]: "+response+"\n")
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
          response = ("""`DEBUG:`
`\ttopic = {}, requested_slot = {},`
`\tsport = {}, sport_duration = {}, sport_period = {},`
`\tpain_duration = {}, pain_level = {}, body_part = {}, pain_change = {}, pain_period = {}, `
`\tdistance = {}, period = {}, duration = {}`""").format(topic,requested_slot,sport, sport_duration, sport_period, pain_duration, pain_level, body_part, pain_change, pain_period, distance, period, duration)
          dispatcher.utter_message(response)
          conv.write("BOT ["+str(date)+"]: "+response+"\n")
          conv.close()
  
class ActionHello(Action):
    def name(self):
        return 'sum_up_hello'
        
    def run(self, dispatcher, tracker, domain):
        choice = random.randint(1, 5)
        if choice == 1:
            response="Hello! :smile:"
        elif choice == 2:
            response="Hi, human friend! :smile:"
        elif choice == 3:
            response="Nice to see you! :smile:"
        elif choice == 4:
            response="Hey! :smile:"
        else:
            response="Happy to see you! :smile:"
        dispatcher.utter_message(response)
        
class ActionBye(Action):
    def name(self):
        return 'sum_up_bye'
        
    def run(self, dispatcher, tracker, domain):
          response = ("Goodbye, human friend! :smile:\n`DEBUG:reset slots, your story is saved on the servor, a test reminder will be triggerd in 10 seconds!`")
          dispatcher.utter_message(response)
          return [AllSlotsReset(),StoryExported("/home/ex/Desktop/MediBot/history/history.txt"),ReminderScheduled("action_test_reminder", dt.now() + timedelta(seconds=int(reminder_time)), kill_on_user_message=False)]

class ActionTestReminder(Action):
    def name(self):
        return 'action_test_reminder'
        
    def run(self, dispatcher, tracker, domain):
          response = ("It's been 10 seconds! :smile:")
          dispatcher.utter_message(response)
         
class ActionSportPeriod(Action):
    def name(self):
        return 'action_period_sport'
    
    def run(self, dispatcher, tracker, domain):
        duration = tracker.get_slot("period")
        tracker.update(SlotSet("sport_period",duration))
        tracker.update(SlotSet("period",None))

class ActionPainPeriod(Action):
    def name(self):
        return 'action_period_pain'
    
    def run(self, dispatcher, tracker, domain):
        duration = tracker.get_slot("period")
        tracker.update(SlotSet("pain_period",duration))
        tracker.update(SlotSet("period",None))

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
        response = """To sum up, you did some {} sport: {} with a duration of {}""".format(sport_level, sport, sport_duration)
        
        if distance != None:
            response += """ and a distance of {}""".format(distance)
        if sport_period != None:
            response +=""" and a period/recurrence of {}""".format(sport_period)
        
        dispatcher.utter_message(response+".")
        return [SlotSet("sport_duration",None), SlotSet("sport_level",None), SlotSet("sport",None), SlotSet("distance",None), SlotSet("sport_period", None), SlotSet("topic", None)]

class ActionFillSlotsPain(FormAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields():
        return obligatory_pain
    
    def name(self):
        return 'action_check_slots_pain'
    
    def submit(self, dispatcher, tracker, domain):
        pain_duration = tracker.get_slot("pain_duration")
        pain_level = tracker.get_slot("pain_level")
        body_part = tracker.get_slot("body_part")
        pain_change = tracker.get_slot("pain_change")
        pain_period = tracker.get_slot("pain_period")
        response = """To sum up, you have some {} pain localized at {} with a duration of {}""".format(pain_level, body_part, pain_duration)
        if pain_period != None:
            response += """ and a period/recurrence of {}""".format(pain_period)
        response += """. The pain seems to be {}.""".format(pain_change)
        dispatcher.utter_message(response)
        return [SlotSet("pain_duration",None), SlotSet("pain_level",None), SlotSet("body_part",None), SlotSet("pain_change",None), SlotSet("pain_period",None), SlotSet("topic", None)]
