from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep

driver=webdriver.Chrome()

driver.get("http://www.baidu.com")


driver.find_element_by_css_selector(".s_ipt").send_keys("自学网 Selenium")

sleep(2)

#显示等待--判断搜索按钮是否存在
element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"su1")),message="不存在搜索按钮")
element.click()
sleep(3)

driver.quit()