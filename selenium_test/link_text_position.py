from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.51zxw.net/")

driver.find_element_by_link_text("程序设计").click()
sleep(3)

driver.find_element_by_link_text("Selenium").click()
sleep(3)

driver.quit()