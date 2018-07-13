import json

def get_utterance(key,language):
    """
    @param key: id of the sentence to search for in ressources.json file
    @param language: language to use
    @return: the utterance the bot have to say for a given key and language
    """
    ressources = json.load(open('ressources.json'))
    utterance = ressources['utterances'][key][language]
    return utterance
    
#if __name__ == '__main__':
#    key = 'bye'
#    language = 'fr'
#    print(get_utterance(key,language))