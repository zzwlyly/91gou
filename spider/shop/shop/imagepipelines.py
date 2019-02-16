# -*- coding:utf-8 -*-
from scrapy.pipelines.images import ImagesPipeline

__author__ = "zhou"
__date__ = "2018/12/28 9:35"

import scrapy


class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        item_name = item.get_name()
        if item_name == 'ShopGood':
            good_image_url = item.get('good_image_url', None)
            if good_image_url != None:
                print(good_image_url)
                yield scrapy.Request(url=good_image_url)
        elif item_name == 'ShopImage':
            img_url = item.get('img_url', None)
            if img_url != None:
                print(img_url)
                yield scrapy.Request(url=img_url)
