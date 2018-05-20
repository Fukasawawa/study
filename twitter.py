# coding: UTF-8
import json, config
import format, rm_emoji
import sys
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
url = "https://api.twitter.com/1.1/search/tweets.json"

def tweet_search(word):
    #検索語と検索数を設定
    params = {'q' : word, 'count' : 10}

    req = twitter.get(url, params = params)
    #正常につながれば
    if req.status_code == 200:
        search_timeline = json.loads(req.text)
        #ツイート数だけループ
        for tweet in search_timeline['statuses']:
            #ツイート本文から絵文字を削除しMecabようにフォーマットしreturn
            yield format.format_text(rm_emoji.remove_emoji(tweet['text'].translate(non_bmp_map)))
            #yield rm_emoji.remove_emoji(tweet['text'].translate(non_bmp_map))
    else:
        print("ERROR: %d" % req.status_code)

data = tweet_search("盛岡駅")
for i in data:
    print(i)
