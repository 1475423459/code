from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from time import sleep,ctime

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
sleep(3)

#设置隐式时间s
driver.implicitly_wait(5)

#检测搜索框是否存在
#try:
    #print(ctime())
    #driver.find_element_by_css_selector("#kw11").send_keys("python")
#except NoAlertPresentException as msg:
    #print(msg)
#finally:
    #print(ctime())

#用isdisplay()方法判断
print(ctime())
for i in range(10):
    el=driver.find_element_by_id("kw")
    try:
        if el.isdisplayed():
            break
    except:pass
    else:
        print("timeout")
print(ctime())


sleep(3)
driver.quit()