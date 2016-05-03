#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-02 20:09:12
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import threading
from Queue import Queue
from spider import Spider
from domain import *
from general import *
import os

PROJECT_NAME='ssdut'
HOME_PAGE='http://ssdut.dlut.edu.cn'
DOMAIN_NAME=get_domain_name(HOME_PAGE)
BASE_DIR=os.path.abspath('../target')+'/'
QUEUE_FILE=BASE_DIR+PROJECT_NAME+'/queue.txt'
CRAWLED_FILE=BASE_DIR+PROJECT_NAME+'/crawled.txt'
NUMBER_OF_THREADS=8

queue=Queue()

Spider(PROJECT_NAME,HOME_PAGE,DOMAIN_NAME)

#Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t=threading.Thread(target=work)
        t.daemon=True
        t.start()

#Do the next job in the queue
def work():
    while True:
        url=queue.get()
        Spider.crawl_page(threading.currentThread().name,url)
        queue.task_done()

# 以下两个函数一直迭代直到队列中没有url
#Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

#Check if there are items in the queue,if so crawl them
def crawl():
    queue_links=file_to_set(QUEUE_FILE)
    if len(queue_links)>0:
        print(str(len(queue_links))+' links in the queue')
        create_jobs()


create_workers()
crawl()

