#!-*- coding:utf8 -*-
import re
import uuid
import json


class StrTool():

    @classmethod
    def getStringWithLBRB(cls, sourceStr, lbStr, rbStr, offset=0):
        """
        根据字符串左右边界获取内容
        offset:要获得匹配的第几个数据,默认第一个
        :param sourceStr:
        :param lbStr:
        :param rbStr:
        :param offset:
        :return:
        """
        regex = '([\\s\\S]*?)'
        r = re.compile(lbStr + regex + rbStr)
        result = r.findall(sourceStr)
        if str(offset) == 'all':
            return result
        else:
            if len(result) >= offset and len(result) != 0:
                return result[offset]
            else:
                return None

    @classmethod
    def addUUID(cls, source):
        """
        字符串加上uuid
        :param source:
        :return:
        """
        return source + '_' + str(uuid.uuid4())

    @classmethod
    def objectToJsonStr(cls, object):
        """
        将类对象转为json字符串
        :param object:
        :return:
        """
        return json.dumps(object, default=lambda obj: obj.__dict__)
