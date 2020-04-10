#coding:utf-8
import serial
 
ser = serial.Serial('/dev/tty.',9600,timeout=None)
ser.write("test")
ser.close()