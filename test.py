from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS()
print("urlを入力して下さい")
url = input()
#print("urlを取得中") #PhantomJSがURLを取得するまで時間がかかるので
driver.get(url)
#print("url取得完了")
data = driver.page_source.encode('utf-8')
#print("utf-8にエンコード完了")
html = BeautifulSoup(data,"lxml")
#print("bs4オブジェクト取得完了")
#print(html)  # htmlソースを表示する
print("取得するタグを入力してください")
tag = input()
print("取得する属性を入力してください")
attribute = input()
print("取得する要素を入力して下さい")
elements = input()
data = html.find_all(tag,attribute =elements)
print(data)  # linkタグかつhrefがstyle.cssのもののリスト
