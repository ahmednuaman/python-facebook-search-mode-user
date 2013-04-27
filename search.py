import json
import urllib2
from collections import Counter

def search():
  req = urllib2.urlopen('https://graph.facebook.com/search?q=watermelon&type=post')
  res = json.loads(req.read())
  users = []

  for status in res['data']:
    users.append(status['from']['name'])

  count = Counter(users)

  print count.most_common()

if __name__ == '__main__':
  search()