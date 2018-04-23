# MediBot
A little chat bot

## Getting started 
* Install RASA 12.01 doing :
```
sudo pip3 install -r requirements.txt
sudo python3 -m spacy download en
sudo apt-get install python3-tk
```

## Choose your pipeline
* For MITIE:

Use this command to download MITIE Models

```
wget https://github.com/mit-nlp/MITIE/releases/download/v0.4/MITIE-models-v0.2.tar.bz2
```


Unzip the model

```
tar xvjf MITIE-models-v0.2.tar.bz2
```

We are interested in total_word_feature_extractor.dat file. This is inside MITIE-models/english folder. Move this file to /data folder

```
cp MITIE-models/english/total_word_feature_extractor.dat ./data/
rm MITIE-models-v0.2.tar.bz2
```


In the conf.yml file, add this where the word 'pipeline' is :

```
pipeline:
- name: "nlp_mitie"
  model: "data/total_word_feature_extractor.dat"
- name: "tokenizer_mitie"
- name: "ner_mitie"
- name: "ner_synonyms"
- name: "intent_entity_featurizer_regex"
- name: "intent_classifier_mitie"
```


* For spacy_sklearn:
	* In the conf.yml file, add this where the word 'pipeline' is :
```
pipeline:
- name: "nlp_spacy"
- name: "tokenizer_spacy"
- name: "intent_entity_featurizer_regex"
- name: "intent_featurizer_spacy"
- name: "ner_crf"
- name: "ner_synonyms"
- name: "intent_classifier_sklearn"
```

* For mitie_sklearn:
	* In the conf.yml file, add this where the word 'pipeline' is :
```
pipeline:
- name: "nlp_mitie"
  model: "data/total_word_feature_extractor.dat"
- name: "tokenizer_mitie"
- name: "ner_mitie"
- name: "ner_synonyms"
- name: "intent_entity_featurizer_regex"
- name: "intent_featurizer_mitie"
- name: "intent_classifier_sklearn"
```

* For tensorflow_embedding:
	* In the conf.yml file, add this where the word 'pipeline' is :
```
pipeline:
- name: "intent_featurizer_count_vectors"
- name: "intent_classifier_tensorflow_embedding"
```

	* If you want to recognize many intents add intent_tokenization_flag and specify the split symbol:
```
  intent_tokenization_flag: true
  intent_split_symbol: "."
```
	

* Duckling for entity recognition :
```
sudo apt-get install default-jdk
```

## Train NLU model
* _data.json_ file have to be filled with examples (text + entities in it + intent).
To do so :
	* manually complete json file
	* use rasa-nlu-trainer : `npm i -g rasa-nlu-trainer` and `rasa-nlu-trainer` in data folder
:heavy_exclamation_mark: Use Google Chrome!
* train the model with _data.json_ file :
```
python3 -m rasa_nlu.train -c conf.yml --fixed_model_name current --data data/data.json --path models/nlu
```

## Evaluate the model
To evaluate the model :
```
python3 -m rasa_nlu.evaluate -d data/data.json -m models/nlu/default/current -c conf.yml
```
Or with cross validation (f=10 folds):
```
python3 -m rasa_nlu.evaluate -d data/data.json -c conf.yml --mode crossvalidation -f 10
```

## Train bot
```
python3 -m rasa_core.train -s data/stories.md -d domain.yml -o models/dialogue --epochs 300
```
To train 'online' (interactive learning) :

```
python3 train_online.py
```
Creates a file (stories.md by default). You have to add it into the stories.md file in /data


## Vizualize your stories

You can vizualize your stories by using graphviz. 
```
sudo apt-get install graphviz libgraphviz-dev graphviz-dev pkg-config
sudo pip3 install git+https://github.com/pygraphviz/pygraphviz
python3 vizualize.py
```

## Talk to bot :space_invader:

```
python3 -m rasa_core.run -d models/dialogue -u models/nlu/default/current
```
