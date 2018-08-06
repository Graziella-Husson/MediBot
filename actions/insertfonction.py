#import sys
#import os
#import django
#sys.path.append("../../../")
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ailixir_dev.settings")
#django.setup()
#from appli.models import ANSWER, ENTITY, SESSION, CONVERSATION, PATIENT_DETAILS


def insert_to_answer(value, session, entity, patient, conversation):
    print("insert!")
#    entity = ENTITY.objects.get(entity_name=entity)
#    session = SESSION.objects.get(session_id=session)
#    conversation = CONVERSATION.objects.get(conversation_id=conversation)
#    patient = PATIENT_DETAILS.objects.get(id=patient)
#    answer = ANSWER(answer_value=value, answer_is_fallback=False, session_id=session, entity_id=entity, patient_id=patient, conversation_id=conversation)
#    answer.save()


def insert_to_conversation(data, conversation_id=None):
    print("insert!")
    # CONVERSATION.objects.filter(pk=some_value).update(raw_data=raw_data+data)
#    if conversation_id == None:
#        conversation = CONVERSATION(raw_data=data)
#        conversation.save()
#    else:
#        conversation = CONVERSATION.objects.get(conversation_id=conversation_id)
#        conversation.raw_data = conversation.raw_data+" "+data
#        conversation.save()
