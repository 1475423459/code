from selenium import webdriver
from time import sleep

#加载浏览器驱动
driver = webdriver.Chrome()

#打开百度网页
driver.get('http://www.baidu.com')
print(driver.title)
sleep(3)

#关闭浏览器
driver.quit()