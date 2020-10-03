# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
#from scrapy_djangoitem import DjangoItem
from restmember.models import Member

class CrawlingItem(scrapy.Item):
    django_model = Member

    name = scrapy.Field()
    birth_date = scrapy.Field()
    birth_place = scrapy.Field()
    profession = scrapy.Field()
    languages = scrapy.Field()
    political_force = scrapy.Field()
    email = scrapy.Field()

    