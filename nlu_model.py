from rasa_nlu.model import Metadata, Interpreter

# where `model_directory points to the folder the model is persisted in
interpreter = Interpreter.load('models/nlu/default/fr_duckling')
print (interpreter.parse(u"Je ressens cette forte douleur depuis hier"))
print (interpreter.parse(u"J'ai fait du sport pendant 5 heures"))
print (interpreter.parse(u"J'ai couru 3 kilomètres"))
print (interpreter.parse(u"J'ai 39°C de fièvre."))
#print (interpreter.parse(u"I feel a sharp pain in the leg"))
# 'pain', 'confidence': 0.985409655949852
#print (interpreter.parse(u"My horse is sharp"))
# 'fallback', 'confidence': 0.48489013585950913
#print (interpreter.parse(u"The pain in my back is horrible"))
# 'pain', 'confidence': 0.9635503367430202
#print (interpreter.parse(u"fziqhf"))
# 'fallback', 'confidence': 0.9189299103884638
#print (interpreter.parse(u"I am not in a good mood"))
#print (interpreter.parse(u"I am in a good mood"))
# 'emotional_hapiness', 'confidence': 0.6461365116817862}
#print (interpreter.parse(u"I am not ok"))
#print (interpreter.parse(u"I am ok"))
# 'emotional_hapiness', 'confidence': 0.40076629140404485
#print (interpreter.parse(u"I did some sport. I have a pain in the leg now"))

