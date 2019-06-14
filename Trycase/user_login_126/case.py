import unittest
import sys
sys.path.append('../')
from Trycase.case.log126 import Login

class Login_Test(unittest.TestCase):
    def setUp(self) -> None:
        print('begin')
    def tearDown(self) -> None:
        print('end')
    def test_001(self):
        login = Login()
        login.log('log_normal')

    def test_002(self):
        login = Login()
        login.log('log_err_01')

    def test_003(self):
        login = Login()
        login.log('log_err_02')

if __name__ == '__main__':
    unittest.main()