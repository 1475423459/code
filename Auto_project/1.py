from selenium import webdriver
from time import sleep

driver= webdriver.Chrome()
driver.get("https://passport.ctrip.com/user/login?BackUrl=https%3A%2F%2Fhotels.ctrip.com%2Fhotel%2F6278770.html%23ctm_ref%3Dhod_hp_hot_dl_n_2_7")
print(driver.title)