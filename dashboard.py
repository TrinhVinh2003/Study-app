from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image, ImageDraw
from course import CourseClass
from HuyTrung import ScorePredict
from thoikhoabieu import thoikhoabieu
from clock import dem_nguoc
import os
from datetime import *
import time
from math import *

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Support Student System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg = "white")
        
#===============================icon=====================================
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")
        
#===============================title=====================================        
        title = Label(self.root, text = "Hệ thống giúp đỡ sinh viên", font=("Times New Roman", 20, "bold"), bg = "#033054", 
                      fg = "white", image=self.logo_dash, compound=LEFT, padx=10).place(x=0, y=0, relwidth=1, height=50)
#================================Clock====================================
        self.lbl = Label(self.root, bg = "white")
        self.lbl.place(x=10, y=180, height=450, width=350)
        self.working() 
#================================Menu=====================================
        M_Frame = LabelFrame(self.root, text = "Menus", font=("times new roman", 15))        
        M_Frame.place(x=10, y=70, width=1340, height=80)
        
        btn_predict = Button(M_Frame, text = "Dự đoán điểm thi", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white", cursor = "hand2", command=self.scorePredict).place(x=20, y=5, width=200, height=40)
        btn_calendar = Button(M_Frame, text = "Đếm ngược", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white", cursor = "hand2", command=self.countDown).place(x=240, y=5, width=200, height=40)
        btn_arrange = Button(M_Frame, text = "Sắp xếp thời gian", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white", cursor = "hand2", command=self.calendar).place(x=460, y=5, width=200, height=40)
        btn_free = Button(M_Frame, text = "Khóa học miễn phí", font=("times new roman", 15, "bold", ), bg="#0b5377", fg="white", cursor = "hand2", command=self.add_course).place(x=680, y=5, width=200, height=40)
        btn_logout = Button(M_Frame, text = "Đăng xuất", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white", cursor = "hand2", command=self.logout).place(x=900, y=5, width=200, height=40)
        btn_exit = Button(M_Frame, text = "Thoát", font=("times new roman", 15, "bold"), bg="#0b5377", fg="white", cursor = "hand2", command=self.quit).place(x=1120, y=5, width=200, height=40)
#================================Content window=============================
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.ANTIALIAS )
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=400, y=180, width=920, height=350)
#================================Footer=====================================
        footer = Label(self.root, text = "Hệ thống giúp đỡ sinh viên\nLiên hệ 0353693xxx để biết thêm thông tin chi tiết", font=("times new roman", 12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)        
        M_Frame.place(x=10, y=70, width=1340, height=80)
#================================Update Details==============================
        self.lbl_course = Label(self.root, text="Total Course\n[4]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=400,y=530, width=300, height=100)
        
        self.lbl_student = Label(self.root, text="Total Result\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=710,y=530, width=300, height=100)
        
        self.lbl_result = Label(self.root, text="Total Student\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1020,y=530, width=300, height=100)
#===================================Function================================
    def clock_image(self, hr, mn, sec):
        clock=Image.new("RGB", (400, 400), (255, 255, 255))
        draw=ImageDraw.Draw(clock)
        #==============For clock image============
        bg = Image.open("images/c.png")
        bg = bg.resize((300, 300), Image.ANTIALIAS)
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
        
    def scorePredict(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ScorePredict(self.new_win)

    def calendar(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = thoikhoabieu(self.new_win)

    def countDown(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = dem_nguoc(self.new_win)
    
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)
    
    def logout(self):
        op = messagebox.askyesno("Xác nhận", "Bạn muốn đăng xuất chứ ?", parent=self.root)
        if op == True:
            self.root.destroy()
            os.system("python login.py")
        
    def quit(self):
        op = messagebox.askyesno("Xác nhận", "Bạn muốn thoát chứ ?", parent=self.root)
        if op == True:
            self.root.destroy()

        
if __name__ == '__main__':
    root = Tk()
    obj = RMS(root)
    root.mainloop()
        