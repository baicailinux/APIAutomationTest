#-*- coding:utf8 -*-
import datetime
import time

class DateTimeTool():
    @classmethod
    def getNowTime(cls,format='%Y-%m-%d %H:%M:%S'):
        return datetime.datetime.now().strftime(format)

    @classmethod
    def getNowDate(cls):
        return datetime.date.today()

    @classmethod
    def getNowTimeStampWithSecond(cls):
        return int(time.time())

    @classmethod
    def getNowTimeStampWithMillisecond(cls):
        return int(round(time.time()*1000))

    @classmethod
    def getHowDaysAgo(cls,howDaysAgo=0,format='%Y-%m-%d'):
        tmpDateTime=datetime.datetime.now()-datetime.timedelta(days=howDaysAgo)
        return tmpDateTime.strftime(format)
