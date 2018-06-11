## Story 01bis
* pain{"period": "every day"}
	- save_conv
     - action_period_pain
     - sum_up_slots

## Story 01ter
* activity{"period": "every day"}
	- save_conv
     - action_period_sport
     - sum_up_slots

## Story 03
* emotional_sadness
	- save_conv
	- sum_up_emotionnal_sadness
     - sum_up_slots

## Story 04
* emotional_hapiness
	- save_conv
	- sum_up_emotional_hapiness
     - sum_up_slots

## Story 05
* fallback
	- save_conv
	- sum_up_fallback
     - sum_up_slots

## Story 06
* social
	- save_conv
	- sum_up_social
     - sum_up_slots

## Generated Story -6941724149388542790
* pain
	- save_conv
    - set_topic_pain
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots

## Generated Story 5875206738412970191
* pain
	- save_conv
    - set_topic_pain
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* activity
	- save_conv
    - set_topic_sport
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* pain
	- save_conv
    - set_topic_pain
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* activity
	- save_conv
    - set_topic_sport
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots

## Generated Story -5610843510145814846
* activity
	- save_conv
    - set_topic_sport
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* pain{"duration": "1h"}
	- save_conv
    - slot{"duration": "1h"}
    - set_topic_pain
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_pain
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots

## Generated Story 4238931968757555282
* pain
	- save_conv
    - set_topic_pain
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* pain{"duration": "1h"}
	- save_conv
    - slot{"duration": "1h"}
    - set_topic_pain
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - sum_up_slots
    - slot{"duration": null}
    - action_check_slots_pain
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots


## Generated Story -1271088715166499960
* activity
	- save_conv
    - set_topic_sport
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
	- save_conv
    - slot{"duration": "1h"}
    - set_topic_sport
    - slot{"topic": "sport"}
    - slot{"sport_duration": "1h"}
    - action_duration
    - sum_up_slots
    - slot{"duration": null}
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots

## Generated Story 8012220161918558796
* fallback
	- save_conv
    - sum_up_fallback
    - sum_up_slots
* fallback{"duration": "1h"}
	- save_conv
    - slot{"duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - sum_up_fallback
    - sum_up_slots

## Generated Story -1271088715166499960
* activity
	- save_conv
    - set_topic_sport
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* fallback{"duration": "1h"}
	- save_conv
    - slot{"duration": "1h"}
    - slot{"topic": "sport"}
    - slot{"sport_duration": "1h"}
    - action_duration
    - sum_up_slots
    - slot{"duration": null}
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots

## Generated Story -779845410824225099
* pain
	- save_conv
    - set_topic_pain
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "body_part"}
    - sum_up_slots
* pain{"body_part": "leg"}
	- save_conv
    - slot{"body_part": "leg"}
    - set_topic_pain
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* fallback{"duration": "1h"}
	- save_conv
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
	- save_conv
    - slot{"pain_change": "continuous"}
    - set_topic_pain
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"requested_slot": "pain_level"}
    - sum_up_slots
* pain{"pain_level": "sharp"}
	- save_conv
    - slot{"pain_level": "sharp"}
    - set_topic_pain
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}

## Generated Story -7732988583674420202
* activity{"sport": "gym"}
	- save_conv
    - slot{"sport": "gym"}
    - set_topic_sport
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* fallback{"duration": "1h"}
	- save_conv
    - slot{"duration": "1h"}
    - slot{"sport_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - sum_up_slots

## Generated Story 5006306901738416024
* pain{"body_part": "leg", "pain_level": "sharp"}
	- save_conv
    - slot{"body_part": "leg"}
    - slot{"pain_level": "sharp"}
    - set_topic_pain
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
	- save_conv
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
	- save_conv
    - slot{"pain_change": "continuous"}
    - set_topic_pain
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - sum_up_slots

## Generated Story 464443274835785522
* activity{"sport": "gym"}
	- save_conv
    - slot{"sport": "gym"}
    - set_topic_sport
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* fallback{"duration": "1h"}
	- save_conv
    - slot{"duration": "1h"}
    - slot{"sport_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - sum_up_slots
* pain{"pain_level": "sharp", "body_part": "leg"}
	- save_conv
    - slot{"body_part": "leg"}
    - slot{"pain_level": "sharp"}
    - set_topic_pain
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
	- save_conv
    - slot{"pain_change": "continuous"}
    - set_topic_pain
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
	- save_conv
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - sum_up_slots

## Generated Story 193901622314387211
* activity{"sport": "gym"}
	- save_conv
    - slot{"sport": "gym"}
    - set_topic_sport
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* pain{"duration": "1h"}
	- save_conv
    - slot{"duration": "1h"}
    - slot{"sport_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - sum_up_slots

## Generated Story -1950389272781253170
* pain{"duration": "1h"}
	- save_conv
    - slot{"duration": "1h"}
    - set_topic_pain
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_pain
    - slot{"requested_slot": "pain_level"}
    - sum_up_slots
* pain{"pain_level": "sharp", "body_part": "leg"}
	- save_conv
    - slot{"body_part": "leg"}
    - slot{"pain_level": "sharp"}
    - set_topic_pain
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
	- save_conv
    - slot{"pain_change": "continuous"}
    - set_topic_pain
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - sum_up_slots


## Generated Story -5176651320026530081
* activity{"duration": "1h"}
	- save_conv
    - slot{"duration": "1h"}
    - set_topic_sport
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots

* activity{"sport": "gym"}
	- save_conv
    - slot{"sport": "gym"}
    - set_topic_sport
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - sum_up_slots


