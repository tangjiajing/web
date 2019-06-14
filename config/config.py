import logging
import os
import time
#项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#当前上一级目录

data_path = prj_path
test_path = prj_path

today = time.strftime('%Y%m%d',time.localtime())
now = time.strftime('%Y%m%d_%H%M%S',time.localtime())
log_file = os.path.join(prj_path, 'log.txt')
report_file = os.path.join(prj_path,'report','report_{}.html'.format(now))

#log配置
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y:%m:%d %H:%M:%S',
                    filename='log.text',
                    filemode='a',

                    )


#数据库配置
db_host = '127.0.0.1'
db_port = 3306
db_user = 'test'
db_passwd = '123456'
db = 'api_test'

#邮件配置
smtp_server = 'smtp.qq.com'
smtp_user = '1475423207@qq.com'
smtp_password = 'psekbgeujlhdhgfa'

sender = smtp_user  # 发件人
receiver = 'jiajingtang@126.com'  # 收件人
subject = '接口测试报告'  # 邮件主题

if __name__ == '__main__':
    logging.info('hello')