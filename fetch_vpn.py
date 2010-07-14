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
        return [form['username'],form['password1']]
    else:
        return 

def user(feed = time.time(), feed2 = random.random()):
    usename = str(feed)[0:10]+str(feed2)[2:5]
    passwd = str(feed2)[3:6]+str(feed)[0:10]
    email =  "mickey.fetchbot+"+str(feed2)[2:6]+'@gmail.com'
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

def table():
    sql = """CREATE TABLE vpn_items (
`id` int not null auto_increment,
`account` varchar(13) not null,
`password` varchar(13) not null,
`ip1` varchar(15),
`ip2` varchar(15),
`ip3` varchar(15),
`used` tinyint,
`update` varchar(10) not null,
primary key (`id`),
unique key (`account`)
)"""
    r = query(sql)
    return

def store(res):
    account,password = res
    if account and password:
        update = str(time.time())[0:10]
        sql = "INSERT INTO vpn_items (`account`,`password`,`used`,`update`) VALUES ('%s','%s',0,'%s')"%(account,password,update)
        r = query(sql)
        print "ACCT:%s\nPASD:%s\nREST:"%(account,password),r
    else:
        print "no account or passwor!\n"
    return

if __name__ == '__main__':
    import sys
    cmd = sys.argv[1]
    if cmd == 'help':
        print "help: show help;\ninit: init database tables;\nrun: get one vpn account into database\n"
    elif cmd == 'init':
        table()
    elif cmd == 'run':
        result = register()
        if result:
            store(result)
        else:
            print "something failed!\n"
    else:
        print "%s is not allowed"%cmd
