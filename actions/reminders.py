"""
This module is used to regroup all reminders actions.\n
A reminder is an action performed at a given time\n
Created on Tue Jun 26 10:22:40 2018\n
@author: U{@Graziella-Husson<https://github.com/Graziella-Husson>}
"""
from datetime import datetime as dt, timedelta, timezone
import os
from rasa_core.actions.action import Action
from rasa_core.events import (
    SlotSet,
    ReminderScheduled,
    AllSlotsReset,
    ConversationPaused
)
from rasa_core.actions.forms import (
    EntityFormField
)
import init_and_complex as init
from ressources import get_utterance


def get_reminder(followed_reminders, now):
    """@param followed_reminders: list of reminders of type
    follow_reminders send and not triggered.
    @param now: the current date
    Get the reminder that have a trigger date closest as now
    (the one that triggered this action)."""
    diff = timedelta(weeks=1000000)
    to_return = None
    for reminder in followed_reminders:
        to_check = abs(reminder.trigger_date_time - now)
        if to_check < diff:
            diff = to_check
            to_return = reminder
    return to_return


def string_in_entity_form_list(string, listing):
    """@param string: entity name to find in listing of EntityFormField
    @param listing: listing of EntityFormField
    @return True if string is one of the EntityFormField
    entity name in the listing"""
    for i in listing:
        if i.entity_name == string:
            return True
    return False


class ChangeSessionReminder(Action):
    """Change session. Called at the end of the current session."""
    def name(self):
        """@return: the name of the action."""
        return 'change_session_reminder'

    def run(self, dispatcher, tracker, domain):
        """Display all not broached requested_intents;
        the global score of the session\n
        Call the C{init} method and send reminder
        C{ChangeSessionReminder} to change session.\n
        If it's the last session, pause the conversation."""
        language = init.get_language()
#        print(language)
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
        obligatories = init.get_obligatories()
        #TODO: send a notification instead
        unacomplished = []
        obligatory_intent = obligatories['requested_intent']
        for i in obligatory_intent:
            slot_name = i.slot_name
            j = tracker.get_slot(slot_name)
            if j is None:
                unacomplished.append(slot_name)
        #TODO: save global score in DB
#        print(global_score)
        if global_score is not None and global_score != 0:
            response = get_utterance("score", language, tracker.sender_id, [global_score])
            dispatcher.utter_message(response)
        global_score = 0
        #TODO: send a notif saying missing intents
        if len(unacomplished) > 0:
            response = get_utterance("not_broached", language, tracker.sender_id, [str(unacomplished)])
            dispatcher.utter_message(response)
        last_session = init.get_last_session_in_db(tracker.sender_id)
        if not last_session:
            to_return = init.InitBot().run(dispatcher, tracker, domain)
            for i in to_return:
                tracker.update(i)
            to_return = []
            date_end = init.get_date_end_in_db(tracker.sender_id)
            reminder_end_session = init.get_reminder_end_session()
            response = get_utterance("change_session", language, tracker.sender_id)
            dispatcher.utter_message(response)
            to_return.append(SlotSet("global_score", global_score))
#            print("reminder change session scheduled at "+str(date_end))
            to_return.append(ReminderScheduled("change_session_reminder",
                                               date_end,
                                               kill_on_user_message=False))
#            print("reminder before change session scheduled at "+str(date_end - reminder_end_session))
            to_return.append(ReminderScheduled("session_end_reminder",
                                               date_end - reminder_end_session,
                                               kill_on_user_message=False))
        else:
            response = get_utterance("last_session", language, tracker.sender_id)
            dispatcher.utter_message(response)
            return [AllSlotsReset(), ConversationPaused()]
        return to_return


class UserReminder(Action):
    """Call the patient after a while."""
    def name(self):
        """@return: the name of the action."""
        return 'user_reminder'

    def run(self, dispatcher, tracker, domain):
        """Send reminder C{UserReminder} to call again
        if the patient did not respond.\n
        If the number of calls exceed the slot count_user_reminder_max,
        we have to raise an alert."""
        language = init.get_language()
        count_user_reminder = tracker.get_slot("count_user_reminder")
        count_user_reminder_max = tracker.get_slot("count_user_reminder_max")
        reminder_patient = init.get_reminder_patient()
        #TODO : Send a notif instead
        response = get_utterance("user_reminder", language, tracker.sender_id)
        dispatcher.utter_message(response)
        count_user_reminder += 1
        if count_user_reminder > count_user_reminder_max:
         #TODO : Send a notif instead
            response = get_utterance("count_user_reminder",
                                     language, tracker.sender_id, [count_user_reminder])
            dispatcher.utter_message(response)
        to_return = []
        to_return.append(SlotSet("count_user_reminder", count_user_reminder))
#        print("reminder user scheduled at "+str(dt.now(timezone.utc) + reminder_patient))
        to_return.append(ReminderScheduled("user_reminder",
                                           dt.now(timezone.utc) +
                                           reminder_patient,
                                           kill_on_user_message=True))
        return to_return


class SessionEndReminder(Action):
    """Call the patient before the session ends."""
    def name(self):
        """@return: the name of the action."""
        return 'session_end_reminder'

    def run(self, dispatcher, tracker, domain):
        """Display all broached requested_intents."""
        language = init.get_language()
        #TODO : Send a notif instead
        unacomplished = 0
        acomplished = []
        obligatories = init.get_obligatories()
        obligatory_intent = obligatories['requested_intent']
        for i in obligatory_intent:
            slot_name = i.slot_name
            j = tracker.get_slot(slot_name)
            if j is not None:
                acomplished.append(slot_name)
            else:
                unacomplished += 1
        if unacomplished != 0:
            response = get_utterance("talk", language, tracker.sender_id)
            if len(acomplished) > 0:
                response += get_utterance("so_far", language, tracker.sender_id)
                for i in acomplished:
                    response += get_utterance(str(i), language, tracker.sender_id)
            dispatcher.utter_message(response)


class UserReminderLittle(Action):
    """Call the patient after a little while."""
    def name(self):
        """@return: the name of the action."""
        return 'user_reminder_little'

    def run(self, dispatcher, tracker, domain):
        """Call the patient after a little time"""
        language = init.get_language()
        #TODO : Send a notif instead
        response = get_utterance("user_reminder_little", language, tracker.sender_id)
        dispatcher.utter_message(response)


class FollowedIntentReminder(Action):
    """Reminder that get the intent followed and make it
    mandatory for the current session."""
    def name(self):
        """@return: the name of the action."""
        return 'followed_intent_reminder'

    def run(self, dispatcher, tracker, domain):
        """Get the intent followed and linked entities\n
        Make intent mandatory and add an EntityFormField for each
        entity to make them requested for the intent\n
        Remove reminder in followed_reminders list (it has been triggered)"""
        now = dt.now(timezone.utc)
        obligatories = init.get_obligatories()
        followed_reminders = init.get_follow_reminder_in_db(tracker.sender_id)
        reminder = get_reminder(followed_reminders, now)
        name = reminder.name
#        print(name)
        intent, *entities = name.split('-')
#        print(entities)
        entities = str(entities)[2:-2].split("*")[0]
#        print(entities)
        entities = entities.split('.')
#        print(entities)
        for i in entities:
            try:
                if not string_in_entity_form_list(i, obligatories[intent]):
                    obligatories[intent].append(EntityFormField(i, i))
            except:
                obligatories[intent] = []
                obligatories[intent].append(EntityFormField(i, i))
            if not string_in_entity_form_list(intent,
                                              obligatories['requested_intent']):
                obligatories['requested_intent'].append(EntityFormField(intent, intent))
#        for i in obligatories:
#            print(i)
#            for j in obligatories[i]:
#                print("\t"+j.entity_name)
        followed_reminders.remove(reminder)
        init.set_follow_reminder_in_db(tracker.sender_id, followed_reminders)
