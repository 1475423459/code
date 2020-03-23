import unittest
import requests
from time import sleep
class LoginEmaliTest(unittest.TestCase):
    def setUp(self):
        self.url='http://192.168.150.230'
        self.para1='/api/w2/account/login_token_email'
    def test_email_wrong(self):
        '''测试邮箱错误'''
        data={'email':'123','password':'Wj123456'}
        r=requests.post(self.url+self.para1,data=data)
        result=r.json()
        self.assertAlmostEqual(result['error'],10002)
        sleep(3)
    def test_passwd_wrong(self):
        '''测试密码错误'''
        data={'email':'1475423459@qq.com','password':'Wj'}
        r=requests.post(self.url+self.para1,data=data)
        result=r.json()
        self.assertAlmostEqual(result['error'],10002)
        sleep(3)
    def test_value_lose(self):
        '''测试密码参数缺失'''
        data={'email':'1475423459@qq.com'}
        r=requests.post(self.url+self.para1,data=data)
        result=r.json()
        self.assertAlmostEqual(result['error'],10002)
        sleep(3)
if __name__=='__main__':
    unittest.main()



