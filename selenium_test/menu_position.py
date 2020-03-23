from selenium import webdriver
from  time import sleep
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()

driver.get("https://www.baidu.com")
sleep(2)

#利用Select类来进行定位
select = Select(driver.find_element_by_css_selector("[name='tj_settingicon']"))
select.select_by_index(1)
#select.select_by_value()
#select.select_by_visible_text()

sleep(2)
driver.quit()