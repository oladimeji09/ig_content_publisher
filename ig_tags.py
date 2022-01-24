#@auto-fold regex \.\
import random, quote

def comments(N =1):
    comments = ["Follow me if you want to learn how magical life really is.",
    "You can either lead, follow me or not be around me at all.",
    "By following me, you're going to realize how elusive I am.",
    "Be cautious because the devil is my biggest follower.",
    "If you don't like me, don't follow or watch me.",
    "Follow me if you are courageous enough.",
    "If you're my friend, then follow me on Instagram.",
    "If you want to achieve greatness, follow me.",
    "The follow for follow strategy works online.",
    "Follow me if you want to get the most authentic version of me.",
    "Follow me because I have many rare and highly desirable qualities.",
    "Follow me if you want to become a better version of yourself.",
    "Don't follow me.",
    "Follow me and run away with all your might.",
    "Don't make the mistake of following me – I'm also lost.",
    "Follow the music and the lyrics, but don't follow me.",
    "Requesting you to follow me.",
    "No one can follow us in the afterlife.",
    "My followers know that I'm real, not perfect.",
    "A wise man will follow me from a distance.",
    "Criticism is inevitable when there are people following you.",
    "I don't want to be a follower; I want others to follow my lead.",
    "I'm not interested in getting people to follow me.",
    "I want ethical and rational people to be following me.",
    "The people who follow me know everything about me.",
    "I have an increasing number of followers on Twitter.",
    "I'm blessed to have wonderful people following me.",
    "I want to give hope and faith to the girls that follow me."]
    return  random.sample(comments,N)

def quotes(words, L=171):
    X = True
    while X == True:
        try:
            qut  = quote.search(words)[random.randint(1, 20)].get('quote')
            if len(qut) < L:
                return qut
                X = False
            print('trying to find another quote')
        except:
            pass

def tags(type,N = 20):
    if type =='comedy':
        return random.sample(["comedy","funny","memes","funnymemes","meme","lol","love","humor","dankmemes","fun","tiktok","memesdaily","follow","like",
        "funnyvideos","lmao","instagood","jokes","dank","dailymemes","viral","edgymemes","laugh","memepage","dankmeme","bhfyp",
        "comedian","reddit","like4like","likeforfollow"] ,N)
    elif type == 'travel':
        return random.sample(["uktravel","ukredlist","travel","nature","photography","travelphotography","love","photooftheday","likeforfollow",
        "travelgram","picoftheday","instagram","photo","bhfyp","art","like","naturephotography","explore","vacation",
        "wanderlust","adventure","summer","instatravel","follow","travelblogger","followforfollowback","happy","fashion","trip","like4like"],N)
    elif type == 'money':
        return random.sample(["billionaire","millionairelifestyle","billionairesclub","millionaire","luxurylife","millionairetoys","billionairelifestyle","millionairelife","likeforfollow",
        "billionairelife","millionairesclub","billionaireclub","luxury","millionaireliving","onlyforluxury","richlifestyle","instaluxury","luxlife","luxurycollection",
        "luxurylifestyle","finance","money","instatravel","success","rich","entrepreneurlife","inspiration","investment","billionaireboysclub","wealth"
        "TSLA","AMZN","META","AAPL", "MSFT", "GOOG", "PYPL"],N)
# quotes('money')
