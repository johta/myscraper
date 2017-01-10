from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import unittest, time

class TestAddition(unittest.TestCase):
    driver = None
    def setUp(self):
        print("Setting up the test")
        global driver
        driver = webdriver.PhantomJS()
        driver.implicitly_wait(10)
        url = 'http://gamy.jp/tagatame'
        driver.get(url)

    def tearDown(self):
        print("Tearing down the test")
        global driver
        data = driver.page_source.encode('utf-8')
        html = BeautifulSoup(data, "html5lib")
        print(html.title.text)
        print(html.find('h1').text)
        driver.quit

    def test_SaveScreenshot(self):
        global driver
        driver.save_screenshot("ss.png")


if __name__ == '__main__':
    unittest.main()
