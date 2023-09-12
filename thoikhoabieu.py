from tkinter import *
from tkinter import ttk 


class thoikhoabieu():
    def __init__(self, root):
        self.root = root
      
        self.root.title('Thời khóa biểu')
        self.root.geometry('1350x700+0+0')
       
        
        def update_record():
            selected =member_records.focus()  #trả về hàng mục đã chọn trong treeview
        
            member_records.item(selected,text = '',values=(entsearch.get() ,entbay_chin.get(),entten_eleven.get(),
            entthirteen_fifteen.get(), entseventeen_nineteen.get(),entseventeen_nineteen.get(),entnineteen_twenty_one.get(),enttwenty_one_three.get()))
             #trả về tất cả các giá trị trong mục đã chọn .Câc giá trị này được trả về một tuple
            entbay_chin.delete(0,END)
            entten_eleven.delete(0,END)
            entthirteen_fifteen.delete(0,END)
            entsixteen_eighteen.delete(0,END)
            entnineteen_twenty_one.delete(0,END)
            entseventeen_nineteen.delete(0,END)
            enttwenty_one_three.delete(0,END)
            
        
        
        def select_record():
            entsearch.delete(0,END)
            entbay_chin.delete(0,END)
            entten_eleven.delete(0,END)
            entthirteen_fifteen.delete(0,END)
            entsixteen_eighteen.delete(0,END)
            entnineteen_twenty_one.delete(0,END)
            entseventeen_nineteen.delete(0,END)
            enttwenty_one_three.delete(0,END)
            
            selected =  member_records.focus()

            values = member_records.item(selected, 'values')
            entsearch.insert(0, values[0])
            entbay_chin.insert(0, values[1])
            entten_eleven.insert(0, values[2])
            entthirteen_fifteen.insert(0,values[3])
            entsixteen_eighteen.insert(0,values[4])
            entnineteen_twenty_one.insert(0,values[5])
            entseventeen_nineteen.insert(0,values[6])
            enttwenty_one_three.insert(0,values[7])
            





        mainframe = Frame(self.root,bd = 10,width = 1350, height = 700, relief= RIDGE, bg ='pink')
        mainframe.grid()
        titleframe = Frame(mainframe,bd = 7,width = 1320, height = 100, relief= RIDGE, bg ='pink')
        titleframe.grid(row = 0 , column= 0)
        searchframe  = Frame(mainframe,bd = 7,padx = 5,width = 1320, height = 50, relief= RIDGE, bg ='pink')
        searchframe.grid(row =1 ,column= 0)
        midframe = Frame(mainframe,bd = 5,padx = 5,width = 1320, height = 500, relief= RIDGE, bg ='pink')
        midframe.grid(row  =2 , column=  0)
        detailframe = Frame(midframe,bd = 5,width = 1320, height = 100,padx= 6,pady =4, relief= RIDGE)
        detailframe.grid(row =1, column=0 )
        treeviewframe = Frame(midframe,bd = 5,padx = 2,width = 1320, height = 400, relief= RIDGE)
        treeviewframe.grid(row =0, column=0 )
        buttonframe = Frame(midframe,bd = 5,width = 1320, height = 50, relief= RIDGE)
        buttonframe.grid(row =2, column=0 )

        lbltitle = Label(titleframe , font = ('arial', 40,'bold'),text = 'THỜI KHÓA BIỂU',bd = 7)
        lbltitle.grid(row = 0, column=0 ,padx =422)
        #=====================================
        lblbay_chin = Label(detailframe, font=(' arial',12,'bold'), text= '7h-9h', bd= 7)
        lblbay_chin.grid(row =0, column= 0 ,sticky = W, padx = 5)
        entbay_chin = Entry(detailframe , font = ('arial',12,'bold'), bd=5 ,justify=LEFT)
        entbay_chin.grid(row =0, column= 1,padx =10)
        
        lblten_eleven = Label(detailframe, font=(' arial', 12,'bold'), text= '10h-12h', bd= 7, anchor='w', justify= LEFT)
        lblten_eleven.grid(row =1, column= 0 ,sticky = W, padx = 5)
        entten_eleven = Entry(detailframe , font = ('arial',12,'bold'), bd=5 ,justify=LEFT)
        entten_eleven.grid(row =1, column= 1,padx =10)
        
        lblthirteen_fifteen = Label(detailframe, font=(' arial', 12,'bold'), text= '13h-15h', bd= 7, anchor='w', justify= LEFT)
        lblthirteen_fifteen.grid(row =2, column= 0 ,sticky = W, padx = 5)
        entthirteen_fifteen = Entry(detailframe , font = ('arial',12,'bold'), bd=5 ,justify=LEFT)
        entthirteen_fifteen.grid(row =2, column= 1,padx =10)

        lblsixteen_eighteen = Label(detailframe, font=(' arial', 12,'bold'), text= '16h-18h', bd= 7, anchor='w', justify= LEFT)
        lblsixteen_eighteen.grid(row =0, column= 2 ,sticky = W, padx = 5)
        entsixteen_eighteen = Entry(detailframe , font = ('arial',12,'bold'), bd=5 ,justify=LEFT)
        entsixteen_eighteen.grid(row =0, column= 3,padx =10)

        lblseventeen_nineteen = Label(detailframe, font=(' arial', 12,'bold'), text= '19h-20h', bd= 7, anchor='w', justify= LEFT)
        lblseventeen_nineteen.grid(row =1, column= 2 ,sticky = W, padx = 5)
        entseventeen_nineteen = Entry(detailframe , font = ('arial',12,'bold'), bd=5 ,justify=LEFT)
        entseventeen_nineteen.grid(row =1, column= 3,padx =10)

        lblnineteen_twenty_one = Label(detailframe, font=(' arial', 12,'bold'), text= '21h-22h', bd= 7, anchor='w', justify= LEFT)
        lblnineteen_twenty_one.grid(row =2, column= 2 ,sticky = W, padx = 5)
        entnineteen_twenty_one = Entry(detailframe , font = ('arial',12,'bold'), bd=5 ,justify=LEFT)
        entnineteen_twenty_one.grid(row =2, column= 3,padx =10)

        lbltwenty_one_three = Label(detailframe, font=(' arial', 12,'bold'), text= '22h-23h45', bd= 7, anchor='w', justify= LEFT)
        lbltwenty_one_three.grid(row =0, column= 4 ,sticky = W, padx = 5)
        enttwenty_one_three = Entry(detailframe , font = ('arial',12,'bold'), bd=5 ,justify=LEFT)
        enttwenty_one_three.grid(row =0, column= 5,padx =10)

        member_records = ttk.Treeview(treeviewframe, height=10 ,columns=( 'thu', '7h-9h', '10h-12h','13h-15h','16h-18h','19h-20h','21h-22h','22h-23h45'))
        member_records.heading('thu',text= '')          # hiện thị cột có tiêu đề
        member_records.heading('7h-9h',text= '7h-9h')
        member_records.heading('10h-12h',text= '10-12h')
        member_records.heading('13h-15h',text= '13h-15h')
        member_records.heading('16h-18h',text= '16h-18h')
        member_records.heading('19h-20h',text= '19h-20h')
        member_records.heading('21h-22h',text= '21h-22h')
        member_records.heading('22h-23h45',text= '22h-23h45')

        data = ['Thứ 2', '','','','','','','']
        data1 = ['Thứ 3', '','','','','','','']
        data2 = ['Thứ 4', '','','','','','','']
        data3 = ['Thứ 5', '','','','','','','']
        data4 = ['Thứ 6', '','','','','','','']
        data5 = ['Thứ 7', '','','','','','','']
        data6 = ['Chủ nhật', '','','','','','','']
        member_records.insert('',END, values=data)
        member_records.insert('',END, values=data1)
        member_records.insert('',END, values=data2)
        member_records.insert('',END, values=data3)
        member_records.insert('',END, values=data4)
        member_records.insert('',END, values=data5)
        member_records.insert('',END, values=data6)
        member_records['show'] ='headings'

        member_records.column('thu',width= 100)
        member_records.column('7h-9h',width= 160)
        member_records.column('10h-12h',width= 160)
        member_records.column('13h-15h',width= 160)
        member_records.column('16h-18h',width= 160)
        member_records.column('19h-20h',width= 160)
        member_records.column('21h-22h',width= 160)
        member_records.column('22h-23h45',width= 160)

        member_records.pack(fill= BOTH, expand=1)
        #=========================================


        def back():
            root.destroy()
        entsearch = Entry(searchframe, font = ('arial',16,'bold'),width=33,justify=RIGHT)
        entsearch.grid(row = 0, column=0,padx= 20 )

        btnadd = Button(buttonframe,command =update_record, font = ('arial',16,'bold'),text= 'OK',width=19,padx= 2, pady =23, bd =4 , height=1 ,bg ='pink')
        btnadd.grid(row =0 , column = 0,padx = 10)
        btnshow = Button(buttonframe,command=select_record, font = ('arial',16,'bold'),text= 'Select',width=19,padx= 2, pady =23, bd =4 , height=1 ,bg ='pink')
        btnshow.grid(row =0 , column = 1,padx = 10)
        btnback = Button(buttonframe, font = ('arial',16,'bold'),text= 'Back',width=19,padx= 2, pady =23, bd =4 , height=1 ,bg ='pink', command= back)
        btnback.grid(row =0 , column = 2,padx = 10)

if __name__ =='__main__':
    root= Tk()
    application = thoikhoabieu(root)
    root.mainloop()