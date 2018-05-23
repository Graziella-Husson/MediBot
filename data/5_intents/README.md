# 5 intents description
## 5 intents + 7 entities

* intent examples: 430 (5 distinct intents)
* Found intents: 'emotional_hapiness', 'emotional_sadness', 'activity', 'fallback', 'pain'
* entity examples: 169 (6 distinct entities)
* found entities: 'body_part', 'pain_level', 'duration', 'sport', 'period', 'distance'
* Intent evaluation results with spacy large:
	* Intent Evaluation: Only considering those 430 examples that have a defined intent out of 430 examples
	* F1-Score:  0.9906840745274038
	* Precision: 0.9906973562816149
	* Accuracy:  0.9906976744186047
* Evaluation for entity extractor: ner_crf 
	* F1-Score:  0.9337122991477859
	* Precision: 0.9391592286526494
	* Accuracy:  0.9385834571570084






