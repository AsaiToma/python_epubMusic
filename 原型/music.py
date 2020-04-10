#coding:utf-8
import pygame.mixer
import time

def sound():
    pygame.mixer.init() #初期化

    pygame.mixer.music.load("Melci.mp3") #読み込み

    pygame.mixer.music.play(1) #再生

    time.sleep(10)

    pygame.mixer.music.stop() #終了

if __name__ == '__main__':
    sound()