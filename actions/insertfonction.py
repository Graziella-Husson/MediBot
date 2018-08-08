#import sys
#import os
#import django
#sys.path.append("../../../")
#os.environ.setdefault("DJANGO_SETTINGS_MODULE","ailixir_dev.settings")
#django.setup()
# import importlib.util
# spec = importlib.util.spec_from_file_location("ANSWER", "/home/django/stage2a/ailixir_dev/appli/models.py")
# foo = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(foo)
# foo.MyClass()

# print(foo)
#from appli.models import ENTITY, SESSION, CONVERSATION, PATIENT_DETAILS,ANSWER, PATIENT_BOT

def insert_to_answer(value,session,entity,slack_id,conversation):
    print("insert_to_answer")
#	entity_obj=ENTITY.objects.get(entity_name=entity)
#	session_obj=SESSION.objects.get(session_id=session)
#	conversation_obj=CONVERSATION.objects.get(conversation_id=conversation)
#	patient_id=PATIENT_BOT.objects.get(patient_bot_slack_id=slack_id).value('patient_id')
#	patient_obj=PATIENT_DETAILS.objects.get(id=patient_id)
#	answer = ANSWER(answer_value=value,answer_is_fallback=False,session_id=session_obj,entity_id=entity_obj,patient_id=patient_obj,conversation_id=conversation_obj)
#	answer.save()

def insert_to_conversation(data,speaker,slack_id):
    print("insert_to_conversation")
#	patient_id=PATIENT_BOT.objects.get(patient_bot_slack_id=slack_id).value('patient_id')
#	patient_obj=PATIENT_DETAILS.objects.get(id=patient_id)
#	conversation = CONVERSATION(raw_data=data,speaker=speaker,patient_id=patient_obj)
#	conversation.save()

def get_id_patient(slack_id):
    return "patient_id"
#	return PATIENT_BOT.objects.get(patient_bot_slack_id=slack_id).values('patient_id')

def get_follow_insert_trigger_date(slack_id):
    return "patient_bot_follow_intent_trigger_date"
#	return PATIENT_BOT.objects.get(patient_bot_slack_id=slack_id).values('patient_bot_follow_intent_trigger_date')

def get_last_session(slack_id):
    return False
#	return PATIENT_BOT.objects.get(patient_bot_slack_id=slack_id).values('patient_bot_last_session')

def get_end_date(slack_id):
    return "patient_bot_end_date"
#	return PATIENT_BOT.objects.get(patient_bot_slack_id=slack_id).values('patient_bot_end_date')

def get_first(slack_id):
    return True
#	return PATIENT_BOT.objects.get(patient_bot_slack_id=slack_id).values('patient_bot_first')

def get_begin_date(slack_id):
    return "patient_bot_begin_date"
#	return PATIENT_BOT.objects.get(patient_bot_slack_id=slack_id).values('patient_bot_begin_date')

def set_follow_insert_trigger_date(slack_id,new_value):
    print("set_follow_insert_trigger_date", new_value)
#	patient_bot = PATIENT_BOT.objects.get(patient_bot_slack_id=slack_id)
#	patient_bot.follow_insert_trigger_date=new_value
#	patient_bot.save()

def set_last_session(slack_id,new_value):
    print("set_last_session", new_value)
#	patient_bot = PATIENT_BOT.objects.get(patient_bot_slack_id=slack_id)
#	patient_bot.last_session=new_value
#	patient_bot.save()

def set_end_date(slack_id,new_value):
    print("set_end_date", new_value)
#	patient_bot = PATIENT_BOT.objects.get(patient_bot_slack_id=slack_id)
#	patient_bot.end_date=new_value
#	patient_bot.save()

def set_first(slack_id,new_value):
    print("set_first", new_value)
#	patient_bot = PATIENT_BOT.objects.get(patient_bot_slack_id=slack_id)
#	patient_bot.first=new_value
#	patient_bot.save()

def set_begin_date(slack_id,new_value):
    print("set_begin_date", new_value)
#	patient_bot = PATIENT_BOT.objects.get(patient_bot_slack_id=slack_id)
#	patient_bot.set_begin_date=new_value
#	patient_bot.save()

def set_follow_reminder(slack_id,new_value):
    print("set_follow_reminder", new_value)

def get_follow_reminder(slack_id):
    return "[{\"a\":\"b\",\"c\":\"d\"}, {\"e\":\"f\"}]"