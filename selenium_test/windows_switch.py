from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()

#打开Selenium课程页面
driver.get("http://www.51zxw.net/list.aspx?cid=615")
# 获取课程主页的窗口句柄
selenium_index=driver.current_window_handle

sleep(2)
#点击2-1课程链接。进入课程详情页面
driver.find_element_by_partial_link_text('2-1').click()
sleep(4)

#跳转到课程主页窗口，点击3-1课程
driver.switch_to.window(selenium_index)
sleep(3)
driver.find_element_by_partial_link_text('3-1').click()
sleep(3)

driver.quit()