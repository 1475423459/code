import unittest
from model import function,myunit
from Website.test_case.page_object.LoginPage import  *
from time import sleep

class LoinTest(myunit.StartEnd):
    # @unittest.skip('skip this case')
    def test_login1_normal(self):
        '''username password is normal'''
        print("test_login1_normal is start run...")
        po=LoginPage(self.driver)
        po.unlock('18665596456','Wj123456')
        sleep(3)
        #断言与截屏
        #self.assertEqual(po.type_loginPass_hint(),'尊敬的会员')
        self.assertEqual(po.type_loginPass_hint(),'尊敬的会员')
        function.inser_img(self.driver,"18665596456_login1_normal.png")
        print("test_login1_normal is test end!")
    #def test_login2_passwdError(self):
        #'''username is ok,passwd is error!'''
        #print("test_login2_PasswdError is start run...")
        #po=LoginPage(self.driver)
        #po.unlock("18665596456",'123')
        #sleep(2)

       # self.assertEqual(po.type_loginFail_hint(),'30天内自动登录')
        #function.inser_img(self.driver,"18665596456_login2_fail.png")
        #print("test_login2_PasswdError is test end!")

    #def test_login3_empty(self):
        #'''username and passwd is empty!'''
        # print("test_login3_empty is start run...")
        #po=LoginPage(self.driver)
        #po.unlock('','')
        #sleep(2)

        #断言与截屏
        #self.assertEqual(po.type_loginFail_hint(),'30天内自动登录')
        #function.inser_img(self.driver,"18665596456_login3_empty.png")
        #print("test_login3_empty is test end!")


if __name__ == '__main__':
    unittest.main()