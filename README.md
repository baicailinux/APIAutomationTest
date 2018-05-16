![avatar](https://github.com/yanchunhuo/resources/blob/master/APIAutomationTest/report.png)

# [概况]()
* 本项目由pytest、assertpy、requests、PyMySQL、allure组成
    * pytest是python的一个单元测试框架,https://docs.pytest.org/en/latest/
    * assertpy是一个包含丰富的断言库，支持pytest,https://github.com/ActivisionGameScience/assertpy
    * requests是http请求框架,http://docs.python-requests.org/en/master/
    * PyMySQL用于操作MySQL数据库,https://github.com/PyMySQL/PyMySQL
    * allure用于生成测试报告,http://allure.qatools.ru/

# [使用]()
## 一、环境准备
### 1、安装python依赖模块
* pip install -r requirements.txt

### 2、安装allure
* sudo apt-add-repository ppa:qameta/allure
* sudo apt-get update 
* sudo apt-get install allure
* 其他安装方式：https://github.com/allure-framework/allure2

### 3、安装JDK1.8

### 4、安装openjdk8
* sudo add-apt-repository ppa:openjdk-r/ppa
* sudo apt-get update
* sudo apt-get install openjdk-8-jdk

## 二、修改配置
* vim config/init.int 配置需要初始化的项目
* vim config/projectName.init 配置测试项目的信息

## 三、运行测试
* cd APIAutomationTest/
* python runTest.py --help
* python runTest.py 运行cases目录所有的用例
* python runTest.py -k keyword 运行匹配关键字的用例，会匹配文件名、类名、方法名
* python runTest.py -d dir     运行指定目录的用例

## 三、生成测试报告
* cd APIAutomationTest/
* python generateReport.py 
* 访问地址http://ip:9080

# [项目结构]()
* base 基础请求类
* cases 测试用例目录
* common 公共模块
* config　配置文件
* init 初始化
* logs 日志目录
* output 测试结果输出目录 
* pojo 存放自定义类对象
* test_data 测试所需的测试数据目录
* runTest.py 测试运行脚本
* generateReport.py 报告生成脚本


# [编码规范]()
* 统一使用python 2.7
* 编码使用-\*- coding:utf8 -\*-,且不指定解释器
* 类/方法的注释均写在class/def下一行，并且用三个双引号形式注释
* 局部代码注释使用#号
* 所有的测试模块文件都以test_projectName_moduleName.py命名
* 所有的测试类都以Test开头，类中方法(用例)都以test_开头
* 每个测试项目都在cases目录里创建一个目录，且目录都包含有api、scenrarios两个目录

# [pytest常用]()
* @pytest.mark.skip(reason='该功能已废弃')
* @pytest.mark.parametrize('key1,key2',[(key1_value1,key2_value2),(key1_value2,key2_value2)])
* @pytest.mark.usefixture('func_name')





