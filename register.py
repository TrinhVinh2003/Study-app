from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
import pymysql
import os

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registeration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg = "white")
        
#==============================BG image=======================
        self.bg = ImageTk.PhotoImage(file="images/b2.jpg")
        bg = Label(self.root, image=self.bg).place(x=250, y=0, relheight=1, relwidth=1)
        
#===============================Left image=====================
        self.left = ImageTk.PhotoImage(file="images/side.png")
        bg = Label(self.root, image=self.left).place(x=80, y=100, height=500, width=400)

#===============================Register frame=================
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)
        
        title = Label(frame1, text = "REGISTER HERE", font = ("Times New Roman", 20, "bold"),bg="white", fg="green").place(x=50, y=30)
        #=======================================================
        
        fname = Label(frame1, text = "First Name", font = ("Times New Roman", 15),bg="white", fg="gray").place(x=50, y=100)
        self.txt_fname = Entry(frame1, font = ("Times New Roman", 15, "bold"),bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)
        
        lname = Label(frame1, text = "Last Name", font = ("Times New Roman", 15),bg="white", fg="gray").place(x=370, y=100)
        self.txt_lname = Entry(frame1, font = ("Times New Roman", 15, "bold"),bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)
        #=========================================================
        contact = Label(frame1, text = "Contact No.", font = ("Times New Roman", 15),bg="white", fg="gray").place(x=50, y=170)
        self.txt_contact = Entry(frame1, font = ("Times New Roman", 15, "bold"),bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)
        
        email = Label(frame1, text = "Email", font = ("Times New Roman", 15),bg="white", fg="gray").place(x=370, y=170)
        self.txt_email = Entry(frame1, font = ("Times New Roman", 15, "bold"),bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)
        #==========================================================
        questions = Label(frame1, text = "Security Question", font = ("Times New Roman", 15),bg="white", fg="gray").place(x=50, y=240)
        self.ccb_quest = ttk.Combobox(frame1, font = ("Times New Roman", 13), state="readonly", justify=CENTER)
        self.ccb_quest['values']=("Select", "Your first pet name", "Your birth date", "Your best friend name")
        self.ccb_quest.place(x=50, y=270, width=250)
        self.ccb_quest.current(0)
        
        answer = Label(frame1, text = "Answer", font = ("Times New Roman", 15),bg="white", fg="gray").place(x=370, y=240)
        self.txt_answer = Entry(frame1, font = ("Times New Roman", 15, "bold"),bg="lightgray")
        self.txt_answer.place(x=370, y=270, width=250)
        #============================================================
        password = Label(frame1, text = "Password", font = ("Times New Roman", 15),bg="white", fg="gray").place(x=50, y=310)
        self.txt_password = Entry(frame1, font = ("Times New Roman", 15, "bold"),bg="lightgray")
        self.txt_password.place(x=50, y=340, width=250)
        
        cpassword = Label(frame1, text = "Confirm Password", font = ("Times New Roman", 15),bg="white", fg="gray").place(x=370, y=310)
        self.txt_cpassword = Entry(frame1, font = ("Times New Roman", 15, "bold"),bg="lightgray")
        self.txt_cpassword.place(x=370, y=340, width=250)
#==========================================Terms===========================================
        self.var_chk=IntVar()
        chk = Checkbutton(frame1, text="I Agree With The Terms & Condition", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", font = ("Times New Roman", 12)).place(x=50, y=380)
        
        self.button_img = ImageTk.PhotoImage(file="images/register1.png")
        btn_register = Button(frame1, image=self.button_img, bd=0, cursor="hand2", command=self.register_data).place(x=50, y=420)
        btn_login = Button(self.root, text="Sign In",font = ("Times New Roman", 20), bd=0, cursor="hand2", command=self.login).place(x=250, y=460)
    def login(self):
        self.root.destroy()
        os.system("python login.py")
    
    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.ccb_quest.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.ccb_quest.current(0)
    
    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.txt_email.get()==""or self.ccb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()==""or self.txt_cpassword.get()=="":
            messagebox.showerror("Error", "All Fields are required!", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "Password and Confirm Password should be same!", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "You need to agree terms and conditions!", parent=self.root)
        else:
            try:
                con=pymysql.connect(host='localhost', user="root", password="", database="employee2")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s", self.txt_email.get())
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User Already!", parent=self.root)
                else:
                    cur.execute("insert into employee (f_name, l_name, contact, email, question, answer, password) values(%s, %s, %s, %s, %s, %s, %s)",
                                (self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.ccb_quest.get(),
                                self.txt_answer.get(),
                                self.txt_password.get(),
                                ))
                    con.commit()
                    con.close()
                    self.clear()
                messagebox.showinfo("Success", "Register successful", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
        
        

if __name__ == '__main__':
    root = Tk()
    obj = Register(root)
    root.mainloop()