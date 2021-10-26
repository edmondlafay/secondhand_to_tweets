import scrapy
import json

class QuotesSpider(scrapy.Spider):
  name = "quotes"
  start_urls = [
      'https://www.leboncoin.fr/recherche?category=2&regdate=min-1989&mileage=min-175000&price=100-9000',
  ]

  def parse(self, response):
    ads = json.loads(response.css('#__NEXT_DATA__::text').get())["props"]["pageProps"]["searchData"]["ads"]
    for ad in ads:
      if len(ad['images']['urls_thumb'])<1:
        continue

      yield {
        'title': ad['subject'],
        'url': ad['url'],
        'price': "%d€" % (ad['price_cents']/100),
        'imgs': ad['images']['urls_thumb'][0:3],
      }

    next_page = response.xpath('//a[@title="Page suivante"]/@href').get()
    if next_page is not None:
        yield response.follow(next_page, callback=self.parse)
