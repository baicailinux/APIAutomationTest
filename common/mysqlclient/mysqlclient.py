#-*- coding:utf-8 -*-
#!/usr/bin/python
import pymysql
class MysqlClient(object):
    def __init__(self,host,port,username,password,dbname,charset='utf8'):
        self.host=host
        self.port=port
        self.username=username
        self.password=password
        self.dbname=dbname
        self.charset=charset
        self.conn=pymysql.connect(host=self.host,port=int(self.port),user=self.username,passwd=self.password,db=self.dbname,charset=self.charset)
        self.cursor=self.conn.cursor()

    def executeSQL(self,sql):
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        return result