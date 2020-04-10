#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import ebooklib
from ebooklib import epub 
from bs4 import BeautifulSoup
import os, tkinter, tkinter.filedialog, tkinter.messagebox
from naivebayes import NaiveBayes
import csv
import pprint
from tkinter import Text
import getch
import pygame.mixer
import time
import textwrap


#------------------------------ファイル選択-----------------------
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*.epub")]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('ファイル選択','.epubを選択してください')
file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

tkinter.messagebox.showinfo('ファイル選択',file)


#-------------------------------ファイル選択終了----------------------

nb = NaiveBayes()

#書籍指定
book = epub.read_epub(file)
text_list = []
t = 0

#ファイルの結合を結合する関数
#章ごとのファイルをひとつに結合
def join_file(filepath):
    with open(filepath, 'wb') as savefile:
        #for f in filelist:
        for f in textfileList:
            data = open(f, "rb").read()
            savefile.write(data)
            savefile.flush()



#-------------文書変換-----------------------------------
def main():
    i = 1
    q = 0
    textfileList = []
    
    filepath = "all_text.txt"

    items = book.get_items()
    for item in items:
        print(q)

        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            path = str(i) + '.html'
            path_txt = str(i) + '.txt'

            with open(path , mode = 'w') as file:
                
                #s1 = item.get_content().encode('utf-8')
                
                file.write(item.get_content().decode())
                file.close 
        
            htmlfile = open(path) 
            
            line = BeautifulSoup(htmlfile.read(),"lxml")
            
            line = line.get_text()
            text_list.append(line)
            ##print(line + "///")
            #file.write(line)
            htmlfile.close()
            #s1 = line.encode('utf-8')
            #print((s1))
            with open(path_txt , mode = 'a') as file_txt:
                #print(type(line))
                file_txt.write(line)    
        
            #判別
            q += 1
            
            

       
        
     ##textfileList.append(path_txt)
            


    #print(textfileList)

    ##join_file(filepath)

#------------------文書変換終わり---------------------------------

def readCSV():
    with open('naive_data.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                nb.train(row[0],row[1])




def pushed(event):

    pygame.mixer.init() #初期化
    pygame.mixer.music.stop() 

    global t
    t+=1
    var = text_list[t]
    label["text"] = textwrap.fill(var, 40)

    doc = text_list[t]
    print(nb.classify(doc)) 
    thema = nb.classify(doc) 

    ##音鳴らす
    
    music = ""
    if thema == "白熱":
        music ="music/kinnpaku.mp3"

    if thema == "感動":
        music ="music/kanndou.mp3"

    if thema == "ほのぼの":
        music ="music/honobono.mp3"

    if thema == "ミステリー":
        music ="music/misuteri.mp3"
    
    pygame.mixer.music.load(music) #読み込み

    pygame.mixer.music.play(1) #再生
    
    #音鳴らすの終了



    

if __name__ == '__main__':
    
    readCSV()
    main()

    root2 = tkinter.Tk()

    var = text_list[t]

    root2.title("リストに追加")
    root2.geometry("800x910")

    #ボタン
    Button = tkinter.Button(root2,text="次へ")
    Button.bind("<Button-1>",pushed)
    Button.place(x=610,y=70)
    

    #文章
    label = tkinter.Label(root2, text=textwrap.fill(var, 40),font=("",15),anchor='e',justify='left')
    #表示
    label.grid()

    root2.mainloop()


    

    
        


    

    
