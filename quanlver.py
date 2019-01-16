#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''

基础网页图片文件爬虫

'''
from bs4 import BeautifulSoup
import urllib.request
import ssl
import requests

# http请求
def getHttp(url, headers):
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read()
    return imageFilter(html)

# 抓取图片
def imageFilter(html, classStr = "img", classField = "image", label='data-original'):
    soup = BeautifulSoup(html, 'lxml')

    images = soup.find_all(classStr, {"class": classField})

    list = []

    for img in images:
        list.append(img[label])

    return list

# 下载图片
def download(list):
    for l in list:
        r = requests.get(l)
        image_name = l.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            f.write(r.content)
        print("OK")
if __name__ == "__main__":
    # 忽略ssl 证书
    ssl._create_default_https_context = ssl._create_stdlib_context
    url = "https://fabiaoqing.com/search/search/keyword/%E6%9D%83%E5%BE%8B%E4%BA%8C"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    download(getHttp(url, headers))
