#!/usr/bin/env python3

print("学籍番号を入力してください")
str = int(input())

if (19001<=str<=19122):
    print ("あなたは1班です！")
    exit()
if (19123<=str<=19244):
    print("あなたは2班です！")
    exit()
if (19245<=str<=19366):
    print("あなたは3班です！!")
    exit()
if (19367<=str<=19488):
    print("あなたは4班です！")
    exit()
