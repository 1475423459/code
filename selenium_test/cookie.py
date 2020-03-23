from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://baidu.com")

#手动添加cookie
driver.add_cookie({"name":"BAIDUID","value":"B18A3EACE99F1854DA2CCC3095774A61"})
driver.add_cookie({"name":"BDUSS","value":"x1V21FazR0OS1SQnBtSEkxYi1yd253bjBKeFoyYmJaVks2VkMzbWwxRGFvSnBlSVFBQUFBJCQAAAAAAAAAAAEAAACucUmhd3oyMDE2MjAxOQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANoTc17aE3NeSW"})

sleep(3)
driver.refresh()
sleep(3)
driver.quit()