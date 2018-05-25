#-*- coding:utf8
from init.init import init
import argparse
import pytest
import sys

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('-k','--keyword',help='只执行匹配关键字的用例，会匹配文件名、类名、方法名',type=str)
    parser.add_argument('-d','--dir',help='指定要测试的目录',type=str)
    args=parser.parse_args()

    #初始化
    print '开始初始化......'
    init()
    print '初始化完成......'

    #执行pytest
    print '开始测试......'
    keyword=None
    dir='cases/'
    exit_code=None
    if args.keyword:
        keyword=args.keyword
        if args.dir:
            dir=args.dir
        exit_code=pytest.main(['-c','config/pytest.ini','-v','--alluredir','output/','-k',keyword,dir])
        #pytest.main(['-c', 'config/pytest.ini', '-v','--show-capture', 'no', '--alluredir', 'output/', '-k', keyword, dir])
    else:
        if args.dir:
            dir=args.dir
        exit_code=pytest.main(['-c', 'config/pytest.ini','-v','--alluredir', 'output/', dir])
        #pytest.main(['-c', 'config/pytest.ini', '-v','--show-capture', 'no', '--alluredir', 'output/', dir])
    sys.exit(exit_code)