from nltk.classify import PositiveNaiveBayesClassifier

def classifier(positive_featuresets, unlabeled_featuresets,text):
    classifier = PositiveNaiveBayesClassifier.train(positive_featuresets,
                                                     unlabeled_featuresets)
    return (classifier.classify(features(text)))

def features(sentence):
    words = sentence.lower().split()
    return dict(('contains(%s)' % w, True) for w in words)                       
    
def get_pain_level(text):
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
           
    if(classifier(list(map(features, mild)),list(map(features, not_mild)),text)):
        return 'mild'
    elif (classifier(list(map(features, moderate)),list(map(features, not_moderate)),text)):
        return 'moderate'
    elif (classifier(list(map(features, severe)),list(map(features, not_severe)),text)):
        return 'severe'
    else:
        return 'None'
        
if __name__ == '__main__':
    text = "brutal"
    res = get_pain_level(text)
    print(res)
 
                       