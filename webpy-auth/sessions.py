#!/usr/bin/env python
"""
Session Management with Relation DataBase Backend
"""
import os, time, datetime, random, base64
import hashlib

__all__ = ['SessionDB']

sha1 = hashlib.sha1
maxlife  = 60;


class SessionDB(Storage):
    """Store for saving a session in database
       Needs a table with the following columns:

       id bigint not null auto_increment, 
       userid int not null, 
       ip varchar(15) not null, 
       createtime int not null, 
       updatetime int not null, 
       keyval varchar(41) not null, primary key(id)
    """
    
    def __init__(self,db,table_name = 'session'):
        self.db = db
        self.table = table_name
    
    def updatets(self,key):
        now = int(time.time())
        return self.db.update(self.table, where="keyval=$key", updatetime=now, vars=locals())

    def __contains__(self,key):
        before = int(time.time()) - maxlife
        data = self.db.select(self.table, where="keyval=$key",vars=locals())
        if bool(list(data)) and data[0].updatetime > before:
            self.updatets(key)
            return True
        else:
            self.__delitem__(data[0].id)
            return None

    def __getitem__(self,key):
        try:
            s = self.db.select(self.table, where="keyval=$key", vars=locals())[0]
            self.updatets(key)
        except IndexError:
            raise KeyError
        else:
            return s

    def newitem (self,**kw):
        now = int(time.time())
        sha1.update(kw['userid'] + str(now) + 'simple')
        keyval = sha1.hexdigest()
        return db.insert(self.table,ip = ip,createtime = now,updatetime = now,keyval = keyval)
    
    def __delitem__(self, key):
        self.db.delete(self.table, where="id=$key", vars=locals())
