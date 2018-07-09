import json

def get_utterance(key,language):
    ressources = json.load(open('ressources.json'))
    utterance = ressources['utterances'][key][language]
    return utterance
    
if __name__ == '__main__':
    key = 'bye'
    language = 'fr'
    print(get_utterance(key,language))