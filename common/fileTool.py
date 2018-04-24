#!-*- coding:utf8 -*-
import json
def writeObjectIntoFile(obj,filePath):
    """
    将对象转为json字符串，写入到文件
    :param obj:
    :param filePath:
    :return:
    """
    str = json.dumps(obj, default=lambda obj: obj.__dict__)
    with open(filePath,'w') as f:
        f.write(str)
        f.close()

def readJsonFromFile(filePath):
    """
    从文件里读取json字符串
    :param filePath:
    :return:
    """
    with open(filePath,'r') as f:
        result=f.read()
        f.close()
    result=json.loads(result)
    return result

def truncateFile(fielPath):
    """
    清空文件
    :param fielPath:
    :return:
    """
    with open(fielPath,'r+') as f:
        f.truncate()
        f.close()