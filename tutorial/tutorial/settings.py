# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

FEED_EXPORT_ENCODING = 'utf-8'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'dnt': '1',
  'cache-control': 'max-age=0',
  'authority': 'www.leboncoin.fr',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
  'sec-ch-ua-platform': '"macOS"',
  'upgrade-insecure-requests': '1',
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "navigate",
  'sec-fetch-user': "?1",
  'sec-fetch-dest': "document",
  'cookie': "xtvrn=$562498$; xtant562498=1; ry_ry-l3b0nco_realytics=eyJpZCI6InJ5X0ExOEUxREJDLTA4NEEtNDU4NS1BMUU1LTEzRjdCQzMyMUQyNyIsImNpZCI6bnVsbCwiZXhwIjoxNjM4MTg5MjAzMjc0LCJjcyI6bnVsbH0%3D; uuid=16bd197b-eaf1-4762-bf61-b5767018330d; xtan562498=-undefined; _pulse2data=c47d065e-8fd9-4881-87ac-e1ad5a1daf67%2Cv%2C27410061%2C1614706762647%2CeyJpc3N1ZWRBdCI6IjIwMjAtMDgtMDVUMTM6MzA6NTZaIiwiZW5jIjoiQTEyOENCQy1IUzI1NiIsImFsZyI6ImRpciIsImtpZCI6IjIifQ..K-sFD2nHVgetWeQz6BMXQg.wjZEB0APo9GHyyJui9vYkuqBEHrGU2m71xV3sN9bB-AGrlC-s61mllxjBKS6RYBjJbNySv3KYFOIA8BfVJzy6FFP1oBblzELsNXkvYSfgSn9LUqvGzD1SnWGFmktw8SI6HXQqIAgnlOogiUPXImbe4gvwzByvs6NoRr1OPwiRxdgf4KON9pqMqCK6hLicslVDG_TZt5QUdUU_heTBISoVHUE2wzRCjEk9Pkfxc5PBiQ.2Z88KwzfOW_50mqUNnbP-Q%2C%2C0%2Ctrue%2C%2CeyJraWQiOiIyIiwiYWxnIjoiSFMyNTYifQ..2_Dtx0ojHg_C2I9HlLSF1dOx-PfJhFlGPJ4UkblJhZI; srt=eyJhbGciOiJSUzI1NiIsImtpZCI6IjA2MGMwYTgyLTk0YzktNTQ0Ny1iYjFjLWFkMGI1YzhkNGU5NSIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiJsYmMtZnJvbnQtd2ViIiwiaWF0IjoxNjE5MTkwOTc3LCJpZCI6IjVkMDFiZmM0LTkzNjItNGZjMi05ODM5LTMwNjFlOWY5YjhjNCIsImp0aSI6ImRlNTU2MDVlLWE5MDgtNDIwYi1hZGQ0LTVhODY4OTE2YjIxOCIsInJlcXVlc3RfaWQiOiIxNjYxMTQxNy1jODhmLTQ4OGMtOGRkZC05MmI4NzY0YTdkOGEiLCJzZXNzaW9uX2lkIjoiNDJkOGE5NDMtOWFkZS00ZmE2LWEzMDgtMjQ2NWQwMDM3NzZhIiwic3ViIjoibGJjOzE5NDI4MmFmLWQwNDItNDVhYi04OTI5LWVhNjNjYzUzZTk2NTsyNzQxMDA2MSJ9.wH7Ea30gQmaqDHlk2LNqvkmPI3azm_xlKmsd4MbFjxAnNX0U-qJyOeh-zrJiWiPYqjkVybSCtLuacKmdMvZlVaYayYmjAn8FOB8zpIU5ypsXJyuTz25aKM2gJdEd0ZpNSsYP5mCU-6tXvG_dQGrb-yuq-W_WZUDoC7_hFyNOG9dsiuM3GJF42FsKjbJltHzygfCy2pbRbPXL2acS4eBVWeX--v4kq0AQbgtFoUUmn8d_-tX54fENhOiI3IVEzzN5-D0eh2WDkOUSjTyIyziDiW1qvqsMpLtC1_gAEDA48skF3XtSELMLpSlRAT-H8RsZSQZ0tMcarJOL1sMm0GxpyrnXV-bJKS1kuQ3LUPWi7JBhcbYNk-W2DPoMEat1_juHNNyu03Ba3r6rokwhT1yI5B7uVjyYzctZykJzp8zUqlByTwrESxNquv_OX7-AaBYRCvbWEsZhpZhq5fwZ5rSUXzZC_C57bkJh34YRbaJ_w_2zvh798KQYPZkwTOTUy7m7ROr14E-1LWf4-cAO9lvT99dUtrYacmEqm9faypts1OXndvAeonb9UvRFVhEgy2nKyovCIURFpl02WJRFYni1UCzK-hjFiEXAXlgwMJK6qYE6-bWw0AYc4Hnp4gXfcd1Lfb1hu9krpxc0ymR9JpF285iR8MP5pipMDF9sqtOkJ2M; __Secure-InstanceId=c05f35c4-b3af-486a-8cc8-884e06a889b8; didomi_token=eyJ1c2VyX2lkIjoiMTcxMmM1OTYtOTkxMS02NTE2LWI5OTAtNzU4MWMwMmU1OWM5IiwiY3JlYXRlZCI6IjIwMjEtMTAtMjFUMDk6MzE6NDguODQ1WiIsInVwZGF0ZWQiOiIyMDIxLTEwLTIxVDA5OjMxOjQ4Ljg0NVoiLCJ2ZW5kb3JzIjp7ImRpc2FibGVkIjpbImdvb2dsZSIsImM6cm9ja3lvdSIsImM6cHVib2NlYW4tYjZCSk10c2UiLCJjOnJ0YXJnZXQtR2VmTVZ5aUMiLCJjOnNjaGlic3RlZC1NUVBYYXF5aCIsImM6Z3JlZW5ob3VzZS1RS2JHQmtzNCIsImM6cmVhbHplaXRnLWI2S0NreHlWIiwiYzpsZW1vbWVkaWEtemJZaHAyUWMiLCJjOnlvcm1lZGlhcy1xbkJXaFF5UyIsImM6c2Fub21hIiwiYzpyYWR2ZXJ0aXMtU0pwYTI1SDgiLCJjOnF3ZXJ0aXplLXpkbmdFMmh4IiwiYzpyZXZsaWZ0ZXItY1JwTW5wNXgiLCJjOnJlc2VhcmNoLW5vdyIsImM6d2hlbmV2ZXJtLThWWWh3YjJQIiwiYzphZG1vdGlvbiIsImM6dGhpcmRwcmVzZS1Tc0t3bUhWSyIsImM6aW50b3dvd2luLXFhenQ1dEdpIiwiYzpkaWRvbWkiLCJjOmpxdWVyeSIsImM6YWItdGFzdHkiLCJjOm1vYmlmeSIsImM6bGJjZnJhbmNlIiwiYzpwb3dlcmxpbmstQTNMZURNRjQiXX0sInB1cnBvc2VzIjp7ImRpc2FibGVkIjpbInBlcnNvbm5hbGlzYXRpb25jb250ZW51IiwicGVyc29ubmFsaXNhdGlvbm1hcmtldGluZyIsInByaXgiLCJtZXN1cmVhdWRpZW5jZSIsImV4cGVyaWVuY2V1dGlsaXNhdGV1ciJdfSwidmVuZG9yc19saSI6eyJkaXNhYmxlZCI6WyJnb29nbGUiXX0sInZlcnNpb24iOjIsImFjIjoiQUFBQS5BQUFBIn0=; euconsent-v2=CPObAMwPObAMwAHABBENBxCgAAAAAAAAAAAAAAAAAABigAMAAQQkGAAYAAghIQAAwABBCQAA.YAAAAAAAAAAA; include_in_experiment=false; _pbjs_userid_consent_data=2411486564781085; adview_clickmeter=search__listing__0__e0bc2375-3679-11ec-b0a4-aebac24620cb; luat=eyJhbGciOiJSUzI1NiIsImtpZCI6IjA2MGMwYTgyLTk0YzktNTQ0Ny1iYjFjLWFkMGI1YzhkNGU5NSIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfaWQiOiJsYmMtZnJvbnQtd2ViIiwiZXhwIjoxNjM1Mjc2NTczLCJpYXQiOjE2MzUyNzI5NzIsImlkIjoiYzY2MWNkOWMtNTM4MC00OWU1LTk5NGEtZTUwM2NlN2I3MDk1IiwiaW5zdGFsbF9pZCI6IjU5Mjg0MTIxLTdlNzctNDQ4MC04ZDdhLWQwOTNlYjkyNmU0NiIsImp0aSI6ImU3M2Y5MzdjLWM3MWYtNDU1NC1iMWVkLWU4ODhhYjhjZmJkNiIsInJlZnVzZWRfc2NvcGVzIjpudWxsLCJyZXF1ZXN0X2lkIjoiOWI1YjljYTItMzg0ZS00MzQzLTkwMDItMTIyYmE1Yjk4NDEzIiwic2NvcGVzIjpbImJldGEubGJjLmF1dGgudHdvZmFjdG9yLm1lLioiLCJsYmNncnAuYXV0aC5zZXNzaW9uLm1lLmRpc3BsYXkiLCJsYmNncnAuYXV0aC5zZXNzaW9uLm1lLmRlbGV0ZSIsImxiY2dycC5hdXRoLnR3b2ZhY3Rvci5tZS4qIiwibGJjLmVzY3Jvd2FjY291bnQubWFpbnRlbmFuY2UucmVhZCIsImxiYy4qLm1lLioiLCJvZmZsaW5lIiwibGJjLmF1dGguZW1haWwucGFydC5jaGFuZ2UiLCJsYmNncnAuYXV0aC50d29mYWN0b3Iuc21zLm1lLmFjdGl2YXRlIiwibGJjLiouKi5tZS4qIiwibGJjZ3JwLmF1dGguc2Vzc2lvbi5tZS5yZWFkIl0sInNlc3Npb25faWQiOiI0MmQ4YTk0My05YWRlLTRmYTYtYTMwOC0yNDY1ZDAwMzc3NmEiLCJzdWIiOiJsYmM7MTk0MjgyYWYtZDA0Mi00NWFiLTg5MjktZWE2M2NjNTNlOTY1OzI3NDEwMDYxIn0.yB_Uln7aslpWdmeSrk47cIvG2oq_rW20hv_EpIfb-l-kohqX5jIQZ4v8emeJgx2XrffzxbUfUNSai02nzPBC7EvFgETwMwbvGenKuvvJ8MU74aRAtp8Rstfyf6b9RQ5KdwY5N1i4xid5KdylwwIQmLbLgQhzz6y80R9DAAxo6sMny-otfG_GyhmOTXDICdq_8DJw1W2wIjBbBw_yEWYzOKThw38F5SzVxChLl7NKtPExRIsEqJMc3DMTgfNB2dazNLz1TjOIM44-Br70zTyE_8oTIPWsovI2JkhMcPu56rtANws6Fvxv84ncSg7lZpiYgzIFOBF7gQ0wZpmH_LRyxi6xKmUD1SyLfSHAAx2obSyCnrH_B2Po3KUCYDwqpseJyyMXlAcEcKHg656ZSwd0ySn_So7bcnDNMOShhL1BKMMcDF7WvTyvqgqU7YwkHg-jio4kPaRHs1L0_zbGPyJsa_JXL1AuXRW6UsKvjQBfIhfpmi6Cy9Ec7jKwDp8ejAhUu2f1Z3qz-9jhq9un4bap0m_J-Eq_VkVWUo7oMvemXaOEM-Fky8OG9Y9ImxHQNV7Vu8Yh-AqormUWbInLZKw8T4DROANV7vlp6SCFzG-BZZ1UDkkxcTd5CHvbtLOiO2OnFeVYm0bOhsMyai1U6M12j_5ibWDeSgtjWAqF41WecAA; ry_ry-l3b0nco_so_realytics=eyJpZCI6InJ5X0ExOEUxREJDLTA4NEEtNDU4NS1BMUU1LTEzRjdCQzMyMUQyNyIsImNpZCI6bnVsbCwib3JpZ2luIjp0cnVlLCJyZWYiOm51bGwsImNvbnQiOm51bGwsIm5zIjpmYWxzZX0%3D; atauthority=%7B%22name%22%3A%22atauthority%22%2C%22val%22%3A%7B%22authority_name%22%3A%22cnil%22%2C%22visitor_mode%22%3A%22exempt%22%7D%2C%22options%22%3A%7B%22end%22%3A%222022-11-25T18%3A56%3A20.695Z%22%2C%22path%22%3A%22%2F%22%7D%7D; utag_main=v_id:017cb65852330025446a7c13392c05078006007000bd0$_sn:11$_ss:0$_st:1635276380707$_pn:5%3Bexp-session$ses_id:1635272972085%3Bexp-session; datadome=5nl~h8zpQJ.J.dK_IptBKJ1VRnSQ~I-wffOsg8JVr-Ds2T.nihIh.gdyvPimo~gb0M63uMDqla.i3E-JB73YNLRX~bm8u6A5.dgTDPfawE",
  'if-none-match': '"6924a-nh0ah39n/DVmahYjv5AIWE/VHl8"',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'tutorial.pipelines.TutorialPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
