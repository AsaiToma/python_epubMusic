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
        

        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            path = str(i) + '.html'
            path_txt = str(i) + '.txt'

            with open(path , mode = 'w') as file:
                
                #s1 = item.get_content().encode('utf-8')
                
                file.write(item.get_content().decode())
                file.close 
        
            htmlfile = open(path) 
            
            #文章を章ごとにリストへ
            line = BeautifulSoup(htmlfile.read(),"lxml")
            
            line = line.get_text()

            #改行ごとに分割、40文字以上なら改行を挿入していく
            k = 0
            paragraph = line.splitlines()
            for para in paragraph:
                if len(para) > 40:
                    para_40 = [para[i: i+40] for i in range(0, len(para), 40)]
                    paragraph[k] = '\n'.join(para_40)
                paragraph[k] += "\n"
                k += 1
            var = ''.join(paragraph)
            #text_list.append(var)
            #new_varが45行以上のものを複数ページに直しつつ新しく配列を生成
            page_num = (var.count('\n') // 35) + 1
            new_paragraph = var.splitlines(True)
            
            for  u in range(page_num):
                if u>0:
                    page = "\n\n\n"
                else:
                    page = ""
                ran = 40 if (var.count('\n') - 40*u) >= 40 else (var.count('\n')- 45*u)
                for s in range(ran):
                    page += new_paragraph[s + 40*u]
                text_list.append(page)
            
                
            
            htmlfile.close()
            #リストへの格納終了

            with open(path_txt , mode = 'a') as file_txt:
                
                file_txt.write(line)    
        
            #判別
           
            
            

       
        
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
    
    
    lab = text_list[t]
    label["text"] = lab

    print(nb.classify(lab)) 
    thema = nb.classify(lab) 

    ##音鳴らす
    if len(lab)>40:
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
    t+=1



    

if __name__ == '__main__':
    
    readCSV()
    main()

    root2 = tkinter.Tk()

    lab = ""

    root2.title("リストに追加")
    root2.geometry("800x910")

    #ボタン
    Button = tkinter.Button(root2,text="次へ")
    Button.bind("<Button-1>",pushed)
    Button.place(x=610,y=70)
    

    #文章
    label = tkinter.Label(root2, text=lab,font=("",15),anchor='e',justify='left')
    #表示
    label.grid()

    root2.mainloop()


    

    
        


    

    
