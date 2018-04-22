# -*- coding: utf-8 -*-
import scrapy
import json
from Panda.items import PandaItem


class GetpandatvroompictureSpider(scrapy.Spider):
    name = 'GetPandaTVRoomPicture'
    allowed_domains = ['www.panda.tv']
    base_url = "https://www.panda.tv/ajax_sort?pagenum=120&classification=lol&pageno="
    offset = 1
    start_urls = [base_url + str(offset)]
    # https://www.panda.tv/ajax_sort?pageno=1&pagenum=120&classification=yzdr

    def parse(self, response):
        re_data = json.loads(response.body)

        if re_data["errno"] == 0:
            data_list = re_data["data"]["items"]
            if len(data_list) > 0:
                for single in data_list:
                    item = PandaItem()
                    item["room_name"] = single["name"]
                    item["anchor_name"] = single["userinfo"]["nickName"]
                    item["img_url"] = single["userinfo"]["avatar"]

                    yield item

                self.offset += 1
                new_url = self.base_url + str(self.offset)
                yield scrapy.Request(new_url, callback=self.parse)
