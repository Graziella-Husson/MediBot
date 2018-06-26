from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from simpleActions import Fallback
from formActions import ActionFillSlotsSport, ActionFillSlotsPain

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
