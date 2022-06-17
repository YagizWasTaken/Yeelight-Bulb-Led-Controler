#pip install yeelight#




import imp
from multiprocessing.spawn import import_main_path
from this import s
from turtle import title
from yeelight import Bulb
import tkinter as tk
from yeelight import LightType
from yeelight import Flow
from yeelight import TemperatureTransition
from yeelight import SleepTransition
from yeelight import RGBTransition

pencere=tk.Tk()
pencere.geometry("400x400+50+100")
pencere.title("Led için kumanda by Yağız Arslan")
led=Bulb("192.168.1.46")

from yeelight import *
transitions = [HSVTransition(hue, 100, duration=3000)
               for hue in range(0, 359, 40)]

flow = Flow(
    count=0,  # Cycle forever.
    transitions=transitions
)







def aç():
  led.turn_on()

def kapa():
  led.turn_off()

def parlak():
  led.set_rgb(255, 0, 0)

def parlak1():
  led.set_rgb(0, 0, 255)

def parlak2():
  led.set_rgb(0, 255, 0)

def par():
  led.set_brightness(100)

def par1():
  led.set_brightness(50)

def par2():
  led.set_brightness(10)

def dalga():
  led.start_flow(flow)

def dalga1():
  led.stop_flow(flow)
  






  

dugme1=tk.Button(pencere,text="Aç",command=aç)
dugme1.pack()

dugme2=tk.Button(pencere,text="Kapa",command=kapa)
dugme2.pack()

dugme3=tk.Button(pencere,text="Rengi Kırmızı Yap",command=parlak)
dugme3.pack()

dugme4=tk.Button(pencere,text="Rengi Mavi Yap",command=parlak1)
dugme4.pack()

dugme5=tk.Button(pencere,text="Rengi Yeşil Yap",command=parlak2)
dugme5.pack()

dugme6=tk.Button(pencere,text="Full Parlaklık",command=par)
dugme6.pack()

dugme7=tk.Button(pencere,text="Yarım Parlaklık",command=par1)
dugme7.pack()

dugme8=tk.Button(pencere,text="Kısık Parlaklık(Uyku modu)",command=par2)
dugme8.pack()

dugme9=tk.Button(pencere,text="Dalgalanma Açık",command=dalga)
dugme9.pack()

dugme10=tk.Button(pencere,text="Dalgalanma Kapalı",command=dalga1)
dugme10.pack()




pencere.mainloop()
