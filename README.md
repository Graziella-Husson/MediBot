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
