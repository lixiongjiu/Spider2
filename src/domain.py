#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-02 19:52:19
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from urlparse import urlparse

#Get sub domain name
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


#Get domain name
def get_domain_name(url):
    try:
        results=get_sub_domain_name(url).split('.')
        return results[-3]+'.'+results[-2]+'.'+results[-1]
    except:
        return ''


#print get_domain_name('http://blog.csdn.net/uestcyao/article/details/7876686')
