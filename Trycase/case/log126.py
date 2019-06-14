# -*- coding:UTF-8 -*-
import unittest
import time
import sys
sys.path.append('../../')
from lib.lib import Common
from lib.ReadExc import ReadExc
class Login(unittest.TestCase):
    def log(self,name):
        com = Common('Chrome')
        com.openurl('https://mail.126.com/')
        com.click('id','lbNormal')
        # self.driver.switch_to.frame('xpath',"//iframe[starts-with(@id,'x-URS-iframe')]")
        com.driver.switch_to.frame(com.driver.find_element_by_xpath("//iframe[starts-with(@id,'x-URS-iframe')]"))
        data_list = ReadExc().get_list('../../data/login163.xlsx','login')
        data = ReadExc().get_data(data_list,name)
        user = data['username']
        pwd = data['password']
        exp_res = data['exp_res']
        ele = data['ele']
        ele_name = data['ele_name']
        com.input('name','email',user)
        com.input('name','password',pwd)
        time.sleep(1)
        com.click('id','dologin')
        time.sleep(3)
        self.res = com.locateelement(ele,ele_name)
        print('提示信息为：%s' % self.res.text)
        print('预期信息为：%s' % exp_res)
        self.assertEqual(self.res.text,exp_res)

if __name__ == '__main__':
    login = Login()
    login.log('log_normal')