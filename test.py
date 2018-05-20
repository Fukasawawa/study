import requests
r = requests.get('http://gihyo.jp/dp')
type(r)
r.status_code
r.headers['content-type']
r.encoding
r.text
r.content
