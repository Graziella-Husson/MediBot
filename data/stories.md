## Story 0
* pain
     - action_check_slots_pain
     - slot{"requested_slot": "pain_duration"}
     - sum_up_slots
* pain{"duration": "1h"}
     - action_duration_pain
     - action_check_slots_pain
     - slot{"pain_duration": "1h"}
     - slot{"requested_slot": "pain_level"}
     - sum_up_slots
* pain{"pain_level": "sharp"}
     - action_check_slots_pain
     - slot{"pain_level": "sharp"}
     - slot{"requested_slot": "body_part"}
     - sum_up_slots
* pain{"body_part": "leg"}
     - action_check_slots_pain
     - slot{"body_part": "leg"}
     - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
     - action_check_slots_pain
    - slot{"pain_change": "null"}
    - slot{"pain_level": "null"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
     - sum_up_slots

## Story 01
* pain{"duration": "1h"}
     - action_duration_pain
     - sum_up_slots

## Story 01bis
* pain{"period": "every day"}
     - action_period_pain
     - sum_up_slots

## Story 01ter
* activity{"period": "every day"}
     - action_period_sport
     - sum_up_slots

## Story 02
* activity
     - action_check_slots_sport
     - slot{"requested_slot": "sport"}
     - sum_up_slots
* activity{"sport":"gym"}
     - action_check_slots_sport
     - slot{"requested_slot": "sport_duration"}
     - sum_up_slots
* activity{"duration":"1h"}
     - action_duration_sport
     - action_check_slots_sport
     - sum_up_slots

## Story 03
* emotional_sadness
	- sum_up_emotionnal_sadness
     - sum_up_slots

## Story 04
* emotional_hapiness
	- sum_up_emotional_hapiness
     - sum_up_slots

## Story 05
* fallback
	- sum_up_fallback
     - sum_up_slots

## Story 06
* social
	- sum_up_social
     - sum_up_slots

## Generated Story 722101905010440397
* pain
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
     - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_level"}
     - sum_up_slots
* pain{"pain_level": "sharp"}
    - slot{"pain_level": "sharp"}
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"requested_slot": "body_part"}
     - sum_up_slots
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_change": "null"}
    - slot{"pain_level": "null"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_period": null}
     - sum_up_slots

## Generated Story -2136431400931770555
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_level"}
     - sum_up_slots
* pain{"pain_level": "sharp"}
    - slot{"pain_level": "sharp"}
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"requested_slot": "body_part"}
     - sum_up_slots
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_change": "null"}
    - slot{"pain_level": "null"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_period": null}
     - sum_up_slots

## Generated Story 191259154191054094
* pain{"body_part": "leg", "duration": "1h", "pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"pain_level": "sharp"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
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
     - sum_up_slots

## Generated Story 5709456383841361645
* activity
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
     - sum_up_slots
* activity{"sport": "gym", "duration": "1h"}
    - slot{"sport": "gym"}
    - slot{"duration": "1h"}
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
     - sum_up_slots

## Generated Story 9221331798160448382
* pain{"body_part": "leg", "duration": "1h"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_level"}
     - sum_up_slots
* pain{"body_part": "knee"}
    - slot{"body_part": "knee"}
    - action_check_slots_pain
    - slot{"body_part": "knee"}
    - slot{"requested_slot": "pain_level"}
     - sum_up_slots
* activity{"sport": "gym", "duration": "4h"}
    - slot{"sport": "gym"}
    - slot{"duration": "4h"}
    - slot{"sport_duration": "4h"}
    - slot{"duration": null}
    - action_duration_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
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
    - slot{"pain_period": null}
     - sum_up_slots

## Generated Story 5053259330493117297
* activity{"sport": "run"}
    - slot{"sport": "run"}
    - action_check_slots_sport
    - slot{"sport": "run"}
    - slot{"requested_slot": "sport_duration"}
     - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
     - sum_up_slots
    - action_check_slots_sport
     - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_level"}
     - sum_up_slots
* pain{"pain_level": "sharp"}
    - slot{"pain_level": "sharp"}
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"requested_slot": "body_part"}
     - sum_up_slots
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "null"}
    - slot{"pain_level": "null"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_period": null}
     - sum_up_slots

## Generated Story 837279504460973062
* pain{"pain_level": "sharp"}
    - slot{"pain_level": "sharp"}
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"requested_slot": "pain_duration"}
     - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "body_part"}
     - sum_up_slots
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_change": "null"}
    - slot{"pain_level": "null"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_period": null}
     - sum_up_slots

## Generated Story -7764066776472192813
* pain{"body_part": "leg", "duration": "1h", "pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_level": "sharp"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_change": "null"}
    - slot{"pain_level": "null"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_period": null}
     - sum_up_slots
* fallback
    - sum_up_fallback
     - sum_up_slots

## Generated Story -8341527311165886813
* pain{"body_part": "leg", "pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"pain_level": "sharp"}
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_duration"}
     - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_change": "null"}
    - slot{"pain_level": "null"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_period": null}
     - sum_up_slots

## Generated Story 785441509283062307
* pain{"duration": "1h", "pain_level": "sharp", "body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
     - sum_up_slots

## Generated Story -6185495892162401337
* fallback
    - sum_up_fallback
     - sum_up_slots
* emotional_hapiness
    - sum_up_emotional_hapiness
     - sum_up_slots
* emotional_sadness
    - sum_up_emotionnal_sadness
     - sum_up_slots
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
     - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
     - sum_up_slots
* activity
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
     - sum_up_slots
* activity{"duration": "1h", "sport": "gym"}
    - slot{"duration": "1h"}
    - slot{"sport": "gym"}
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
     - sum_up_slots

## Generated Story -5397964749154749766
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "sport_duration"}
     - sum_up_slots
* pain{"body_part": "leg", "pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"pain_level": "sharp"}
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_duration"}
     - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
     - sum_up_slots
* pain{"duration": "4h"}
    - slot{"duration": "4h"}
    - action_check_slots_pain
    - slot{"pain_duration": "4h"}
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
     - sum_up_slots

## Generated Story 4220756104176823679
* pain{"period": "week", "body_part": "leg"}
    - slot{"period": "week"}
    - slot{"body_part": "leg"}
    - slot{"pain_period": "week"}
    - slot{"period": null}
    - action_period_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_duration"}
     - sum_up_slots
* pain{"pain_level": "sharp", "duration": "1h"}
    - slot{"pain_level": "sharp"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
     - sum_up_slots

## Generated Story 7076041307982687244
* pain{"period": "week"}
    - slot{"period": "week"}
    - slot{"pain_period": "week"}
    - slot{"period": null}
    - action_period_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
     - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_level"}
     - sum_up_slots
* pain{"body_part": "leg", "pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"pain_level": "sharp"}
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
     - sum_up_slots

## Generated Story 4044829176005772172
* pain{"pain_level": "sharp", "duration": "1h", "period": "week"}
    - slot{"pain_level": "sharp"}
    - slot{"duration": "1h"}
    - slot{"period": "week"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - slot{"pain_period": "week"}
    - slot{"period": null}
    - action_period_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"requested_slot": "body_part"}
     - sum_up_slots
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
     - sum_up_slots

## Generated Story -3367351413203109552
* pain{"body_part": "leg", "pain_level": "sharp", "duration": "1h"}
    - slot{"body_part": "leg"}
    - slot{"pain_level": "sharp"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
     - sum_up_slots
* activity{"period": "week", "sport": "gym"}
    - slot{"period": "week"}
    - slot{"sport": "gym"}
    - slot{"sport_period": "week"}
    - slot{"period": null}
    - action_period_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "sport_duration"}
     - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
     - sum_up_slots
* fallback
    - sum_up_fallback
     - sum_up_slots

## Generated Story -5630000584122667189
* activity{"distance": "1m", "period": "week"}
    - slot{"distance": "1m"}
    - slot{"period": "week"}
    - slot{"sport_period": "week"}
    - slot{"period": null}
    - action_period_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
     - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
     - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
     - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
     - sum_up_slots

## Generated Story -9168179622117607597
* activity{"period": "week"}
    - slot{"period": "week"}
    - slot{"sport_period": "week"}
    - slot{"period": null}
    - action_period_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
     - sum_up_slots
* activity{"period": "month"}
    - slot{"period": "month"}
    - slot{"sport_period": "month"}
    - slot{"period": null}
    - action_period_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
     - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
     - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
     - sum_up_slots

## Generated Story 1641166772239024342
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_level"}
     - sum_up_slots
* activity{"duration": "4h"}
    - slot{"duration": "4h"}
    - slot{"sport_duration": "4h"}
    - slot{"duration": null}
    - action_duration_sport
     - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_level"}
     - sum_up_slots
* pain{"period": "week"}
    - slot{"period": "week"}
    - slot{"pain_period": "week"}
    - slot{"period": null}
    - action_period_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_level"}
     - sum_up_slots
* activity{"period": "month"}
    - slot{"period": "month"}
    - slot{"sport_period": "month"}
    - slot{"period": null}
    - action_period_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
     - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
     - sum_up_slots
* pain
    - action_check_slots_pain
    - slot{"requested_slot": "pain_level"}
     - sum_up_slots
* pain{"pain_level": "sharp"}
    - slot{"pain_level": "sharp"}
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"requested_slot": "body_part"}
     - sum_up_slots
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
     - sum_up_slots
    - slot{"pain_period": null}

## Generated Story -253565599840558856
* pain{"body_part": "leg", "period": "week"}
    - slot{"body_part": "leg"}
    - slot{"period": "week"}
    - slot{"pain_period": "week"}
    - slot{"period": null}
    - action_period_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_duration"}
     - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_level"}
     - sum_up_slots
* pain{"pain_level": "sharp"}
    - slot{"pain_level": "sharp"}
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
     - sum_up_slots

## Generated Story 2030766820558037114
* pain{"pain_level": "sharp", "body_part": "leg", "period": "week"}
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"period": "week"}
    - slot{"pain_period": "week"}
    - slot{"period": null}
    - action_period_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_duration"}
     - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
     - sum_up_slots
* activity{"distance": "1m", "period": "month"}
    - slot{"distance": "1m"}
    - slot{"period": "month"}
    - slot{"sport_period": "month"}
    - slot{"period": null}
    - action_period_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
     - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
     - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
     - sum_up_slots
* emotional_hapiness
    - sum_up_emotional_hapiness
     - sum_up_slots

## Generated Story 324216077116376887
* pain{"duration": "1h", "pain_level": "sharp", "period": "month", "body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_level": "sharp"}
    - slot{"period": "month"}
    - slot{"body_part": "leg"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - slot{"pain_period": "month"}
    - slot{"period": null}
    - action_period_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
     - sum_up_slots
* activity{"duration": "4h", "period": "week", "sport": "gym"}
    - slot{"duration": "4h"}
    - slot{"period": "week"}
    - slot{"sport": "gym"}
    - slot{"sport_period": "week"}
    - slot{"period": null}
    - action_period_sport
     - sum_up_slots
    - slot{"sport_duration": "4h"}
    - slot{"duration": null}
    - action_duration_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
     - sum_up_slots
* fallback
    - sum_up_fallback
     - sum_up_slots
* emotional_sadness
    - sum_up_emotionnal_sadness
     - sum_up_slots

## Generated Story -1164123198409745515
* pain{"period": "week"}
    - slot{"period": "week"}
    - slot{"pain_period": "week"}
    - slot{"period": null}
    - action_period_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
     - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"requested_slot": "pain_level"}
     - sum_up_slots
* pain{"period": "month", "pain_level": "sharp"}
    - slot{"period": "month"}
    - slot{"pain_level": "sharp"}
    - slot{"pain_period": "month"}
    - slot{"period": null}
    - action_period_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"requested_slot": "body_part"}
     - sum_up_slots
* pain{"body_part": "leg", "pain_level": "horrible"}
    - slot{"body_part": "leg"}
    - slot{"pain_level": "horrible"}
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"pain_level": "horrible"}
    - slot{"requested_slot": "pain_change"}
     - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
     - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "sport_duration"}
     - sum_up_slots
* activity{"period": "month"}
    - slot{"period": "month"}
    - slot{"sport_period": "month"}
    - slot{"period": null}
    - action_period_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
     - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
     - sum_up_slots
* fallback
    - sum_up_fallback
     - sum_up_slots

## Generated Story -2769106415451194898
* activity{"distance": "1m", "period": "week"}
    - slot{"distance": "1m"}
    - slot{"period": "week"}
    - slot{"sport_period": "week"}
    - slot{"period": null}
    - action_period_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
     - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
     - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - action_check_slots_sport
     - sum_up_slots

## Generated Story 5066745705215134412
* activity{"period": "week", "duration": "1h"}
    - slot{"period": "week"}
    - slot{"duration": "1h"}
    - slot{"sport_period": "week"}
    - slot{"period": null}
    - action_period_sport
     - sum_up_slots
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
     - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
     - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
     - sum_up_slots
* pain{"period": "week", "duration": "1h", "pain_change": "continuous", "body_part": "leg", "pain_level": "sharp"}
    - slot{"period": "week"}
    - slot{"duration": "1h"}
    - slot{"pain_change": "continuous"}
    - slot{"body_part": "leg"}
    - slot{"pain_level": "sharp"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
     - sum_up_slots
    - slot{"pain_period": "week"}
    - slot{"period": null}
    - action_period_pain
     - sum_up_slots
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
     - sum_up_slots

## Generated Story -6506308330820466453
* pain
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* pain{"body_part": "leg", "duration": "1h"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_duration_pain
    - sum_up_slots
    - action_check_slots_pain
    - slot{"body_part": "leg"}
    - slot{"requested_slot": "pain_level"}
    - sum_up_slots
* pain{"pain_level": "sharp"}
    - slot{"pain_level": "sharp"}
    - action_check_slots_pain
    - slot{"pain_level": "sharp"}
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_duration": null}
    - slot{"pain_level": null}
    - slot{"body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - sum_up_slots

## Generated Story -3443672156825314135
* activity
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - sum_up_slots

## Generated Story 5123775614961870568
* activity
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* activity{"duration": "1h", "sport": "gym"}
    - slot{"duration": "1h"}
    - slot{"sport": "gym"}
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
* social
    - sum_up_social
    - sum_up_slots
* fallback
    - sum_up_fallback
    - sum_up_slots

## Generated Story -5973619435568715613
* activity{"duration": "3 hours", "sport": "ran"}
    - slot{"duration": "3 hours"}
    - slot{"sport": "ran"}
    - slot{"sport_duration": "3 hours"}
    - slot{"duration": null}
    - action_duration_sport
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "ran"}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
* fallback
    - sum_up_fallback
    - sum_up_slots

## Generated Story -5907892820628899883
* activity
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
    - sum_up_slots
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots
* activity{"sport": "run"}
    - slot{"sport": "run"}
    - action_check_slots_sport
    - slot{"sport": "run"}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - sum_up_slots

## Generated Story -2025036746559240685
* activity
    - action_check_slots_sport
    - slot{"requested_slot": "sport_duration"}
    - sum_up_slots
* activity{"sport": "gym", "duration": "1h"}
    - slot{"sport": "gym"}
    - slot{"duration": "1h"}
    - slot{"sport_duration": "1h"}
    - slot{"duration": null}
    - action_duration_sport
    - sum_up_slots
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"sport_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"sport_period": null}
    - sum_up_slots
* social
    - sum_up_social
    - sum_up_slots
