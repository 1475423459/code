from  Website.test_case.page_object.BasePage import *
from Website.verification_code.unlockScrapy import *
#导入极验验证
from driver import *
from  selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage(Page):
    '''新闻登录页面'''
    url = '/user/login?BackUrl=https%3A%2F%2Fhotels.ctrip.com%2Fhotel%2F6278770.html%23ctm_ref%3Dhod_hp_hot_dl_n_2_7'

    # 定位器——对相关元素进行定位
    username_loc = (By.ID,'nloginname')
    password_loc = (By.ID,'npwd')
    submit_loc = (By.ID,'nsubmit')


    def type_username(self, username):
        #self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        #self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)


    def type_submit(self):
        self.find_element(*self.submit_loc).click()


    def unlock(self,name,pwd):
        # 创建浏览器对象
        self.open()
        #  输入账号密码
        self.type_username(name)
        self.type_password(pwd)


        # 此时可能出现有滑动验证码与点选文字
        ##  若出现滑块,则开始破解滑块
        unlock = unlockScrapy(self.driver)
        unlock.unlockScroll()
        ## 若出现点选文字,开始破解点选文字
        unlock.pic_main()
        # 点击登录
        print("3" * 10)
        """
        //*[@id="nsubmit"]
        """
        # browser.find_element_by_xpath('//*[@class="form__button"]/button').click()
        self.type_submit()
        time.sleep(19)

        # 如果破解成功，html的title会变
        if unlock.driver.title != '携程在手，说走就走':
            print('破解成功')
        else:
            # 再次尝试
            print('破解失败，再次破解')
            unlock = unlockScrapy(webdriver.Chrome())
            unlock.unlockScroll()
            unlock.pic_main()

            # 再次点击登录
            print("3" * 10)

            # browser.find_element_by_xpath('//*[@class="form__button"]/button').click()
            self.type_submit()
            time.sleep(19)

    LoginPass_loc = (By.LINK_TEXT, '尊敬的会员')
    loginFail_loc = (By.LINK_TEXT, '30天内自动登录')

    def type_loginPass_hint(self):
        return self.find_element(*self.LoginPass_loc).text


    def type_loginFail_hint(self):
        return self.find_element(*self.loginFail_loc).text



