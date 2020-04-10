#!/usr/bin/python3
# -*- coding: utf8 -*-
import tkinter as tk
from tkinter import Text
import csv
import pprint

from PIL import Image
import pyocr
import pyocr.builders

import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt




#---------------文字認識関連------------------------------------------------

# グローーバル変数
drawing = False
complete_region = False
ix,iy,width,height = -1,-1,0,0
box = [ix, iy, width, height]
 
 
# マウスコールバック関数
def my_mouse_callback(event,x,y,flags,param):
    global ix,iy,width,height,box,drawing,complete_region
 
    if event == cv2.EVENT_MOUSEMOVE:      # マウスが動いた時
        if(drawing == True):
            width = x - ix
            height = y - iy
 
    elif event == cv2.EVENT_LBUTTONDOWN:  # マウス左押された時
        drawing = True
 
        ix = x
        iy = y
        width = 0
        height = 0
 
    elif event == cv2.EVENT_LBUTTONUP:    # マウス左離された時
        drawing = False
        complete_region = True
 
        if(width < 0):
            ix += width
            width *= -1
        if(height < 0):
           iy += height
           height *= -1
 
    box = [ix, iy, width, height]         # 切り取り範囲格納
 
 
 
 
# メイン関数
def main():
    global ix,iy,width,height,box,drawing,complete_region
 
    source_window = "draw_rectangle"
    roi_window = "region_of_image"
 
    img = cv2.imread(sys.argv[1],1)  # 画像の読み込み
    temp = img.copy()                # 画像コピー
 
    cv2.namedWindow(source_window)
    cv2.setMouseCallback(source_window, my_mouse_callback)
 
    while(1):
        cv2.imshow(source_window,temp)
 
        if(drawing):             # 左クリック押されてたら
            temp = img.copy()    # 画像コピー
            cv2.rectangle(temp,(ix,iy),(ix + width, iy+ height),(0,255,0),2)  # 矩形を描画
 
        if(complete_region): # 矩形の選択が終了したら
            complete_region = False
 
            roi = img[iy:iy+height, ix:ix+width] # 元画像から選択範囲を切り取り
            np.save("read",roi)
            cv2.destroyWindow(source_window)
            ##cv2.imshow(roi_window, roi)          # 切り取り画像表示
 
            #文字認識
            tools = pyocr.get_available_tools()
            if len(tools) == 0:
                print("No OCR tool found")
                sys.exit(1)

            tool = tools[0]
            print("Will use tool '%s'" % (tool.get_name()))


            langs = tool.get_available_languages()
            print("Available languages: %s" % ", ".join(langs))
            lang = langs[1]
            print("Will use lang '%s'" % (lang))
            # Ex: Will use lang 'fra'

            pilImg = Image.fromarray(np.uint8(roi))
            pilImg.save("use.png")
            txt = tool.image_to_string(
                Image.open("use.png"),
                lang=lang,
                builder=pyocr.builders.TextBuilder()
            )

            print(txt)
            #認識終了
 
        # キー操作
        k = cv2.waitKey(1) & 0xFF
        if k == 27:          # esc押されたら終了
            break
        elif k ==ord('s'):   # 's'押されたら画像を保存
            cv2.imwrite('roi.png', roi)
            cv2.imwrite('draw_src.png', temp)
            plt.savefig('histgram.png')
 
    cv2.destroyAllWindows()
 
 
 


#---------------文字認識関連終了------------------------------------------------

#----------------------ウィンドウ関連--------------------------------------

#追加ボタン押されたとき
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

if __name__ == "__main__":
    main()

#メインループ
#root.mainloop()

#---------------ウィンドウ関連終了-------------------------------------------

