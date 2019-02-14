# -*- coding:utf-8 -*-
import logging

from twisted.enterprise import adbapi

from shop.settings import DB_SET_MAP

__author__ = "zhou"
__date__ = "2018/12/28 11:04"


class AsyncMysqlPipelines(object):
    def __init__(self, dbpool):
        self.__dbpool = dbpool

    @classmethod
    def from_crawler(cls, *args, **kwargs):
        # cls 等同于 AsyncMySQLPipeLine
        # 读取配置文件内容
        dbparams = dict(
            host=DB_SET_MAP['host'],
            db=DB_SET_MAP['database'],
            user=DB_SET_MAP['user'],
            password=DB_SET_MAP['password'],
            port=DB_SET_MAP['port'],
            charset='utf8',
        )
        # 创建mysql数据库实例
        dbpool = adbapi.ConnectionPool("pymysql", **dbparams)
        return cls(dbpool)

    def process_item(self, item, spider):
        '''
        使用twisted库提供的adbapi进行异步操作
        :param item:
        :param spider:
        :return:
        '''
        deferd = self.__dbpool.runInteraction(self.db_insert_handle, item, spider)
        deferd.addErrback(self.db_error_process, item, spider)
        return item

    def db_insert_handle(self, cursor, item, spider):
        '''
        数据库插入成功的处理函数
        :param cursor:
        :param item:
        :param spider:
        :return:
        '''
        item_name = item.get_name()
        if item_name == "ShopGood":
            insert_sql = "insert into goods(good_id,cid,good_name,show_img,good_desc,good_price)" \
                         " values(%s, %s, %s,%s,%s, %s)"
            insert_list = (
                item['good_id'],
                item['cid'],
                item['good_name'],
                item['show_img'],
                item['good_desc'],
                item['good_price'])
            cursor.execute(insert_sql, insert_list)
            return True
        elif item_name == 'ShopImage':
            insert_sql = "insert into goods_images(good_id,img) value (%s,%s)"
            insert_list = (
                item['good_id'],
                item['img']
            )
            cursor.execute(insert_sql, insert_list)
            return True
        elif item_name == 'ShopGoodSpu':
            insert_sql = "insert into goods_spu(good_id, spu_prop) value (%s, %s)"
            insert_list = (
                item['good_id'],
                item['spu_prop']
            )
            cursor.execute(insert_sql, insert_list)
            return True
        elif item_name == 'ShopGoodSku':
            insert_sql = " insert into goods_sku(good_id,sku_name,current_price)" \
                         " value (%s, %s, %s)"
            insert_list = (
                item['good_id'],
                item['sku_name'],
                item['current_price']
            )
            cursor.execute(insert_sql, insert_list)
            return True

    def db_error_process(self, error, item, spider):
        item_name = item.get_name()
        logging.error(f"spider:{spider.name}, item_name:{item_name} db_insert_handle has error with {error}")
        return False
