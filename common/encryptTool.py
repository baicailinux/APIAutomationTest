#-*- coding:utf8 -*-
import hashlib
import base64

def md5Encode(str):
    """
    md5加密，32位
    :param str:
    :return:
    """
    m=hashlib.md5()
    m.update(str)
    return m.hexdigest()

def base64Encode(str):
    return base64.b64encode(bytes(str))

def base64Decode(base64Str):
    return base64.b64decode(base64Str)
