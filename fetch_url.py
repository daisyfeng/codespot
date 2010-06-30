#!/use/bin/env python
#-*- encoding:utf-8 -*-

import urllib2,re
from urlparse import urlparse

def find_url(url):
    re_a = re.compile(r'<a.+?href=.+?>.+?</a>')        
    html = fetch(url)
    
    tags = re_a.findall(html)
    return map(lambda x:parse(x,url),tags)
    
def parse(item,url = None,chartset = 'utf8'):
    re_herf = re.compile("href=\"(\S.*?)\"")
    re_title = re.compile(r'(?<=>).*?(?=</a>)')
    h = re_herf.findall(item)
    t = re_title.findall(item)
    if h:
        uobj = urlparse(h[0])
        if (not uobj.netloc and uobj.path):
            uri = urlparse(url).netloc + uobj.path
        else:
            uri = uobj.geturl()
    else: uri = ''
    if t:
        title = t[0]
    else: title = ''
    
    return (uri,title)
        

def fetch(url):
    try:
        f = urllib2.urlopen(url)
        return f.read()
    except urllib2.HTTPError,err:
        print err.read()


print find_url('http://www.163.com')
