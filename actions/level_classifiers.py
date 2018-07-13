from nltk.classify import PositiveNaiveBayesClassifier
from textblob import TextBlob

def classifier(positive_featuresets, unlabeled_featuresets,text):
    """
    @param positive_featuresets: A list of featuresets that are known as positive examples (i.e., their label is ``True``).
    @param unlabeled_featuresets: A list of featuresets whose label is unknown.
    @param text: text to classify
    @return: The probability of the text to be classify positive
    
    A variant of the Naive Bayes Classifier that performs binary classification with
    partially-labeled training sets. In other words, assume we want to build a classifier
    that assigns each example to one of two complementary classes (e.g., male names and
    female names).
    If we have a training set with labeled examples for both classes, we can use a
    standard Naive Bayes Classifier. However, consider the case when we only have labeled
    examples for one of the classes, and other, unlabeled, examples.
    Then, assuming a prior distribution on the two labels, we can use the unlabeled set
    to estimate the frequencies of the various features.
    
    Let the two possible labels be 1 and 0, and let's say we only have examples labeled 1
    and unlabeled examples. We are also given an estimate of P(1).
    
    We compute P(feature|1) exactly as in the standard case.
    
    To compute P(feature|0), we first estimate P(feature) from the unlabeled set (we are
    assuming that the unlabeled examples are drawn according to the given prior distribution)
    and then express the conditional probability as:
    P(feature|0) =(P(feature) - P(feature|1) * P(1))/P(0)
    """
    classifier = PositiveNaiveBayesClassifier.train(positive_featuresets,
                                                     unlabeled_featuresets)
    return classifier.prob_classify(features(text))
    #return (classifier.classify(features(text)))

def features(sentence):
    """
    @param sentence: the sentence or word to check
    @return: a dictionnary of features
    """
    words = sentence.lower().split()
    return dict(('contains(%s)' % w, True) for w in words) 

def score(positive_words, text):
    """
    @param positive_words: a list of postives examples
    @param text: text to check
    @return: the number of time the text is in the positives examples
    """
    raw_words = text.lower().split(" ")
    return len([word for word in raw_words if word in positive_words])
                         
def get_physical_activity_level(text):
    """
    @param text: the sport's name, corrected by C{TextBlob} to avoid mispelling
    @return: the sport's level 'little','moderate','vigorous' or None. Call C{save_None} if None.
    """
    corrected =TextBlob(text).correct()
    print(corrected)
    vigorous = ["running","lifting heavy stuff","extrem sports","tennis","marathon",
            "cycling","nordic walking","cycling","run","cycle","bicylcle",
            "ride a bike","swiming","triathlon","marathon","urban trail",
            "climbing brisky up a hill","aerobics","competitive","football",
            "volleyball","hockey","basketball","handball","soccer","ping pong",
            "tennis single","heavy shoveling","digging ditches","carrying heavy loads",
            "hiking","Wheeling your wheelchair","Backpacking","Mountain climbing",
            "rock climbing","rapelling","bicycling","Step aerobics","Water jogging",
            "aerobic","Calisthenics","Karate","judo","tae kwon do","jujitsu",
            "Jumping rope","jumping jacks","Circuit weight training","Boxing",
            "sparring","Wrestling competitive","Professional ballroom",
            "Folk dancing","Clogging","Wheelchair tennis",
            "Rugby Kickball","hockey","beach volleyball","racquetball","squash",
            "skiing","speedskating","Cross-country skiing","sledding","tobogganing",
            "ice hockey","synchronized swimming","treading water","water jogging",
            "water polo","water basketball","scuba diving","kayaking","horsebackriding",
            "trotting","galloping","jumping","playing polo","Skipping",
            "heavy musical instrument","Pushing a nonmotorized lawn mower",
            "Shoveling heavy snow","moving or pushing heavy furniture",
            "carrying heavy objects","Carrying several heavy bags",
            "Carrying child","forking bales","cleaning a barn or stables",
            "Hand-sawing hardwoods","Pushing a disabled car","Firefighting",
            "Masonry and heavy construction work","Loading and unloading a truck",
            "Most forestry work","Coal mining","competition","fast","vigourous",
            "actively","rapid","heavy","strenuous effort","extensive", "race walk",
            "jogging", "running","swimming laps", "Tennis single", "aerobic dancing"
            "Bicycling","digging","hoeing","Hiking","heavy backpack"]
    moderate = ["moving table","pushing vacuum cleaner","moving stuff",
                "vacuum cleaning","clean the house","washing window","bowling",
                "stairs","floors","active walking**","walking","jogging","yoga",
                "walk","jog","bowl","nordic walking","playing golf","golf",
                "dancing","brisk walking","walking domestic animals",
                "general building tasks","roofing","thatching","painting",
                "carrying moderate loads","gardening","mopping","tennis doubles",
                "bacycling light","mowing lawn","Racewalking","roller skating",
                "in-line skating","water aquatic aerobics","gymnastics",
                "trampoline","punching bag","ballroom dancing","Line dancing",
                "square dancing","modern dancing","disco balle",
                "shooting baskets","coaching sports","frisbee","juggling","curling",
                "Cricket","bowling","badminton","archery","fencing","waterskiing","snorkeling",
                "surfing","canoeing","rafting whitewater","Sailing","paddle boating",
                "kayaking","hunting","horseback riding","guitar", "drums","twirling",
                "singing","raking lawn","bagging grass","bagging leaves","digging",
                "hoeing","shoveling","planting trees","trimming","hauling",
                "stacking wood","scrubbing the floor","hanging laundry",
                "sweeping","cleaning out","washing windows","packing","unpacking",
                "General household tasks","putting groceries away",
                "climbing","walking while carrying","animal care","shoveling grain",
                "feeding farm animals","grooming animals","manually milking cows", 
                "Home repair","cleaning gutters","caulking","refinishing furniture",
                "sanding floors with a power sander","laying","removing carpet tiles",
                "general home construction work", "roofing","painting","wall papering","scraping","plastering",
                "remodeling","automobile bodywork","hand washing and waxing a car",
                "maid service or cleaning services","waiting tables or dishwashing",
                "driving or maneuvering heavy vehicles","Operating heavy power tools",
                "electrical work","plumbing","carpentry","dry wall",
                "Farming feeding and grooming animals, milking cows, shoveling grain",
                "picking fruit from trees","picking vegetables","packing boxes for shipping or moving",
                "assembly-line work","mail carriers","dressing","moving patients","Walking briskly",
                "Water aerobics","Bicycling","tennis double","general gardening",
                "gym","gymnastic","double","tennis double"]
    little = ["litfing groceries","carrying groceries","laundry","bending","kneeling",
              "reading","stairs","bathing","dressing yourself","walking the dog",
              "watching tv","walking slowly","computer","fishing","instrument",
              "sitting","litfing groceries","carrying groceries","laundry","bending","kneeling",
              "reading","stairs","bathing","dressing yourself","walking the dog",
              "watching tv","walking slowly","computer","fishing","instrument",
              "sitting","litfing groceries","carrying groceries","laundry","bending","kneeling",
              "reading","stairs","bathing","dressing yourself","walking the dog",
              "watching tv","walking slowly","computer","fishing","instrument",
              "sitting","litfing groceries","carrying groceries","laundry","bending","kneeling",
              "reading","stairs","bathing","dressing yourself","walking the dog",
              "watching tv","walking slowly","computer","fishing","instrument",
              "sitting","litfing groceries","carrying groceries","laundry","bending","kneeling",
              "reading","stairs","bathing","dressing yourself","walking the dog",
              "watching tv","walking slowly","computer","fishing","instrument",
              "sitting","litfing groceries","carrying groceries","laundry","bending","kneeling",
              "reading","stairs","bathing","dressing yourself","walking the dog",
              "watching tv","walking slowly","computer","fishing","instrument",
              "sitting"]
    
    not_little = vigorous +  moderate
    not_vigorous = little +  moderate
    not_moderate = vigorous +  little
#    
#    if(score(little,text))>0:
#        print("score says: little")
#    if(score(vigorous,text))>0:
#        print("score says: vigorous")
#    if(score(moderate,text))>0:
#        print("score says: moderate")
     
    prob_vig = (classifier(list(map(features, vigorous)),list(map(features, not_vigorous)),text).prob(True)) 
    prob_lit = (classifier(list(map(features, little)),list(map(features, not_little)),text).prob(True))     
    prob_mod = (classifier(list(map(features, moderate)),list(map(features, not_moderate)),text).prob(True)) 
    print(prob_vig,prob_lit,prob_mod)    
    best = max(prob_vig,prob_lit,prob_mod)
    
    if best <= 0.5:
        return save_None(corrected,text,'save_classif_activity.txt') 
    if prob_lit == best:
        return 'little'
    elif prob_mod == best:
        return 'moderate'
    elif prob_vig == best:
        return 'vigorous'
    else:
        return save_None(corrected,text,'save_classif_activity.txt') 
        
def get_pain_level(text):
    """
    @param text: the pain descritpion word, corrected by C{TextBlob} to avoid mispelling
    @return: the pain level 'mild','moderate', 'severe' or None. Call C{save_None} if None.
    """
    corrected =TextBlob(text).correct()
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
        return save_None(corrected,text,'save_classif_pain.txt') 
    if prob_mild == best:
        return 'mild'
    elif prob_mod == best:
        return 'moderate'
    elif prob_sev == best:
        return 'severe'
    else:
        return save_None(corrected,text,'save_classif_pain.txt') 

def save_None(corrected,text,file_name):
    """
    @param corrected: corrected text
    @param text: text failed to be classified
    @param file_name: name of the file to save text
    Save text and corrected in a file named file_name to allow them to be classified manually later.
    """
    file = open(file_name, 'a+')
    file.write(str(corrected)+"\n"+str(text)+"\n")
    file.close()
    
#if __name__ == '__main__':
#    text =TextBlob("sbrdeh")
#    res = get_pain_level(text)
#    print(res)  