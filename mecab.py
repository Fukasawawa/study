import MeCab

import twitter
import selen

m = MeCab.Tagger('')
t = selen.tweet_get("盛岡駅")
#print(t)

for i in t[:,0]:
    cnt = 0
    result = m.parse(i).split('\n')
    #print(result)
    for j in result:
        word = j.split('\t')
        #print(len(word))
        if(len(word) >= 2):
            clazz = word[1].split(',')
            #print(word[0], clazz[0], clazz[6])
            if((clazz[0] == "形容詞") or (clazz[0] == "連体詞") or (clazz[0] == "副詞")):
            #if(clazz[0] == "連体詞"):
                cnt = cnt+1
    if(cnt >= 5):
        print(i)
    #print(result)
    #print(result[0], result[4])

t = twitter.tweet_search("盛岡駅")

for i in t[:,0]:
    cnt = 0
    result = m.parse(i).split('\n')
    #print(result)
    for j in result:
        word = j.split('\t')
        #print(len(word))
        if(len(word) >= 2):
            clazz = word[1].split(',')
            #print(word[0], clazz[0], clazz[6])
            if((clazz[0] == "形容詞") or (clazz[0] == "連体詞") or (clazz[0] == "副詞")):
            #if(clazz[0] == "連体詞"):
                cnt = cnt+1
    if(cnt >= 5):
        print(i)
    #print(result)
    #print(result[0], result[4])
