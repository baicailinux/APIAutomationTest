#-*- coding:utf8
import argparse
import pytest
import os
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('-k','--keyword',help='只执行匹配关键字的用例，会匹配文件名、类名、方法名',type=str)
    parser.add_argument('-d','--dir',help='指定要测试的目录',type=str)
    args=parser.parse_args()

    keyword=None
    dir='cases/'
    if args.keyword:
        keyword=args.keyword
        if args.dir:
            dir=args.dir
        pytest.main(['-c','config/pytest.ini','--alluredir','output/','-k',keyword,dir])
        #pytest.main(['-c', 'config/pytest.ini', '--show-capture', 'no', '--alluredir', 'output/', '-k', keyword, dir])
    else:
        if args.dir:
            dir=args.dir
        pytest.main(['-c', 'config/pytest.ini','--alluredir', 'output/', dir])
        #pytest.main(['-c', 'config/pytest.ini', '--show-capture', 'no', '--alluredir', 'output/', dir])