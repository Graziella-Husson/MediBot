from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, config, model_dir):
	training_data = load_data(data)
	trainer = Trainer(RasaNLUConfig(config))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'test')
	
def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/test', RasaNLUConfig('config/conf_spacy.json'))
	print(interpreter.parse("Pain in my leg"))
	print(interpreter.parse("The pain is in my leg"))
	print(interpreter.parse("My leg is aching"))
	print(interpreter.parse("I feel a sharp pain in the leg"))
	print(interpreter.parse("Every morning, when I wake up, I feel a sharp pain in the leg"))
	print(interpreter.parse("My horse is ok"))
	
if __name__ == '__main__':
	#train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
	run_nlu()
