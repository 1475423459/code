from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://localhost:63342/selenium_test/1.html?_ijt=higc62t7nsess3v0ca9p8o4qqu")

inputs=driver.find_elements_by_tag_name("input")

print("复选框的个数为")
print(len(inputs))

for i in inputs:
    if i.get_attribute("type")=="checkbox":
        i.click()
        time.sleep(1)

driver.find_elements_by_xpath("//input[@type='checkbox']").pop(-1).click()
