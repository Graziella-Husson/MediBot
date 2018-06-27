from nltk.classify import PositiveNaiveBayesClassifier
from textblob import TextBlob

def classifier(positive_featuresets, unlabeled_featuresets,text):
    classifier = PositiveNaiveBayesClassifier.train(positive_featuresets,
                                                     unlabeled_featuresets)
    return classifier.prob_classify(features(text))
    #return (classifier.classify(features(text)))

def features(sentence):
    words = sentence.lower().split()
    return dict(('contains(%s)' % w, True) for w in words) 

def score(positive_words, text):
    raw_words = text.lower().split(" ")
    return len([word for word in raw_words if word in positive_words])                         
    
def get_pain_level(text):
    corrected = (text.correct())
    print(corrected)
    mild = ['tender','scratchy','unsmooth', 'abrasive','rough','discomforting',
            'malaise','incommodious','inconvenient','unease','uncomfortable',
            'passable','tolerable','satisfactory','supportable','endurable',
            'resistant','sufferable','bearable','allowable','ok','strange',
            'mild','soft','clement','balmy','awkward','disquieting','uneasy',
            'discernible','noticeable','marked','pronounced','noticeability',
            'patency','detectable','notable','minor','insignificant','secondary',
            'peanut','pardonable','limited','modest','small','light', 'distracting',
            'confuse','confusing','disturb','disturbing','trouble','disorder',
            'worrying','control','lower','decrease','decreasing','low','boring',
            'deplorable', 'annoying', 'disagreeable', 'pestering', 'nettlesome',
            'plaguey','plaguy', 'galling', 'tesaing', 'vexing', 'pesky', 'bothersome',
             'vexatious', 'pestiferous', 'mistreatment', 'exasperating','bit']
    moderate = ['upsetting', 'displeasing', 'disconcerting', 'flickering', 'aflicker',
                'unsteady', 'pulsing', 'twiching', 'spasm', 'wrick', 'suffering',
                'flashing', 'pricking', 'drilling', 'cramps', 'pulling', 'hot',
                'burning', 'hurting', 'important', 'flaming', 'titillating',
                'tickling', 'tingle', 'tingling', 'itchy', 'painful', 'edged',
                'unkind', 'sting', 'unhealthy', 'sensitive', 'stinging', 'tiring',
                'exhausting', 'effortful', 'wearing', 'wrong', 'spreading', 'propagating',
                'diffusing', 'irritating', 'diverging', 'sharp', 'incisive',
                'acute', 'keen', 'discriminating','radiating', 'penetrating',
                'acold', 'refrigerated', 'heatless', 'nippy', 'raw', 'nipping',
                'frosty', 'frigorific', 'stone-cold', 'frore', 'ice-cold', 'shivery',
                'refrigerant', 'parky', 'temperature', 'icy', 'snappy', 'rimed',
                'glacial', 'polar', 'algid', 'unheated', 'arctic', 'rimy', 'frigid',
                'gelid', 'bleak', 'cool', 'crisp', 'frozen', 'chilly', 'refrigerating',
                'unwarmed', 'passionless', 'wintry', 'chilliness', 'nip', 'gelidity',
                'chill', 'shrewish', 'queasy', 'vile', 'neauseous', 'offensive',
                'loathsome', 'sickening', 'noisome', 'unwholesome', 'barbed',
                'mordacious', 'pungent', 'sarcastic', 'changeless', 'invariable',
                'unvarying', 'invariant', 'constancy', 'faithful', 'steadfast',
                'unfailing', 'invariable', 'unflagging', 'stability', 'unswerving',
                'stable', 'staunch', 'unchangeable', 'ceaseless', 'unceasing',
                'continuous', 'perpetual', 'never-ending', 'incessant', 'unremitting',
                'uninterrupted', 'chew', 'cold', 'nagging', 'nauseating', 'biting',
                'constant', 'dragging', 'gnawing','medium']
    severe = ['dying','last','moribund','anxious','eager', 'piercing', 'lancinate',
              'cutting', 'atrocious', 'alarming', 'ugly', 'horrifying', 'awful',
              'extraordinary', 'terrible', 'tremendous','fearful', 'excruciating',
              'agonising', 'torturous', 'agonizing', 'harrowing', 'torturesome',
              'crushing', 'destructive', 'stabbing', 'vicious', 'knifelike',
              'savage', 'barbarous', 'inhumane', 'brutal', 'fell', 'roughshod',
              'evil', 'wicked', 'poisonous', 'malicious', 'venomous', 'condemnable',
              'reprehensible', 'criminal','intense','aggravated''violent','thick',
              'terrific','raging','unabated','vehement','extreme','overwhelming',
              'big','exquisite','main','intensified','wicked','bad','horrible',
              'agonizing','dreadful','heavily','severe','shooting','lacerating',
              'crushing', 'destructive','devastating','pressing','urgent','imperative',
              'distress','stitch','excruciation','agony','neuralgia','sore',
              'soreness','growing','aching','torment','tormenting','throb',
              'gripes','suffocating','frightful','terrifying','punishing','cruel', 
              'killing','unbearable','squeezing','compressing','squeeze','tweak',
              'agonizing','torturing', 'hard','hardly']
    
    not_mild = severe +  moderate
    not_severe = mild +  moderate
    not_moderate = severe +  mild
    
    prob_sev = (classifier(list(map(features, severe)),list(map(features, not_severe)),corrected).prob(True)) 
    prob_mild = (classifier(list(map(features, mild)),list(map(features, not_mild)),corrected).prob(True))     
    prob_mod = (classifier(list(map(features, moderate)),list(map(features, not_moderate)),corrected).prob(True)) 
    print(prob_sev,prob_mild,prob_mod)    
    best = max(prob_sev,prob_mild,prob_mod)
    if best <= 0.5:
        return save_None(corrected,text) 
    if prob_mild == best:
        return 'mild'
    elif prob_mod == best:
        return 'moderate'
    elif prob_sev == best:
        return 'severe'
    else:
        return save_None(corrected,text) 

def save_None(corrected,text):
    file = open('save_classif_pain.txt', 'a+')
    file.write(str(corrected)+"\n"+str(text)+"\n")
    file.close()
    
if __name__ == '__main__':
    text =TextBlob("sbrdeh")
    res = get_pain_level(text)
    print(res)  