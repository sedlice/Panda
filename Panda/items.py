# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PandaItem(scrapy.Item):
    # define the fields for your item here like:
    room_name = scrapy.Field()
    anchor_name = scrapy.Field()
    img_url = scrapy.Field()
