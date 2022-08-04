import imp
from multiprocessing.spawn import import_main_path
from this import s
from turtle import title
from yeelight import *
import tkinter as tk
pencere=tk.Tk()
pencere.geometry("400x400+50+100")
pencere.title("Led Controler by Yağız Arslan")

#bot 2.0 part
bulb_id=str(discover_bulbs())
bulb_id_cut=bulb_id[9:21]
led=Bulb(bulb_id_cut)


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

def parlak3():
  led.set_rgb(100, 255, 255)

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
  






  

dugme1=tk.Button(pencere,text="Open",command=aç)
dugme1.pack()

dugme2=tk.Button(pencere,text="Close",command=kapa)
dugme2.pack()

colorlabel= tk.Label(pencere, text="Colors", font="100")
colorlabel.pack()
dugme3=tk.Button(pencere,text="Make The Color Red",command=parlak)
dugme3.pack()

dugme4=tk.Button(pencere,text="Make The Color Blue",command=parlak1)
dugme4.pack()

dugme5=tk.Button(pencere,text="Make The Color Green",command=parlak2)
dugme5.pack()

dugme11=tk.Button(pencere,text="Make The Color White",command=parlak3)
dugme11.pack()

briglabel= tk.Label(pencere, text="Brightness", font="100")
briglabel.pack()

dugme6=tk.Button(pencere,text="Full Brightness",command=par)
dugme6.pack()

dugme7=tk.Button(pencere,text="Half Brightness",command=par1)
dugme7.pack()

dugme8=tk.Button(pencere,text="Low Brightness(Sleep Mode)",command=par2)
dugme8.pack()

flowlabel= tk.Label(pencere, text="Flow", font="100")
flowlabel.pack()

dugme9=tk.Button(pencere,text="Flow on",command=dalga)
dugme9.pack()

dugme10=tk.Button(pencere,text="Flow off",command=dalga1)
dugme10.pack()

pencere.mainloop()
