"""
This module is used to regroup init, save and sum_up_slots actions.\n
This module contains a lot of global constant and global methods\n
Created on Tue Jun 26 10:22:40 2018\n
Last update on Mon Jul 30 10:30:00 2018\n
@author: U{@Graziella-Husson<https://github.com/Graziella-Husson>}
"""
import os
from datetime import datetime as dt
from datetime import timedelta
import dateutil
from rasa_core.actions.action import Action, ActionListen
from rasa_core.actions.forms import (
    EntityFormField
)
from rasa_core.events import (
    SlotSet,
    AllSlotsReset,
    UserUtteranceReverted,
    ReminderScheduled,
    ConversationPaused
)
import yaml
from simple_actions import Fallback
from duckling import DucklingWrapper
from ressources import get_utterance
from ressources import get_language_duckling
from insertfonction import insert_to_conversation

global CONFIG, FIRST, MANDATORIES, REMINDER_PATIENT, REMINDER_END_SESSION, REMINDER_PATIENT_LITTLE, LAST_SESSION, DUCKLING_WRAPPER, BEGIN_DATE, LANGUAGE_GLOBAL, FOLLOWED_INTENT, COMPLEX_ENTITIES
CONFIG = yaml.load(open('./ressources/config.yml'))
BEGIN_DATE = None
FIRST = True
MANDATORIES = dict()
REMINDER_PATIENT = timedelta(seconds=0)
REMINDER_END_SESSION = timedelta(seconds=0)
REMINDER_PATIENT_LITTLE = timedelta(seconds=0)
DATE_END = timedelta(seconds=0)
LAST_SESSION = False
LANGUAGE_GLOBAL = str(CONFIG['language'])
lang = get_language_duckling(LANGUAGE_GLOBAL)
DUCKLING_WRAPPER = DucklingWrapper(language=lang)
FOLLOWED_REMINDERS = []
FOLLOW_INTENT_TRIGGER_DATE = timedelta(seconds=0)
COMPLEX_ENTITIES = ["time", "body_part", "distance", "duration", "period", "temperature", "drug", "dosing"]

def get_complex_entities():
    """Get COMPLEX_ENTITIES list"""
    return COMPLEX_ENTITIES

def get_followed_reminders():
    """Get FOLLOWED_REMINDERS list"""
    return FOLLOWED_REMINDERS

def set_followed_reminders(to_set):
    """Set FOLLOWED_REMINDERS list"""
    global FOLLOWED_REMINDERS
    FOLLOWED_REMINDERS = to_set

def get_language():
    """Get language"""
    return LANGUAGE_GLOBAL

def get_obligatories():
    """Get mandatories dictionnary"""
    return MANDATORIES

def get_reminder_patient():
    """Get REMINDER_PATIENT time"""
    return REMINDER_PATIENT

def get_date_end():
    """Get date of the ending current session"""
    return DATE_END

def get_reminder_end_session():
    """Get REMINDER_END_SESSION time"""
    return REMINDER_END_SESSION

def get_last_session():
    """Get last session boolean"""
    return LAST_SESSION

def set_begin_date():
    """Set the global variable BEGIN_DATE\n
    If the BEGIN_DATE for this patient is in the DB, get it\n
    If not, set it to now"""
    global BEGIN_DATE
    # TODO: get in DB if exists
    # if not :
    BEGIN_DATE = dt.now()
    # TODO: save in DB

def load_config(current_session, to_return):
    """Get all requested slots, requested intents, followed intent
    and add them into a dictionary used by many other actions.
    Get all config texts:
        - stopword
        - emergency word
        - nickname of the bot
        - exit word
        - language
        - count_user_reminder_max"""
    global MANDATORIES, LANGUAGE_GLOBAL
    MANDATORIES = dict()
    ressource = CONFIG['sessions'][current_session]['requested_slot']
    if ressource != "None":
        for j in ressource:
            MANDATORIES[j] = []
            for i in ressource[j].split(','):
                MANDATORIES[j].append(EntityFormField(i, i))
    ressource = CONFIG['sessions'][current_session]['requested_intent']
    if ressource != "None":
        MANDATORIES['requested_intent'] = []
        for i in ressource.split(','):
            MANDATORIES['requested_intent'].append(EntityFormField(i, i))
    ressource = CONFIG['sessions'][current_session]['followed_intent']
    followed = []
    if ressource != "None":
        for i in ressource.split(','):
            followed.append(i)
    stopword = str(CONFIG['stopword'])
    emergency = str(CONFIG['emergency'])
    nickname = str(CONFIG['nickname'])
    exitword = str(CONFIG['exit'])
    LANGUAGE_GLOBAL = str(CONFIG['language'])
    count_user_reminder_max = CONFIG['count_user_reminder_max']
    to_return.append(SlotSet("stopword", stopword))
    to_return.append(SlotSet("emergency", emergency))
    to_return.append(SlotSet("nickname", nickname))
    to_return.append(SlotSet("exitword", exitword))
    to_return.append(SlotSet("count_user_reminder_max", count_user_reminder_max))
    to_return.append(SlotSet("count_user_reminder", 0))
    to_return.append(SlotSet("followed_intent", followed))
    to_return.append(SlotSet("language", LANGUAGE_GLOBAL))
    return to_return

def get_current_session():
    """@return current session number using BEGIN_DATE and current date"""
    delta_time = dt.now() - BEGIN_DATE
    duration_done = timedelta(seconds=0)
    for i in CONFIG['sessions']:
        session = CONFIG['sessions'][i]
        duration = session['duration']
        for k in duration.keys():
            j = duration[k]
            if k == 'minutes':
                duration_done += timedelta(minutes=int(j))
            if k == 'weeks':
                duration_done += timedelta(weeks=int(j))
            if k == 'days':
                duration_done += timedelta(days=int(j))
            if k == 'hours':
                duration_done += timedelta(hours=int(j))
            if duration_done > delta_time:
                return i

def last_session(current_session):
    """@return True if it's the last session, False otherwise"""
    try:
        CONFIG['sessions'][int(current_session)+1]
        current_session = int(current_session)
        return False
    except:
        current_session = int(current_session)
        return True

def get_duration_until(begin, end, time):
    """@param begin: number of begin session
    @param end: number of end session
    @param time: time(0 or duration already set)
    @return time past between begin session and end session, add it to time paramter
    @raise LastSessionException : if the number of session
    between begin and end includes a non existent session"""
    for i in range(begin, end):
        try:
            CONFIG['sessions'][i+1]['duration']
            duration = CONFIG['sessions'][i]['duration']
            for k in duration.keys():
                j = duration[k]
                if k == 'minutes':
                    time += timedelta(minutes=int(j))
                if k == 'weeks':
                    time += timedelta(weeks=int(j))
                if k == 'days':
                    time += timedelta(days=int(j))
                if k == 'hours':
                    time += timedelta(hours=int(j))
        except:
            print("This is the last session!")
    return time

def get_current_reminder_times(current_session, to_return):
    """@return: List of SlotSet
    Get all reminders times in config file:
        - reminder_patient
        - reminder_end_session
        - reminder_patient_little
        - FOLLOW_INTENT_TRIGGER_DATE (time = date of
        Xst next session beginning, with X
        follow_in_current_session_plus config parameter)"""
    global REMINDER_PATIENT, REMINDER_END_SESSION, REMINDER_PATIENT_LITTLE, DATE_END, FOLLOW_INTENT_TRIGGER_DATE
    reminders = ['reminder_patient', 'reminder_end_session', 'reminder_patient_little']
    duration_session = timedelta(seconds=0)
    session = CONFIG['sessions'][current_session]
    for i in session['duration'].keys():
        j = session['duration'][i]
        if i == 'minutes':
            duration_session += timedelta(minutes=int(j))
        if i == 'weeks':
            duration_session += timedelta(weeks=int(j))
        if i == 'days':
            duration_session += timedelta(days=int(j))
        if i == 'hours':
            duration_session += timedelta(hours=int(j))
    DATE_END = dt.now() + duration_session
    for reminder in reminders:
        reminder_config = CONFIG[reminder]
        reminder1 = timedelta(seconds=0)
        for i in reminder_config.keys():
            j = reminder_config[i]
            if i == 'minutes':
                reminder1 += timedelta(minutes=int(j))
            if i == 'weeks':
                reminder1 += timedelta(weeks=int(j))
            if i == 'days':
                reminder1 += timedelta(days=int(j))
            if i == 'hours':
                reminder1 += timedelta(hours=int(j))
        if reminder == 'reminder_patient':
            REMINDER_PATIENT = reminder1
        elif reminder == 'reminder_end_session':
            REMINDER_END_SESSION = reminder1
        elif reminder == 'reminder_patient_little':
            REMINDER_PATIENT_LITTLE = reminder1
    follow_in_current_session_plus = int(CONFIG['follow_in_current_session_plus'])
    time = timedelta(seconds=5)
    time = get_duration_until(1, current_session, time)
    time = get_duration_until(current_session,
                              follow_in_current_session_plus+current_session,
                              time)
    FOLLOW_INTENT_TRIGGER_DATE = BEGIN_DATE+time
    return to_return

def duckling_set_slots(data, to_return):
    """@return: List of SlotSet
    @param data: all entities detected
    Check all the complex entities detected with duckling to know what slot to set:
        - time
        - distance
        - duration
        - temperature
    If distance, duration or temperature have a unit, set them
    For every times founded, check if it's the traduction of others entiity and, if not set time
    If time has a 'to' and 'from' date, check the duration and set it."""
    try:
        to_set = {'time':[], 'distance':None, 'duration':None, 'temperature':None}
        time = None
        for i in data:
            entity = i['entity']
            if entity in to_set.keys():
                if i['extractor'] == 'ner_duckling' or i['extractor'] == 'ner_duckling_http':
                    if entity != 'time':
                        unit = i['additional_info']['unit']
                        if unit is not None:
                            value = str(i['additional_info']['value'])+" "+str(i['additional_info']['unit'])
                            to_set[entity] = value
                    else:
                        value = str(i['additional_info']['value'])
                        to_set[entity].append(value)
                else:
                    if i['entity'] == 'time':
                        time = i['value']
        print(to_set)
        count = 0
        for i in to_set.keys():
            if to_set[i] is not None:
                if i != 'time':
                    to_return.append(SlotSet(i, to_set[i]))
                    count += 1
            else:
                to_return.append(SlotSet(i, None))
        if len(to_set['time']) > count:
            for i in to_set.keys():
                if i != 'time' and to_set[i] is not None:
                    print(to_set[i])
                    to_check = []
                    to_check_list = DUCKLING_WRAPPER.parse_time(to_set[i])
                    for k in to_check_list:
                        for j in k['value']['others']:
                            to_check.append(j['value'])
                    for j in to_set['time']:
                        if j.startswith('{'):
                            dict_to_from = yaml.load(j)
                            for to_from in dict_to_from:
                                time = dict_to_from[to_from]
                                if time != 'None':
                                    for checki in to_check:
                                        year = int(time[:4])
                                        if time[:-1] in checki or year < 2010:
                                            to_set['time'].remove(j)
                                            break
                        else:
                            for checki in to_check:
                                year = int(j[:4])
                                if j[:-1] in checki or year < 2010:
                                    to_set['time'].remove(j)
                                    break
            to_return.append(SlotSet('time', to_set['time']))
            for i in to_set['time']:
                dict_to_from = yaml.load(i)
                if dict_to_from['to'] is not None and dict_to_from['from'] is not None:
                    from_date = dateutil.parser.parse(dict_to_from['from'])
                    to_date = dateutil.parser.parse(dict_to_from['to'])
                    duration = to_date-from_date
                    if to_set['duration'] is None:
                        to_return.append(SlotSet('duration', duration))
        else:
            to_return.append(SlotSet('time', None))
    except:
        pass
    return to_return

def check(to_return, intent, entities, tracker, dispatcher, response, domain):
    """@return: List of SlotSet
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
            - Send user_reminder_little and user_reminder"""
    language = tracker.get_slot("language")
    response1 = ("""`\tIntent : {}`
`\tEntities : {}`""").format(intent, entities)
    dispatcher.utter_message(response1)
    if intent['confidence'] < 0.5:
        action = Fallback()
        tracker.trigger_follow_up_action(action)
        return to_return
    else:
        emergency = tracker.get_slot("emergency")
        stopword = tracker.get_slot("stopword")
        exitword = tracker.get_slot("exitword")
        if response == emergency:
            #TODO : send a notification instead
            dispatcher.utter_message(get_utterance("emergency", language))
            SumUpSLots().run(dispatcher, tracker, domain)
            action = ActionListen()
            tracker.trigger_follow_up_action(action)
            return to_return
        elif response == stopword and not FIRST:
            for i in range(0, 2):
                if not (tracker.latest_action_name is None or tracker.latest_action_name == 'init'):
                    #print(tracker.latest_action_name)
                    to_return.append(UserUtteranceReverted())
                    if not (tracker.latest_action_name is None or tracker.latest_action_name == 'init'):
                        to_return.append(UserUtteranceReverted())
                    return to_return
        elif response == exitword:
            dispatcher.utter_message(get_utterance("exit", language))
            SumUpSLots().run(dispatcher, tracker, domain)
            action = ActionListen()
            tracker.trigger_follow_up_action(action)
            count_user_reminder = 0
            to_return.append(SlotSet("count_user_reminder", count_user_reminder))
#                print("reminder user scheduled at "+str(dt.now() + REMINDER_PATIENT))
#                to_return.append(ReminderScheduled("user_reminder",
#                                                   dt.now() + REMINDER_PATIENT,
#                                                   kill_on_user_message=True))
            return to_return
        else:
            count_user_reminder = 0
#                to_return.append(SlotSet("count_user_reminder", count_user_reminder))
#                print("reminder user little scheduled at "+str(dt.now() + REMINDER_PATIENT_little))
#                to_return.append(ReminderScheduled("user_reminder_little",
#                                                   dt.now() + REMINDER_PATIENT_LITTLE,
#                                                   kill_on_user_message=True))
#                print("reminder user scheduled at "+str(dt.now() + REMINDER_PATIENT))
#                to_return.append(ReminderScheduled("user_reminder",
#                                                   dt.now() + REMINDER_PATIENT,
#                                                   kill_on_user_message=True))
            return to_return

def followed_intent_found(to_return, intent_name, current_session, followed_intent):
    """@return: List of SlotSet
    @param to_return: the list of SlotSet
    @param intent_name: the name of the intent followed
    @param current_session: number of the current session
    Set mandatory for this session the intent and entities linked\n
    Send a followed_intent_reminder reminder at the begining of the Xst next session """
    global FOLLOWED_REMINDERS
    found = False
    for i in MANDATORIES['requested_intent']:
        if intent_name in i.entity_name:
            found = True
    if not found:
        MANDATORIES['requested_intent'].append(EntityFormField(intent_name, intent_name))
    entities = ""
    for entity in MANDATORIES[intent_name]:
        entities += entity.entity_name+"."
    entities = entities[:-1]
#        name = intent_name+"-"+entities+"*"+str(current_session)
#        print("Reminder scheduled at "+str(FOLLOW_INTENT_TRIGGER_DATE)+" for following intent: "+intent_name)
#        reminder = ReminderScheduled("followed_intent_reminder",
#                                     FOLLOW_INTENT_TRIGGER_DATE, name,
#                                     kill_on_user_message=False)
#        #TODO : add reminder in DB using reminder.as_dict()
#        FOLLOWED_REMINDERS.append(reminder)
#        to_return.append(reminder)
    followed_intent.remove(intent_name)
    to_return.append(SlotSet("followed_intent", followed_intent))

def save(tracker, to_return):
    """@return: List of :
        - intent detected
        - entities detected
        - a list of SlotSet
        - response of the user
    Save everything the user said in a file named after the
    current session number in a folder named after the ID of patient\n
    Call C{followed_intent_found} method if the intent is followed"""
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
    followed = tracker.get_slot("followed_intent")
    if intent_name in followed:
        followed_intent_found(to_return, intent_name, current_session, followed)
    to_return.append(SlotSet("topic", intent_name))
    entities = tracker.latest_message.entities
    #nlu_infos = tracker.latest_message.parse_data
    conv.write("{ '"+str(date)+"' : [{'intent':"+str(intent)+"}, {'entities':"+str(entities)+"}, {'text':'"+str(response)+"'}]},\n")
    conv.close()
    return [intent, entities, to_return, response]

class InitBot(Action):
    """To init the bot"""
    def name(self):
        """@return: the name of the action."""
        return 'init'

    def run(self, dispatcher, tracker, domain):
        """@return: List of SlotSet
        If it's the first time we talk, call method C{set_begin_date}\n
        Get the current session\n
        Check if it's the last session\n
        Set the reminders times\n
        Do the complex config calling C{load_config}\n
        Set global score to 0"""
        global FIRST, LAST_SESSION
        to_return = []
        if FIRST:
            FIRST = False
            set_begin_date()
        else:
            to_return.append(SlotSet("requested_slot", None))
            to_return.append(AllSlotsReset())
        current_session = get_current_session()
        print("Current session is : "+str(current_session))
        LAST_SESSION = last_session(current_session)
        to_return = get_current_reminder_times(current_session, to_return)
        to_return = load_config(current_session, to_return)
        to_return.append(SlotSet("current_session", current_session))
        to_return.append(SlotSet("global_score", 0))
        return to_return

class SaveConv(Action):
    """Use to save the conversation"""
    def name(self):
        """@return: the name of the action."""
        return 'save_conv'

    def run(self, dispatcher, tracker, domain):
        """@return: List of SlotSet
        If it's the first time we talk, call the method C{InitBot().run} and send reminders\n
        Save conversation\n
        Set slots checking complex entities with duckling\n
        Check if there's no noticeable word or low confidence\n"""
        language = tracker.get_slot("language")
        to_return = []
        if FIRST:
            to_return = InitBot().run(dispatcher, tracker, domain)
            for i in to_return:
                tracker.update(i)
            nickname = tracker.get_slot("nickname")
            language = tracker.get_slot("language")
            print(language)
            to_return = []
#            print("reminder change session scheduled at "+str(DATE_END))
#            to_return.append(ReminderScheduled("change_session_reminder",
#                                               DATE_END, kill_on_user_message=False))
#            print("reminder before change session scheduled at "+str(DATE_END - REMINDER_END_SESSION))
#            to_return.append(ReminderScheduled("session_end_reminder",
#                                               DATE_END - REMINDER_END_SESSION,
#                                               kill_on_user_message=False))
            dispatcher.utter_message(get_utterance("welcome", language)+" "+nickname)
        [intent, entities, to_return, response] = save(tracker, to_return)
        insert_to_conversation(response,"PATIENT")
        to_return = duckling_set_slots(entities, to_return)
        to_return = check(to_return, intent, entities, tracker, dispatcher, response, domain)
        return to_return

class SumUpSLots(Action):
    """Sum up slots and save bot utterances"""
    def name(self):
        """@return: the name of the action."""
        return 'sum_up_slots'

    def run(self, dispatcher, tracker, domain):
        """Sum up slots from the tracker (for debug)\n
        Save bot utterances in conversation save file"""
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
        if response is not None:
            conv.write("{ '"+str(date)+"' : [{'text': '"+response+"'}]],\n")
            response = ("""`\ttopic = {}, requested_slot = {},`
`\tactivity = {}, activity_sport = {}, activity_level = {}, activity_duration = {}, activity_period = {}, activity_hard = {}, activity_time = {}, activity_distance = {},`
`\tpain = {}, pain_duration = {}, pain_desc = {}, pain_body_part = {}, pain_change = {}, pain_period = {}, pain_level = {}, pain_time = {},` 
`\tpathology = {}, pathology_symptom = {}, pathology_body_part = {}, pathology_time = {}, pathology_change = {}, pathology_period = {}, pathology_treatment_linked = {}, pathology_duration = {},`
`\ttreatment = {}, treatment_medicinal = {}, treatment_being_taken = {}, treatment_drug = {}, treatment_dosing = {}, treatment_time = {}, treatment_prescripted = {}, treatment_ok = {}, treatment_overdosage = {}, treatment_period = {}, treatment_duration = {}`
`\tinfoPatient = {}, infoPatient_addiction = {}, infoPatient_weight = {}, infoPatient_distance = {}, infoPatient_gender = {}, infoPatient_temperature = {}, infoPatient_heart_rate = {}, infoPatient_blood_pressure = {}, infoPatient_time= {},`
`\tsleep = {}, sleep_duration = {}, sleep_quality = {}`
`\teatingDisorders = {}, eatingDisorders_duration = {}, eatingDisorders_time = {}`
`\tdrugAddiction = {}, drugAddiction_period = {}, drugAddiction_drug = {}, drugAddiction_dosing = {}, drugAddiction_duration = {}, drugAddiction_time = {}, `
`\tsmoking = {}, smoking_period = {}, smoking_dosing = {}, smoking_duration = {}, smoking_time = {},`
`\talcohol = {}, alcohol_period = {}, alcohol_dosing = {}, alcohol_duration = {}, alcohol_time = {},`
`\tnegativeEmo = {},`
`\tpositiveEmo = {},`
`\tsocial = {},`
`\trisk = {},`
`\tdistance = {}, period = {}, duration = {}, time = {}, body_part = {}, temperature = {}, drug = {}, dosing = {}`""").format(
    tracker.get_slot("topic"), tracker.get_slot("requested_slot"),
    tracker.get_slot("activity"), tracker.get_slot("activity_sport"), tracker.get_slot("activity_level"), tracker.get_slot("activity_duration"), tracker.get_slot("activity_period"), tracker.get_slot("activity_hard"), tracker.get_slot("activity_time"), tracker.get_slot("activity_distance"),
    tracker.get_slot("pain"), tracker.get_slot("pain_duration"), tracker.get_slot("pain_desc"), tracker.get_slot("pain_body_part"), tracker.get_slot("pain_change"), tracker.get_slot("pain_period"), tracker.get_slot("pain_level"), tracker.get_slot("pain_time"),
    tracker.get_slot("pathology"), tracker.get_slot("pathology_symptom"), tracker.get_slot("pathology_body_part"), tracker.get_slot("pathology_time"), tracker.get_slot("pathology_change"), tracker.get_slot("pathology_period"), tracker.get_slot("pathology_treatment_linked"), tracker.get_slot("pathology_duration"),
    tracker.get_slot("treatment"), tracker.get_slot("treatment_medicinal"), tracker.get_slot("treatment_being_taken"), tracker.get_slot("treatment_drug"), tracker.get_slot("treatment_dosing"), tracker.get_slot("treatment_time"), tracker.get_slot("treatment_prescripted"), tracker.get_slot("treatment_ok"), tracker.get_slot("treatment_overdosage"), tracker.get_slot("treatment_period"), tracker.get_slot("treatment_duration"),
    tracker.get_slot("infoPatient"), tracker.get_slot("infoPatient_addiction"), tracker.get_slot("infoPatient_weight"), tracker.get_slot("infoPatient_distance"), tracker.get_slot("infoPatient_gender"), tracker.get_slot("infoPatient_temperature"), tracker.get_slot("infoPatient_heart_rate"), tracker.get_slot("infoPatient_blood_pressure"), tracker.get_slot("infoPatient_time"),
    tracker.get_slot("sleep"), tracker.get_slot("sleep_duration"), tracker.get_slot("sleep_quality"),
    tracker.get_slot("eatingDisorders"), tracker.get_slot("eatingDisorders_duration"), tracker.get_slot("eatingDisorders_time"),
    tracker.get_slot("drugAddiction"), tracker.get_slot("drugAddiction_period"), tracker.get_slot("drugAddiction_drug"), tracker.get_slot("drugAddiction_dosing"), tracker.get_slot("drugAddiction_duration"), tracker.get_slot("drugAddiction_time"), 
    tracker.get_slot("smoking"), tracker.get_slot("smoking_period"), tracker.get_slot("smoking_dosing"), tracker.get_slot("smoking_duration"), tracker.get_slot("smoking_time"),
    tracker.get_slot("alcohol"), tracker.get_slot("alcohol_period"), tracker.get_slot("alcohol_dosing"), tracker.get_slot("alcohol_duration"), tracker.get_slot("alcohol_time"),
    tracker.get_slot("negativeEmo"),
    tracker.get_slot("positiveEmo"),
    tracker.get_slot("social"),
    tracker.get_slot("risk"),
    tracker.get_slot("distance"), tracker.get_slot("period"), tracker.get_slot("duration"), tracker.get_slot("time"), tracker.get_slot("body_part"), tracker.get_slot("temperature"), tracker.get_slot("drug"), tracker.get_slot("dosing"))
            dispatcher.utter_message(response)
            conv.write("{ '"+str(date)+"' : [{'text': '"+response+"'}]},\n")
        conv.close()
