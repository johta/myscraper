#!/usr/bin/env python
#coding:utf-8

f = open('testcode.py')
# lines = f.readlines()

fout = open("mytest.py", "w") # result.txtファイルを書き込みモードで作成

for line in f:
    if line[0] == "#":  #コメント行は無視する
        continue
    if "get" in line:
        fout.writelines(line)
        fout.write("    ")
        fout.writelines("#url取得処理\n")
        fout.write("    ")
        fout.writelines("url = wd.title\n")
        fout.write("    ")
        fout.writelines("#ここまでurl取得処理\n    #ここからcsv処理\n")
        fout.write("    ")
        fout.writelines("import csv\n")
        fout.write("    ")
        fout.writelines("csvFile = open('tmp.csv', 'w+', newline='')\n    ")
        fout.writelines("try:\n    ")
        fout.writelines("    writer = csv.writer(csvFile)\n    ")
        fout.writelines("    writer.writerow(('url'))\n    ")
        fout.writelines("    writer.writerow((url))\n    ")
        fout.writelines("finally:\n    ")
        fout.writelines("    csvFile.close()\n    ")
        fout.writelines("#ここまでcsv処理\n")
        #print(line)
        print("#h1取得してみっかー")
        continue
    if "click()" in line:
        fout.writelines(line)
        fout.write("    ")
        fout.writelines("#クリックを保存\n")
        #print(line)
        print("#クリックされたぞ")
    else :
        fout.writelines(line)
fout.close()
f.close()
print("Finish!")
