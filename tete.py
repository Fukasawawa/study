import sys
import MeCab
#m = MeCab.Tagger ("-Ochasen")
m = MeCab.Tagger ("")

a = "aaa"
while a!="終わり":
    print("入力")
    a = input()
    result = m.parse(a).split('\n')
    #print(result)
    for j in result:
        word = j.split('\t')
        #print(len(word))
        if(len(word) >= 2):
            clazz = word[1].split(',')
            print(word[0], clazz[0], clazz[6])
            #if((clazz[0] == "形容詞") or (clazz[0] == "連体詞") or (clazz[0] == "副詞")):
            #if((clazz[0] == "名詞") or (clazz[0] == "動詞")):
            #    print(word[0], clazz[0], clazz[6])

    #print(m.parse (a))
