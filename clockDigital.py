from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image, ImageDraw
from datetime import *
import time
from math import *

class Clock:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Clock")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg = "white")
        
        title = Label(self.root, text = "Wellcome", font=("times new roman", 50, "bold")).place(x=0, y=50, relwidth=1)
        
        self.lbl = Label(self.root, bg = "blue")
        self.lbl.place(x=450, y=150, height=400, width=400)
        self.working() 
    def clock_image(self, hr, mn, sec):
        clock=Image.new("RGB", (400, 400), (255, 255, 255))
        draw=ImageDraw.Draw(clock)
        #==============For clock image============
        bg = Image.open("images/c.png")
        bg = bg.resize((300, 300), Image.Resampling.LANCZOS)
        clock.paste(bg, (50, 50))
        #==============Hour Line Image============
        origin = 200, 200
        draw.line((origin, 200+50*sin(radians(hr)), 200-50*cos(radians(hr))), fill = "pink", width=3)
        #==============Minute Line Image============
        draw.line((origin, 200+80*sin(radians(mn)), 200-80*cos(radians(mn))), fill = "blue", width=3)
        #==============Second Line Image============
        draw.line((origin, 200+100*sin(radians(sec)), 200-100*cos(radians(sec))), fill = "green", width=3)
        draw.ellipse((195, 195, 210, 210), fill = "black")
        clock.save("images/clock_new.png")
    
    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        hr = (h/12)*360
        mn = (m/60)*360
        sec = (s/60)*360 
        self.clock_image(hr, mn, sec)
        self.img = ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)

if __name__ == '__main__':
    root = Tk()
    obj = Clock(root)
    root.mainloop()