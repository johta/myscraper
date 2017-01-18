#!/usr/bin/env python
#coding:utf-8

f = open('testcode.py')
# lines = f.readlines()

fout = open("mytest.py", "w") # result.txtファイルを書き込みモードで作成

for line in f:
    if line[0] == "#":  #コメント行は無視する
        continue
    if "import time" in line:
        fout.writelines(line)
        fout.writelines("#必要なモジュールインポートしておく\n")
        fout.writelines("import csv\n")
        fout.writelines("from bs4 import BeautifulSoup\n")
        continue
    if "get" in line:
        fout.writelines(line)
        fout.writelines("    #url取得処理\n")
        fout.writelines("    time.sleep(3)\n    url = wd.current_url\n")
        fout.writelines("    #ここまでurl取得処理\n    #ここからcsv処理\n    print(url)\n")
        fout.writelines("    csvFile = open('tmp.csv', 'w+', newline='')\n")
        fout.writelines("    try:\n")
        fout.writelines("        writer = csv.writer(csvFile)\n")
        fout.writelines("        writer.writerow(('url'))\n")
        fout.writelines("        writer.writerow((url))\n")
        fout.writelines("    finally:\n")
        fout.writelines("        csvFile.close()\n")
        fout.writelines("    #ここまでcsv処理\n")
        #print(line)
        continue
    if "click()" in line:
        fout.writelines(line)
        fout.writelines("    #クリックを保存\n")
        fout.writelines(line)
        fout.writelines("    #title取得処理\n")
        fout.writelines("    time.sleep(3)\n    print('タイトルを取得')\n    title = wd.title\n    print(title)\n")
        fout.writelines("    #ここまでtitle取得処理\n    #ここからcsv処理\n")
        #print(line)
    else :
        fout.writelines(line)
fout.close()
f.close()
print("Finish!")
