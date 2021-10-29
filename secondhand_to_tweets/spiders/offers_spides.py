import scrapy
import json
from secondhand_to_tweets.twitter import Twitter

class OfferSpider(scrapy.Spider):
  name = "offers"
  start_urls = [
      'https://www.leboncoin.fr/recherche?category=2&regdate=min-1989&mileage=min-175000&price=100-9000',
  ]

  def __init__(self, *a, **kw):
    super(OfferSpider, self).__init__(*a, **kw)
    self.twitter = Twitter()
    previous_tweets = self.twitter.getLastTweet()['data']
    self.already_tweeted_offers = list(map(self.twitter.extractUrlFromTweet, previous_tweets))

  def parse(self, response):
    ads = json.loads(response.css('#__NEXT_DATA__::text').get())["props"]["pageProps"]["searchData"]["ads"]
    for ad in ads:
      if 'urls_thumb' not in ad['images']:
        continue
      if len(ad['images']['urls_thumb'])<1:
        continue

      url = ad['url']
      if url in self.already_tweeted_offers:
        return

      self.twitter.tweet({
        'title': ad['subject'],
        'url': ad['url'],
        'price': "%d€" % (ad['price_cents']/100),
        'imgs': ad['images']['urls'][0:3],
        'lat': ad['location']['lat'],
        'lng': ad['location']['lng'],
      })

    next_page = response.xpath('//a[@title="Page suivante"]/@href').get()
    if next_page is not None:
        yield response.follow(next_page, callback=self.parse)
