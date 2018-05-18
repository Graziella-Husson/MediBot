## Story 0
* pain
     - action_check_slots_pain
     - slot{"requested_slot": "pain_duration"}
* pain{"duration": "1h"}
     - action_duration_pain
     - action_check_slots_pain
     - slot{"pain_duration": "1h"}
     - slot{"requested_slot": "pain_level"}
* pain{"pain_level": "sharp"}
     - action_check_slots_pain
     - slot{"pain_level": "sharp"}
     - slot{"requested_slot": "body_part"}
* pain{"body_part": "leg"}
     - action_check_slots_pain
     - slot{"body_part": "leg"}
     - slot{"requested_slot": "pain_change"}
* pain{"pain_change": "continuous"}
     - action_check_slots_pain
    - slot{"pain_change": "null"}
    - slot{"pain_level": "null"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}

## Story 01
* pain{"duration": "1h"}
     - action_duration_pain

## Story 02
* activity
     - action_check_slots_sport
     - slot{"requested_slot": "sport"}
* activity{"sport":"gym"}
     - action_check_slots_sport
     - slot{"requested_slot": "sport_duration"}
* activity{"duration":"1h"}
     - action_duration_sport
     - action_check_slots_sport

## Story 03
* emotional_sadness
	- sum_up_emotionnal_sadness

## Story 04
* emotional_hapiness
	- sum_up_emotional_hapiness

## Story 05
* fallback
	- sum_up_fallback

## Generated Story 722101905010440397
* pain
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
    - action_check_slots_pain
    - slot{"requested_slot": "pain_level"}
* pain{"pain_level": "sharp"}
    - slot{"pain_level": "sharp"}
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"requested_slot": "body_part"}
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_change": "null"}
    - slot{"pain_level": "null"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"period": null}

## Generated Story -2136431400931770555
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
    - action_check_slots_pain
    - slot{"requested_slot": "pain_level"}
* pain{"pain_level": "sharp"}
    - slot{"pain_level": "sharp"}
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"requested_slot": "body_part"}
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_change": "null"}
    - slot{"pain_level": "null"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"period": null}

## Generated Story 191259154191054094
* pain{"body_part": "leg", "duration": "1h", "pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"pain_level": "sharp"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_change": "null"}
    - slot{"pain_level": "null"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"period": null}

## Generated Story 5709456383841361645
* activity
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
* activity{"sport": "gym", "duration": "1h"}
    - slot{"sport": "gym"}
    - slot{"duration": "1h"}
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
    - action_check_slots_sport
    - slot{"sport": "gym"}

## Generated Story 9221331798160448382
* pain{"body_part": "leg", "duration": "1h"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_level"}
* pain{"body_part": "knee"}
    - slot{"body_part": "knee"}
    - action_check_slots_pain
    - slot{"body_part": "knee"}
    - slot{"requested_slot": "pain_level"}
* activity{"sport": "gym", "duration": "4h"}
    - slot{"sport": "gym"}
    - slot{"duration": "4h"}
    - slot{"sport_duration": "4h"}
    - slot{"duration": null}
    - action_duration_sport
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - action_check_slots_pain
    - slot{"requested_slot": "pain_level"}
* pain{"pain_level": "sharp"}
    - slot{"pain_level": "sharp"}
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"requested_slot": "pain_change"}
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_change": "null"}
    - slot{"pain_level": "null"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"period": null}

## Generated Story 5053259330493117297
* activity{"sport": "run"}
    - slot{"sport": "run"}
    - action_check_slots_sport
    - slot{"sport": "run"}
    - slot{"requested_slot": "sport_duration"}
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
    - action_check_slots_sport
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
    - action_check_slots_pain
    - slot{"requested_slot": "pain_level"}
* pain{"pain_level": "sharp"}
    - slot{"pain_level": "sharp"}
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"requested_slot": "body_part"}
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "null"}
    - slot{"pain_level": "null"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"period": null}

## Generated Story 837279504460973062
* pain{"pain_level": "sharp"}
    - slot{"pain_level": "sharp"}
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"requested_slot": "pain_duration"}
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
    - action_check_slots_pain
    - slot{"requested_slot": "body_part"}
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_change": "null"}
    - slot{"pain_level": "null"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"period": null}

## Generated Story -7764066776472192813
* pain{"body_part": "leg", "duration": "1h", "pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_level": "sharp"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_change": "null"}
    - slot{"pain_level": "null"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"period": null}
* fallback
    - sum_up_fallback

## Generated Story -8341527311165886813
* pain{"body_part": "leg", "pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"pain_level": "sharp"}
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_duration"}
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
    - action_check_slots_pain
    - slot{"requested_slot": "pain_change"}
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_change": "null"}
    - slot{"pain_level": "null"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"period": null}

## Generated Story 785441509283062307
* pain{"duration": "1h", "pain_level": "sharp", "body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"period": null}

## Generated Story -6185495892162401337
* fallback
    - sum_up_fallback
* emotional_hapiness
    - sum_up_emotional_hapiness
* emotional_sadness
    - sum_up_emotionnal_sadness
* pain
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
* pain{"pain_level": "sharp", "duration": "1h", "body_part": "leg"}
    - slot{"pain_level": "sharp"}
    - slot{"duration": "1h"}
    - slot{"body_part": "leg"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"period": null}
* activity
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
* activity{"duration": "1h", "sport": "gym"}
    - slot{"duration": "1h"}
    - slot{"sport": "gym"}
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}

## Generated Story -5397964749154749766
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "sport_duration"}
* pain{"body_part": "leg", "pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"pain_level": "sharp"}
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_duration"}
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
    - action_check_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
* pain{"duration": "4h"}
    - slot{"duration": "4h"}
    - action_check_slots_pain
    - slot{"pain_duration": "4h"}
    - slot{"requested_slot": "pain_change"}
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"period": null}
