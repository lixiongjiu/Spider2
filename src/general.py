#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-05-02 11:18:38
# @Author  : lixiongjiu (lixiongjiu@foxmail.com)
# @Link    : http://example.org
# @Version : $Id$

import os

base_dir = os.path.abspath('../target') + '/'

# Each website you crawl is a seperate project


def create_project_dir(project_name):
    if not os.path.exists(base_dir + project_name):
        print("Creating project " + project_name)
        os.mkdir(base_dir + project_name)

    # 返回创建的工程的位置
    return base_dir + project_name


# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = base_dir + project_name + "/queue.txt"
    crawled = base_dir + project_name + '/crawled.txt'

    paths = list()  # 返回记录两个txt文件的位置
    paths.append(queue)
    paths.append(crawled)

    if not os.path.isfile(queue):
        write_to_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_to_file(crawled, '')

    return paths

# Write data(Param:data) to file(Param:path)


def write_to_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
        f.close()

# Write data onto an existing file


def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data + '\n')


def delete_file_contents(path):
    with open(path, 'w') as f:
        pass
# delete_file_contents('F://sample_new0408.txt')

# Read a file and convert each line to set items


def file_to_set(path):
    results = set()
    with open(path, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# Iterate through set,each item will be a new line of file


def set_to_file(links, path):
    for link in links:
        append_to_file(path, link)

#Unit测试
if __name__ == '__main__':
    #Test create_project_dir(passed)
    create_project_dir('baidu')

    #Test create_data_files & write_to_file(passed)
    create_data_files('baidu','www.baidu.com')

    #Test append_to_file(passed)
    append_to_file('../target/baidu/queue.txt','test')
    append_to_file('../target/baidu/queue.txt','test')


