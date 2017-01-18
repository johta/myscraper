#!/usr/bin/env python
#coding:utf-8
import os
import sys

f = open('k.py')
# lines = f.readlines()

fout = open("mytest.py", "w") # result.txtファイルを書き込みモードで作成

for line in f:
    if line[0] == "#":  #コメント行は無視する
        continue
    if line[0] == "¥t": #全角スペース入っててsyntaxError出てたの許せない
        print("タブ")
    # if "try" in line:
    #     print(line)
    #     print("あったよ！")
    if "get" in line:
        fout.writelines(line)
        fout.write("\t")
        fout.writelines("#urlとか取得\n")
        #print(line)
        print("#h1取得してみっかー")
        continue
    if "click()" in line:
        fout.writelines(line)
        fout.write("\t")
        fout.writelines("#クリックを保存\n")
        #print(line)
        print("#クリックされたぞ")
    else :
        fout.writelines(line)
fout.close()
f.close()
print("Finish!")
