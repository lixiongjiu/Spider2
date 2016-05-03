#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-02 15:00:16
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from HTMLParser import HTMLParser
from urlparse import urlparse
from urlparse import urljoin


class LinkFinder(HTMLParser):

    def __init__(self, base_url):
        HTMLParser.__init__(self)
        self.base_url = base_url
        self.links = set()

    # When we call HTMLParser feed(),this function is called when opening tag
    # is <a>
    def handle_starttag(self,tag,attrs):
        if tag=='a':
            for (attribute,value) in attrs:
                if attribute =='href':
                    url=urljoin(self.base_url,value)
                    self.links.add(url)

    def get_links(self):
        return self.links

#Test(passed)
if __name__ == '__main__':
    from urllib import urlopen
    response=urlopen('https://github.com/buckyroberts/Spider/blob/master/link_finder.py')
    link_finder=LinkFinder('https://github.com')
    html_str=response.read().decode('utf-8')
    link_finder.feed(html_str)
    results=link_finder.get_links()
    for url in results:
        print url


