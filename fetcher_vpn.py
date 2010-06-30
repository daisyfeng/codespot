#!/usr/bin/env python

import re
import urllib,urllib2
import time,random
import MySQLdb

def fetch(url,data = None):
    agent = "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/6.0.447.0 Safari/534.2"
    headers = {'User-Agent':agent}
    if data:
        data = urllib.urlencode(data)
    
    response = urllib.urlopen(url,data)
    html = response.read()
    info = response.info()
    response.close()
    return [html,info]

def register(form = None):
    url = "http://billing.macrovpn.com/reg.php?cont=store_user"
    if form:
        pass
    else:
        form = user()
    r = fetch(url,form)
    #print form['username'],'----',form['password1']
    #print r[0]
    if r[0].find('created'):
        return "account:%s\npassword:%s\n"%(form['username'],form['password1'])
    else:
        return "bad service\n"

def user(feed = time.time(), feed2 = random.random()):
    usename = str(feed)[0:10]+str(feed2)[2:5]
    passwd = str(feed2)[3:6]+str(feed)[0:10]
    email =  str(feed2)[2:6]+'@qq.com'
    fname = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz',6))
    lname = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz',4))
    addr = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz',12))
    city = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz',3))
    post = '020'
    mobile = ''.join(random.sample('912345678912345657896',11))
    data = {'username':usename,'password1':passwd,'password2':passwd,'firstname':fname,'lastname':lname,'address':addr,'city':city,'zip':post,'country':'China','mobile':mobile,'email':email,'srvid':19,'acceptterms':'1'}
    return data


def query(sql):
    conn = MySQLdb.connect('localhost','root','123',db='fetcher')
    c  = conn.cursor()
    r = c.execute(sql)
    c.close()
    conn.close()
    return r



