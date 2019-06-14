from lib.HTMLTestReportCN import HTMLTestRunner
from config.config import *
from lib.send import send_email

def run(suit):

    with open(report_file,'wb')as f:
        HTMLTestRunner(
            stream=f,  #测试数据写入哪个文件
            title='126邮箱登录测试用例',  #谁当测试报告标题
            description='web自动化测试',
            tester='唐加敬',
            verbosity=2
        ).run(suit)
    send_email(report_file)




