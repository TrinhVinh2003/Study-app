from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import random

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        colors = ["red",  "green", "blue", "yellow", "pink", "red2", "gold2"]
        def IntroLabelColorTick():
            fg = random.choice(colors)
            SliderLabel.config(fg = fg)
            SliderLabel.after(100, IntroLabelColorTick)
        def IntroLabelTick():
            global count, text, time
            if self.time < 100:
                if(self.count >= len(ss)):
                    self.count = 0
                    self.text = ""
                    SliderLabel.config(text=self.text)
                else:
                    self.text = self.text + ss[self.count]
                    SliderLabel.config(text=self.text)
                    self.count += 1
            SliderLabel.after(200, IntroLabelTick)
#==================================Label==========================================
        ss = "Welcome to Student Management System"
        self.count = 0
        self.text = ""
        self.time = 0
        SliderLabel = Label(self.root, text = ss, bd = 12, relief = GROOVE, 
                      font = ("Times New Roman", 40, "bold"), bg = "yellow", fg = "red")
        SliderLabel.pack(side = TOP, fill = X)
        IntroLabelTick()
        #IntroLabelColorTick()
#==================================All Variables==================================
        self.Roll_No_Var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        
        self.search_by = StringVar() 
        self.search_txt = StringVar()
        
#==================================Manage_Frame===================================        
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=450, height=580)
        
        m_title=Label(Manage_Frame, text="Manage Students", font = ("Times New Roman", 30, "bold"), bg = "crimson", fg = "white")
        m_title.grid(row=0, columnspan=2, pady=20)
        
        lbl_roll=Label(Manage_Frame, text="Roll No.", font = ("Times New Roman", 20, "bold"), bg = "crimson", fg = "white")
        lbl_roll.grid(row=1, column=0, pady=10, padx= 20, sticky="w")
        
        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No_Var ,font = ("Times New Roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx= 20, sticky="w")
        
        lbl_name=Label(Manage_Frame, text="Name", font = ("Times New Roman", 20, "bold"), bg = "crimson", fg = "white")
        lbl_name.grid(row=2, column=0, pady=10, padx= 20, sticky="w")
        
        txt_Name = Entry(Manage_Frame, textvariable=self.name_var,font = ("Times New Roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=10, padx= 20, sticky="w")
        
        lbl_email=Label(Manage_Frame, text="Email", font = ("Times New Roman", 20, "bold"), bg = "crimson", fg = "white")
        lbl_email.grid(row=3, column=0, pady=10, padx= 20, sticky="w")
        
        txt_Email = Entry(Manage_Frame, textvariable=self.email_var, font = ("Times New Roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx= 20, sticky="w")
        
        lbl_Gender=Label(Manage_Frame, text="Gender", font = ("Times New Roman", 20, "bold"), bg = "crimson", fg = "white")
        lbl_Gender.grid(row=4, column=0, pady=10, padx= 20, sticky="w")
        
        combo_Gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font = ("Times New Roman", 13, "bold"), state = "readonly")
        combo_Gender['values']=("Male", "Female", "Other")
        combo_Gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")
        
        lbl_contact=Label(Manage_Frame, text="Contact", font = ("Times New Roman", 20, "bold"), bg = "crimson", fg = "white")
        lbl_contact.grid(row=5, column=0, pady=10, padx= 20, sticky="w")
        
        txt_Contact = Entry(Manage_Frame, textvariable=self.contact_var, font = ("Times New Roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx= 20, sticky="w")
        
        lbl_dob=Label(Manage_Frame, text="D.O.B", font = ("Times New Roman", 20, "bold"), bg = "crimson", fg = "white")
        lbl_dob.grid(row=6, column=0, pady=10, padx= 20, sticky="w")
        
        txt_DOB = Entry(Manage_Frame, textvariable=self.dob_var, font = ("Times New Roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_DOB.grid(row=6, column=1, pady=10, padx= 20, sticky="w")
        
        lbl_address=Label(Manage_Frame, text="Address", font = ("Times New Roman", 20, "bold"), bg = "crimson", fg = "white")
        lbl_address.grid(row=7, column=0, pady=10, padx= 20, sticky="w")
        
        self.txt_Address = Text(Manage_Frame, width=30, height=4, font = ("", 10))
        self.txt_Address.grid(row=7, column=1, pady=10, padx= 20, sticky="w")
        
        
#==================================Button Frame===================================
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=10, y=520, width=420)
        
        Addbtn = Button(btn_Frame, text="Add", width=10, command=self.add_student).grid(row=0, column=0, padx=10, pady=10)
        Updatebtn = Button(btn_Frame, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        Deletebtn = Button(btn_Frame, text="Delete", width=10, command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_Frame, text="Clear", width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)
        
#==================================Detail Frame===================================       
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=800, height=580)
        
        lbl_search=Label(Detail_Frame, text="Search By", font = ("Times New Roman", 20, "bold"), bg = "crimson", fg = "white")
        lbl_search.grid(row=0, column=0, pady=10, padx= 20, sticky="w")
        
        combo_Search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=10, font = ("Times New Roman", 13, "bold"), state = "readonly")
        combo_Search['values']=("Roll_no", "Name", "Contact")
        combo_Search.grid(row=0, column=1, pady=10, padx=20, sticky="w")
        
        txt_Search = Entry(Detail_Frame, width=20, textvariable=self.search_txt, font = ("Times New Roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx= 20, sticky="w")
        
        Searchbtn = Button(Detail_Frame, text="Search", width=10, pady=5, command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        Showallbtn = Button(Detail_Frame, text="Show All", width=10, pady=5, command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)
        
#==================================Table Frame=====================================
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)
        
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame, columns=("Roll", "Name", "Email", "Gender", "Contact", "D.O.B", "Address"), xscrollcommand=scroll_x, yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Roll", text="Roll No.")
        self.Student_table.heading("Name", text="Name")
        self.Student_table.heading("Email", text="Email")
        self.Student_table.heading("Gender", text="Gender")
        self.Student_table.heading("Contact", text="Contact")
        self.Student_table.heading("D.O.B", text="D.O.B")
        self.Student_table.heading("Address", text="Address")
        self.Student_table['show'] = 'headings'
        self.Student_table.column("Roll", width=100)
        self.Student_table.column("Name", width=100)
        self.Student_table.column("Email", width=100)
        self.Student_table.column("Gender", width=100)
        self.Student_table.column("Contact", width=100)
        self.Student_table.column("D.O.B", width=100)
        self.Student_table.column("Address", width=150)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()
        
    def add_student(self):
        if self.Roll_No_Var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            con=pymysql.connect(host='localhost', user="root", password="", database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s, %s, %s, %s, %s, %s, %s)", (self.Roll_No_Var.get(),
                                                                                    self.name_var.get(),
                                                                                    self.email_var.get(),
                                                                                    self.gender_var.get(),
                                                                                    self.contact_var.get(),
                                                                                    self.dob_var.get(),
                                                                                    self.txt_Address.get('1.0', END)
                                                                                    ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
    
    def fetch_data(self):
        con=pymysql.connect(host='localhost', user="root", password="", database="stm")
        cur=con.cursor()
        cur.execute("Select * from students")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values = row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_Var.set('')
        self.name_var.set('')
        self.email_var.set('')
        self.gender_var.set('')
        self.contact_var.set('')
        self.dob_var.set('')
        self.txt_Address.delete('1.0', END)
        
    def get_cursor(self, ev):
        curosor_row = self.Student_table.focus()
        contents = self.Student_table.item(curosor_row)
        row = contents['values']
        self.Roll_No_Var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete('1.0', END)
        self.txt_Address.insert(END, row[6])
        
    def update_data(self):
        con=pymysql.connect(host='localhost', user="root", password="", database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s where roll_no=%s", (
                                                                                self.name_var.get(),
                                                                                self.email_var.get(),
                                                                                self.gender_var.get(),
                                                                                self.contact_var.get(),
                                                                                self.dob_var.get(),
                                                                                self.txt_Address.get('1.0', END),
                                                                                self.Roll_No_Var.get()
                                                                                ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        
    def delete_data(self):
        con=pymysql.connect(host='localhost', user="root", password="", database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s", self.Roll_No_Var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        
    def search_data(self):
        con=pymysql.connect(host='localhost', user="root", password="", database="stm")
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" Like '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values = row)
            con.commit()
        con.close()

if __name__ == '__main__':
    root = Tk()
    ob = Student(root)
    root.mainloop()
        