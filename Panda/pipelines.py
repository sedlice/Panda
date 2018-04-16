# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from Panda.settings import IMAGES_STORE


class PandaPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        imgUrl = item["img_url"]
        yield scrapy.Request(imgUrl)

    def item_completed(self, results, item, info):
        status = results[0][0]
        if status:
            image_name = item["anchor_name"]
            image_path = results[0][1]["path"]
            suffix = image_path.split(".")[-1]
            os.rename(IMAGES_STORE + image_path, IMAGES_STORE + image_name + "." + suffix)
            return item


