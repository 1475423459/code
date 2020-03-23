from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.find_element_by_css_selector("#kw").send_keys("python")
sleep(2)

#键盘操作ctrl+a
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,"a")

#键盘选择复制或者剪切操作ctrl+c
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,"c")
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,"x")
sleep(2)

#打开sogo界面
driver.get("http://www.sogo.com")
sleep(2)

#点击搜索按钮
driver.find_element_by_css_selector("#query").send_keys(Keys.CONTROL,"v")
driver.find_element_by_css_selector("#stb").click()
sleep(3)
driver.quit()