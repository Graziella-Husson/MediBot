from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from simpleActions import Fallback
from initAndComplex import get_complex_entities
from formActions import (
ActionFillSlotsSport, 
ActionFillSlotsPain, 
InfoPatient, 
Pathology,
Treatment
)

class SetMultiple(Action):
    def get_topic(self, tracker):
        """
        @return The topic 
        
        If the slot 'requested_slot' is not null and requires something with a topic ('sport' slot has no topic, because it's not a complex slot) 
        the topic is set to from the topic of 'requested_slot' {topic}_{entity}
        else, the topic is set with the name of the intent detected.
        """   
        topic = tracker.get_slot("topic")
        requested_slot = tracker.get_slot("requested_slot")
        if requested_slot != None and len(requested_slot.split('_'))>1:
            head, *tail = requested_slot.split('_')
            topic = head
        return topic

    def get_next_action(self,topic):
        """
        @return The next action to do. 
        @param topic: used to know which action to do.
        
        The possibilities are intents that can handle complex entities:
            - activity
            - pain
            - infPatient
            - pathology
            - treatment
        """   
        return {
        'activity': ActionFillSlotsSport(),
        'pain': ActionFillSlotsPain(),
        'infoPatient': InfoPatient(),
        'pathology': Pathology(),
        'treatment': Treatment()
        }.get(topic, Fallback())    # fallback is default if topic not found
    
    def name(self):
        """
        @return: the name of the action.
        """
        return 'action_multiple_set_complex'
    
    def run(self, dispatcher, tracker, domain):
        """
        For each possible complex entity, verify if there's a value in the linked slot. If there's one, use the topic to know in which slot to put it.
        If the slot does not exists, do nothing (e.g 'pain_distance' slot)
        Trigger the action related to the topic with the method C{get_next_action(topic)}
        """
        every = get_complex_entities()
        topic = self.get_topic(tracker)
        real_topic = topic
        for i in every:
            if tracker.get_slot(str(i)) != None:
                value = tracker.get_slot(i)
                print(topic+"_"+str(i))
                print(value)
                if topic+"_"+str(i) in tracker.slots:
                    tracker.update(SlotSet(topic+"_"+str(i),value))
                tracker.update(SlotSet(str(i),None))
        tracker.update(SlotSet("requested_slot",None))
        action = self.get_next_action(topic)
        if action != None:
            tracker.trigger_follow_up_action(action)
        
#class SetPeriod(Action):
#    def name(self):
#        return 'action_period'
#    
#    def run(self, dispatcher, tracker, domain):
#        requested_slot = tracker.get_slot("requested_slot")
#        topic = tracker.get_slot("topic")
#        period = tracker.get_slot("period")
#        action = None
#        if requested_slot=="pain_period":
#            tracker.update(SlotSet("pain_period",period))
#            action = ActionFillSlotsPain()
#        elif requested_slot=="sport_period":
#            tracker.update(SlotSet("sport_period",period))
#            action = ActionFillSlotsSport()
#        else:
#            if topic=="pain":
#                tracker.update(SlotSet("pain_period",period))
#                action = ActionFillSlotsPain()
#            elif topic=="activity":
#                tracker.update(SlotSet("sport_period",period))
#                action = ActionFillSlotsSport()
#            else:
#                action = Fallback()
#        tracker.trigger_follow_up_action(action)
#        tracker.update(SlotSet("period",None))
#
#class SetDuration(Action):
#    def name(self):
#        return 'action_duration'
#    
#    def run(self, dispatcher, tracker, domain):
#        requested_slot = tracker.get_slot("requested_slot")
#        topic = tracker.get_slot("topic")
#        duration = tracker.get_slot("duration")
#        action = None
#        if requested_slot=="pain_duration":
#            tracker.update(SlotSet("pain_duration",duration))
#            action = ActionFillSlotsPain()
#        elif requested_slot=="sport_duration":
#            tracker.update(SlotSet("sport_duration",duration))
#            action = ActionFillSlotsSport()
#        else:
#            if topic=="pain":
#                tracker.update(SlotSet("pain_duration",duration))
#                action = ActionFillSlotsPain()
#            elif topic=="activity":
#                tracker.update(SlotSet("sport_duration",duration))
#                action = ActionFillSlotsSport()
#            else:
#                action = Fallback()
#        #print(action)
#        tracker.trigger_follow_up_action(action)
#        tracker.update(SlotSet("duration",None))
#
#class SetTime(Action):
#    def name(self):
#        return 'action_time'
#    
#    def run(self, dispatcher, tracker, domain):
#        requested_slot = tracker.get_slot("requested_slot")
#        topic = tracker.get_slot("topic")
#        time = tracker.get_slot("time")
#        action = None
#        if requested_slot=="pain_begin_time":
#            tracker.update(SlotSet("pain_begin_time",time))
#            action = ActionFillSlotsPain()
#        elif requested_slot=="activity_begin_time":
#            tracker.update(SlotSet("activity_begin_time",time))
#            action = ActionFillSlotsSport()
#        elif requested_slot=="date_check_up":
#            tracker.update(SlotSet("date_check_up",time))
#            action = InfoPatient()
#        else:
#            if topic=="pain":
#                tracker.update(SlotSet("pain_begin_time",time))
#                action = ActionFillSlotsPain()
#            elif topic=="activity":
#                tracker.update(SlotSet("activity_begin_time",time))
#                action = ActionFillSlotsSport()
#            elif topic=="info_patient":
#                tracker.update(SlotSet("date_check_up",time))
#                action = InfoPatient()
#            else:
#                action = Fallback()
#        #print(action)
#        tracker.trigger_follow_up_action(action)
#        tracker.update(SlotSet("time",None))
#        
#class SetDistance(Action):
#    def name(self):
#        return 'action_distance'
#    
#    def run(self, dispatcher, tracker, domain):
#        requested_slot = tracker.get_slot("requested_slot")
#        topic = tracker.get_slot("topic")
#        distance = tracker.get_slot("distance")
#        action = None
#        if requested_slot=="sport_distance":
#            tracker.update(SlotSet("sport_distance",distance))
#            action = ActionFillSlotsSport()
#        elif requested_slot=="size":
#            tracker.update(SlotSet("size",distance))
#            action = InfoPatient()
#        else:
#            if topic=="activity":
#                tracker.update(SlotSet("sport_distance",distance))
#                action = ActionFillSlotsSport()
#            elif topic=="info_patient":
#                tracker.update(SlotSet("size",distance))
#                action = InfoPatient()
#            else:
#                action = Fallback()
#        #print(action)
#        tracker.trigger_follow_up_action(action)
#        tracker.update(SlotSet("distance",None))
#        
#class SetBodyPart(Action):
#    def name(self):
#        return 'action_body_part'
#    
#    def run(self, dispatcher, tracker, domain):
#        requested_slot = tracker.get_slot("requested_slot")
#        topic = tracker.get_slot("topic")
#        body_part = tracker.get_slot("body_part")
#        action = None
#        if requested_slot=="pain_body_part":
#            tracker.update(SlotSet("pain_body_part",body_part))
#            action = ActionFillSlotsPain()
#        elif requested_slot=="pathology_body_part":
#            tracker.update(SlotSet("pathology_body_part",body_part))
#            action = Pathology()
#        else:
#            if topic=="pain":
#                tracker.update(SlotSet("pain_body_part",body_part))
#                action = ActionFillSlotsPain()
#            elif topic=="pathology":
#                tracker.update(SlotSet("pathology_body_part",body_part))
#                action = Pathology()
#            else:
#                action = Fallback()
#        #print(action)
#        tracker.trigger_follow_up_action(action)
#        tracker.update(SlotSet("body_part",None))