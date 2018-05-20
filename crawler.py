import requests
import lxml.html
#import cssselect

#https://qiita.com/7of9/items/5fb6d57ccb0ce9a47dd6
url = 'http://chizutwi.jp/twitter/'
target_html = requests.get(url,
                  data={'data-lat':'35.7099',
                        'data-lng':'139.8114'}).content
dom = lxml.html.fromstring(target_html)
 
text = dom.cssselect('li')[0].text
title = dom.cssselect('title')[0].text
print(title)
print(text)


'''
PythonによるWebスクレイピング
3,240円
'''
 

#text_contentにすると以下のテキストをすべて取得します。
#info = dom.cssselect('.innerSection')[0].text_content()
#print(info)

