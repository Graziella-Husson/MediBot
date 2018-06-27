from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action, ActionListen
from rasa_core.events import SlotSet, AllSlotsReset, ReminderScheduled, UserUtteranceReverted, ConversationPaused
from rasa_core.dispatcher import Button
from datetime import datetime as dt
from datetime import timedelta
from pain_classifier import get_pain_level
from physical_activity_classifier import get_physical_activity_level
from textblob import TextBlob

from rasa_core.actions.forms import (
EntityFormField,
FormAction,
BooleanFormField
)

import yaml
import os

global config, first
first = True
config = yaml.load(open('config.yml'))

########################################################
###########          INIT & CONFIG           ###########
########################################################
class InitBot(Action):

    def loadConfig(self,current_session,to_return):
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
        to_return.append(SlotSet("obligatories",obligatories))
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
                
    def last_session(self,tracker):
        try:
            current_session = tracker.get_slot("current_session") 
            config['sessions'][int(current_session)+1]
            current_session=int(current_session)
            return False
        except:
            current_session=int(current_session)
            return True
            
    def get_current_reminder_times(self,current_session):
        reminders = ['reminder_patient','reminder_end_session','reminder_patient_little'] 
        to_return = [] 
        end = config['sessions'][current_session]['end']
        date_el = end.split(',')
        date=dt(int(date_el[0]), int(date_el[1]),int(date_el[2]),
                                  int(date_el[3]),int(date_el[4]), int(date_el[5]))
        print("reminder change session scheduled at "+str(date))
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
#            if reminder == 'reminder_patient':
#                to_return.append(SlotSet("reminder_patient",reminder1))
#            elif reminder == 'reminder_end_session':
#                to_return.append(SlotSet("reminder_end_session",reminder1))
#                #print("reminder before change session scheduled at "+str(date - reminder1))
#                #to_return.append(ReminderScheduled("session_end_reminder", date - reminder1, kill_on_user_message=False))   
#            elif reminder == 'reminder_patient_little':
#                to_return.append(SlotSet("reminder_patient_little",reminder1))
        follow_in_current_session_plus = int(config['follow_in_current_session_plus'])
        to_return.append(SlotSet("follow_in_current_session_plus",follow_in_current_session_plus))
        #to_return.append(ReminderScheduled("change_session_reminder", date, kill_on_user_message=False))     
        return to_return
    
    def name(self):
        return 'init'
        
    def run(self, dispatcher, tracker, domain):
        global first
        current_session = self.get_current_session()
#        last_session = self.last_session(tracker)
#        if last_session:
#            dispatcher.utter_message("It was the last session! Goodbye and thank you! :smile:")
#            return [AllSlotsReset(), ConversationPaused()]
        to_return = self.get_current_reminder_times(current_session)
        to_return = self.loadConfig(current_session,to_return)
        print("Current session is : "+str(current_session))
        to_return.append(SlotSet("current_session",current_session))
        if first :
            first = False
        else:
            to_return.append(SlotSet("requested_slot",None))
            to_return.append(AllSlotsReset())
        return to_return

class SaveConv(Action):
    def name(self):
        return 'save_conv'
        
    def run(self, dispatcher, tracker, domain):
        global first
        if first:
            to_return = InitBot().run(dispatcher, tracker, domain)
            for i in to_return:
                tracker.update(i)
            nickname = tracker.get_slot("nickname")
            dispatcher.utter_message("Nice to meet you! My name is "+nickname)
        to_return = []
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
            dispatcher.utter_message("Sorry, I did not understand what you said...\n`This is a fallback for NLU part (intent fallback)`")
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
                #to_return.append(ReminderScheduled("user_reminder", dt.now() + reminder_patient, kill_on_user_message=True))
                return to_return
            
            else:
                count_user_reminder = 0
                to_return.append(SlotSet("count_user_reminder",count_user_reminder))
                #to_return.append(ReminderScheduled("user_reminder_little", dt.now() + reminder_patient_little,kill_on_user_message=True))
                #to_return.append(ReminderScheduled("user_reminder", dt.now() + reminder_patient, kill_on_user_message=True))
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
`\tpain = {}, pain_duration = {}, pain_desc = {}, body_part = {}, pain_change = {}, pain_period = {}, pain_level = {},` 
`\tsadness = {},`
`\thappy = {},`
`\tsocial = {},`
`\tdistance = {}, period = {}, duration = {}`""").format(topic,requested_slot,
activity,sport, sport_duration, sport_period, activity_hard, pain, pain_duration, 
pain_desc, body_part, pain_change, pain_period, pain_level, emotional_sadness,
emotional_hapiness,social,distance, period, duration)
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
        global_score = tracker.get_slot("global_score") 
        obligatories = tracker.get_slot("obligatories") 
        #TODO: send a notification instead
        unacomplished = []
        obligatory_intent = obligatories['requested_intent']
        for i in obligatory_intent:
            slot_name = i.slot_name
            j = tracker.get_slot(slot_name)
            if j == None:
                unacomplished.append(slot_name)
        #TODO: save global score in DB
        response = ("This session score was of "+str(global_score)+" points.")
        dispatcher.utter_message(response)
        global_score = 0
        #TODO: send a notif saying missing intents
        if len(unacomplished)>0:
            response = ("The following intents were not broached : ")
            response+=str(unacomplished)
            dispatcher.utter_message(response)
        to_return = []
        to_return.append(InitBot().run(dispatcher, tracker, domain))
        response = ("We just changed session! :smile:\nNow, let's talk!")
        dispatcher.utter_message(response)
        to_return.append(SlotSet("global_score",global_score))
        return to_return
          
class UserReminder(Action):
    def name(self):
        return 'user_reminder'
        
    def run(self, dispatcher, tracker, domain):
        count_user_reminder = tracker.get_slot("count_user_reminder") 
        count_user_reminder_max = tracker.get_slot("count_user_reminder_max") 
        reminder_patient = tracker.get_slot("reminder_patient") 
        #TODO : Send a notif instead
        response = ("Hey! It's been a while! We have to talk about you :smile:")
        dispatcher.utter_message(response)   
        count_user_reminder+=1
        if count_user_reminder > count_user_reminder_max:
         #TODO : Send a notif instead
            response = ("It seems that you did not response for "+str(count_user_reminder)+" times. I contacted someone. I hope you're ok.")
            dispatcher.utter_message(response)   
        to_return = []
        to_return.append(SlotSet("count_user_reminder",count_user_reminder))
        #to_return.append(ReminderScheduled("user_reminder", dt.now() + reminder_patient, kill_on_user_message=True))
        return to_return
        
          
class SessionEndReminder(Action):
    def name(self):
        return 'session_end_reminder'
        
    def run(self, dispatcher, tracker, domain):
        #TODO : Send a notif instead
        unacomplished = 0
        acomplished = []
        obligatories = tracker.get_slot("obligatories") 
        obligatory_intent = obligatories['requested_intent']
        for i in obligatory_intent:
            slot_name = i.slot_name
            j = tracker.get_slot(slot_name)
            if j != None:
                acomplished.append(slot_name)
            else:
                unacomplished+=1
        if unacomplished != 0:
            response = ("Hey! We have to talk about you :smile:\n")
            if len(acomplished)>0:
                response+= ("So far, we talked about:\n")
                for i in acomplished:
                    response+= ("\t Your "+str(i)+"\n")
            dispatcher.utter_message(response)

class UserReminderLittle(Action):
    def name(self):
        return 'user_reminder_little'
        
    def run(self, dispatcher, tracker, domain):
        #TODO : Send a notif instead
          response = ("Are you still there?")
          dispatcher.utter_message(response)      

########################################################
###########            FORM ACTIONS          ###########
########################################################
class ActionFillSlotsPain(FormAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields(tracker):
        obligatories = tracker.get_slot("obligatories") 
        try:
            return obligatories['pain']
        except:
            return []
    
    def name(self):
        return 'action_check_slots_pain'
    
    def submit(self, dispatcher, tracker, domain):
        level = tracker.get_slot("pain_level")
        if not level == "Incorrect":
            pain_duration = tracker.get_slot("pain_duration")
            pain_desc = tracker.get_slot("pain_desc")
            if pain_desc!=None:
                pain_desc = TextBlob(pain_desc).correct()
                tracker.update(SlotSet("pain_desc",pain_desc))
            body_part = tracker.get_slot("body_part")
            pain_change = tracker.get_slot("pain_change")
            pain_period = tracker.get_slot("pain_period")
            obligatories = tracker.get_slot("obligatories") 
            try:
                len(obligatories['pain'])
                response = "To sum up:\n"
                if pain_desc != None:
                    if level == None:
                        #get pain level
                        level = get_pain_level(pain_desc)                
                        tracker.update(SlotSet("pain_level",level))
                        #TODO : do something if None
                    response += "\tYou have some {} pain (it's considered has a {} pain).\n".format(pain_desc, level)
                if body_part != None:
                    body_part = TextBlob(body_part).correct()
                    tracker.update(SlotSet("body_part",body_part))
                    response += "\tThe pain is localized at {}.\n".format(body_part)
                if pain_duration != None:
                    pain_duration = TextBlob(pain_duration).correct()
                    tracker.update(SlotSet("pain_duration",pain_duration))
                    response += "\tThe duration of this pain is of{}.\n".format(pain_duration)
                if pain_period != None:
                    pain_period = TextBlob(pain_period).correct()
                    tracker.update(SlotSet("pain_period",pain_period))
                    response += "\tThe period/recurrence is {}.\n".format(pain_period)
                if pain_change != None:
                    response += "\tThe pain seems to be {}.\n".format(pain_change)
                response += "Is it right?"
            except:
                response= "So, you feel some pain."
                # TODO: add to database
            tracker.update(SlotSet("topic",None))
            tracker.update(SlotSet("requested_slot",None))
            dispatcher.utter_message(response)
        else:
            buttons = [Button(title="Mild", payload="/pain{\"pain_level\":\"mild\"}"),
                       Button(title="Moderate", payload="/pain{\"pain_level\":\"moderate\"}"),
                       Button(title="Severe", payload="/pain{\"pain_level\":\"severe\"}")]
            dispatcher.utter_button_message("I failed to calculate your pain level. Can you tell me it? Click on one of the buttons above.", buttons)
        
        
class ActionFillSlotsSport(FormAction):
    RANDOMIZE = True

    @staticmethod
    def required_fields(tracker):
        obligatories = tracker.get_slot("obligatories") 
        try:
            return obligatories['activity']    
        except:
            return []    
    
    def name(self):
        return 'action_check_slots_sport'
    
    def submit(self, dispatcher, tracker, domain):
        sport_level = tracker.get_slot("sport_level")
        if not sport_level == "Incorrect":
            sport_duration = tracker.get_slot("sport_duration")
            sport = tracker.get_slot("sport")
            sport_period = tracker.get_slot("sport_period")
            distance = tracker.get_slot("distance")
            if sport!=None:
                sport = (TextBlob(sport).correct())
                tracker.update(SlotSet("sport",sport))
            activity_hard = tracker.get_slot("activity_hard")
            try:
                obligatories = tracker.get_slot("obligatories") 
                len(obligatories['activity'])>0
                response = "To sum up:\n"
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
                    response += "\tYou did some {} physical activity ({}). The sport detected is {}.\n".format(sport_level, MET, sport)
                if sport_duration != None:
                    sport_duration = TextBlob(sport_duration).correct()
                    tracker.update(SlotSet("sport_duration",sport_duration))
                    response += "\tThe duration is of {}.\n".format(sport_duration)
                if distance != None:
                    distance = TextBlob(distance).correct()
                    tracker.update(SlotSet("distance",distance))
                    response += "\tThe distance you did is of {}.\n".format(distance)
                if sport_period != None:
                    sport_period = TextBlob(sport_period).correct()
                    tracker.update(SlotSet("sport_period",sport_period))
                    response +="\tThe period/recurrence detected is {}.\n".format(sport_period)
                if activity_hard != None:
                    if activity_hard:
                        response +="\tYour activity was hard because of your general health.\n"
                    else:
                        response +="\tYour general health did not make your activity harder.\n"
                response += "Is it right?"
            except:
                response= "So, you did some physical activities."
                # TODO: save in database
            tracker.update(SlotSet("topic",None))
            tracker.update(SlotSet("requested_slot",None))
            dispatcher.utter_message(response)
        else:
            buttons = [Button(title="Little", payload="/pain{\"sport_level\":\"little\"}"),
                       Button(title="Moderate", payload="/pain{\"sport_level\":\"moderate\"}"),
                       Button(title="Vigorous", payload="/pain{\"sport_level\":\"vigorous\"}")]
            dispatcher.utter_button_message("I failed to calculate your physical activity level. Can you tell me it? Click on one of the buttons above.", buttons)
        

class CheckRequestedIntents(FormAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields(tracker):
        obligatories = tracker.get_slot("obligatories") 
        try:
            return obligatories['requested_intent']
        except:
            return []
    
    def name(self):
        return 'action_check_intents'
    
    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_message("We talked about everything we had to! But feel free to talk to me about avrything else!")

class Sadness(FormAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields(tracker):
        obligatories = tracker.get_slot("obligatories") 
        try:
            return obligatories['emotional_sadness']
        except:
            return []

    def name(self):
        return 'sum_up_emotionnal_sadness'
        
    def submit(self, dispatcher, tracker, domain):
        global_score = tracker.get_slot('global_score')
        global_score+=1
        #TODO: save score
        response = "It seems that you are in a bad mood... Do you want to talk about it in details?"
        dispatcher.utter_message(response)
        tracker.update(SlotSet("emotional_sadness",True))
        tracker.update(SlotSet("global_score",global_score))
      
class Happy(FormAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields(tracker):
        obligatories = tracker.get_slot("obligatories") 
        try:
            return obligatories['emotional_hapiness']
        except:
            return []
        
    def name(self):
        return 'sum_up_emotional_hapiness'
        
    def submit(self, dispatcher, tracker, domain):
        global_score = tracker.get_slot('global_score')
        global_score+=3
        #TODO: save score
        response = "Great! You are in a good mood!"
        dispatcher.utter_message(response)
        tracker.update(SlotSet("emotional_hapiness",True))
        tracker.update(SlotSet("global_score",global_score))

class Social(FormAction):
    RANDOMIZE = True
    
    @staticmethod
    def required_fields(tracker):
        obligatories = tracker.get_slot("obligatories") 
        try:
            return obligatories['social']
        except:
            return []
        
    def name(self):
        return 'sum_up_social'
        
    def submit(self, dispatcher, tracker, domain):
        global_score = tracker.get_slot('global_score')
        global_score+=2
        #TODO: save score
        response = "It seems that you talked about a social thing."
        dispatcher.utter_message(response)
        tracker.update(SlotSet("social",True))
        tracker.update(SlotSet("global_score",global_score))
        
########################################################
###########            RESET SLOTS           ###########
########################################################        
class ResetSportSlots(Action):
    def name(self):
        return 'reset_slots_sport'
    
    def run(self, dispatcher, tracker, domain):
        global_score = tracker.get_slot("global_score")
        dispatcher.utter_message("Saved!")
        # TODO: save to DB
        sport_level = tracker.get_slot("sport_level")
        if sport_level=='little':
            global_score+=1
            MET = "< 3 MET"
        elif sport_level=='moderate':
            global_score+=2
            MET = "3-6 MET"
        elif sport_level=='vigorous':
            global_score+=3
            MET = "> 6 MET"
        #TODO: save score and MET
        return[SlotSet("global_score",global_score),SlotSet("activity_hard",None), SlotSet("sport_duration",None), SlotSet("sport_level",None), SlotSet("sport",None), SlotSet("distance",None), SlotSet("sport_period", None), SlotSet("topic", None), SlotSet("requested_slot", None), SlotSet("activity",True)]

class ResetPainSlots(Action):
    def name(self):
        return 'reset_slots_pain'
    
    def run(self, dispatcher, tracker, domain):
        global_score = tracker.get_slot("global_score")
        dispatcher.utter_message("Saved!")
        # TODO: save to DB
        sport_level = tracker.get_slot("sport_level")
        if sport_level=='severe':
            global_score+=1
        elif sport_level=='moderate':
            global_score+=2
        elif sport_level=='mild':
            global_score+=3
        #TODO: save score
        return [SlotSet("global_score",global_score),SlotSet("pain_duration",None), SlotSet("pain_desc",None), SlotSet("body_part",None), SlotSet("pain_change",None), SlotSet("pain_period",None), SlotSet("topic", None), SlotSet("requested_slot", None),SlotSet("pain",True), SlotSet("pain_level",None)]

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
            elif topic=="activity":
                tracker.update(SlotSet("sport_period",period))
                action = ActionFillSlotsSport()
            else:
                action = Fallback()
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
            elif topic=="activity":
                tracker.update(SlotSet("sport_duration",duration))
                action = ActionFillSlotsSport()
            else:
                action = Fallback()
        #print(action)
        tracker.trigger_follow_up_action(action)
        tracker.update(SlotSet("duration",None))
        
########################################################
###########             ASK WHAT             ###########
######################################################## 
class AskWhatSport(Action):
    def name(self):
        return 'ask_what_sport'
        
    def run(self, dispatcher, tracker, domain):
        sport_period = tracker.get_slot("sport_period")
        distance = tracker.get_slot("distance")
        sport = tracker.get_slot("sport")
        duration = tracker.get_slot("sport_duration")
        activity_hard = tracker.get_slot("activity_hard")
        buttons = []
        if sport != None:
            buttons.append(Button(title="Sport", payload="/activity{\"sport\":null}"))
            buttons.append(Button(title="Level", payload="/activity{\"sport_level\":\"Incorrect\"}"))
        if duration != None:
            buttons.append(Button(title="Duration", payload="/activity{\"sport_duration\":null}"))
        if distance != None:
            buttons.append(Button(title="Distance", payload="/activity{\"distance\":null}"))
        if sport_period != None:
            buttons.append(Button(title="Period", payload="/activity{\"sport_period\":null}"))
        if activity_hard != None:
            buttons.append(Button(title="Hardness", payload="/activity{\"activity_hard\":null}"))            
        dispatcher.utter_button_message("Ok. So, tell me what's wrong? Click on a button or tell me above!", buttons)
        
class AskWhatPain(Action):
    def name(self):
        return 'ask_what_pain'
        
    def run(self, dispatcher, tracker, domain):
        pain_period = tracker.get_slot("pain_period")
        desc = tracker.get_slot("pain_desc")
        duration = tracker.get_slot("pain_duration")
        body_part = tracker.get_slot("body_part")
        evolution = tracker.get_slot("pain_change")
        buttons = []
        if desc != None:
            buttons.append(Button(title="Description", payload="/pain{\"pain_desc\":null}"))
            buttons.append(Button(title="Level", payload="/pain{\"pain_level\":\"Incorrect\"}"))
        if duration != None:
            buttons.append(Button(title="Duration", payload="/pain{\"pain_duration\":null}"))
        if body_part != None:
            buttons.append(Button(title="Body part", payload="/pain{\"body_part\":null}"))
        if evolution != None:
            buttons.append(Button(title="Evolution", payload="/pain{\"pain_change\":null}"))
        if pain_period != None:
            buttons.append(Button(title="Period", payload="/pain{\"pain_period\":null}"))
        dispatcher.utter_button_message("Ok. So, tell me what's wrong? Click on a button or tell me above!", buttons)
        
########################################################
###########         SIMPLE ACTIONS           ###########
######################################################## 
class Fallback(Action):
    def name(self):
        return 'sum_up_fallback'
        
    def run(self, dispatcher, tracker, domain):
        response = "Sorry, I did not understand what you said...\n`This is a fallback for NLU part (intent fallback)`"
        dispatcher.utter_message(response)