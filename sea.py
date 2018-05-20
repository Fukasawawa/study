#0312015138深澤啓希 2/22課題
def search(read, word):
    #ファイル読み込み
    file = open(read, "r")
    string = file.read()

    #検索語の文字数格納
    num = len(word)
    #検索
    index = string.find(word)
    #検索できなくなるまでループ
    while(index != -1):
        #検索語の前の文に改行が入らないようにする
        before = index-5
        if((string.find('\n', before, index)) != -1):
            before = string.rfind('\n', before, index)+1

        #検索語の後の文に改行が入らないようにする
        after = index+num+5
        if((string.find('\n', index+num, after)) != -1):
            after = string.find('\n', index+num, after)

        #出力
        print(string[before:index]+'__'+string[index:index+num]+'__'+string[index+num:after])
        #次の検索一致場所に移動
        index = string.find(word, index+1)


search("text.txt", "いる")
    
    
