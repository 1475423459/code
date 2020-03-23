from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#根据id定位
driver.find_element_by_css_selector('#kw').send_keys("selenium我要自学")

#根据class定位
driver.find_element_by_css_selector('.s_ipt').send_keys('python')

#根据属性定位
driver.find_element_by_css_selector('[autocomplete="off"]').send_keys("学")
sleep(3)

driver.quit()