from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

class ForgetPass:
    def __init__(self, root):
        self.root = root
        self.root.title("Forget Password")
        self.root.geometry("350x400+470+150")
        self.root.config(bg = "white")
        self.root.focus_force()
        self.root.grab_set()
        
        t=Label(self.root, text="Forget Password", font=("TimesNew Roman",20, "bold"),bg = "white", fg="red").place(x=0, y=10, relwidth=1)
        #=====================================Forget Password =====================
        questions = Label(self.root, text = "Security Question", font = ("Times New Roman", 15),bg="white", fg="gray").place(x=50, y=100)
        self.ccb_quest = ttk.Combobox(self.root, font = ("Times New Roman", 13), state="readonly", justify=CENTER)
        self.ccb_quest['values']=("Select", "Your first pet name", "Your birth date", "Your best friend name")
        self.ccb_quest.place(x=50, y=130, width=250)
        self.ccb_quest.current(0)
        
        answer = Label(self.root, text = "Answer", font = ("Times New Roman", 15),bg="white", fg="gray").place(x=50, y=180)
        self.txt_answer = Entry(self.root, font = ("Times New Roman", 15, "bold"),bg="lightgray")
        self.txt_answer.place(x=50, y=210, width=250)
        
        new_password = Label(self.root, text = "New Password", font = ("Times New Roman", 15),bg="white", fg="gray").place(x=50, y=260)
        self.txt_new_password = Entry(self.root, font = ("Times New Roman", 15, "bold"),bg="lightgray")
        self.txt_new_password.place(x=50, y=290, width=250)
        
        btn_login=Button(self.root, text="Reset Password", font = ("Times New Roman", 15, "bold"), fg="white", bg="green", cursor="hand2").place(x=100, y=340)
        

if __name__ == '__main__':
    root = Tk()
    obj = ForgetPass(root)
    root.mainloop()