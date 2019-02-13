# -*- coding:utf-8 -*-
import datetime
import random

__author__ = "zhou"
__date__ = "2019/1/24 8:57"


def product_code():
    data_code = datetime.datetime.now().strftime('%m%d')
    random_code = random.randint(100000, 999999)
    product = data_code + str(random_code)
    return product


if __name__ == '__main__':
    a = product_code()
    print(a,type(a))