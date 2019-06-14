import unittest
import sys
sys.path.append('../../')
from Trycase.user_login_126.case import Login_Test
from run import *

list = ['test_001','test_002','test_003']
mysuit = unittest.TestSuite()
for case in list:
    mysuit.addTest(Login_Test(case))

run(mysuit)


