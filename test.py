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
        driver.implicitly_wait(5)
        url = 'https://ja.wikipedia.org/'
        driver.get(url)
        # data = driver.page_source.encode('utf-8')
        # html = BeautifulSoup(data, "html5lib")
        # #print(html.title.text)
        # print("取得要素を入力して下さい")
        # elem = input()
        # print(html.find(elem).text)

    def tearDown(self):
        print("Tearing down the test")
        global driver
        data = driver.page_source.encode('utf-8')
        html = BeautifulSoup(data, "html5lib")
        #print(html.title.text)
        print("取得要素を入力して下さい")
        elem = input()
        print(html.find(elem))

    def test_searchSomething(self):
        print("test_DispTans1")
        global driver
        link = driver.find_element_by_id("")
        print(link.text)

    # def test_SaveScreenshot(self):
    #     print("test_SaveScreenshot")
    #     global driver
    #     driver.save_screenshot("ss.png")

if __name__ == '__main__':
    unittest.main()
