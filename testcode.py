# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://ja.wikipedia.org/wiki/%E8%8C%A8%E5%9F%8E%E5%A4%A7%E5%AD%A6")
    wd.find_element_by_id("searchInput").click()
    wd.find_element_by_id("searchInput").clear()
    wd.find_element_by_id("searchInput").send_keys("hoge")
    wd.find_element_by_id("searchButton").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
