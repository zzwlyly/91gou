# -*- coding:utf-8 -*-
__author__ = "zzw"
__date__ = "2018/12/25 17:10"

import requests

import threading

from threading import Lock

import queue

g_lock = Lock()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


def fetch_web_data(url, proxy=None, timeout=10):
    try:
        r = requests.get(url, headers=headers, timeout=timeout, proxies=proxy)
        return r.text

    except Exception as e:
        print(f"fetch_web_data has error with url: {url}, error: {e}")
        return None


class FetchProxyListThread(threading.Thread):
    '''
    http://www.thebigproxylist.com/members/proxy-api.php?output=all&user=list&pass=8a544b2637e7a45d1536e34680e11adf
    获取代理数据
    '''

    def __init__(self, url, mq):
        threading.Thread.__init__(self)
        self.__url = url
        self.__mq = mq

    def run(self):
        '''
        下载接口数据保存到mq
        :return:
        '''

        data = fetch_web_data(url=self.__url)
        ip_pool_list = data.split('\n')
        [self.__mq.put(ip_pool.split(',')[0]) for ip_pool in ip_pool_list]


CHECK_URL = 'http://httpbin.org/get?x=2&y=4'


class IpProxyCheckThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.__queue = queue

    def run(self):
        global g_lock
        while True:
            # ip_port = None
            # try:
            #     ip_port = self.__queue.get(timeout=10)
            # except Exception as e:
            #     break
            ip_port = self.__queue.get()
            print(f"current ip_port is {ip_port}")
            proxy = {
                'http': ip_port
            }

            data = fetch_web_data(CHECK_URL, proxy=proxy, timeout=5)
            if data is None:
                print(f"当前IP对 {ip_port} 检验失败！丢弃")
                continue
            print(f"当前IP对 {ip_port} 检验成功！保存")
            # 上锁
            g_lock.acquire()
            with open("proxy_list.txt", "a+", encoding="utf-8") as f:
                f.write(f"{ip_port}\n")
            # 放锁
            g_lock.release()


def process():
    mq = queue.Queue()
    url = 'http://www.thebigproxylist.com/members/proxy-api.php?output=all&user=list&pass=8a544b2637e7a45d1536e34680e11adf'
    fth = FetchProxyListThread(url, mq)

    thread_num = 10

    thread_list = []
    for i in range(thread_num):
        t = IpProxyCheckThread(mq)
        thread_list.append(t)

    fth.start()
    [th.start() for th in thread_list]

    fth.join()
    [th.join() for th in thread_list]

    print("all work has done")


if __name__ == '__main__':
    process()
