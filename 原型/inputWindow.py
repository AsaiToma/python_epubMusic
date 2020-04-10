#!/usr/bin/python3
# -*- coding: utf8 -*-
import tkinter as tk
from tkinter import Text
import csv
import pprint

def pushed(event):
    result = t.get('1.0','end -1c')
    print(result)
    print(tb.get())

    with open('naive_data.csv', 'a') as f:
     writer = csv.writer(f)
     writer.writerow(result, tb.get)
 

#ウィンドウ作成
root = tk.Tk()
root.title("リストに追加")
root.geometry("620x410")


#文章入力
label = tk.Label(root, text="文章")
label.place(x=40, y=35)

t = Text(root, height=15, width=40)
t.insert('1.0','ここに入力')
t.pack(fill = 'x', padx = 30, pady = 60)
#文章入力終了

#分類入力
bun2 = tk.Label(root, text="分類")
bun2.place(x=40, y=270)

tb = tk.Entry(width=40)
tb.place(x=45,y=300)
#分類入力終了

#ボタン
Button = tk.Button(text="追加")
Button.bind("<Button-1>",pushed)
Button.place(x=310,y=370)

#メインループ
root.mainloop()

