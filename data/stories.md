## Story 01
* hello
	- save_conv
	- sum_up_hello
	- sum_up_slots

## Generated Story 3306727126556356367
* pain
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", " social"]}
    - slot{"current_session": 3}
    - save_conv
    - slot{"topic": "pain"}
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
* pain{"pain_desc": "sharp"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - save_conv
    - slot{"topic": "pain"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_multiple_set_complex
    - action_check_slots_pain
    - slot{"requested_slot": "pain_body_part"}
    - sum_up_slots
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"pain_body_part": "leg"}
    - slot{"body_part": null}
    - action_multiple_set_complex
    - action_check_slots_pain
    - sum_up_slots
    - export

## Generated Story -1168929800633690446
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", " social"]}
    - slot{"current_session": 3}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_multiple_set_complex
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
* pain{"body_part": "leg", "pain_desc": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"pain_body_part": "leg"}
    - slot{"body_part": null}
    - action_multiple_set_complex
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - save_conv
    - slot{"topic": "pain"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - sum_up_slots
    - export

## Generated Story 6452676939433106071
* activity
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", " social"]}
    - slot{"current_session": 3}
    - save_conv
    - slot{"topic": "activity"}
    - action_check_slots_sport
    - slot{"requested_slot": "activity_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "activity"}
    - slot{"activity_duration": "1h"}
    - slot{"duration": null}
    - action_multiple_set_complex
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - save_conv
    - slot{"topic": "activity"}
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "activity_hard"}
    - sum_up_slots
* activity{"activity_hard": true}
    - slot{"activity_hard": true}
    - save_conv
    - slot{"topic": "activity"}
    - action_check_slots_sport
    - slot{"activity_hard": true}
    - sum_up_slots
    - export

## Generated Story 4679001957397524705
* pain
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", "social"]}
    - slot{"current_session": 1}
    - save_conv
    - slot{"topic": "pain"}
    - action_check_slots_pain
    - slot{"requested_slot": "pain_period"}
    - sum_up_slots
* pain{"period": "every day"}
    - slot{"period": "every day"}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"pain_period": "every day"}
    - slot{"duration": null}
    - action_multiple_set_complex
    - action_check_slots_pain
    - slot{"requested_slot": "pain_body_part"}
    - sum_up_slots
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"pain_body_part": "leg"}
    - slot{"body_part": null}
    - action_multiple_set_complex
    - action_check_slots_pain
    - slot{"requested_slot": "pain_time"}
    - sum_up_slots
* pain{"time": "yesterday"}
    - slot{"time": "yesterday"}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"pain_time": "yesterday"}
    - slot{"time": null}
    - action_multiple_set_complex
    - action_check_slots_pain
    - slot{"requested_slot": "pain_change"}
    - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - save_conv
    - slot{"topic": "pain"}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots
* pain{"pain_desc": "sharp"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "pain_duration"}
    - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - action_multiple_set_complex
    - action_check_slots_pain
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - reset_slots_pain
    - slot{"global_score": null}
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"pain_body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"pain_time": null}
    - slot{"pain": true}
    - slot{"pain_level": null}
    - sum_up_slots
    - export

## Generated Story -7280469206889209180
* activity
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", "social"]}
    - slot{"current_session": 1}
    - save_conv
    - slot{"topic": "activity"}
    - action_check_slots_sport
    - slot{"requested_slot": "activity_period"}
    - sum_up_slots
* activity{"period": "every day"}
    - slot{"period": "every day"}
    - save_conv
    - slot{"topic": "activity"}
    - slot{"activity_period": "every day"}
    - slot{"duration": null}
    - action_multiple_set_complex
    - action_check_slots_sport
    - slot{"requested_slot": "activity_duration"}
    - sum_up_slots
* activity
    - save_conv
    - slot{"topic": "activity"}
    - action_check_slots_sport
    - slot{"requested_slot": "activity_hard"}
    - sum_up_slots
* activity{"activity_hard": true}
    - slot{"activity_hard": true}
    - save_conv
    - slot{"topic": "activity"}
    - action_check_slots_sport
    - slot{"activity_hard": true}
    - slot{"requested_slot": "activity_duration"}
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "activity"}
    - slot{"activity_duration": "1h"}
    - slot{"duration": null}
    - action_multiple_set_complex
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - save_conv
    - slot{"topic": "activity"}
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "activity_time"}
    - sum_up_slots
* activity{"time": "yesterday"}
    - slot{"time": "yesterday"}
    - save_conv
    - slot{"topic": "activity"}
    - slot{"activity_time": "yesterday"}
    - slot{"time": null}
    - action_multiple_set_complex
    - action_check_slots_sport
    - slot{"requested_slot": "activity_distance"}
    - sum_up_slots
* activity{"distance": "1m"}
    - slot{"distance": "1m"}
    - save_conv
    - slot{"topic": "activity"}
    - slot{"activity_distance": "1m"}
    - slot{"duration": null}
    - action_multiple_set_complex
    - action_check_slots_sport
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - reset_slots_sport
    - slot{"global_score": null}
    - slot{"activity_hard": null}
    - slot{"activity_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"distance": null}
    - slot{"activity_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"activity": true}
    - sum_up_slots
    - export

## Generated Story 7855577861615697664
* social
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", "social"]}
    - slot{"current_session": 1}
    - save_conv
    - slot{"topic": "social"}
    - sum_up_social
    - sum_up_slots
    - export

## Generated Story 1343543725078416549
* emotional_sadness
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", "social"]}
    - slot{"current_session": 1}
    - save_conv
    - slot{"topic": "emotional_sadness"}
    - sum_up_emotionnal_sadness
    - sum_up_slots
    - export

## Generated Story 5085525489100949534
* emotional_hapiness
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", "social"]}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "emotional_hapiness"}
    - sum_up_emotional_hapiness
    - sum_up_slots
    - export

## Generated Story 5596269372817250986
* pathology
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", "social"]}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "pathology"}
    - sum_up_pathology
    - slot{"requested_slot": "symtoms"}
    - sum_up_slots
* pathology{"symtoms": "erupt"}
    - slot{"symtoms": "erupt"}
    - save_conv
    - slot{"topic": "pathology"}
    - sum_up_pathology
    - slot{"symtoms": "erupt"}
    - slot{"requested_slot": "pathology_body_part"}
    - sum_up_slots
* pathology{"pathology_body_part": "leg"}
    - slot{"pathology_body_part": "leg"}
    - save_conv
    - slot{"topic": "pathology"}
    - sum_up_pathology
    - slot{"pathology_body_part": "leg"}
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - reset_slots_pathology
    - slot{"global_score": 1}
    - slot{"symtoms": null}
    - slot{"pathology_body_part": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"pathology": true}
    - sum_up_slots
    - export

## Generated Story -1875339855644612428
* treatment
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", "social"]}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "treatment"}
    - sum_up_treatment
    - slot{"requested_slot": "medicinal"}
    - sum_up_slots
* treatment{"medicinal": true}
    - slot{"medicinal": true}
    - save_conv
    - slot{"topic": "treatment"}
    - sum_up_treatment
    - slot{"medicinal": true}
    - slot{"requested_slot": "drug"}
    - sum_up_slots
* treatment{"drug": "drug"}
    - slot{"drug": "drug"}
    - save_conv
    - slot{"topic": "treatment"}
    - sum_up_treatment
    - slot{"drug": "drug"}
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - reset_slots_treatment
    - slot{"global_score": 2}
    - slot{"drug": null}
    - slot{"medicinal": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"treatment": true}
    - sum_up_slots
    - export

## Generated Story -207725796308030161
* infoPatient
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", "social"]}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "infoPatient"}
    - sum_up_info_patient
    - slot{"requested_slot": "infoPatient_distance"}
    - sum_up_slots
* infoPatient{"time": "yesterday"}
    - slot{"time": "yesterday"}
    - save_conv
    - slot{"topic": "infoPatient"}
    - slot{"infoPatient_distance": "yesterday"}
    - slot{"time": null}
    - action_multiple_set_complex
    - sum_up_info_patient
    - slot{"requested_slot": "temperature"}
    - sum_up_slots
* infoPatient{"temperature": "38c"}
    - slot{"temperature": "38c"}
    - save_conv
    - slot{"topic": "infoPatient"}
    - sum_up_info_patient
    - slot{"temperature": "38c"}
    - slot{"requested_slot": "infoPatient_distance"}
    - sum_up_slots
* infoPatient{"distance": "160cm"}
    - slot{"distance": "160cm"}
    - save_conv
    - slot{"topic": "infoPatient"}
    - slot{"infoPatient_distance": "160cm"}
    - slot{"duration": null}
    - action_multiple_set_complex
    - sum_up_info_patient
    - slot{"requested_slot": "blood_pressure"}
    - sum_up_slots
* infoPatient{"blood_pressure": "high"}
    - slot{"blood_pressure": "high"}
    - save_conv
    - slot{"topic": "infoPatient"}
    - sum_up_info_patient
    - slot{"blood_pressure": "high"}
    - slot{"requested_slot": "addiction"}
    - sum_up_slots
* infoPatient{"addiction": "cigarette"}
    - slot{"addiction": "cigarette"}
    - save_conv
    - slot{"topic": "infoPatient"}
    - sum_up_info_patient
    - slot{"addiction": "cigarette"}
    - slot{"requested_slot": "heart_rate"}
    - sum_up_slots
* infoPatient{"heart_rate": "high"}
    - slot{"heart_rate": "high"}
    - save_conv
    - slot{"topic": "infoPatient"}
    - sum_up_info_patient
    - slot{"heart_rate": "high"}
    - slot{"requested_slot": "weight"}
    - sum_up_slots
* infoPatient{"weight": "80kg"}
    - slot{"weight": "80kg"}
    - save_conv
    - slot{"topic": "infoPatient"}
    - sum_up_info_patient
    - slot{"weight": "80kg"}
    - slot{"requested_slot": "gender"}
    - sum_up_slots
* infoPatient{"gender": "woman"}
    - slot{"gender": "woman"}
    - save_conv
    - slot{"topic": "infoPatient"}
    - sum_up_info_patient
    - slot{"gender": "woman"}
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - reset_slots_info_patient
    - slot{"addiction": null}
    - slot{"weight": null}
    - slot{"infoPatient_distance": null}
    - slot{"temperature": null}
    - slot{"blood_pressure": null}
    - slot{"heart_rate": null}
    - slot{"infoPatient_distance": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"infoPatient": true}
    - sum_up_slots
    - export

## Generated Story 5403296936906036569
* pathology
    - save_conv
    - slot{"topic": "pathology"}
    - sum_up_pathology
    - slot{"requested_slot": "pathology_body_part"}
    - sum_up_slots
* pathology{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"pathology_body_part": "leg"}
    - slot{"body_part": null}
    - action_multiple_set_complex
    - sum_up_pathology
    - slot{"requested_slot": "symtoms"}
    - sum_up_slots
* pathology{"symtoms": "erupt"}
    - slot{"symtoms": "erupt"}
    - save_conv
    - slot{"topic": "pathology"}
    - sum_up_pathology
    - slot{"symtoms": "erupt"}
    - sum_up_slots
* disagree
    - save_conv
    - slot{"topic": "disagree"}
    - ask_what_pathology
    - sum_up_slots
* pathology{"pathology_body_part": null}
    - slot{"pathology_body_part": null}
    - save_conv
    - slot{"topic": "pathology"}
    - sum_up_pathology
    - slot{"requested_slot": "pathology_body_part"}
    - sum_up_slots
* pathology{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"pathology_body_part": "leg"}
    - slot{"body_part": null}
    - action_multiple_set_complex
    - sum_up_pathology
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - reset_slots_pathology
    - slot{"global_score": 1}
    - slot{"symtoms": null}
    - slot{"pathology_body_part": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"pathology": true}
    - sum_up_slots
    - export

## Generated Story -1504926829070170944
* treatment
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", "social"]}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "treatment"}
    - sum_up_treatment
    - slot{"requested_slot": "medicinal"}
    - sum_up_slots
* treatment{"medicinal": true}
    - slot{"medicinal": true}
    - save_conv
    - slot{"topic": "treatment"}
    - sum_up_treatment
    - slot{"medicinal": true}
    - slot{"requested_slot": "drug"}
    - sum_up_slots
* treatment{"drug": "drug"}
    - slot{"drug": "drug"}
    - save_conv
    - slot{"topic": "treatment"}
    - sum_up_treatment
    - slot{"drug": "drug"}
    - sum_up_slots
* disagree
    - save_conv
    - slot{"topic": "disagree"}
    - ask_what_treatment
    - sum_up_slots
* treatment{"medicinal": false, "drug": "no_drug"}
    - slot{"drug": "no_drug"}
    - slot{"medicinal": false}
    - save_conv
    - slot{"topic": "treatment"}
    - sum_up_treatment
    - slot{"drug": "no_drug"}
    - slot{"medicinal": false}
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - reset_slots_treatment
    - slot{"global_score": 2}
    - slot{"medicinal": null}
    - slot{"drug": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"treatment": true}
    - sum_up_slots
    - export

## Generated Story -6499246815192630439
* infoPatient{"blood_pressure": "high", "addiction": "cigarette", "weight": "80kg", "time": "yesterday", "gender": "woman", "temperature": "high"}
    - slot{"addiction": "cigarette"}
    - slot{"blood_pressure": "high"}
    - slot{"gender": "woman"}
    - slot{"temperature": "high"}
    - slot{"time": "yesterday"}
    - slot{"weight": "80kg"}
    - save_conv
    - slot{"topic": "infoPatient"}
    - slot{"infoPatient_distance": "yesterday"}
    - slot{"time": null}
    - action_multiple_set_complex
    - sum_up_info_patient
    - slot{"addiction": "cigarette"}
    - slot{"gender": "woman"}
    - slot{"weight": "80kg"}
    - slot{"blood_pressure": "high"}
    - slot{"temperature": "high"}
    - slot{"requested_slot": "heart_rate"}
    - sum_up_slots
* infoPatient{"heart_rate": "high"}
    - slot{"heart_rate": "high"}
    - save_conv
    - slot{"topic": "infoPatient"}
    - sum_up_info_patient
    - slot{"heart_rate": "high"}
    - slot{"requested_slot": "infoPatient_distance"}
    - sum_up_slots
* infoPatient{"distance": "160cm"}
    - slot{"distance": "160cm"}
    - save_conv
    - slot{"topic": "infoPatient"}
    - slot{"infoPatient_distance": "160cm"}
    - slot{"distance": null}
    - action_multiple_set_complex
    - sum_up_info_patient
    - sum_up_slots
* disagree
    - save_conv
    - slot{"topic": "disagree"}
    - ask_what_info_patient
    - sum_up_slots
* infoPatient{"addiction": null}
    - slot{"addiction": null}
    - save_conv
    - slot{"topic": "infoPatient"}
    - sum_up_info_patient
    - slot{"requested_slot": "addiction"}
    - sum_up_slots
* infoPatient{"addiction": "cigarette"}
    - slot{"addiction": "cigarette"}
    - save_conv
    - slot{"topic": "infoPatient"}
    - sum_up_info_patient
    - slot{"addiction": "cigarette"}
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - reset_slots_info_patient
    - slot{"addiction": null}
    - slot{"weight": null}
    - slot{"infoPatient_distance": null}
    - slot{"gender": null}
    - slot{"temperature": null}
    - slot{"heart_rate": null}
    - slot{"blood_pressure": null}
    - slot{"infoPatient_distance": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"infoPatient": true}
    - sum_up_slots

## Generated Story -1043421889474253187
* pain{"period": "every day", "time": "yesterday", "duration": "1h", "body_part": "leg"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"period": "every day"}
    - slot{"time": "yesterday"}
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", "social"]}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"pain_time": "yesterday"}
    - slot{"time": null}
    - slot{"pain_body_part": "leg"}
    - slot{"body_part": null}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - slot{"pain_period": "every day"}
    - slot{"period": null}
    - action_multiple_set_complex
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - sum_up_slots

## Generated Story -4517094345874675222
* activity{"time": "yesterday", "period": "every day", "distance": "1km", "duration": "1h"}
    - slot{"distance": "1km"}
    - slot{"duration": "1h"}
    - slot{"period": "every day"}
    - slot{"time": "yesterday"}
    - save_conv
    - slot{"topic": "activity"}
    - slot{"activity_time": "yesterday"}
    - slot{"time": null}
    - slot{"activity_distance": "1km"}
    - slot{"distance": null}
    - slot{"activity_duration": "1h"}
    - slot{"duration": null}
    - slot{"activity_period": "every day"}
    - slot{"period": null}
    - action_multiple_set_complex
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots

## Generated Story 2194076682910950593
* pain{"body_part": "leg", "pain_duration": "1h", "period": "every day", "time": "yesterday", "pain_desc": "sharp"}
    - slot{"body_part": "leg"}
    - slot{"pain_desc": "sharp"}
    - slot{"pain_duration": "1h"}
    - slot{"period": "every day"}
    - slot{"time": "yesterday"}
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness"]}
    - slot{"current_session": 2}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"pain_time": "yesterday"}
    - slot{"time": null}
    - slot{"pain_body_part": "leg"}
    - slot{"body_part": null}
    - slot{"pain_period": "every day"}
    - slot{"period": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - reset_slots_pain
    - slot{"global_score": 0}
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"pain_body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"pain_time": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"pain": true}
    - slot{"pain_level": null}
    - sum_up_slots
* activity
    - save_conv
    - slot{"topic": "activity"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - sum_up_slots
* activity{"sport": "gym", "duration": "1h", "period": "every day", "time": "yesterday", "distance": "1km"}
    - slot{"distance": "1km"}
    - slot{"duration": "1h"}
    - slot{"period": "every day"}
    - slot{"sport": "gym"}
    - slot{"time": "yesterday"}
    - save_conv
    - slot{"topic": "activity"}
    - slot{"activity_time": "yesterday"}
    - slot{"time": null}
    - slot{"activity_distance": "1km"}
    - slot{"distance": null}
    - slot{"activity_duration": "1h"}
    - slot{"duration": null}
    - slot{"activity_period": "every day"}
    - slot{"period": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "activity_hard"}
    - sum_up_slots
* activity{"activity_hard": true}
    - slot{"activity_hard": true}
    - save_conv
    - slot{"topic": "activity"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - action_check_slots_sport
    - slot{"activity_hard": true}
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - reset_slots_sport
    - slot{"global_score": 0}
    - slot{"activity_hard": null}
    - slot{"activity_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"activity_distance": null}
    - slot{"activity_period": null}
    - slot{"activity_time": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"activity": true}
    - sum_up_slots
* pathology{"symtoms": "erupt"}
    - slot{"symtoms": "erupt"}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_pathology
    - sum_up_slots
    - export

## Generated Story 7598399040769412982
* pathology
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", "social"]}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - sum_up_pathology
    - slot{"requested_slot": "pathology_body_part"}
    - sum_up_slots
* pain
    - save_conv
    - slot{"topic": "pain"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - action_check_slots_pain
    - slot{"requested_slot": "pain_period"}
    - sum_up_slots
    - export

## Generated Story 7943145471150607596
* pain
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", "social"]}
    - slot{"language": "fr"}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"time": null}
    - action_check_slots_pain
    - slot{"requested_slot": "pain_change"}
    - utter_ask_pain_change
* activity
    - save_conv
    - slot{"topic": "activity"}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"time": null}
    - action_check_slots_sport
    - slot{"requested_slot": "activity_time"}
    - utter_ask_activity_time
    - sum_up_slots
* pain
    - save_conv
    - slot{"topic": "pain"}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"time": null}
    - action_check_slots_pain
    - slot{"requested_slot": "pain_time"}
    - utter_ask_pain_time
    - sum_up_slots
* social
    - save_conv
    - slot{"topic": "social"}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"time": null}
    - sum_up_social
    - sum_up_slots
    - export

## Generated Story -884436195164616062
* activity
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", "social"]}
    - slot{"language": "fr"}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "activity"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - action_check_slots_sport
    - slot{"requested_slot": "activity_duration"}
    - utter_ask_activity_duration
    - sum_up_slots
* activity{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "activity"}
    - slot{"activity_duration": "1h"}
    - slot{"duration": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - action_check_slots_sport
    - slot{"requested_slot": "sport"}
    - utter_ask_sport
    - sum_up_slots
* activity{"sport": "gym"}
    - slot{"sport": "gym"}
    - save_conv
    - slot{"topic": "activity"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"requested_slot": "activity_period"}
    - utter_ask_activity_period
    - sum_up_slots
* activity{"period": "every day"}
    - slot{"period": "every day"}
    - save_conv
    - slot{"topic": "activiy"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - slot{"activity_period": "every day"}
    - slot{"period": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - action_check_slots_sport
    - slot{"requested_slot": "activity_hard"}
    - utter_ask_activity_hard
    - sum_up_slots
* activity{"activity_hard": true}
    - slot{"activity_hard": true}
    - save_conv
    - slot{"topic": "activity"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - action_check_slots_sport
    - slot{"activity_hard": true}
    - slot{"requested_slot": "activity_time"}
    - utter_ask_activity_time
    - sum_up_slots
* activity{"time": "yesterday"}
    - slot{"time": "yesterday"}
    - save_conv
    - slot{"topic": "activity"}
    - slot{"activity_time": "yesterday"}
    - slot{"time": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - action_check_slots_sport
    - slot{"requested_slot": "activity_distance"}
    - utter_ask_activity_distance
    - sum_up_slots
* activity{"distance": "1km"}
    - slot{"distance": "1km"}
    - save_conv
    - slot{"topic": "activity"}
    - slot{"activity_distance": "1km"}
    - slot{"distance": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - action_check_slots_sport
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - reset_slots_sport
    - slot{"global_score": 0}
    - slot{"activity_hard": null}
    - slot{"activity_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"activity_distance": null}
    - slot{"activity_period": null}
    - slot{"activity_time": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"activity": true}
    - sum_up_slots
* pain
    - save_conv
    - slot{"topic": "pain"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - utter_ask_pain_desc
    - sum_up_slots
* pain{"pain_desc": "sharp"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - slot{"requested_slot": "pain_period"}
    - utter_ask_pain_period
    - sum_up_slots
* pain{"period": "every day"}
    - slot{"period": "every day"}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - action_check_slots_pain
    - slot{"requested_slot": "pain_time"}
    - utter_ask_pain_time
    - sum_up_slots
* pain{"time": "yesterday"}
    - slot{"time": "yesterday"}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"pain_time": "yesterday"}
    - slot{"time": null}
    - slot{"pain_period": "every day"}
    - slot{"period": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - action_check_slots_pain
    - slot{"requested_slot": "pain_change"}
    - utter_ask_pain_change
    - sum_up_slots
* pain{"pain_change": "continuous"}
    - slot{"pain_change": "continuous"}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"requested_slot": "pain_duration"}
    - utter_ask_pain_duration
    - sum_up_slots
* pain
    - save_conv
    - slot{"topic": "pain"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - action_check_slots_pain
    - slot{"requested_slot": "pain_duration"}
    - utter_ask_pain_duration
    - sum_up_slots
* pain{"duration": "1h"}
    - slot{"duration": "1h"}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - action_check_slots_pain
    - slot{"requested_slot": "pain_body_part"}
    - utter_ask_pain_body_part
    - sum_up_slots
* pain{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - slot{"pain_body_part": "leg"}
    - slot{"body_part": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - action_check_slots_pain
    - sum_up_slots
* disagree
    - save_conv
    - slot{"topic": "disagree"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - ask_what_pain
    - sum_up_slots
* pain{"pain_desc": null}
    - slot{"pain_desc": null}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - utter_ask_pain_desc
    - sum_up_slots
* pain{"pain_desc": "sharp"}
    - slot{"pain_desc": "sharp"}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - action_check_slots_pain
    - slot{"pain_desc": "sharp"}
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - reset_slots_pain
    - slot{"global_score": 0}
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"pain_body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"pain_time": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"pain": true}
    - slot{"pain_level": null}
    - sum_up_slots
* social
    - save_conv
    - slot{"topic": "social"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - sum_up_social
    - sum_up_slots
* emotional_sadness
    - save_conv
    - slot{"topic": "emotional_sadness"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - sum_up_emotionnal_sadness
    - sum_up_slots
    - export

## Generated Story -159933520263136298
* pain{"time": "yesterday", "pain_desc": "sharp", "body_part": "leg", "duration": "1h", "period": "every day", "pain_change": "continuous"}
    - slot{"body_part": "leg"}
    - slot{"duration": "1h"}
    - slot{"pain_change": "continuous"}
    - slot{"pain_desc": "sharp"}
    - slot{"period": "every day"}
    - slot{"time": "yesterday"}
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", "social"]}
    - slot{"language": "fr"}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"pain_time": "yesterday"}
    - slot{"time": null}
    - slot{"pain_body_part": "leg"}
    - slot{"body_part": null}
    - slot{"pain_duration": "1h"}
    - slot{"duration": null}
    - slot{"pain_period": "every day"}
    - slot{"period": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - action_check_slots_pain
    - slot{"pain_change": "continuous"}
    - slot{"pain_desc": "sharp"}
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"time": null}
    - reset_slots_pain
    - slot{"global_score": 0}
    - slot{"pain_duration": null}
    - slot{"pain_desc": null}
    - slot{"pain_body_part": null}
    - slot{"pain_change": null}
    - slot{"pain_period": null}
    - slot{"pain_time": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"pain": true}
    - slot{"pain_level": null}
    - sum_up_slots
    - export

## Generated Story 2263343696262618051
* activity{"distance": "1km", "period": "every day", "sport": "gym", "duration": "1h", "activity_hard": true, "time": "yesterday"}
    - slot{"activity_hard": true}
    - slot{"distance": "1km"}
    - slot{"duration": "1h"}
    - slot{"period": "every day"}
    - slot{"sport": "gym"}
    - slot{"time": "yesterday"}
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["emotional_sadness", "social"]}
    - slot{"language": "fr"}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "activity"}
    - slot{"activity_time": "yesterday"}
    - slot{"time": null}
    - slot{"activity_distance": "1km"}
    - slot{"distance": null}
    - slot{"activity_duration": "1h"}
    - slot{"duration": null}
    - slot{"activity_period": "every day"}
    - slot{"period": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - action_check_slots_sport
    - slot{"sport": "gym"}
    - slot{"activity_hard": true}
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"time": null}
    - reset_slots_sport
    - slot{"global_score": 0}
    - slot{"activity_hard": null}
    - slot{"activity_duration": null}
    - slot{"sport_level": null}
    - slot{"sport": null}
    - slot{"activity_distance": null}
    - slot{"activity_period": null}
    - slot{"activity_time": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"activity": true}
    - sum_up_slots
    - export

## Generated Story -7589975809010727540
* pain
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["activity"]}
    - slot{"language": "en"}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "pain"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - action_check_slots_pain
    - slot{"requested_slot": "pain_desc"}
    - utter_ask_pain_desc
    - sum_up_slots
    - export

##change_session_reminder
	- change_session_reminder
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": ["activity"]}
    - slot{"language": "en"}
    - slot{"current_session": 2}
    - slot{"global_score": 0}
    - sum_up_slots
* emotional_sadness
    - save_conv
    - slot{"topic": "emotional_sadness"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - sum_up_emotionnal_sadness
    - sum_up_slots
    - export

##user_reminder
	- user_reminder
	- slot{"count_user_reminder":1}
    - sum_up_slots
* emotional_sadness
    - save_conv
    - slot{"topic": "emotional_sadness"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - sum_up_emotionnal_sadness
    - sum_up_slots

##session_end_reminder
    - session_end_reminder
    - sum_up_slots
* emotional_sadness
    - save_conv
    - slot{"topic": "emotional_sadness"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - sum_up_emotionnal_sadness
    - sum_up_slots

##user_reminder_little
	- user_reminder_little
    - sum_up_slots
* emotional_sadness
    - save_conv
    - slot{"topic": "emotional_sadness"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - sum_up_emotionnal_sadness
    - sum_up_slots

## followed_intent_reminder
	- followed_intent_reminder
    - sum_up_slots
* emotional_sadness
    - save_conv
    - slot{"topic": "emotional_sadness"}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"duration": null}
    - slot{"time": null}
    - sum_up_emotionnal_sadness
    - sum_up_slots

## Generated Story 3907304576003883024
* pathology
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": []}
    - slot{"language": "fr"}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"duration": null}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_pathology
    - slot{"requested_slot": "pathology_period"}
    - utter_ask_pathology_period
    - sum_up_slots
* pathology{"period": "every day"}
    - slot{"period": "every day"}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"duration": null}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"time": null}
    - slot{"pathology_period": "every day"}
    - slot{"period": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - sum_up_pathology
    - slot{"requested_slot": "pathology_body_part"}
    - utter_ask_pathology_body_part
    - sum_up_slots
* pathology{"body_part": "leg"}
    - slot{"body_part": "leg"}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"duration": null}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"time": null}
    - slot{"pathology_body_part": "leg"}
    - slot{"body_part": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - sum_up_pathology
    - slot{"requested_slot": "symtoms"}
    - utter_ask_symtoms
    - sum_up_slots
* pathology{"symtoms": "test"}
    - slot{"symtoms": "test"}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"duration": null}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_pathology
    - slot{"symtoms": "test"}
    - slot{"requested_slot": "pathology_time"}
    - utter_ask_pathology_time
    - sum_up_slots
* pathology{"time": "yesterday"}
    - slot{"time": "yesterday"}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"pathology_time": "yesterday"}
    - slot{"time": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - sum_up_pathology
    - slot{"requested_slot": "pathology_treatment_linked"}
    - utter_ask_pathology_treatment_linked
    - sum_up_slots
* pathology{"pathology_treatment_linked": true}
    - slot{"pathology_treatment_linked": true}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"duration": null}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_pathology
    - slot{"pathology_treatment_linked": true}
    - slot{"requested_slot": "pathology_change"}
    - utter_ask_pathology_change
    - sum_up_slots
* pathology{"pathology_change": true}
    - slot{"pathology_change": true}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"duration": null}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_pathology
    - slot{"pathology_change": true}
    - sum_up_slots
    - export

## Generated Story -1371737913548953694
* pathology
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": []}
    - slot{"language": "fr"}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"time": null}
    - sum_up_pathology
    - slot{"requested_slot": "pathology_treatment_linked"}
    - utter_ask_pathology_treatment_linked
    - sum_up_slots
* pathology{"pathology_treatment_linked": true}
    - slot{"pathology_treatment_linked": true}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"time": null}
    - sum_up_pathology
    - slot{"pathology_treatment_linked": true}
    - slot{"requested_slot": "symtoms"}
    - utter_ask_symtoms
    - sum_up_slots
* pathology{"symtoms": "test", "body_part": "leg", "period": "every day", "time": "yesterday"}
    - slot{"body_part": "leg"}
    - slot{"period": "every day"}
    - slot{"symtoms": "test"}
    - slot{"time": "yesterday"}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"pathology_time": "yesterday"}
    - slot{"time": null}
    - slot{"pathology_body_part": "leg"}
    - slot{"body_part": null}
    - slot{"pathology_period": "every day"}
    - slot{"period": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - sum_up_pathology
    - slot{"symtoms": "test"}
    - slot{"requested_slot": "pathology_change"}
    - utter_ask_pathology_change
    - sum_up_slots
* pathology{"pathology_change": true}
    - slot{"pathology_change": true}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"time": null}
    - sum_up_pathology
    - slot{"pathology_change": true}
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"time": null}
    - reset_slots_pathology
    - slot{"global_score": 1}
    - slot{"symtoms": null}
    - slot{"pathology_body_part": null}
    - slot{"pathology_time": null}
    - slot{"pathology_change": null}
    - slot{"pathology_period": null}
    - slot{"pathology_treatment_linked": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"pathology": true}
    - sum_up_slots
    - export

## Generated Story 1994290313936740529
* pathology{"period": "every day", "time": "yesterday", "body_part": "leg"}
    - slot{"body_part": "leg"}
    - slot{"period": "every day"}
    - slot{"time": "yesterday"}
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": []}
    - slot{"language": "fr"}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"pathology_time": "yesterday"}
    - slot{"time": null}
    - slot{"pathology_body_part": "leg"}
    - slot{"body_part": null}
    - slot{"pathology_period": "every day"}
    - slot{"period": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - sum_up_pathology
    - slot{"requested_slot": "symtoms"}
    - utter_ask_symtoms
    - sum_up_slots
* pathology{"symtoms": "test"}
    - slot{"symtoms": "test"}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_pathology
    - slot{"symtoms": "test"}
    - slot{"requested_slot": "pathology_change"}
    - utter_ask_pathology_change
    - sum_up_slots
* pathology{"pathology_change": true}
    - slot{"pathology_change": true}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_pathology
    - slot{"pathology_change": true}
    - slot{"requested_slot": "pathology_treatment_linked"}
    - utter_ask_pathology_treatment_linked
    - sum_up_slots
* pathology{"pathology_treatment_linked": true}
    - slot{"pathology_treatment_linked": true}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_pathology
    - slot{"pathology_treatment_linked": true}
    - sum_up_slots
* disagree
    - save_conv
    - slot{"topic": "disagree"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - ask_what_pathology
    - sum_up_slots
* pathology{"symtoms": null}
    - slot{"symtoms": null}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_pathology
    - slot{"requested_slot": "symtoms"}
    - utter_ask_symtoms
    - sum_up_slots
* pathology{"symtoms": "test"}
    - slot{"symtoms": "test"}
    - save_conv
    - slot{"topic": "pathology"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_pathology
    - slot{"symtoms": "test"}
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - reset_slots_pathology
    - slot{"global_score": 1}
    - slot{"symtoms": null}
    - slot{"pathology_body_part": null}
    - slot{"pathology_time": null}
    - slot{"pathology_change": null}
    - slot{"pathology_period": null}
    - slot{"pathology_treatment_linked": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"pathology": true}
    - sum_up_slots
    - export

## Generated Story 1879510231223465700
* treatment
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": []}
    - slot{"language": "fr"}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"requested_slot": "medicinal"}
    - utter_ask_medicinal
    - sum_up_slots
* treatment{"medicinal": true}
    - slot{"medicinal": true}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"medicinal": true}
    - slot{"requested_slot": "treatment_being_taken"}
    - utter_ask_treatment_being_taken
    - sum_up_slots
* treatment{"treatment_being_taken": "pris"}
    - slot{"treatment_being_taken": "pris"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"treatment_being_taken": "pris"}
    - slot{"requested_slot": "drug"}
    - utter_ask_drug
    - sum_up_slots
* treatment{"drug": "drug"}
    - slot{"drug": "drug"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"drug": "drug"}
    - slot{"requested_slot": "treatment_ok"}
    - utter_ask_treatment_ok
    - sum_up_slots
* treatment{"treatment_ok": true}
    - slot{"treatment_ok": true}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"treatment_ok": true}
    - slot{"requested_slot": "dosing"}
    - utter_ask_dosing
    - sum_up_slots
* treatment{"dosing": "dosing"}
    - slot{"dosing": "dosing"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"dosing": "dosing"}
    - slot{"requested_slot": "treatment_time"}
    - utter_ask_treatment_time
    - sum_up_slots
* treatment{"time": "yesterday"}
    - slot{"time": "yesterday"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"treatment_time": "yesterday"}
    - slot{"time": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - sum_up_treatment
    - slot{"requested_slot": "treatment_overdosage"}
    - utter_ask_treatment_overdosage
    - sum_up_slots
* treatment{"treatment_overdosage": "pris"}
    - slot{"treatment_overdosage": "pris"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"treatment_overdosage": "pris"}
    - slot{"requested_slot": "treatment_prescripted"}
    - utter_ask_treatment_prescripted
    - sum_up_slots
* treatment{"treatment_prescripted": true}
    - slot{"treatment_prescripted": true}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"treatment_prescripted": true}
    - slot{"requested_slot": "treatment_period"}
    - utter_ask_treatment_period
    - sum_up_slots
* treatment{"period": "every day"}
    - slot{"period": "every day"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - slot{"treatment_period": "every day"}
    - slot{"period": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - sum_up_treatment
    - sum_up_slots
    - export

## Generated Story -5311939058495428836
* treatment
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": []}
    - slot{"language": "en"}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"requested_slot": "medicinal"}
    - utter_ask_medicinal
    - sum_up_slots
* treatment{"medicinal": true}
    - slot{"medicinal": true}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"medicinal": true}
    - slot{"requested_slot": "treatment_being_taken"}
    - utter_ask_treatment_being_taken
    - sum_up_slots
* treatment{"treatment_being_taken": "taken"}
    - slot{"treatment_being_taken": "taken"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"treatment_being_taken": "taken"}
    - slot{"requested_slot": "drug"}
    - utter_ask_drug
    - sum_up_slots
* treatment{"drug": "drug"}
    - slot{"drug": "drug"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"drug": "drug"}
    - slot{"requested_slot": "treatment_ok"}
    - utter_ask_treatment_ok
    - sum_up_slots
* treatment{"treatment_ok": true}
    - slot{"treatment_ok": true}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"treatment_ok": true}
    - slot{"requested_slot": "dosing"}
    - utter_ask_dosing
    - sum_up_slots
* treatment{"dosing": "dosing"}
    - slot{"dosing": "dosing"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"dosing": "dosing"}
    - slot{"requested_slot": "treatment_time"}
    - utter_ask_treatment_time
    - sum_up_slots
* treatment{"time": "yesterday"}
    - slot{"time": "yesterday"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"treatment_time": "yesterday"}
    - slot{"time": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - sum_up_treatment
    - slot{"requested_slot": "treatment_overdosage"}
    - utter_ask_treatment_overdosage
    - sum_up_slots
* treatment{"treatment_overdosage": "taken"}
    - slot{"treatment_overdosage": "taken"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"treatment_overdosage": "taken"}
    - slot{"requested_slot": "treatment_prescripted"}
    - utter_ask_treatment_prescripted
    - sum_up_slots
* treatment{"treatment_prescripted": true}
    - slot{"treatment_prescripted": true}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"treatment_prescripted": true}
    - slot{"requested_slot": "treatment_period"}
    - utter_ask_treatment_period
    - sum_up_slots
* treatment{"period": "every day"}
    - slot{"period": "every day"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"temperature": null}
    - slot{"time": null}
    - slot{"treatment_period": "every day"}
    - slot{"period": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - sum_up_treatment
    - sum_up_slots
    - export

## Generated Story 435050222365266094
* treatment{"dosing": "dosing", "drug": "drug"}
    - slot{"dosing": "dosing"}
    - slot{"drug": "drug"}
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": []}
    - slot{"language": "en"}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"drug": "drug"}
    - slot{"dosing": "dosing"}
    - slot{"requested_slot": "medicinal"}
    - utter_ask_medicinal
    - sum_up_slots
* treatment{"medicinal": true}
    - slot{"medicinal": true}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"medicinal": true}
    - slot{"requested_slot": "treatment_being_taken"}
    - utter_ask_treatment_being_taken
    - sum_up_slots
* treatment{"treatment_being_taken": "forgotten"}
    - slot{"treatment_being_taken": "forgotten"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"treatment_being_taken": "forgotten"}
    - slot{"requested_slot": "treatment_ok"}
    - utter_ask_treatment_ok
    - sum_up_slots
* treatment{"treatment_ok": false}
    - slot{"treatment_ok": false}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"treatment_ok": false}
    - slot{"requested_slot": "treatment_time"}
    - utter_ask_treatment_time
    - sum_up_slots
* treatment{"time": "yesterday"}
    - slot{"time": "yesterday"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"treatment_time": "yesterday"}
    - slot{"time": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - sum_up_treatment
    - slot{"requested_slot": "treatment_overdosage"}
    - utter_ask_treatment_overdosage
    - sum_up_slots
* treatment{"treatment_overdosage": "overdosed"}
    - slot{"treatment_overdosage": "overdosed"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"treatment_overdosage": "overdosed"}
    - slot{"requested_slot": "treatment_prescripted"}
    - utter_ask_treatment_prescripted
    - sum_up_slots
* treatment{"treatment_prescripted": false}
    - slot{"treatment_prescripted": false}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"treatment_prescripted": false}
    - slot{"requested_slot": "treatment_period"}
    - utter_ask_treatment_period
    - sum_up_slots
* treatment{"period": "every day"}
    - slot{"period": "every day"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - slot{"treatment_period": "every day"}
    - slot{"period": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - sum_up_treatment
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - slot{"temperature": null}
    - slot{"duration": null}
    - slot{"distance": null}
    - slot{"time": null}
    - reset_slots_treatment
    - slot{"global_score": 2}
    - slot{"medicinal": null}
    - slot{"drug": null}
    - slot{"treatment_being_taken": null}
    - slot{"dosing": null}
    - slot{"treatment_time": null}
    - slot{"treatment_prescripted": null}
    - slot{"treatment_ok": null}
    - slot{"treatment_overdosage": null}
    - slot{"treatment_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"treatment": true}
    - sum_up_slots
    - export

## Generated Story 7250209104722528063
* treatment{"dosing": "dosing", "drug": "drug"}
    - slot{"dosing": "dosing"}
    - slot{"drug": "drug"}
    - slot{"stopword": "stop"}
    - slot{"emergency": "help"}
    - slot{"nickname": "Ailixir"}
    - slot{"exitword": "gone"}
    - slot{"count_user_reminder_max": 1}
    - slot{"count_user_reminder": 0}
    - slot{"followed_intent": []}
    - slot{"language": "en"}
    - slot{"current_session": 1}
    - slot{"global_score": 0}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"duration": null}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"drug": "drug"}
    - slot{"dosing": "dosing"}
    - slot{"requested_slot": "medicinal"}
    - utter_ask_medicinal
    - sum_up_slots
* treatment{"medicinal": true}
    - slot{"medicinal": true}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"duration": null}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"medicinal": true}
    - slot{"requested_slot": "treatment_being_taken"}
    - utter_ask_treatment_being_taken
    - sum_up_slots
* treatment{"treatment_being_taken": "forgotten"}
    - slot{"treatment_being_taken": "forgotten"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"duration": null}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"treatment_being_taken": "forgotten"}
    - slot{"requested_slot": "treatment_ok"}
    - utter_ask_treatment_ok
    - sum_up_slots
* treatment{"treatment_ok": false}
    - slot{"treatment_ok": false}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"duration": null}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"treatment_ok": false}
    - slot{"requested_slot": "treatment_time"}
    - utter_ask_treatment_time
    - sum_up_slots
* treatment{"time": "yesterday"}
    - slot{"time": "yesterday"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"treatment_time": "yesterday"}
    - slot{"time": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - sum_up_treatment
    - slot{"requested_slot": "treatment_overdosage"}
    - utter_ask_treatment_overdosage
    - sum_up_slots
* treatment{"treatment_overdosage": "underdosed"}
    - slot{"treatment_overdosage": "underdosed"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"duration": null}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"treatment_overdosage": "underdosed"}
    - slot{"requested_slot": "treatment_prescripted"}
    - utter_ask_treatment_prescripted
    - sum_up_slots
* treatment{"treatment_prescripted": true}
    - slot{"treatment_prescripted": true}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"duration": null}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"treatment_prescripted": true}
    - slot{"requested_slot": "treatment_period"}
    - utter_ask_treatment_period
    - sum_up_slots
* treatment{"period": "every day"}
    - slot{"period": "every day"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"duration": null}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"time": null}
    - slot{"treatment_period": "every day"}
    - slot{"period": null}
    - slot{"requested_slot": null}
    - action_multiple_set_complex
    - sum_up_treatment
    - sum_up_slots
* disagree
    - save_conv
    - slot{"topic": "disagree"}
    - slot{"duration": null}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"time": null}
    - ask_what_treatment
    - sum_up_slots
* treatment{"dosing": "no_drug", "treatment_overdosage": "no_drug", "treatment_being_taken": "no_drug", "medicinal": false, "treatment_period": "no_drug", "drug": "no_drug"}
    - slot{"dosing": "no_drug"}
    - slot{"drug": "no_drug"}
    - slot{"medicinal": false}
    - slot{"treatment_being_taken": "no_drug"}
    - slot{"treatment_overdosage": "no_drug"}
    - slot{"treatment_period": "no_drug"}
    - save_conv
    - slot{"topic": "treatment"}
    - slot{"duration": null}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"time": null}
    - sum_up_treatment
    - slot{"medicinal": false}
    - slot{"treatment_being_taken": "no_drug"}
    - slot{"drug": "no_drug"}
    - slot{"dosing": "no_drug"}
    - slot{"treatment_overdosage": "no_drug"}
    - slot{"treatment_period": "no_drug"}
    - sum_up_slots
* agree
    - save_conv
    - slot{"topic": "agree"}
    - slot{"duration": null}
    - slot{"temperature": null}
    - slot{"distance": null}
    - slot{"time": null}
    - reset_slots_treatment
    - slot{"global_score": 2}
    - slot{"medicinal": null}
    - slot{"drug": null}
    - slot{"treatment_being_taken": null}
    - slot{"dosing": null}
    - slot{"treatment_time": null}
    - slot{"treatment_prescripted": null}
    - slot{"treatment_ok": null}
    - slot{"treatment_overdosage": null}
    - slot{"treatment_period": null}
    - slot{"topic": null}
    - slot{"requested_slot": null}
    - slot{"treatment": true}
    - sum_up_slots
    - export

