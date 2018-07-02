## Story 01
* hello
	- save_conv
	- sum_up_hello
	- sum_up_slots

## Generated Story 3306727126556356367
* pain
    - slot{"follow_in_current_session_plus": 1}
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
    - slot{"follow_in_current_session_plus": 1}
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
    - slot{"follow_in_current_session_plus": 1}
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
    - slot{"follow_in_current_session_plus": 1}
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
    - slot{"follow_in_current_session_plus": 1}
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
    - slot{"follow_in_current_session_plus": 1}
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
    - slot{"follow_in_current_session_plus": 1}
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
    - slot{"follow_in_current_session_plus": 1}
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
    - slot{"follow_in_current_session_plus": 1}
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
    - slot{"follow_in_current_session_plus": 1}
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
    - slot{"follow_in_current_session_plus": 1}
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
    - slot{"follow_in_current_session_plus": 1}
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
    - slot{"follow_in_current_session_plus": 1}
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
    - export



