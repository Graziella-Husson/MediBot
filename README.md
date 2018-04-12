# MediBot
A little chat bot

## Train NLU model
* _data.json_ file have to be filled with examples (text + entities in it + intent).
To do so :
	* manually complete json file
	* use rasa-nlu-trainer : `npm i -g rasa-nlu-trainer` and `rasa-nlu-trainer` in data folder
:heavy_exclamation_mark: Use Google Chrome!
* train the model with _data.json_ file :
```
python3 nlu_model.py
```

## Evaluate the model
To evaluate the model :
```
python3 -m rasa_nlu.evaluate -d data/data.json -m models/nlu/default/medibotnlu -c config_spacy.json
```
Or with cross validation :
```
python3 -m rasa_nlu.evaluate -d data/data.json -c config_spacy.json --mode crossvalidation
```

## Train bot
```
python3 train_init.py
```
To train 'online' (interactive learning) :

```
python3 train_online.py
```

## Talk to bot :space_invader:

```
python3 dialogue_management_model.py
```
