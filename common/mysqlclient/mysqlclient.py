# -*- coding:utf-8 -*-
# !/usr/bin/python
import pymysql


class MysqlClient(object):
    def __init__(self, host, port, username, password, dbname, charset='utf8'):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._dbname = dbname
        self._charset = charset
        self._conn = pymysql.connect(host=self._host, port=int(self._port), user=self._username, passwd=self._password,
                                     db=self._dbname, charset=self._charset)
        self._cursor = self._conn.cursor()

    def executeSQL(self, sql):
        self._cursor.execute(sql)
        result = self._cursor.fetchall()
        self._conn.commit()
        return result

    def closeAll(self):
        self._cursor.close()
        self._conn.close()
