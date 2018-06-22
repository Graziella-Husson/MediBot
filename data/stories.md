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
    - action_check_intents
    - slot{"requested_slot": "pain"}
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
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Story 07
* hello
	- save_conv
	- sum_up_hello
     - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Story 08
	- change_session_reminder
    - sum_up_slots 
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots

## Story 09
	- user_reminder_little
    - sum_up_slots 
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots

## Generated Story -6941724149388542790
* pain
	- save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots

## Generated Story 5875206738412970191
* pain
	- save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* activity
	- save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* pain
	- save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* activity
	- save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots

## Generated Story -5610843510145814846
* activity
	- save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* pain{"duration": "1h"}
	- save_conv
    - slot{"duration": "1h"}
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
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* pain{"duration": "1h"}
	- save_conv
    - slot{"duration": "1h"}
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
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
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
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "body_part"}
    - sum_up_slots
* pain{"body_part": "leg"}
	- save_conv
    - slot{"body_part": "leg"}
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
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
* pain{"pain_desc": "sharp"}
	- save_conv
    - slot{"pain_desc": "sharp"}
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}

## Generated Story -7732988583674420202
* activity{"sport": "gym"}
	- save_conv
    - slot{"sport": "gym"}
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
* pain{"body_part": "leg", "pain_desc": "sharp"}
	- save_conv
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
	- save_conv
    - slot{"duration": "1h"}
    - slot{"topic": "sport"}
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
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - sum_up_slots

## Generated Story 464443274835785522
* activity{"sport": "gym"}
	- save_conv
    - slot{"sport": "gym"}
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
* pain{"pain_desc": "sharp", "body_part": "leg"}
	- save_conv
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
	- save_conv
    - slot{"pain_change": "continuous"}
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
	- save_conv
    - slot{"topic": "sport"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - sum_up_slots

## Generated Story 193901622314387211
* activity{"sport": "gym"}
	- save_conv
    - slot{"sport": "gym"}
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* pain{"duration": "1h"}
	- save_conv
    - slot{"topic": "pain"}
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
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
* pain{"pain_desc": "sharp", "body_part": "leg"}
	- save_conv
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
	- save_conv
    - slot{"pain_change": "continuous"}
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - sum_up_slots


## Generated Story -5176651320026530081
* activity{"duration": "1h"}
	- save_conv
    - slot{"duration": "1h"}
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

## Generated Story 2725336697775035628
* activity{"duration": "1", "sport": "gym"}
    - slot{"duration": "1"}
    - slot{"sport": "gym"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"sport_duration": "1"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - sum_up_slots
* agree
    - save_conv
    - reset_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
    - export	

## Generated Story 3723997061960295198
* activity{"sport": "gym", "duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport": "gym"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - sum_up_slots
* disagree
    - save_conv
    - ask_what_sport
    - sum_up_slots

## Generated Story 6461157845935266253
* activity{"sport": "gym", "duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport": "gym"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - sum_up_slots
* disagree
    - save_conv
    - ask_what_sport
    - sum_up_slots
* activity{"sport": null}
    - slot{"sport": null}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - sum_up_slots
* agree
    - save_conv
    - reset_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Generated Story 3019702893302339121
* pain{"body_part": "leg", "duration": "1h", "pain_desc": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - sum_up_slots
* disagree
    - save_conv
    - ask_what_pain
    - sum_up_slots
* pain{"pain_desc": null}
    - slot{"pain_desc": null}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
* pain{"pain_desc": "low"}
    - slot{"pain_desc": "low"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_desc": "low"}
    - sum_up_slots
* agree
    - save_conv
    - reset_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"topic": null}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Generated Story 9196803218796210525
* emotional_sadness
    - save_conv
    - sum_up_emotionnal_sadness
    - sum_up_slots
* agree
    - save_conv
    - ask_why
    - sum_up_slots
* social
    - save_conv
    - sum_up_social
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Generated Story 7685890354649122920
* emotional_sadness
    - save_conv
    - sum_up_emotionnal_sadness
    - sum_up_slots
* disagree
    - save_conv
    - sum_up_disagree
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Generated Story -8513284858755581239
* activity{"sport": "gym", "duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport": "gym"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - sum_up_slots
* agree
    - save_conv
    - reset_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* pain{"body_part": "leg", "duration": "1h", "pain_desc": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - sum_up_slots
* agree
    - save_conv
    - reset_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"topic": null}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Generated Story 4734389401321163188
* hello
    - save_conv
    - sum_up_hello
    - sum_up_slots
* bye
    - save_conv
    - sum_up_bye
    - sum_up_slots 

## reminder
	- change_session_reminder
    - sum_up_slots 
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots

## Generated Story 8845097822793104914
* hello
    - save_conv
    - sum_up_hello
    - sum_up_slots
* emotional_hapiness
    - save_conv
    - sum_up_emotional_hapiness
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* emotional_sadness
    - save_conv
    - sum_up_emotionnal_sadness
    - sum_up_slots
* disagree
    - save_conv
    - sum_up_disagree
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Generated Story -127921750340159113
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_pain
    - slot{"requested_slot": "body_part"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots

## Generated Story 7375445888802048353
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots
* pain{"duration": "2h"}
    - slot{"duration": "2h"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "2h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots

## Generated Story -3562440609605942758
* pain
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
* pain{"pain_desc": "sharp"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "body_part"}
    - sum_up_slots
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* activity{"sport": "gym", "duration": "2h"}
    - slot{"duration": "2h"}
    - slot{"sport": "gym"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"pain_duration": "2h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "sport"}
    - slot{"sport_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_sport
    - sum_up_slots
* agree
    - save_conv
    - reset_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* pain
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots
* disagree
    - save_conv
    - ask_what_pain
    - sum_up_slots
* pain{"pain_duration": null}
    - slot{"pain_duration": null}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots
* agree
    - save_conv
    - reset_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"topic": null}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Generated Story 455122062663373821
* fallback
    - save_conv
    - sum_up_fallback
    - sum_up_slots
* fallback
    - save_conv
    - sum_up_fallback
    - sum_up_slots
* fallback
    - save_conv
    - sum_up_fallback
    - sum_up_slots

## Generated Story -659407491090945029
* fallback
    - save_conv
    - sum_up_fallback
    - sum_up_slots
* social
    - save_conv
    - sum_up_social
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* social
    - save_conv
    - sum_up_social
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* hello
    - save_conv
    - sum_up_hello
    - sum_up_slots
* hello
    - save_conv
    - sum_up_hello
    - sum_up_slots
* bye
    - save_conv
    - sum_up_bye
    - sum_up_slots
* bye
    - save_conv
    - sum_up_bye
    - sum_up_slots

## Generated Story 4102562688386678694
* emotional_sadness
    - save_conv
    - sum_up_emotionnal_sadness
    - sum_up_slots
* disagree
    - save_conv
    - sum_up_disagree
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* emotional_sadness
    - save_conv
    - sum_up_emotionnal_sadness
    - sum_up_slots
* agree
    - save_conv
    - ask_why
    - sum_up_slots

## Generated Story 1343794098013794343
* emotional_hapiness
    - save_conv
    - sum_up_emotional_hapiness
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* emotional_hapiness
    - save_conv
    - sum_up_emotional_hapiness
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Generated Story -2277678836882085909
* pain
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
* pain
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "body_part"}
    - sum_up_slots
* activity
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots

## Generated Story -3820794171829640972
* pain{"period": "every week"}
    - slot{"period": "every week"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_period": "every week"}
    - action_period
    - slot{"period": null}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots

## Generated Story -5434698572183068955
* activity{"period": "every week"}
    - slot{"period": "every week"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"sport_period": "every week"}
    - action_period
    - slot{"period": null}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots

## Generated Story 3140560240339684166
* hello
    - save_conv
    - sum_up_hello
    - sum_up_slots
* pain{"body_part": "leg", "pain_desc": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - sum_up_slots
* agree
    - save_conv
    - reset_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"topic": null}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "sport"}
    - slot{"sport_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_sport
    - sum_up_slots
* disagree
    - save_conv
    - ask_what_sport
    - sum_up_slots
* activity{"sport": null}
    - slot{"sport": null}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - sum_up_slots
* agree
    - save_conv
    - reset_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Generated Story 3038158759323658480
* hello
    - save_conv
    - sum_up_hello
    - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "sport"}
    - slot{"sport_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_sport
    - sum_up_slots
* disagree
    - save_conv
    - ask_what_sport
    - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - sum_up_slots
* agree
    - save_conv
    - reset_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* pain{"pain_desc": "sharp", "duration": "1h", "body_part": "leg"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots
* agree
    - save_conv
    - reset_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"topic": null}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Generated Story -7819480569678491052
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots

## Generated Story 1925504235369835121
* emotional_sadness
    - save_conv
    - sum_up_emotionnal_sadness
    - sum_up_slots
* agree
    - save_conv
    - ask_why
    - sum_up_slots
* social
    - save_conv
    - sum_up_social
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Generated Story 2494799625001486265
* social{"period": "last night"}
    - slot{"period": "last night"}
    - save_conv
    - sum_up_social
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* emotional_sadness
    - save_conv
    - sum_up_emotionnal_sadness
    - sum_up_slots
* agree
    - save_conv
    - ask_why
    - sum_up_slots
* pain
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots

## Generated Story 1754673916680524262
* pain{"body_part": "leg", "pain_desc": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots

## Generated Story 3849858968041243699
* pain
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
* pain{"pain_desc": "sharp"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"requested_slot": "body_part"}
    - sum_up_slots
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots

## Generated Story 4740783391932763923
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* pain{"duration": "2h"}
    - slot{"duration": "2h"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"sport_duration": "2h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_sport
    - sum_up_slots

## Generated Story -1978400107817392474
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
* pain{"pain_desc": "sharp"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots
* agree
    - save_conv
    - reset_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"topic": null}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Reminder
	- change_session_reminder
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots

## Generated Story -5743783724198374108
* pain{"body_part": "leg", "pain_desc": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots
* agree
    - save_conv
    - reset_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"topic": null}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "sport"}
    - slot{"sport_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_sport
    - sum_up_slots
* agree
    - save_conv
    - reset_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Generated Story 336204907209519946
* pain{"pain_desc": "sharp", "body_part": "leg"}
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots

## Generated Story 2576780721904015728
* pain{"pain_desc": "sharp", "body_part": "leg"}
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots

## Generated Story -5409622776363900907
* pain
    - save_conv
    - init
    - sum_up_slots
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots

## Generated Story -5409622776363900900
* activity
    - save_conv
    - init
    - sum_up_slots
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots

## Generated Story 1958217798927396981
* hello
    - save_conv
    - init
    - sum_up_hello
    - sum_up_slots
* pain{"pain_desc": "sharp", "body_part": "leg"}
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots

## Generated Story 8875174060650682806
* hello
    - save_conv
    - init
    - sum_up_hello
    - sum_up_slots
* pain{"pain_desc": "sharp", "body_part": "leg"}
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_pain
    - sum_up_slots

## Generated Story 5146966519383446092
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - init
    - sum_up_slots
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots

## Generated Story 6774627428914349252
* pain
    - save_conv
    - init
    - sum_up_slots
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
    - export

## Generated Story 5051815052804709224
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - init
    - sum_up_slots
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
    - export

## Generated Story 9135239180568302386
* activity
    - save_conv
    - init
    - sum_up_slots
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
    - export

## Generated Story 7944624962110648647
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - init
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots
    - export

## Generated Story 4116875444495830871
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - init
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots
    - export

## Generated Story 252914871264684106
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - init
    - sum_up_slots
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
    - export

## Generated Story 6609619548161180180
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - init
    - sum_up_slots
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
    - export

## Generated Story -4751253490818363637
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - init
    - sum_up_slots
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots
    - export

## Generated Story -8213000219223108873
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - init
    - sum_up_slots
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
    - export

## Generated Story -7634911065912903541
* pain
    - save_conv
    - init
    - sum_up_slots
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
    - export

## Generated Story -1316194614037817956
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - init
    - sum_up_slots
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
* pain{"pain_desc": "sharp"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - sum_up_slots
    - export

## ReminderPatient
    - user_reminder
    - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots

## ReminderSession
    - session_end_reminder
    - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - action_duration
    - slot{"duration": null}
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots

## Generated Story 5765629662883705030
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - save_conv
    - init
    - reset_slots
    - reminder{"action": "change_session_reminder", "name": "33cd4866-7082-11e8-86a6-08002700c687", "date_time": "2018-06-14T16:33:00", "kill_on_user_msg": false}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
* pain{"pain_desc": "sharp"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - sum_up_slots
* agree
    - save_conv
    - reset_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
    - export

## Generated Story -7898190671247152748
* fallback
    - save_conv
    - init
    - reset_slots
    - sum_up_slots
    - sum_up_fallback
    - sum_up_slots
    - export

## Generated Story -5107910006725076745
* activity
    - save_conv
    - init
    - reset_slots
    - sum_up_slots
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - sum_up_slots
* disagree
    - save_conv
    - ask_what_sport
    - sum_up_slots
* activity{"sport": null}
    - slot{"sport": null}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - save_conv
    - slot{"topic": "sport"}
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - sum_up_slots
* agree
    - save_conv
    - reset_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
    - export

## Generated Story -619997790470098379
* hello
    - save_conv
    - init
    - reset_slots
    - sum_up_hello
    - sum_up_slots
    - export

## Generated Story 443237145655768818
* hello
    - save_conv
    - init
    - reset_slots
    - sum_up_hello
    - sum_up_slots

## Generated Story 7304721453901031849
* pain
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"topic": "activity"}
    - save_conv
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"requested_slot": "body_part"}
    - sum_up_slots
    - export

## Generated Story -6113055530208951106
* fallback
    - slot{"topic": "fallback"}
    - save_conv
    - init
    - reset_slots
    - sum_up_slots
    - sum_up_fallback
    - sum_up_slots
    - export

## Generated Story -3589543305838437594
* social
    - slot{"topic": "social"}
    - slot{"social": true}
    - save_conv
    - sum_up_social
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
    - export

## Generated Story 3033039389542335242
* pain{"duration": "1h", "pain_desc": "sharp", "body_part": "leg"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_desc": "sharp"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "brief"}
    - slot{"pain_change": "brief"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "brief"}
    - sum_up_slots
* agree
    - slot{"topic": "agree"}
    - save_conv
    - reset_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"pain": true}
    - action_check_intents
    - sum_up_slots
    - export

## Generated Story 7173006371563821215
* pain{"body_part": "leg", "pain_desc": "sharp", "duration": "1h"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_desc": "sharp"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - sum_up_slots
* agree
    - slot{"topic": "agree"}
    - save_conv
    - reset_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"pain": true}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "activity"}
    - sum_up_slots
* activity{"sport": "gym", "duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport": "gym"}
    - slot{"topic": "activity"}
    - save_conv
    - sum_up_slots
    - slot{"duration": null}
    - slot{"sport_duration": "1h"}
    - action_duration
    - action_check_slots_sport
    - sum_up_slots
* agree
    - slot{"topic": "agree"}
    - save_conv
    - reset_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"activity": true}
    - sum_up_slots
    - action_check_intents
    - sum_up_slots
    - export

## Generated Story -6770758355008112860
* activity{"sport": "gym", "duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport": "gym"}
    - slot{"topic": "activity"}
    - save_conv
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - sum_up_slots
* agree
    - slot{"topic": "agree"}
    - save_conv
    - reset_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"activity": true}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* pain{"pain_desc": "sharp", "duration": "1h", "body_part": "leg"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_desc": "sharp"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - sum_up_slots
* agree
    - slot{"topic": "agree"}
    - save_conv
    - reset_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"pain": true}
    - sum_up_slots
    - action_check_intents
    - sum_up_slots
    - export

## Generated Story 5701796872331960390
* activity{"duration": "1h", "sport": "gym"}
    - slot{"duration": "1h"}
    - slot{"sport": "gym"}
    - slot{"topic": "activity"}
    - save_conv
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - sum_up_slots
* agree
    - slot{"topic": "agree"}
    - save_conv
    - reset_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"activity": true}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* pain{"duration": "1h", "pain_change": "brief", "pain_desc": "sharp", "body_part": "leg"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_change": "brief"}
    - slot{"pain_desc": "sharp"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"pain_change": "brief"}
    - slot{"body_part": "leg"}
    - sum_up_slots
* agree
    - slot{"topic": "agree"}
    - save_conv
    - reset_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"pain": true}
    - sum_up_slots
    - action_check_intents
    - sum_up_slots
    - export

## Generated Story -2115513597039916089
* emotional_sadness
    - slot{"topic": "emotional_sadness"}
    - save_conv
    - sum_up_emotionnal_sadness
    - sum_up_slots
* emotional_hapiness
    - slot{"topic": "emotional_hapiness"}
    - save_conv
    - sum_up_emotional_hapiness
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* pain
    - slot{"topic": "pain"}
    - save_conv
    - action_check_slots_pain
    - slot{"requested_slot": "body_part"}
    - sum_up_slots
    - export

## Generated Story 8349435218258618584
* emotional_sadness
    - slot{"topic": "emotional_sadness"}
    - save_conv
    - sum_up_emotionnal_sadness
    - sum_up_slots
* fallback
    - slot{"topic": "fallback"}
    - save_conv
    - sum_up_fallback
    - sum_up_slots
* emotional_sadness
    - slot{"topic": "emotional_sadness"}
    - save_conv
    - sum_up_emotionnal_sadness
    - sum_up_slots
* emotional_hapiness
    - slot{"topic": "emotional_hapiness"}
    - save_conv
    - sum_up_emotional_hapiness
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Generated Story -4781252341889938497
* activity{"sport": "tennis", "duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport": "tennis"}
    - slot{"topic": "activity"}
    - save_conv
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_sport
    - slot{"sport": "tennis"}
    - sum_up_slots
    - export

## Generated Story -900667790328644784
* pain{"duration": "1h", "pain_desc": "sharp", "pain_change": "continuous", "body_part": "leg"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_change": "continuous"}
    - slot{"pain_desc": "sharp"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"pain_change": "continuous"}
    - sum_up_slots

## Generated Story -9097966225497551092
* pain{"body_part": "leg", "pain_change": "brief", "duration": "1h", "pain_desc": "shaarp"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_change": "brief"}
    - slot{"pain_desc": "shaarp"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "shaarp"}
    - slot{"pain_change": "brief"}
    - sum_up_slots
    - export

## Generated Story -5779974366969085610
* pain{"duration": "1h", "pain_desc": "shaarp", "pain_change": "brief", "body_part": "leeg"}
    - slot{"body_part": "leeg"}
    - slot{"duration": "1h"}
    - slot{"pain_change": "brief"}
    - slot{"pain_desc": "shaarp"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"pain_desc": "shaarp"}
    - slot{"pain_change": "brief"}
    - slot{"body_part": "leeg"}
    - sum_up_slots
    - export

## Generated Story 8964596689202989399
* pain{"pain_change": "brief", "pain_desc": "shaarp", "duration": "1 hoour", "body_part": "leeg"}
    - slot{"body_part": "leeg"}
    - slot{"duration": "1 hoour"}
    - slot{"pain_change": "brief"}
    - slot{"pain_desc": "shaarp"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - slot{"pain_duration": "1 hoour"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"body_part": "leeg"}
    - slot{"pain_desc": "shaarp"}
    - slot{"pain_change": "brief"}
    - sum_up_slots
* agree
    - slot{"topic": "agree"}
    - save_conv
    - sum_up_slots
    - reset_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"pain": true}
    - sum_up_slots

## Generated Story -6913950885500592107
* pain{"duration": "1h", "pain_change": "brief", "pain_desc": "sharp", "body_part": "leg"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_change": "brief"}
    - slot{"pain_desc": "sharp"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"pain_change": "brief"}
    - slot{"pain_desc": "sharp"}
    - slot{"body_part": "leg"}
    - sum_up_slots
* disagree
    - slot{"topic": "disagree"}
    - save_conv
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots
* disagree
    - slot{"topic": "disagree"}
    - save_conv
    - sum_up_slots
    - ask_what_pain
    - sum_up_slots
* pain{"pain_level": "Incorrect"}
    - slot{"pain_level": "Incorrect"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots
* pain{"pain_level": "severe"}
    - slot{"pain_level": "severe"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots
* agree
    - slot{"topic": "agree"}
    - save_conv
    - reset_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"pain": true}
    - slot{"pain_level": true}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "activity"}
    - sum_up_slots

## Generated Story -4699942532333982818
* pain{"pain_desc": "sharp", "pain_change": "brief", "body_part": "leg", "duration": "1h"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_change": "brief"}
    - slot{"pain_desc": "sharp"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"pain_change": "brief"}
    - slot{"pain_desc": "sharp"}
    - sum_up_slots
* disagree
    - slot{"topic": "disagree"}
    - save_conv
    - sum_up_slots
    - ask_what_pain
    - sum_up_slots
* pain{"pain_level": "Incorrect"}
    - slot{"pain_level": "Incorrect"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots
* pain{"pain_level": "severe"}
    - slot{"pain_level": "severe"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots
* agree
    - slot{"topic": "agree"}
    - save_conv
    - reset_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"pain": true}
    - slot{"pain_level": true}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "activity"}
    - sum_up_slots

## Generated Story 4717751032086815065
* pain{"pain_change": "brief", "pain_desc": "sharp", "duration": "1h", "body_part": "leg"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_change": "brief"}
    - slot{"pain_desc": "sharp"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"pain_change": "brief"}
    - slot{"pain_desc": "sharp"}
    - sum_up_slots
* disagree
    - slot{"topic": "disagree"}
    - save_conv
    - sum_up_slots
    - ask_what_pain
    - sum_up_slots
* pain{"pain_level": "Incorrect"}
    - slot{"pain_level": "Incorrect"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots
* pain{"pain_level": "severe"}
    - slot{"pain_level": "severe"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots
* disagree
    - slot{"topic": "disagree"}
    - save_conv
    - ask_what_pain
    - sum_up_slots
* pain{"pain_change": null}
    - slot{"pain_change": null}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - sum_up_slots
* agree
    - slot{"topic": "agree"}
    - save_conv
    - reset_slots_pain
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"pain": true}
    - slot{"pain_level": true}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "activity"}
    - sum_up_slots

## Generated Story -2068357885649084874
* pain{"pain_change": "brief", "duration": "1h", "body_part": "leg", "pain_desc": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_change": "brief"}
    - slot{"pain_desc": "sharp"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - slot{"pain_change": "brief"}
    - sum_up_slots
* disagree
    - slot{"topic": "disagree"}
    - save_conv
    - sum_up_slots
    - ask_what_pain
    - sum_up_slots
* pain{"pain_duration": null}
    - slot{"pain_duration": null}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_pain
    - sum_up_slots
* disagree
    - slot{"topic": "disagree"}
    - save_conv
    - sum_up_slots
    - ask_what_pain
    - sum_up_slots
* pain{"pain_level": "Incorrect"}
    - slot{"pain_level": "Incorrect"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots
* pain{"pain_level": "severe"}
    - slot{"pain_level": "severe"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - action_check_slots_pain
    - sum_up_slots

## Generated Story -1880632184719415000
* activity{"sport": "gym", "duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport": "gym"}
    - slot{"topic": "activity"}
    - save_conv
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - sum_up_slots
* disagree
    - slot{"topic": "disagree"}
    - save_conv
    - ask_what_sport
    - sum_up_slots
* activity{"sport_level": "Incorrect"}
    - slot{"sport_level": "Incorrect"}
    - slot{"topic": "activity"}
    - save_conv
    - sum_up_slots
    - action_check_slots_sport
    - sum_up_slots
* pain{"sport_level": "moderate"}
    - slot{"sport_level": "moderate"}
    - slot{"topic": "pain"}
    - save_conv
    - sum_up_slots
    - action_check_slots_sport
    - sum_up_slots
* agree
    - slot{"topic": "agree"}
    - save_conv
    - reset_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"activity": true}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Generated Story 3906586576574648949
* social{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"topic": "social"}
    - save_conv
    - sum_up_slots
    - slot{"duration": null}
    - action_duration
    - sum_up_fallback
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "activity"}
    - sum_up_slots

## Generated Story -5504331230297784607
* social{"period": "every day"}
    - slot{"period": "every day"}
    - slot{"topic": "social"}
    - save_conv
    - sum_up_slots
    - slot{"duration": null}
    - action_period
    - sum_up_fallback
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "activity"}
    - sum_up_slots

## Generated Story 5660479239404242272
* hello
    - slot{"topic": "hello"}
    - save_conv
    - sum_up_slots
    - sum_up_hello
    - sum_up_slots
    - export

## Generated Story -4638856733112731626
* activity{"duration": "1h", "sport": "gym"}
    - slot{"duration": "1h"}
    - slot{"sport": "gym"}
    - slot{"topic": "activity"}
    - save_conv
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "activity_hard"}
    - sum_up_slots
* activity{"activity_hard": false}
    - slot{"activity_hard": false}
    - slot{"topic": "activity"}
    - save_conv
    - action_check_slots_sport
    - slot{"activity_hard": false}
    - sum_up_slots
* agree
    - slot{"topic": "agree"}
    - save_conv
    - reset_slots_sport
    - slot{"activity_hard": null}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"activity": true}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots

## Generated Story -7443025511629933735
* activity{"sport": "gym", "duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport": "gym"}
    - slot{"topic": "activity"}
    - save_conv
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "activity_hard"}
    - sum_up_slots
* activity{"activity_hard": true}
    - slot{"activity_hard": true}
    - slot{"topic": "activity"}
    - save_conv
    - action_check_slots_sport
    - slot{"activity_hard": true}
    - sum_up_slots
* agree
    - slot{"topic": "agree"}
    - save_conv
    - reset_slots_sport
    - slot{"activity_hard": null}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"activity": true}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* activity{"sport": "gym", "duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport": "gym"}
    - slot{"topic": "activity"}
    - save_conv
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "activity_hard"}
    - sum_up_slots
* activity{"activity_hard": false}
    - slot{"activity_hard": false}
    - slot{"topic": "activity"}
    - save_conv
    - action_check_slots_sport
    - slot{"activity_hard": false}
    - sum_up_slots
* agree
    - slot{"topic": "agree"}
    - save_conv
    - reset_slots_sport
    - slot{"activity_hard": null}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"activity": true}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
* activity{"sport": "gym", "duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport": "gym"}
    - slot{"topic": "activity"}
    - save_conv
    - sum_up_slots
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "activity_hard"}
    - sum_up_slots
* activity{"activity_hard": false}
    - slot{"activity_hard": false}
    - slot{"topic": "activity"}
    - save_conv
    - action_check_slots_sport
    - slot{"activity_hard": false}
    - sum_up_slots
* disagree
    - slot{"topic": "disagree"}
    - save_conv
    - ask_what_sport
    - sum_up_slots
* activity{"activity_hard": null}
    - slot{"activity_hard": null}
    - slot{"topic": "activity"}
    - save_conv
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "activity_hard"}
    - sum_up_slots
* activity{"activity_hard": true}
    - slot{"activity_hard": true}
    - slot{"topic": "activity"}
    - save_conv
    - action_check_slots_sport
    - slot{"activity_hard": true}
    - sum_up_slots
* agree
    - slot{"topic": "agree"}
    - save_conv
    - reset_slots_sport
    - slot{"activity_hard": null}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"activity": true}
    - sum_up_slots
    - action_check_intents
    - slot{"requested_slot": "pain"}
    - sum_up_slots
    - export



