# -*- coding: utf-8 -*-
import sys
import ebooklib
from ebooklib import epub 
from bs4 import BeautifulSoup
import os, tkinter, tkinter.filedialog, tkinter.messagebox
from naivebayes import NaiveBayes


#------------------------------ファイル選択-----------------------
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*.epub")]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('ファイル選択','.epubを選択してください')
file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

tkinter.messagebox.showinfo('ファイル選択',file)
#-------------------------------ファイル選択終了----------------------


#書籍指定
book = epub.read_epub(file)

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

i = 1
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
        
        line = BeautifulSoup(htmlfile.read(),"lxml")
        
        line = line.get_text()
        print(line + "///")
        #file.write(line)
        htmlfile.close()
        #s1 = line.encode('utf-8')
        #print((s1))
        with open(path_txt , mode = 'a') as file_txt:
            #print(type(line))
            file_txt.write(line)    
     
        #判別
        nb = NaiveBayes()
        doc = line
        print('%s => 推定カテゴリ: %s' % (doc, nb.classify(doc)))  # 推定カテゴリ: Pythonになるはず

        textfileList.append(path_txt)
        


#print(textfileList)

join_file(filepath)

#------------------文書変換終わり---------------------------------


