# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy import Request

from items import ShopGood, ShopGoodSku, ShopGoodSpu, ShopImage
from utils.bshead import create_bs_driver
from utils.helper import create_fingerprint, img_replace

url_list = ['9987,653,655',
            '670,671,672',
            '737,794,798',
            '1672,2576,12071',
            '1316,1381,1396']


class JdSpider(scrapy.Spider):
    name = 'JD'
    allowed_domains = ['jd.com']
    start_urls = ['https://list.jd.com/list.html?cat=']

    def __init__(self):
        scrapy.Spider.__init__(self, self.name)
        self.driver = create_bs_driver()
        self.driver.set_page_load_timeout(40)

    def __del__(self):
        self.driver.quit()

    def start_requests(self):
        """
        #重写初始化url请求，携带上信息，下载中间件能识别
        :return:
        """
        global url_list
        for url in self.start_urls:
            for url1 in url_list:
                urls = url + url1
                r = scrapy.Request(url=urls, meta={'type': 'home'}, callback=self.parse,
                                   dont_filter=True)
                yield r

    # 商品表
    def parse(self, response):
        global url_list
        cid = None
        if url_list[0] in response.url:
            cid = 1
        elif url_list[1] in response.url:
            cid = 2
        elif url_list[2] in response.url:
            cid = 3
        elif url_list[3] in response.url:
            cid = 4
        elif url_list[4] in response.url:
            cid = 5
        good_list = response.xpath('//div[@id="plist"]/ul/li')
        for good in good_list:
            # 标题
            # good_title = good.xpath("./div/div/a/@title").extract_first()
            good_image_url = good.xpath("./div/div/a/img/@data-lazy-img | ./div/div/a/img/@src").extract_first()
            if good_image_url == 'done':
                good_image_url = good.xpath("./div/div/a/img/@src").extract_first()
            good_image_url = response.urljoin(good_image_url)

            # 对图片url进行sha1加密
            show_img = create_fingerprint(good_image_url)
            # 商品价格
            good_price = good.xpath("./div/div[@class='p-price']/strong[1]/i/text()").extract_first()
            # 商品简介
            desc = good.xpath("./div/div[4]/a/em/text() | "
                              "./div/div[3]/a/em/text()").extract()

            # good_desc = desc.strip()

            good_desc = [name.strip() for name in desc if len(name.strip()) > 0][0]

            good_name = good_desc.split(" ")[0]

            # 详情页url
            # //div[@id="plist"]/ul/li/div/div/div[2]/div/div/a/@href
            # //div[@id="plist"]/ul/li/div/div[1]/a/@href

            good_detail_url = good.xpath("./div/div[1]/a/@href").extract_first()

            good_detail_url = response.urljoin(good_detail_url)

            good_id = re.search("(\d+)", good_detail_url).group()

            r = Request(url=good_detail_url, meta={'type': 'detail', 'good_id': good_id},
                        callback=self.parse_good_detail, dont_filter=True)
            yield r

            good = ShopGood(good_id=good_id,
                            cid=cid,
                            good_name=good_name,
                            # good_title=good_title,
                            good_price=good_price,
                            show_img=show_img,
                            good_desc=good_desc,
                            good_image_url=good_image_url)
            yield good

    # 商品详情页
    def parse_good_detail(self, response):

        # good_id = re.search("(\d+)", response.url).group()

        good_id = response.meta.get('good_id')

        sku_name = response.xpath("//div[@class='sku-name']/text()").extract()

        # sku_name = [s_name.strip() for s_name in sku_name][0]
        sku_name = [s_name.strip() for s_name in sku_name if len(s_name.strip()) > 0][0]

        # 现价
        current_price = response.xpath("//div[@class='dd']/span[@class='p-price']/span[2]/text()").extract_first()
        # 原价
        # current_price = response.xpath("//div[@class='dd']/span[@class='pricing']/del/text()").extract_first()
        # current_price = int(str(current_price)[1:])
        sku = ShopGoodSku(good_id=good_id,
                          sku_name=sku_name,
                          current_price=current_price)
        yield sku

        # 商品spu表
        spu_list = response.xpath \
            ("//div[@class='p-parameter']/ul[@class='parameter2 p-parameter-list']/li/text()").extract()
        spu_prop = str(spu_list)
        spu = ShopGoodSpu(good_id=good_id, spu_prop=spu_prop)
        yield spu

        # 图片表
        img_list = response.xpath("//div[@class='spec-items']/ul/li/img/@src").extract()
        for img_url in img_list:
            img_url = response.urljoin(img_url)
            # 处理详情页图片的尺寸问题
            p = re.compile(r"s\d{2}x\d{2}_jfs")
            img = img_replace(img_url, p)
            image = create_fingerprint(img)
            img = ShopImage(good_id=good_id, img=image, img_url=img)
            yield img
