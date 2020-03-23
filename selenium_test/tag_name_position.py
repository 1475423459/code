from  selenium import webdriver
from  time import sleep

driver=webdriver.Chrome()

driver.get("http://www.51zxw.com")

#定位标签名为input的元素
driver.find_element_by_tag_name("input").send_keys("selenium")

sleep(3)
driver.find_element_by_tag_name("button").click()
#获取页面所有标签名称为“input”的标签。
#driver.find_elements_by_tag_name("input")[0].send_keys("selenium")

sleep(3)

driver.quit()