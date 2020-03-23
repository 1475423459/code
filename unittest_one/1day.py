# coding=utf-8
from appium import webdriver
import time
desired_caps = {
    'platformName': 'Android',
    'deviceName': '1bee95fd',
    'platformVersion': '23',
    # apk包名
    'appPackage': 'cn.itsite.glomax',
    # apk的launcherActivity
    'appActivity': 'cn.itsite.launcher.LauncherActivity',
    'appWaitActivity': ''
}
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)
driver.find_element_by_id("cn.itsite.glomax:id/tv_notice_home_fragment").click()