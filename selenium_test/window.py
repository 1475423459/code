from selenium import webdriver
import time

driver = webdriver.Chrome()
print("打开百度首页")
driver.get("http://www.talkweb.com.cn")

print("打开联系我们")
driver.get("http://www.talkweb.com.cn/contact/")

time.sleep(2)

#回退到首页
print("回退到首页")
driver.back()

time.sleep(3)
#前景到联系我们界面
print("前景到联系我们界面")
driver.forward()

print("刷新界面")
driver.refresh()

print("显示当前标题: ",driver.title)

print("显示url： ",driver.current_url)




























