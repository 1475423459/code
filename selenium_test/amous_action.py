from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()

driver.get("http://baidu.com")
driver.maximize_window()

driver.find_element_by_css_selector("#kw").send_keys("python")

#获取搜索框元素对象

element = driver.find_element_by_css_selector("#kw")
sleep(3)

#双击操作
ActionChains(driver).double_click(element).perform()
sleep(2)

#右击操作
ActionChains(driver).context_click(element).perform()
sleep(2)

#鼠标悬停
above = driver.find_element_by_css_selector(".soutu-btn")
ActionChains(driver).move_to_element(above).perform()
sleep(4)

driver.quit()













