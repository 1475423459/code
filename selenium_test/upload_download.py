from selenium import webdriver
import os
from time import  sleep
#上传文件
driver=webdriver.Firefox()
file_path = "file:///C:\\Users\\wangjuan\\Desktop\\upload.html"
driver.get(file_path)

sleep(3)
driver.find_element_by_name("myfile").send_keys("C:\\Users\\wangjuan\\Desktop\\test1.txt")

#下载文件
driver.get("http://jmeter.apache.org/download_jmeter.cgi")
#浏览器下载属性设置
fp=webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList",2)					#设置浏览器下载路径，0表示默认，2表示指定路径
fp.set_preference("browser.download.manager.showWenStarting",True)	#是否显示开始
fp.set_preference("browser.download.dir","C:\\Users\\wangjuan\\Desktop")				#指定下载保存的路径

driver=webdriver.Firefox(firefox_profile=fp)
driver.get("http://jmeter.apache.org/download_jmeter.cgi")
driver.find_element_by_partial_link_text("apache-jmeter-3.0.tgz").click()
