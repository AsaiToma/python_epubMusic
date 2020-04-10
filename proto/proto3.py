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
from flask import Flask, render_template


#------------------------------ファイル選択-----------------------
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*.epub")]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('ファイル選択','.epubを選択してください')
file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

##tkinter.messagebox.showinfo('ファイル選択',file)


#-------------------------------ファイル選択終了----------------------

nb = NaiveBayes()
app = Flask(__name__)

#書籍指定
book = epub.read_epub(file)
text_list = []
text_type = []
t = 0

#ファイルの結合を結合する関数




#-------------文書変換-----------------------------------
def main():
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
            
            ##テキストを分類、格納
            line = line.get_text()
            newline = line.replace('\n','</br>')
            text_list.append(newline)
            doc = line
            thema = nb.classify(doc)
            text_type.append(thema)
            
            ##分類、格納終了

            
            
            htmlfile.close()
          
             
        
      
    


        
            
            

            
            


   

#------------------文書変換終わり---------------------------------

def readCSV():
    with open('naive_data.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                nb.train(row[0],row[1])


@app.route('/')
def data():
    pages = len(text_list);
    return render_template('get_data.php', text_list=text_list, text_type=text_type,pages=pages)







    



    

if __name__ == '__main__':
    
    readCSV()
    main()

    app.run(host='0.0.0.0', port=8082)

    

    

    
        


    

    
