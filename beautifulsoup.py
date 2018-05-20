import requests
from bs4 import BeautifulSoup

s = requests.Session()
r = s.post('http://chizutwi.jp/twitter/', data = {
    'data-lat':'35.7099',
    'data-lng':'139.8114',
})
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

'''
itemTags = soup.select('.item-caption a')
for itemTag in itemTags:
    r = s.get(itemTag['href'])
    soup = BeautifulSoup(r.text, 'html.parser')
    itemDetailTag = soup.select_one('.item-detail')
    print('{}: {}'.format(itemTag.text.strip(), itemDetailTag.text.strip()))
'''
