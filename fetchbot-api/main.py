from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import os,hashlib,base64,urlparse,urllib
from google.appengine.ext.webapp import template
from google.appengine.ext import db

class Site(db.Model):
    name = db.StringProperty()
    url = db.StringProperty()
    keyid = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class Req(db.Model):
    keyid = db.StringProperty(multiline=True)
    url = db.StringProperty()
    refer = db.StringProperty()
    agent = db.StringProperty()
    remoteip = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)

class App(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'main.html')
        self.response.out.write(template.render(path,None))
    
    def post(self):
        sites = Site()
                    
        query = db.GqlQuery("SELECT __key__ FROM Site WHERE name = :1 ",
                    self.request.get('name'))
        if not self.request.get('name') or  query.count() > 1:
            template_value = {'info':"Sorry your identifier name has been taken."}
            path = os.path.join(os.path.dirname(__file__), 'main.html')
            self.response.out.write(template.render(path,template_value))
        else:
            if not urlparse.urlparse(self.request.get('url')).netloc:
                sites.url = urlparse.urlparse("http://"+self.request.get('url')).netloc
            else:
                sites.url = urlparse.urlparse(self.request.get('url')).netloc
            m = hashlib.md5()
            m.update(sites.url)
            sites.keyid = m.hexdigest()+'|'+base64.encodestring(self.request.get('name'))
            sites.name = self.request.get('name')
            sites.put()
            code = """<script type="text/javascript" src="http://fetchbot-api.appspot.com/statics/api.js"></script>
                      <script type="text/javascript">
                      api.key='%s';
                      api.init();
                      </script>"""%(sites.keyid)
            template_value = {'appkey':sites.keyid,'code':code}
            path = os.path.join(os.path.dirname(__file__), 'success.html')
            self.response.out.write(template.render(path,template_value))

class Analytics(webapp.RequestHandler):
    def get(self):
        apikey = self.request.get('key')
        url = urlparse.urlparse(self.request.get('url')).netloc
        m = hashlib.md5()
        m.update(url)
        name  = base64.decodestring(apikey.split('|')[1])
        query = db.GqlQuery("SELECT * FROM Site WHERE name = :1 ",
                    name)
        
        if (apikey.split('|')[0] == m.hexdigest()) and query.count > 0:
            r = Req()
            r.url = url
            r.keyid = apikey
            r.refer = self.request.get('refer')
            r.agent = self.request.headers['User-Agent']
            r.remoteip = self.request.remote_addr
            r.put()
            self.response.out.write("ok \n")
        else:
            self.response.out.write(m.hexdigest())
    def post(self):
        self.response.out.write("index \n")
        

application = webapp.WSGIApplication(
                                     [('/', App),('/tj',Analytics)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
