from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.51zxw.net/")
driver.maximize_window()
sleep(2)

#将滚动条拖到最底部
#js="var action=document.documentElement.scrollTop=10000"
#driver.execute_script(js)
#sleep(2)

#将滚动条拖到最高处
#js="var action=document.documentElement.scrollTop=0"
#driver.execute_script(js)
#sleep(2)

driver.get_screenshot_as_file(r"D:\CODE\selenium_test\51.png")
sleep(3)
driver.quit()