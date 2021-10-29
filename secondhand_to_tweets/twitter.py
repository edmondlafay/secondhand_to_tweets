import requests
import yaml
from requests_oauthlib import OAuth1
from urllib.request import urlopen

class Twitter:
  def __init__(self):
    with open('.secrets.yaml') as f:
      secrets = yaml.safe_load(f)
    self.user_id = secrets['twitter']['access_token'].split('-')[0]
    self.auth = OAuth1(secrets['twitter']['key'], secrets['twitter']['secret'], secrets['twitter']['access_token'], secrets['twitter']['access_secret'])
    requests.get('https://api.twitter.com/1.1/account/verify_credentials.json', auth=self.auth)

  def upload_medias(self, media_urls):
    result = []
    url = 'https://upload.twitter.com/1.1/media/upload.json?media_category=tweet_image'
    for media_url in media_urls:
      post_resp = requests.post(url, files={'media': urlopen(media_url).read()}, auth=self.auth)
      result.append(post_resp.json()['media_id'])
    return result

  def tweet(self, ad):
    url = 'https://api.twitter.com/1.1/statuses/update.json'
    post_params = {'status': "{} => {}\n{}".format(ad['title'], ad['price'], ad['url']), 'media_ids': self.upload_medias(ad['imgs']), 'lat': ad['lat'], 'long': ad['lng']}
    requests.post(url, data = post_params, auth=self.auth)

  def getLastTweet(self):
    url = "https://api.twitter.com/2/users/{}/tweets?max_results=5&tweet.fields=entities".format(self.user_id)
    return requests.request("GET", url, auth=self.auth).json()

  def extractUrlFromTweet(self, tweet):
    return tweet['entities']['urls'][0]['expanded_url']
