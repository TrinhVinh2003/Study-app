from math import floor
from tkcalendar import *
from tkinter import *
from tkinter import messagebox
from datetime import date 
import time
class dem_nguoc:
    def __init__(self, root):
        self.root = root
        self.root.title('Clock')
        self.root.geometry('1290x550+56+0')
        self.root.config(bg ='#758AA2')


        mainframe = Frame(self.root ,bd= 10 ,width= 1245,height=700, relief= RIDGE, bg= 'pink')
        mainframe.grid()
        Titleframe = Frame(mainframe,bd =5,width= 1245,background='yellow',height=100,relief = RIDGE)
        Titleframe.grid(row =0, column= 0 )

        topframe = Frame(mainframe, bd =7 ,width= 1235 ,height= 500,relief= RIDGE)
        topframe.grid(row =1 , column=0)
        leftframe  = Frame(topframe, bd = 5 , width = 1245,height=400,padx =2,bg ='cadet blue', relief=RIDGE)
        leftframe.pack(side= LEFT)
        leftframe1 = Frame(leftframe, bd =5 ,width = 600,height =180, padx =2,pady =4 , relief=RIDGE)
        leftframe1.pack(side=TOP,padx=10,pady=20)


        rightframe = Frame(topframe,bd =5 , width = 320, height= 400, padx =2,bg ='cadet blue',relief=RIDGE)
        rightframe.pack(side = BOTTOM, padx =2)
        rightframe1 = Frame(rightframe,bd =5 , width=310, height = 300, padx =2 ,pady =2, relief=RIDGE)
        rightframe1.pack(side = TOP, padx=5,pady= 6)

        lbltitle = Label(Titleframe , font=('arial', 50,'bold'),text = 'Countdown time',bd =7, bg = 'yellow')
        lbltitle.grid(row= 0 ,column =0, padx =91) 
# ===================================
        dob =StringVar()
        cdate = StringVar()
        days =StringVar()
        months =StringVar()
        weeks = StringVar()
        hours =StringVar()
        minutes =StringVar()
        seconds = StringVar()
        def reset():
            cdate.set('')
            days.set('')
            months.set('')
            weeks.set('')
            hours.set('')
            minutes.set('')
            seconds.set('')
        def result():


            Currentdate = (entdate.get_date())
            dobdate =  (entdob.get_date())

            day = (((Currentdate-dobdate).days))
            if day < 0:
                messagebox.showerror('error', ' Vui lòng nhập lại ') 
            else:
                days.set(str(day))
                age = int(days.get())
                ages = age/365
    
                week = int(days.get())
                a= floor(week/7)
                weeks.set(str('%.0f'%(a)))
                b = floor(ages*12)
                months.set(str('%.0f'%(b)))
                hours.set(str('%.0f'%(week *24)))
                minute = int(hours.get())
                minutes.set(str('%.0f'%(minute *60)))
                second =int(minutes.get())
                seconds.set(str('%.0f'%(second *60)))

        def countdown():
            day = int(days.get())
            week = int(weeks.get())
            month = int(months.get())
            mins = int(minutes.get())
            secs = int(seconds.get())
            hrs = int(hours.get())
            while month >-1:
                month-=1
                months.set(month)
                if month == -1:
                    months.set(0)
                while week >-1:
                    a= day/365
                    week-=1
                    weeks.set(week)
                    if week == a *12:
                        break 
                    if week ==-1:
                        weeks.set(0)

                    while day > -1:
                        day-=1 
                        days.set(day)
                        if day == week*7:
                            break
                        if day ==-1:
                            days.set(0)
                        while  hrs>-1 :
                            hrs-=1
                            hours.set(hrs)
                            if hrs == day*24:
                                break
                            if hrs ==-1:
                                hours.set(0)
                            while mins > -1:
                                mins-=1 
                                minutes.set(mins)
                                if mins  == hrs*60:
                                    break
                                if mins == -1:
                                    minutes.set(0)
                                while  secs > -1:
                           
                                    secs -= 1
                                    time.sleep(1)                   
                                    seconds.set(secs)
                                    leftframe1.update()
                                    if secs == mins*60: 
                                        break
                                    if secs == -1:
                                        seconds.set(0)
                         
                        
                
            
                

        
        lbldob = Label(leftframe1 ,font = ('arial', 16 , 'bold'),text ='Thời điểm bây giờ',bd =7,anchor='w', justify=LEFT)
        lbldob.grid(row =1 , column =0 ,sticky =W ,padx =5 ) 
        entdob = DateEntry(leftframe1,font= ('arial', 16,'bold' ),bd= 5,width= 43 ,date_pattern = 'dd/mm/yyyy' )
        entdob.grid(row =1 , column =1)
        now = date.today().strftime('%d/%m/%Y') #biễu diễn giá trị ngày giờ, thời gian
        entdob.set_date(now)


        lbldate = Label(leftframe1 ,font = ('arial', 16 , 'bold'),text ='ngày',bd =7,anchor='w', justify=LEFT)
        lbldate.grid(row =2 , column =0 ,sticky =W,padx =5 )
        entdate = DateEntry(leftframe1,font= ('arial', 16,'bold' ),bd= 10,width= 43 ,date_pattern ='dd/mm/yyyy',textvariable =cdate)
        entdate.grid(row =2 , column =1)

        lbldays = Label(leftframe1 ,font = ('arial', 16 , 'bold'),text ='Days',bd =7,anchor='w', justify=LEFT)
        lbldays.grid(row =3 , column =0 ,sticky =W,padx =5 )
        entdays = Entry(leftframe1,font= ('arial', 16,'bold' ),bd= 7,width= 43 ,textvariable= days)
        entdays.grid(row =3 , column =1)


        lblmonths = Label(leftframe1 ,font = ('arial', 16 , 'bold'),text ='Months',bd =7,anchor='w', justify=LEFT)
        lblmonths.grid(row =4 , column =0 ,sticky =W,padx =5 )
        entmonths = Entry(leftframe1,font= ('arial', 16,'bold' ),bd= 5,width= 43 ,textvariable=months)
        entmonths.grid(row =4 , column =1)

        lblhours = Label(leftframe1 ,font = ('arial', 16 , 'bold'),text ='Hours',bd =7,anchor='w', justify=LEFT)
        lblhours.grid(row =6 , column =0 ,sticky =W,padx =5 )
        enthours = Entry(leftframe1,font= ('arial', 16,'bold' ),bd= 5,width= 43 ,textvariable=hours)
        enthours.grid(row =6 , column =1)

        lblweeks = Label(leftframe1 ,font = ('arial', 16 , 'bold'),text ='Weeks',bd =7,anchor='w', justify=LEFT)
        lblweeks.grid(row =5 , column =0 ,sticky =W,padx =5 )
        entweeks = Entry(leftframe1,font= ('arial', 16,'bold' ),bd= 5,width= 43,textvariable= weeks)
        entweeks.grid(row =5 , column =1)

        lblminutes = Label(leftframe1 ,font = ('arial', 16 , 'bold'),text ='Minutes',bd =7,anchor='w', justify=LEFT)
        lblminutes.grid(row =7 , column =0 ,sticky =W,padx =5 )
        entminutes = Entry(leftframe1,font= ('arial', 16,'bold' ),bd= 5,width= 43 ,textvariable= minutes)
        entminutes.grid(row =7 , column =1)


        lblseconds = Label(leftframe1 ,font = ('arial', 16 , 'bold'),text ='Seconds',bd =7,anchor='w', justify=LEFT)
        lblseconds.grid(row =8 , column =0 ,sticky =W,padx =5 )
        entseconds = Entry(leftframe1,font= ('arial', 16,'bold' ),bd= 5,width= 43,textvariable= seconds)
        entseconds.grid(row =8 , column =1)
#=======================================================
        def back():
            self.root.destroy()
        
        btncalculate =  Button(rightframe1,padx =18 , bd = 7 ,font = ('Helvetica',18,'bold'),width=23, text='OK', bg ='pink',command= result)
        btncalculate.grid(row =0,column=0,padx=10,pady =2)
        
        btnreset =  Button(rightframe1,padx =18 , bd = 7 ,font = ('Helvetica',18,'bold'),width=23, text='Reset', bg ='pink',command= reset)
        btnreset.grid(row =1,column=0,padx=10,pady =2)
        Btncountdown = Button(rightframe1, padx=18 , bd = 7 ,font = ('Helvetica',18,'bold'),width=23, text='Countdown', bg ='pink',command= countdown).grid(row =2,column=0,padx=10,pady =2)
        btnback =  Button(rightframe1,padx =18 , bd = 7 ,font = ('Helvetica',18,'bold'),width=23, text='Back', bg ='pink',command=back)
        btnback.grid(row =3,column=0,padx=10,pady =2)

if __name__ =='__main__':
    root= Tk()
    application = dem_nguoc(root)
    root.mainloop() 