import sys
import os
import django
sys.path.append("../../../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ailixir_dev.settings")
django.setup()
# import importlib.util
# spec = importlib.util.spec_from_file_location("ANSWER", "/home/django/stage2a/ailixir_dev/appli/models.py")
# foo = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(foo)
# foo.MyClass()

# print(foo)
from appli.models import ENTITY, SESSION, CONVERSATION, PATIENT_DETAILS,ANSWER

def insert_to_answer(value,session,entity,patient,conversation):
	entity_obj=ENTITY.objects.get(entity_name=entity)
	session_obj=SESSION.objects.get(session_id=session)
	conversation_obj=CONVERSATION.objects.get(conversation_id=conversation)
	patient_obj=PATIENT_DETAILS.objects.get(id=patient)
	answer = ANSWER(answer_value=value,answer_is_fallback=False,session_id=session_obj,entity_id=entity_obj,patient_id=patient_obj,conversation_id=conversation_obj)
	answer.save()

def insert_to_conversation(data,speaker):
	conversation = CONVERSATION(raw_data=data,speaker=speaker)
	conversation.save()

