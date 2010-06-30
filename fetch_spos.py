#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import re
import urllib
import MySQLdb
from BeautifulSoup import BeautifulSoup

def insert(sql):
    conn = MySQLdb.connect('localhost','root','123',db='fetcher')
    c  = conn.cursor()
    r = c.execute(sql)
    c.close()
    conn.close()
    return r

def spoor(url,start = None,limit = None):
    """defined by the target website"""
    urls = [url]
    if limit:
        urls.extend([url[0:-6]+'_'+str(i)+".shtml" for i in range(1,limit)])
    return urls

def items(url):
    itemre = re.compile(r"http://chinese.spos.com.cn/\d{8}/\d{5}.html")
    req = urllib.urlopen(url)
    update = req.info().headers()[1].strip()
    html = req.read()
    req.close()
    sql = "insert into spos_spoor (url,hash,update)values(%s,%s,%s)"%(url,hash(url),update)
    if insert(sql):
        print ("%s has parserd\n"%url)
    return itemre.findall(html)
    

def item(url):
    html = urllib.urlopen(url)
    h = html.read().decode('gbk').encode('utf8')
    #update = html.info().headers()[1].strip()
    html.close()
    end = h.find("<div class=\"bcj\">")
    print end
    soup = BeautifulSoup(h)
    hash_url = soup.find('h1').string
    plist = soup.findAll('p',)

    for i in plist:
            if i.parent.contents[1].name == 'script':
                print i

item('http://menu.spos.com.cn/soup/20091019/soup25104.shtml')


