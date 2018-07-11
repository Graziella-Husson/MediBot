from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from initAndComplex import InitBot
from datetime import datetime as dt, timedelta
from rasa_core.events import (
SlotSet,
ReminderScheduled, 
AllSlotsReset, 
ConversationPaused
)
from rasa_core.actions.forms import (
EntityFormField
)

from initAndComplex import (
get_obligatories, 
get_reminder_patient, 
get_date_end, 
get_reminder_end_session, 
get_last_session, 
get_language,
get_followed_reminders,
set_followed_reminders
)
from ressources import get_utterance
import os

class ChangeSessionReminder(Action):
    def name(self):
        return 'change_session_reminder'
        
    def run(self, dispatcher, tracker, domain):  
        language = get_language()
        print(language)
        global_score = tracker.get_slot("global_score") 
        
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
        conv.write("{}")
        conv.close()        
        
        obligatories = get_obligatories()
        #TODO: send a notification instead
        unacomplished = []
        obligatory_intent = obligatories['requested_intent']
        for i in obligatory_intent:
            slot_name = i.slot_name
            j = tracker.get_slot(slot_name)
            if j == None:
                unacomplished.append(slot_name)
        #TODO: save global score in DB
        print(global_score)
        if global_score != None and global_score != 0:
            response = get_utterance("score",language).format(global_score)
            dispatcher.utter_message(response)
        global_score = 0
        #TODO: send a notif saying missing intents
        if len(unacomplished)>0:
            response = get_utterance("not_broached",language)
            response+=str(unacomplished)
            dispatcher.utter_message(response)
        last_session = get_last_session()
        if not last_session:
            to_return=InitBot().run(dispatcher, tracker, domain)
            for i in to_return:
                tracker.update(i)
            to_return = []
            date_end = get_date_end()
            reminder_end_session = get_reminder_end_session()
            response = get_utterance("change_session",language)
            dispatcher.utter_message(response)
            to_return.append(SlotSet("global_score",global_score))
            print("reminder change session scheduled at "+str(date_end))
            to_return.append(ReminderScheduled("change_session_reminder", date_end, kill_on_user_message=False))  
            print("reminder before change session scheduled at "+str(date_end - reminder_end_session))
            to_return.append(ReminderScheduled("session_end_reminder", date_end - reminder_end_session, kill_on_user_message=False)) 
        else:
            response = get_utterance("last_session",language)
            dispatcher.utter_message(response)
            return [AllSlotsReset(), ConversationPaused()]        
        return to_return
          
class UserReminder(Action):
    def name(self):
        return 'user_reminder'
        
    def run(self, dispatcher, tracker, domain):  
        language = get_language()
        count_user_reminder = tracker.get_slot("count_user_reminder") 
        count_user_reminder_max = tracker.get_slot("count_user_reminder_max") 
        reminder_patient = get_reminder_patient()
        #TODO : Send a notif instead
        response = get_utterance("user_reminder",language)
        dispatcher.utter_message(response)   
        count_user_reminder+=1
        if count_user_reminder > count_user_reminder_max:
         #TODO : Send a notif instead
            response = get_utterance("count_user_reminder",language).format(count_user_reminder)
            dispatcher.utter_message(response)   
        to_return = []
        to_return.append(SlotSet("count_user_reminder",count_user_reminder))
        print("reminder user scheduled at "+str(dt.now() + reminder_patient))
        to_return.append(ReminderScheduled("user_reminder", dt.now() + reminder_patient, kill_on_user_message=True))
        return to_return
        
          
class SessionEndReminder(Action):
    def name(self):
        return 'session_end_reminder'
        
    def run(self, dispatcher, tracker, domain):  
        language = get_language()
        #TODO : Send a notif instead
        unacomplished = 0
        acomplished = []
        obligatories = get_obligatories()
        obligatory_intent = obligatories['requested_intent']
        for i in obligatory_intent:
            slot_name = i.slot_name
            j = tracker.get_slot(slot_name)
            if j != None:
                acomplished.append(slot_name)
            else:
                unacomplished+=1
        if unacomplished != 0:
            response = get_utterance("talk",language)
            if len(acomplished)>0:
                response+= get_utterance("so_far",language)
                for i in acomplished:
                    response+= get_utterance(str(i),language)
            dispatcher.utter_message(response)

class UserReminderLittle(Action):
    def name(self):
        return 'user_reminder_little'
        
    def run(self, dispatcher, tracker, domain):  
        language = get_language()
        #TODO : Send a notif instead
        response = get_utterance("user_reminder_little",language)
        dispatcher.utter_message(response)      
    
class FollowedIntentReminder(Action):
    
    def get_reminder(self,followed_reminders, now):
        diff = timedelta(weeks=1000000)
        to_return = None
        for reminder in followed_reminders:
            to_check = abs(reminder.trigger_date_time - now)
            if to_check<diff:
                diff = to_check
                to_return = reminder
        return to_return
        
    def string_in_entity_form_list(self,string, listing):
        for i in listing:
            if i.entity_name == string:
                return True
        return False
    
    def name(self):
        return 'followed_intent_reminder'
        
    def run(self, dispatcher, tracker, domain):
        now = dt.now()
        obligatories = get_obligatories()
        followed_reminders = get_followed_reminders()
        reminder = self.get_reminder(followed_reminders, now)
        name = reminder.name
        print(name)
        intent, *entities = name.split('-')
        print(entities)
        entities = str(entities)[2:-2].split("*")[0]
        print(entities)
        entities = entities.split('.')
        print(entities)
        for i in entities:
            try:
                if not (self.string_in_entity_form_list(i,obligatories[intent])):
                    obligatories[intent].append(EntityFormField(i, i))
            except:
                obligatories[intent]=[]
                obligatories[intent].append(EntityFormField(i, i))
            
            if not (self.string_in_entity_form_list(intent,obligatories['requested_intent'])):
                obligatories['requested_intent'].append(EntityFormField(intent, intent))
        for i in obligatories:
            print(i)
            for j in obligatories[i]:
                print("\t"+j.entity_name)
        followed_reminders.remove(reminder)
        
        