import urllib3
import json
http = urllib3.PoolManager()
r = http.request('GET', 'https://newsapi.org/v2/everything?q=Python programming langguage&apiKey=e584fe8c8fb545f4b0884204f29437fc&pageSize=5')
articles = json.loads(r.data.decode('utf-8'))
for article in articles['articles']:
    print(article['title'])
    print(article['publishedAt'])
    print(article['url'])


