import MeCab

import selen

m = MeCab.Tagger('')
t = selen.tweet_get("盛岡駅")
for i in t:
    result = m.parse(i).split('\n')
    #print(result)
    for j in result:
        word = j.split('\t')
        #print(len(word))
        if(len(word) >= 2):
            clazz = word[1].split(',')
            #print(word[0], clazz[0], clazz[6])
            if((clazz[0] == "形容詞") or (clazz[0] == "連体詞") or (clazz[0] == "副詞")):
                print(i)
    #print(result)
    #print(result[0], result[4])
    
    
    
