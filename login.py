from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw
import pymysql #pip install pymysql
from datetime import *
import time
from math import *
import os
from forget import ForgetPass

class Login_Window:
   def __init__(self,root):
      self.root=root
      self.root.title("Login and registration system for Apps")
      self.root.geometry("1350x700+0+0")
      self.root.config(bg="#021e2f")
      #========================Background Color========================
      self.left_lbl=Label(self.root, bg="#63B8FF", bd=0)
      self.left_lbl.place(x=0, y=0, relheight=1, width = 600)
      
      self.right_lbl=Label(self.root, bg="#031F3C", bd=0)
      self.right_lbl.place(x=600, y=0, relheight=1,  relwidth=1)
      #==========================Frames=======================
      login_frame = Frame(self.root, bg="white")
      login_frame.place(x=250, y=100, width=800, height=500)
      
      title = Label(login_frame, text="LOGIN HERE", font = ("Times New Roman", 30, "bold"), bg="white", fg="#63B8FF").place(x=250, y=50)
      

      email=Label(login_frame, text="EMAIL ADDRESS",font = ("Times New Roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=150)
      self.txt_email=Entry(login_frame, font = ("Times New Roman", 15), bg="lightgray")
      self.txt_email.place(x=284, y=180, width=350, height=35)
      self.user_icon = ImageTk.PhotoImage(file='images/username_icon.png')
      self.user_label = Label(login_frame, image=self.user_icon, bg='#040405')
      self.user_label.place(x=250, y=180, width=34, height=34)
      #=============================Password==================
      password=Label(login_frame, text="PASSWORD",font = ("Times New Roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=250)
      self.txt_password=Entry(login_frame, font = ("Times New Roman", 15), bg="lightgray")
      self.txt_password.place(x=284, y=280, width=350, height=35)
      self.password_icon = ImageTk.PhotoImage(file='images/password_icon.png')
      self.password_icon_label = Label(login_frame, image=self.password_icon, bg='#040405')
      self.password_icon_label.place(x=250, y=280, width=34, height=34)
      
      btn_forget=Button(login_frame, text="Forget Password", font = ("Times New Roman", 14), bd=0, bg="white", fg="#B00857", cursor="hand2", command=self.forget_pw_win).place(x=250, y=320)
      btn_login=Button(login_frame, text="Login", font = ("Times New Roman", 20, "bold"), fg="white", bg="#B00857", cursor="hand2", command=self.login).place(x=250, y=360, width=180, height=40)
      
      self.bg_register = ImageTk.PhotoImage(file='images/register.png')
      btn_rg=Label(login_frame, text="Don't have account?", font = ("Times New Roman", 14), bg="white", fg="#B00857").place(x=250, y=440)
      btn_register=Button(login_frame,image=self.bg_register, cursor="hand2", bg="white", bd=0, command=self.register).place(x=420, y=437)
      # ========= show/hide password ==================================================================
      self.show_image = ImageTk.PhotoImage(file='images/show.png')

      self.hide_image = ImageTk.PhotoImage(file='images/hide.png')

      self.show_button = Button(self.root, image=self.show_image, command=self.show, relief=RIDGE,
                                   borderwidth=2, background="white", cursor="hand2")
      self.show_button.place(x=900, y=380, width=35, height=35)
      
      #=========================Clock==================================
      self.lbl = Label(self.root, bg = "#081923", bd=10)
      self.lbl.place(x=90, y=120, height=450, width=350)
      self.working()
      
   def show(self):
      self.hide_button = Button(self.root, image=self.hide_image, command=self.hide, relief=RIDGE,
                                   borderwidth=2, background="white", cursor="hand2")
      self.hide_button.place(x=900, y=380, width=35, height=35)
      self.txt_password.config(show='')

   def hide(self):
      self.show_button = Button(self.root, image=self.show_image, command=self.show, relief=RIDGE,
                                 borderwidth=2, background="white", cursor="hand2")
      self.show_button.place(x=900, y=380, width=35, height=35)
      self.txt_password.config(show='*')
   
   def login(self):
      if self.txt_email.get() == "" or self.txt_password.get() == "":
         messagebox.showerror("Error", "All Fields are required!", parent = self.root)
      else:
         try:
            con=pymysql.connect(host='localhost', user="root", password="", database="employee2")
            cur=con.cursor()
            cur.execute("select * from employee where email=%s and password=%s", (self.txt_email.get(), self.txt_password.get()))
            row=cur.fetchone()
            if row == None:
               messagebox.showerror("Error", "Invalid Username or Password", parent = self.root)
            else:
               messagebox.showinfo("Success", "Welcome to", parent = self.root)
               self.root.destroy()
               os.system("python dashboard.py")
            con.close()
         except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root) 
   def register(self):
      self.root.destroy()
      os.system("python register.py") 
      
   def reset(self):
      self.ccb_quest.current(0)
      self.txt_answer.delete(0, END)
      self.txt_new_password.delete(0, END)
      self.txt_password.delete(0, END)
      self.txt_email.delete(0, END)
      
   def forget_pw(self):
      if self.ccb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_password.get()=="":
         messagebox.showerror("Error", "All Fields are required!", parent=self.new)
      else:
         try:
            con=pymysql.connect(host='localhost', user="root", password="", database="employee2")
            cur=con.cursor()
            cur.execute("select * from employee where email=%s and question=%s and answer=%s", (self.txt_email.get(), self.ccb_quest.get(), self.txt_answer.get()))
            row=cur.fetchone()
            if row == None:
               messagebox.showerror("Error", "Please select the correct sercurity question / Enter answer", parent = self.root)
            else:
               cur.execute("update employee set password=%s where email=%s", (self.txt_new_password.get() ,self.txt_email.get()))
               con.commit()
               con.close()
               messagebox.showinfo("Success", "Your password has been reset, please enter your new password", parent=self.root)
               self.reset()
               self.new.destroy()
         except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
         
         
         
   def forget_pw_win(self):
      if self.txt_email.get()=="":
         messagebox.showerror("Error", "Please enter the email address to reset password", parent=self.root)
      else:
         try:
            con=pymysql.connect(host='localhost', user="root", password="", database="employee2")
            cur=con.cursor()
            cur.execute("select * from employee where email=%s", self.txt_email.get())
            row=cur.fetchone()
            if row == None:
               messagebox.showerror("Error", "Please enter the valid email address to reset password", parent = self.root)
            else:
               con.close()
               self.new = Toplevel()
               self.new.title("Forget Password")
               self.new.geometry("350x400+470+150")
               self.new.config(bg = "white")
               self.new.focus_force()
               self.new.grab_set()
               
               t=Label(self.new, text="Forget Password", font=("Times New Roman",20, "bold"),bg = "white", fg="red").place(x=0, y=10, relwidth=1)
               #=====================================Forget Password =====================
               questions = Label(self.new, text = "Security Question", font = ("Times New Roman", 15),bg="white", fg="gray").place(x=50, y=100)
               self.ccb_quest = ttk.Combobox(self.new, font = ("Times New Roman", 13), state="readonly", justify=CENTER)
               self.ccb_quest['values']=("Select", "Your first pet name", "Your birth date", "Your best friend name")
               self.ccb_quest.place(x=50, y=130, width=250)
               self.ccb_quest.current(0)
               
               answer = Label(self.new, text = "Answer", font = ("Times New Roman", 15),bg="white", fg="gray").place(x=50, y=180)
               self.txt_answer = Entry(self.new, font = ("Times New Roman", 15, "bold"),bg="lightgray")
               self.txt_answer.place(x=50, y=210, width=250)
               
               new_password = Label(self.new, text = "New Password", font = ("Times New Roman", 15),bg="white", fg="gray").place(x=50, y=260)
               self.txt_new_password = Entry(self.new, font = ("Times New Roman", 15, "bold"),bg="lightgray")
               self.txt_new_password.place(x=50, y=290, width=250)
               
               btn_change=Button(self.new, text="Reset Password", font = ("Times New Roman", 15, "bold"), fg="white", bg="green", cursor="hand2", command=self.forget_pw).place(x=100, y=340)
            
         except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
         
      
         
   def clock_image(self, hr, mn, sec):
      clock=Image.new("RGB", (400, 400), (8, 25, 35))
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
      
      
if __name__ == "__main__":
    root=Tk()
    ob=Login_Window(root)
    root.mainloop()
