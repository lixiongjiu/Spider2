#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-02 16:54:02
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from general import *
from urllib import *
from link_finder import LinkFinder
class Spider:
    #类属性，所有类对象共享这些属性（始终一致）
    base_url = ''
    domain_name = ''
    project_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        #创建工程所需要的文件
        self.boot()
        #第一只蜘蛛，爬取第一个网页（home页面）
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def boot():
        #创建工程主目录
        create_project_dir(Spider.project_name)
        # 创建待爬取url文件和已爬取url文件
        Spider.queue_file, Spider.crawled_file = create_data_files(
            Spider.project_name, Spider.base_url)
        #创建等待队列，已爬取队列
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + " now crawling " + page_url)
            print('Queue ' + str(len(Spider.queue)) +
                  ' | Crawled ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_str=''
        try:
            response=urlopen(page_url)

            if 'text/html' in response.info().getheader('Content-Type'):
                html_bytes=response.read()
                html_string=html_bytes.decode("utf-8")
            finder=LinkFinder(Spider.base_url)
            finder.feed(html_string)
            # 返回爬取的url集合
            return finder.get_links();
        except:
            print('Error:can not crawl page.')
            return set()


    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)
    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled,Spider.crawled_file)


#Unit test
if __name__ == '__main__':
    #Test gather_links()(passed)
    Spider.base_url='https://github.com'
    results=Spider.gather_links('https://github.com/buckyroberts/Spider/blob/master/link_finder.py')
    for url in results:
        print url
