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
    
def get_physical_activity_level(text):
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
                "surfing","canoeing","rafting—whitewater","Sailing","paddle boating",
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
    
    if prob_lit == best:
        return 'little'
    elif prob_mod == best:
        return 'moderate'
    elif prob_vig == best:
        return 'vigorous'
    else:
        return None
        
if __name__ == '__main__':
    text =TextBlob("evrey day")
    corrected = (text.correct())
    print(corrected)
    res = get_physical_activity_level(corrected)
    print(res)
 
                       