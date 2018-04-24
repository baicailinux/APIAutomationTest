#-*- coding:utf8 -*-
import subprocess

if __name__=='__main__':
    print '检测是否有运行中的allure进程...'
    get_allure_process_id_command="ps -ef|grep -i allure\\.CommandLine|grep -v grep|awk '{print $2}'"
    allure_process_id=subprocess.check_output(get_allure_process_id_command,shell=True)
    if allure_process_id:
        print '关闭allure进程,进程id:'+allure_process_id.strip()
        subprocess.check_output("kill -9 "+allure_process_id,shell=True)
    else:
        print '没有运行中的allure.'
    print '开始生成报告...'
    subprocess.check_output("nohup allure serve -p 9080 output/ >logs/generateReport.log 2>&1 &",shell=True)
