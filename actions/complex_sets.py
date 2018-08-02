"""
This module is used to regroup all complex sets actions.\n
A complex set action is an action where the bot will fill slots with
complex entities\n
Created on Tue Jun 26 10:22:40 2018\n
@author: U{@Graziella-Husson<https://github.com/Graziella-Husson>}
"""
from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from simple_actions import Fallback
from init_and_complex import get_complex_entities
from form_actions import (
    Activity,
    Pain,
    InfoPatient,
    Pathology,
    Treatment,
    Sleep,
    EatingDisorders,
    DrugAddiction,
    Smoking,
    Alcohol
)


def get_topic(tracker):
    """@return: The topic
    If the slot 'requested_slot' is not null and requires something
    with a topic
    the topic is set to from the topic of 'requested_slot' {topic}_{entity}
    else, the topic is set with the name of the intent detected."""
    topic = tracker.get_slot("topic")
    requested_slot = tracker.get_slot("requested_slot")
    if requested_slot is not None and len(requested_slot.split('_')) > 1:
        head, *tail = requested_slot.split('_')
        topic = head
    return topic


def get_next_action(topic):
    """@return: The next action to do.
    @param topic: used to know which action to do.\n
    The possibilities are intents that can handle complex entities:
        - activity
        - pain
        - infPatient
        - pathology
        - treatment"""
    return {
        'activity': Activity(),
        'pain': Pain(),
        'infoPatient': InfoPatient(),
        'pathology': Pathology(),
        'treatment': Treatment(),
        'sleep': Sleep(),
        'eatingDisorders': EatingDisorders(),
        'drugAddiction': DrugAddiction(),
        'smoking': Smoking(),
        'alcohol': Alcohol()
        }.get(topic, Fallback())    # fallback is default if topic not found


class SetMultiple(Action):
    """Fill slots with complex entities values"""
    def name(self):
        """@return: the name of the action."""
        return 'action_multiple_set_complex'

    def run(self, dispatcher, tracker, domain):
        """For each possible complex entity,
        verify if there's a value in the linked slot.
        If there's one, use the topic to know in which slot to put it.
        If the slot does not exists, do nothing (e.g 'pain_distance' slot)
        Trigger the action related to the topic
        with the method C{get_next_action(topic)}"""
        every = get_complex_entities()
        topic = get_topic(tracker)
#        real_topic = topic
        for i in every:
            if tracker.get_slot(str(i)) is not None:
                value = tracker.get_slot(i)
#                print(topic+"_"+str(i))
#                print(value)
                if topic+"_"+str(i) in tracker.slots:
                    tracker.update(SlotSet(topic+"_"+str(i), value))
                tracker.update(SlotSet(str(i), None))
        tracker.update(SlotSet("requested_slot", None))
        action = get_next_action(topic)
        if action is not None:
            tracker.trigger_follow_up_action(action)
