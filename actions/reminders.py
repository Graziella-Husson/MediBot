from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from initAndComplex import InitBot
from datetime import datetime as dt
from rasa_core.events import SlotSet,ReminderScheduled, AllSlotsReset, ConversationPaused

from initAndComplex import get_obligatories, get_reminder_patient, get_date_end, get_reminder_end_session, get_last_session

class ChangeSessionReminder(Action):
    def name(self):
        return 'change_session_reminder'
        
    def run(self, dispatcher, tracker, domain):
        global_score = tracker.get_slot("global_score") 
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
        if global_score != None or global_score != 0:
            response = ("This session score was of "+str(global_score)+" points.")
            dispatcher.utter_message(response)
        global_score = 0
        #TODO: send a notif saying missing intents
        if len(unacomplished)>0:
            response = ("The following intents were not broached : ")
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
            response = ("We just changed session! :smile:\nNow, let's talk!")
            dispatcher.utter_message(response)
            to_return.append(SlotSet("global_score",global_score))
            print("reminder change session scheduled at "+str(date_end))
            to_return.append(ReminderScheduled("change_session_reminder", date_end, kill_on_user_message=False))  
            print("reminder before change session scheduled at "+str(date_end - reminder_end_session))
            to_return.append(ReminderScheduled("session_end_reminder", date_end - reminder_end_session, kill_on_user_message=False)) 
        else:
            dispatcher.utter_message("It was the last session! Goodbye and thank you! :smile:")
            return [AllSlotsReset(), ConversationPaused()]        
        return to_return
          
class UserReminder(Action):
    def name(self):
        return 'user_reminder'
        
    def run(self, dispatcher, tracker, domain):
        count_user_reminder = tracker.get_slot("count_user_reminder") 
        count_user_reminder_max = tracker.get_slot("count_user_reminder_max") 
        reminder_patient = get_reminder_patient()
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
        print("reminder user scheduled at "+str(dt.now() + reminder_patient))
        to_return.append(ReminderScheduled("user_reminder", dt.now() + reminder_patient, kill_on_user_message=True))
        return to_return
        
          
class SessionEndReminder(Action):
    def name(self):
        return 'session_end_reminder'
        
    def run(self, dispatcher, tracker, domain):
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