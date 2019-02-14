# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 商品表
class ShopGood(scrapy.Item):
    good_id = scrapy.Field()
    # 商品分类id
    cid = scrapy.Field()
    # 商品名
    good_name = scrapy.Field()
    # 商品图片
    show_img = scrapy.Field()
    # 商品简介
    good_desc = scrapy.Field()
    # 商品价格
    good_price = scrapy.Field()
    # 商品标题
    good_title = scrapy.Field()
    # 商品图片url
    good_image_url = scrapy.Field()

    def get_name(self):
        return ShopGood.__name__


# 图片表item
class ShopImage(scrapy.Item):
    # 商品id
    good_id = scrapy.Field()
    # 详情页图片
    img = scrapy.Field()
    img_url = scrapy.Field()

    def get_name(self):
        return ShopImage.__name__


# 商品分类表item
class ShopGoodType(scrapy.Item):
    cid = scrapy.Field()
    name = scrapy.Field()
    values = scrapy.Field()

    def get_name(self):
        return ShopGoodType.__name__


# 商品spu表
class ShopGoodSpu(scrapy.Item):
    good_id = scrapy.Field()
    spu_prop = scrapy.Field()

    def get_name(self):
        return ShopGoodSpu.__name__


# 商品sku表
class ShopGoodSku(scrapy.Item):
    good_id = scrapy.Field()
    sku_name = scrapy.Field()
    # original_price = scrapy.Field()
    current_price = scrapy.Field()

    def get_name(self):
        return ShopGoodSku.__name__
