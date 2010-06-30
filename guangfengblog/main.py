#!/usr/bin/env python
#-*- encoding:utf-8 -*-
# Copyright 2010 Guang Feng (breeze.guangfeng@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.appengine.ext.webapp import util
import wsgiref.handlers, urllib, re, base64
from google.appengine.ext import webapp
from google.appengine.api import urlfetch
from google.appengine.api import urlfetch_errors
from google.appengine.ext import db

class Contents(db.Model):
    uri = db.StringProperty(required=True,indexed=True)
    content = db.BlobProperty(required=True)
    update = db.StringProperty(required=True)
    ctype = db.StringProperty(required=True) 

class MainHandler(webapp.RequestHandler):

    headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727; Maxthon 2.0)'}
    
    def get(self):
        url = self.request.get('u')
        f = self.request.get('z')
        
        if not url:
            url = "http://gfnpad.blogspot.com"
        if f and url:
            try:
                resp = self.fetchall(url)
                self.response.headers['Content-Type'] = resp.ctype
                if resp.ctype.find('html'):
                    self.response.out.write(self.parser(resp.content))
                else:
                    self.response.out.write(resp.content)
            except:
                self.err(500)
                return
            
        try:
            resp = self.fetchone(url)
            self.response.headers['Content-Type'] = resp.headers['Content-Type']
            self.response.out.write(self.parser(resp.content))
        except:
            self.err(404)
            return

    def err(self, status):
        self.response.out.write("HTTP/1.1 %d %s\r\n" % (status, \
                                self.response.http_status_message(status)))
        self.response.out.write("Server: Blogspot-fetch 1.2\r\n")
        
        self.response.out.write("EXAMPLE https://guangfengblog.appspot.com?u=http://www.google.com\n")

    def fetchone(self,url,data = None,method = 'GET'):
        for _ in range(3):
            try:
                resp = urlfetch.fetch(url, data, method, self.headers, False, False)
                break
            except urlfetch_errors.ResponseTooLargeError:
                self.err(413)
                return
            except Exception:
                continue
        
        return resp

    def parser(self,html):
        p = re.compile("[a-zA-z]+://(\\w+(-\\w+)*)(\\.(\\w+(-\\w+)*))*(\\?\\S*)?")
        return p.sub(replace,html)
    

    def fetchall(self,url):
        resp = self.fetchone(url)
        items = db.GqlQuery("SELECT * FROM Contents "
                            "WHERE uri = :1 AND update = :2",url,resp.headers['Last-Modified'])
        if items.count() == 0:
            item = Contents(uri = url,content = resp.content,update = resp.headers['Last-Modified'],ctype=resp.headers['Content-Type'])
            db.put(item)
            return item
        
        return items[0]
            


def replace(reobject):
    uri = reobject.group(0)
    #return "http://localhost:8080/?z=1&u="+uri
    return "http://guangfengblog.appspot.com?z=1&u="+uri
    
        

def main():
    application = webapp.WSGIApplication([('/', MainHandler)])
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
