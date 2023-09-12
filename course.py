from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import webbrowser


class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Khóa học miễn phí")
        self.root.geometry("1500x700+80+170")
        self.root.config(bg = "white")
        self.root.state('zoomed')
        
#===============================title=====================================        
        title = Label(self.root, text = "Khóa học miễn phí cho học sinh sinh viên", font=("Times New Roman", 20, "bold"), bg = "#033054", 
                      fg = "white", compound=LEFT, padx=10).place(x=0, y=0, relwidth=1, height=50)
#==========================================================================
        hus_title = Label(self.root, text = "Gợi ý:", font=("Times New Roman", 20, "bold"), bg="white", bd=0).place(x=50, y=60)
#=======================================Nhiệt==============================        
        self.thermal_course = ImageTk.PhotoImage(file="images/thermal.png")
        self.thermal_btn = Button(self.root, image=self.thermal_course, command=self.thermal).place(x=50, y=150)
        thermal_lbl = Label(self.root, text = "Nhiệt động lực học và vật lý phân tử", font=("Times New Roman", 15, "bold"), bg="white", bd=0).place(x=80, y=570)
#=======================================Robotics===========================
        self.robotics_course = ImageTk.PhotoImage(file="images/robotics.png")
        self.robotics_btn = Button(self.root, image=self.robotics_course, command=self.robotics).place(x=410, y=150)
        robotics_lbl = Label(self.root, text = "Nhập môn Robotics", font=("Times New Roman", 15, "bold"), bg="white", bd=0).place(x=500, y=570)
#======================================Python=============================
        self.python_course = ImageTk.PhotoImage(file="images/python.png")
        self.python_btn = Button(self.root, image=self.python_course, command=self.python).place(x=770, y=150)
        python_lbl = Label(self.root, text = "Nhập môn lập trình Python", font=("Times New Roman", 15, "bold"), bg="white", bd=0).place(x=830, y=570)
#======================================Tiếng Anh==========================
        self.english_course = ImageTk.PhotoImage(file="images/english.png")
        self.english_btn = Button(self.root, image=self.english_course, command=self.english).place(x=1130, y=150)
        english_lbl = Label(self.root, text = "Tiếng Anh chuyên ngành", font=("Times New Roman", 15, "bold"), bg="white", bd=0).place(x=1210, y=570)
#==========================================================================
        bonus_title = Label(self.root, text = "Còn rất khóa học đang miễn phí. Các bạn có thể vào đây tham khảo: ", font=("Times New Roman", 20, "bold"), bg="white", bd=0).place(x=50, y=650)
        self.bonus_btn = Button(self.root, text="Tham khảo", font=("Times New Roman", 20, "bold"),bg="red", fg="white", relief=GROOVE, bd="2", command=self.all).place(x=900, y=640)        

        self.bonus_btn = Button(self.root, text="Back", font=("Times New Roman", 20, "bold"),bg="lightgray", fg="black", relief=GROOVE, bd="2", command=self.quit).place(x=750, y=720)

    def thermal(self):
        webbrowser.open('https://www.edx.org/course/thermodynamics-and-phase-equilibria?index=product&queryID=bb5de7075b74016c48fbcaa8e2162ac2&position=3', new=2)
        
    def robotics(self):
        webbrowser.open('https://www.edx.org/course/robotics-foundations-i-robot-modeling?index=product&queryID=d80eae746d75db26b1a12ef060f29f80&position=1', new=2)
        
    def python(self):
        webbrowser.open('https://www.edx.org/course/cs50s-introduction-to-programming-with-python?index=product&queryID=0caeece07bd74bdac63c67321f3b715c&position=1', new=2)
        
    def english(self):
        webbrowser.open('https://www.edx.org/course/academic-english?index=product&queryID=026f116abaf8ca4123d1d7a229eb3d0b&position=2', new=2)
        
    def all(self):
        webbrowser.open('https://www.edx.org/', new=2)
    
    def quit(self):
        self.root.destroy() 

if __name__ == '__main__':
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()