import mysql.connector
import random
from PIL import ImageTk, Image  
import tkinter.messagebox
from tkinter import  *
# GLOBAL VARIABLES DECLARATION
myConnnection =""
cursor=""
c_id=""
#MODULE TO CHECK MYSQL CONNECTIVITY
def MYSQLconnectionCheck ():
    global myConnection
    myConnection=mysql.connector.connect(host="localhost",user="root",passwd="Yur4u4ok!", auth_plugin='mysql_native_password' )
    if myConnection:
        print("\n CONGRATULATIONS ! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED !")
        cursor=myConnection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS RAILWAY")
        cursor.execute("COMMIT")
        cursor.close()
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD !")

#MODULE TO ESTABLISHED MYSQL CONNECTION
def MYSQLconnection ():
    global myConnection
    global c_id
    myConnection=mysql.connector.connect(host="localhost",user="root",passwd="Yur4u4ok!", database="railway" , auth_plugin='mysql_native_password' )
    if myConnection:
        return myConnection
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")
        myConnection.close()

def entry():
    global cid,name,surname,phone,email
    c_id=cid.get()
    c_name=name.get()
    c_surname=surname.get()
    c_phone=phone.get()
    c_email=email.get()

    cursor=myConnection.cursor()
    sql = "INSERT INTO C_DETAILS VALUES(%s,%s,%s,%s,%s)"
    values= (c_id,c_name,c_surname,c_phone,c_email)
    myConnection.commit()
    cursor.execute(sql,values)
    cursor.execute("COMMIT")
    print("\nNew Customer Entered In The System Successfully !")
    cursor.close()

    tkinter.messagebox.showinfo("DONE", "YOU HAVE BEEN REGISTERED")

def registration():
    global cid,name,surname,phone,email
    if myConnection:
        root1=Tk()
        root1.title("registration")
        label=Label(root1,text="REGISTER YOURSELF",font='arial 25 bold')
        label.pack()

        frame=Frame(root1,height=500,width=200)
        frame.pack()
        cursor=myConnection.cursor()
        createTable ="CREATE TABLE IF NOT EXISTS C_DETAILS(CID VARCHAR(20),C_NAME VARCHAR(30),C_SURNAME VARCHAR(30),C_PHONE VARCHAR(30),C_EMAIL VARCHAR(30))"
        cursor.execute(createTable)
        label1=Label(root1,text="ID")
        label1.place(x=10,y=130)
        cid=tkinter.Entry(root1)
        cid.place(x=100,y=130)

        label2=Label(root1,text="NAME")
        label2.place(x=10,y=170)
        name=tkinter.Entry(root1)
        name.place(x=100,y=170)

        label3=Label(root1,text="SURNAME")
        label3.place(x=10,y=210)
        surname=tkinter.Entry(root1)
        surname.place(x=100,y=210)

        label4=Label(root1,text="PHONE")
        label4.place(x=10,y=250)
        phone=tkinter.Entry(root1)
        phone.place(x=100,y=250)

        label5=Label(root1,text="EMAIL")
        label5.place(x=10,y=290)
        email=tkinter.Entry(root1)
        email.place(x=100,y=290)
        
        b1=Button(root1,text="SUBMIT",command=entry)
        b1.place(x=150,y=370)
    
        root1.resizable(False,False)
        root1.mainloop()
    else:
        print("\nERROR ESTABLISHING MYSQL CONNECTION !")

def buyTicket():
    global getTicketID
    root7=Tk()
    root7.title("buy ticket")
    label=Label(root7,text="SEARCH DATA",font='arial 25 bold')
    label.pack()
    frame=Frame(root7,height=200,width=200)
    frame.pack()
    label1=Label(root7,text="Your ID")
    label1.place(x=10,y=130)
    getTicketID=tkinter.Entry(root7)
    getTicketID.place(x=100,y=130)
    b1=Button(root7,text='Submit',command=buyTicket1)
    b1.place(x=100,y=160)
    root7.resizable(False,False)
    root7.mainloop()

def buyTicket1():
    global date,departure,arrival,trainClass,ticketType,ticketNumber
    if myConnection:
        cursor=myConnection.cursor()
        get_id = getTicketID.get()
        sql2 = "SELECT * FROM C_DETAILS WHERE CID= %s"
        cursor.execute(sql2,(get_id,))
        data2 = cursor.fetchall()
        arrayOfData2=[]
        for x in data2:
            arrayOfData2.append(x) 
        if len(arrayOfData2)==0:
            tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
        else:
            root1=Tk()
            label=Label(root1,text="BUY TICKET",font='arial 25 bold')
            label.pack()
            frame=Frame(root1,height=500,width=500)
            frame.pack()
            cursor=myConnection.cursor()
            createTable ="CREATE TABLE IF NOT EXISTS C_TICKETS(C_ID VARCHAR(20),C_TICKETID VARCHAR(20),C_DATE VARCHAR(30),C_DEPARTURE VARCHAR(30),C_ARRIVAL VARCHAR(30),C_TRAINCLASS VARCHAR(30),C_TICKET VARCHAR(30))"
            cursor.execute(createTable)

            ticketLabel=Label(root1,text='TICKET ID:-')
            ticketLabel.place(x=50,y=80)
            ticketNumber = random.randint(100,5000)
            ticketLabel1=Label(root1,text=ticketNumber)
            ticketLabel1.place(x=150,y=80)

            label1=Label(root1,text="DATE")
            label1.place(x=10,y=130)
            date=tkinter.Entry(root1)
            date.place(x=100,y=130)

            label2=Label(root1,text="DEPARTURE")
            label2.place(x=10,y=170)
            departure=tkinter.Entry(root1)
            departure.place(x=100,y=170)

            label3=Label(root1,text="ARRIVAL")
            label3.place(x=10,y=210)
            arrival=tkinter.Entry(root1)
            arrival.place(x=100,y=210)

            label4=Label(root1,text="TRAIN CLASS")
            label4.place(x=10,y=250)
            labelintercity=Label(root1,text='- INTERCITY')
            labelintercity.place(x=10,y=270)
            labelfclass=Label(root1,text='- FIRST CLASS')
            labelfclass.place(x=10,y=290)
            labelsclass=Label(root1,text='- SECOND CLASS')
            labelsclass.place(x=10,y=310)
            labeltclass=Label(root1,text='- THIRD CLASS')
            labeltclass.place(x=10,y=330)
            trainClass=tkinter.Entry(root1)
            trainClass.place(x=100,y=250)

            label5=Label(root1,text="TICKET TYPE")
            label5.place(x=10,y=370)
            labelgeneral=Label(root1,text='- GENERAL')
            labelgeneral.place(x=10,y=390)
            labelstudent=Label(root1,text='- STUDENT')
            labelstudent.place(x=10,y=410)
            labelchild=Label(root1,text='- CHILD')
            labelchild.place(x=10,y=430)
            ticketType=tkinter.Entry(root1)
            ticketType.place(x=100,y=370)
            
            b1=Button(root1,text="SUBMIT",command=buyTicket2)
            b1.place(x=150,y=480)
        
            root1.resizable(False,False)
            root1.mainloop()
    else:
        print("\nERROR", "NO DATA FOUND!")

def buyTicket2():
    ticketID=getTicketID.get()
    c_date=date.get()
    c_departure=departure.get()
    c_arrival=arrival.get()
    c_trainclass=trainClass.get()
    c_ticketType=ticketType.get()

    cursor=myConnection.cursor()
    sql = "INSERT INTO C_TICKETS VALUES(%s,%s,%s,%s,%s,%s,%s)"
    values= (ticketID,ticketNumber,c_date,c_departure,c_arrival,c_trainclass,c_ticketType)
    myConnection.commit()
    cursor.execute(sql,values)
    cursor.execute("COMMIT")
    print("\nNew Customer Bought The Ticket Successfully !")
    cursor.close()

    tkinter.messagebox.showinfo("DONE", "YOU HAVE BOUGHT THE TICKET SUCCESSFULLY")

def yourTicket():
    global TicketID
    root8=Tk()
    root8.title("ticket")
    label=Label(root8,text="SEARCH DATA",font='arial 25 bold')
    label.pack()
    frame=Frame(root8,height=200,width=200)
    frame.pack()
    label1=Label(root8,text="Your ID")
    label1.place(x=10,y=130)
    TicketID=tkinter.Entry(root8)
    TicketID.place(x=100,y=130)
    b1=Button(root8,text='Submit',command=yourTicket1)
    b1.place(x=100,y=160)
    root8.resizable(False,False)
    root8.mainloop()

def yourTicket1():
    C_ID = TicketID.get()
    cursor=myConnection.cursor()
    sql="SELECT * FROM C_DETAILS WHERE CID= %s"
    cursor.execute(sql,(C_ID,))
    data=cursor.fetchall()
    arrayOfData=[]
    for i in data:
        arrayOfData.append(i) 

    sql1 = "SELECT * FROM C_TICKETS WHERE C_ID= %s"
    cursor.execute(sql1,(C_ID,))
    data1 = cursor.fetchall()
    arrayOfData1=[]
    for x in data1:
        arrayOfData1.append(x) 
    if len(arrayOfData)==0 or len(arrayOfData1)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:  
        root9=Tk()
        frame=Frame(root9,height=500,width=500)
        frame.pack()
        label1=Label(root9,text='YOUR  TICKET',font="arial 15 bold")
        label1.place(x=75,y=10)
        for i in data:
            name=Label(root9,text='NAME:',font="arial 10 bold")
            name.place(x=50,y=80)
            name1=Label(root9,text=i[1] + " " + i[2])
            name1.place(x=185,y=80)
        for x in data1:
            tid=Label(root9,text='TICKET ID:',font="arial 10 bold")
            tid.place(x=50,y=100)
            tid1=Label(root9,text=x[1])
            tid1.place(x=185,y=100)
            trainft=Label(root9,text='TRAIN FROM TO:',font="arial 10 bold")
            trainft.place(x=50,y=120)
            trainft1=Label(root9,text=x[3] + " - " + x[4])
            trainft1.place(x=185,y=120)
            date=Label(root9,text='DATE:',font="arial 10 bold")
            date.place(x=50,y=140)
            date1=Label(root9,text=x[2])
            date1.place(x=185,y=140)
            clas=Label(root9,text='TRAIN CLASS:',font="arial 10 bold")
            clas.place(x=50,y=160)
            clas1=Label(root9,text=x[5])
            clas1.place(x=185,y=160)
            carOfTrain=Label(root9,text='CAR OF THE TRAIN:',font="arial 10 bold")
            carOfTrain.place(x=50,y=180)
            car = random.randint(1,20)
            carOfTrain1=Label(root9,text=car)
            carOfTrain1.place(x=185,y=180)
            place=Label(root9,text='PLACE:',font="arial 10 bold")
            place.place(x=50,y=200)
            rplace = random.randint(1,100)
            place1=Label(root9,text=rplace)
            place1.place(x=185,y=200)
            price=Label(root9,text='PRICE:',font="arial 10 bold")
            price.place(x=50,y=220)
            rprice = random.randint(70,500)
            price1=Label(root9,text=rprice)
            price1.place(x=185,y=220)

        root9.resizable(False,False)
        root9.mainloop()


def modify():
    global aidi,inputData,choice,newData,newDetail,root6
    c_id=aidi.get()
    cursor=myConnection.cursor()
    sql="SELECT * FROM C_DETAILS WHERE CID= %s"
    cursor.execute(sql,(c_id,))
    data=cursor.fetchall()
    arrayOfData=[]
    for i in data:
        arrayOfData.append(i)   
    if len(arrayOfData)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else: 
        root6=Tk()
        root6.title("modification")
        frame=Frame(root6,height=500,width=500)
        frame.pack()
        label1=Label(root6,text='DATA MODIFICATION',font="arial 15 bold")
        label1.place(x=75,y=10)
        label2=Label(root6,text='WHAT DO YOU WANT TO CHANGE')
        label2.place(x=50,y=200)
        label3=Label(root6,text='1.NAME')
        label3.place(x=50,y=220)
        label4=Label(root6,text='2.SURNAME')
        label4.place(x=50,y=240)
        label5=Label(root6,text='3.PHONE')
        label5.place(x=50,y=260)
        label6=Label(root6,text='4.EMAIL')
        label6.place(x=50,y=280)
        inputt=Label(root6,text='Enter')
        inputt.place(x=50,y=330)
        inputData=tkinter.Entry(root6)
        inputData.place(x=100,y=330)
        for i in data:
            name=Label(root6,text='NAME:-')
            name.place(x=50,y=80)
            name1=Label(root6,text=i[1])
            name1.place(x=150,y=80)
            age=Label(root6,text='SURNAME:-')
            age.place(x=50,y=100)
            age1=Label(root6,text=i[2])
            age1.place(x=150,y=100)
            gen=Label(root6,text='PHONE:-')
            gen.place(x=50,y=120)
            gen1=Label(root6,text=i[3])
            gen1.place(x=150,y=120)
            pho=Label(root6,text='EMAIL:-')
            pho.place(x=50,y=140)
            pho1=Label(root6,text=i[4])
            pho1.place(x=150,y=140)

        b=Button(root6,text='Submit',command=do_modify)
        b.place(x=50,y=400)
        L1=Label(root6,text='OLD DETAILS')
        L1.place(x=50,y=50)
        L2=Label(root6,text='ENTER NEW DETAIL')
        L2.place(x=50,y=360)
        newDetail=tkinter.Entry(root6)
        newData=newDetail.get()
        newDetail.place(x=160,y=360)

        root6.resizable(False,False)
        root6.mainloop()

def do_modify():
    global aid,aidi,inputData,newDetail
    cursor=myConnection.cursor()
    aid=aidi.get()
    choice=inputData.get()
    new=newDetail.get()
    if choice=='1':
        sql = 'UPDATE C_DETAILS SET C_NAME=%s WHERE CID=%s'
        values = (new,aid)
        myConnection.commit()
        cursor.execute(sql,values)
    elif choice=='2':
        sql = 'UPDATE C_DETAILS SET C_SURNAME=%s WHERE CID=%s'
        values = (new,aid)
        myConnection.commit()
        cursor.execute(sql,values)       
    elif choice=='3':
        sql = 'UPDATE C_DETAILS SET C_PHONE=%s WHERE CID=%s'
        values = (new,aid)
        myConnection.commit()
        cursor.execute(sql,values)
    elif choice=='4':
        sql = 'UPDATE C_DETAILS SET C_EMAIL=%s WHERE CID=%s'
        values = (new,aid)
        myConnection.commit()
        cursor.execute(sql,values)   
    else:
        pass

    cursor.execute("COMMIT")
    cursor.close()
    root6.destroy()
    tkinter.messagebox.showinfo("DONE", "YOUR DATA HAS BEEN MODIFIED")
    
def modification_data():
    global aidi,idi,root7
    root7=Tk()
    root7.title("modification")
    label=Label(root7,text="MODIFICATION",font='arial 25 bold')
    label.pack()
    frame=Frame(root7,height=200,width=200)
    frame.pack()
    label1=Label(root7,text="ID")
    label1.place(x=10,y=130)
    aidi=tkinter.Entry(root7)
    aidi.place(x=100,y=130)
    idi=aidi.get()
    b1=Button(root7,text='Submit',command=modify)
    b1.place(x=100,y=160)
    root7.resizable(False,False)
    root7.mainloop()

     

def search_data():
    global aidi,idi
    root7=Tk()
    label=Label(root7,text="SEARCH DATA",font='arial 25 bold')
    label.pack()
    frame=Frame(root7,height=200,width=200)
    frame.pack()
    label1=Label(root7,text="ID")
    label1.place(x=10,y=130)
    aidi=tkinter.Entry(root7)
    aidi.place(x=100,y=130)
    idi=aidi.get()
    b1=Button(root7,text='Submit',command=viewDataByID)
    b1.place(x=100,y=160)
    root7.resizable(False,False)
    root7.mainloop()

def viewDataByID():
    global c_id
    if myConnection:
        cursor=myConnection.cursor()
        c_id=aidi.get()
        sql="SELECT * FROM C_DETAILS WHERE CID= %s"
        cursor.execute(sql,(c_id,))
        data=cursor.fetchall()
        if data:
            tkinter.messagebox.showinfo("DETAILS",data)

        else:
            tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!")


def viewAllData():
    if myConnection:
        cursor=myConnection.cursor()
        sql="SELECT * FROM C_DETAILS"
        cursor.execute(sql)
        data=cursor.fetchall()
        if data:
            tkinter.messagebox.showinfo("DETAILS",data)

        else:
            tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")

def checkTicket():
    global ticket_aidi
    root7=Tk()
    root7.configure(bg="black")
    label=Label(root7,text="SEARCH TICKET",font='arial 25 bold',fg="red",bg="black")
    label.pack()
    frame=Frame(root7,height=200,width=200)
    frame.pack()
    label1=Label(root7,text="TICKET ID")
    label1.place(x=10,y=130)
    ticket_aidi=tkinter.Entry(root7)
    ticket_aidi.place(x=100,y=130)
    b1=Button(root7,text='Submit',command=checkTicket1)
    b1.place(x=100,y=160)
    root7.resizable(False,False)
    root7.mainloop()

def checkTicket1():
    if myConnection:
        cursor=myConnection.cursor()
        c_id=ticket_aidi.get()
        sql="SELECT * FROM C_TICKETS WHERE C_TICKETID= %s"
        cursor.execute(sql,(c_id,))
        data=cursor.fetchall()
        if data:
            sql2="DELETE FROM C_TICKETS WHERE C_TICKETID= %s"
            myConnection.commit()
            cursor.execute(sql2,(c_id,))
            tkinter.messagebox.showwarning("SUCCESSFULLY", "TICKET WAS RETURNED")
            cursor.execute("COMMIT")
            cursor.close()
        else:
            tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!")

def checkAdmin():
    global admin_id,root12
    root12=Tk()
    root12.configure(bg="black")
    label=Label(root12,text="SEARCH ADMIN",font='arial 25 bold',fg="red",bg="black")
    label.pack()
    frame=Frame(root12,height=200,width=-5)
    frame.pack()
    label1=Label(root12,text="ID")
    label1.place(x=10,y=130)
    admin_id=tkinter.Entry(root12)
    admin_id.place(x=100,y=130)
    b1=Button(root12,text='Submit',command=adminPage)
    b1.place(x=100,y=160)
    root12.resizable(False,False)
    root12.mainloop()

def addAdmin():
    global user_id,root12
    root12=Tk()
    root12.configure(bg="black")
    label=Label(root12,text="SEARCH USER",font='arial 25 bold',fg="red",bg="black")
    label.pack()
    frame=Frame(root12,height=200,width=-5)
    frame.pack()
    label1=Label(root12,text="ID")
    label1.place(x=10,y=130)
    user_id=tkinter.Entry(root12)
    user_id.place(x=100,y=130)
    b1=Button(root12,text='Submit',command=addAdmin1)
    b1.place(x=100,y=160)
    root12.resizable(False,False)
    root12.mainloop()

def addAdmin1():
    if myConnection:
        cursor=myConnection.cursor()
        c_id=user_id.get()
        sql="SELECT * FROM C_DETAILS WHERE CID= %s"
        cursor.execute(sql,(c_id,))
        data=cursor.fetchall()
        if data:
            admin_id = data[0][0]
            admin_name = data[0][1]
            admin_surname = data[0][2]
            admin_phone = data[0][3]
            admin_email = data[0][4]
            cursor=myConnection.cursor()
            sql = "INSERT INTO C_ADMINS VALUES(%s,%s,%s,%s,%s)"
            values= (admin_id,admin_name,admin_surname,admin_phone,admin_email)
            myConnection.commit()
            cursor.execute(sql,values)
            cursor.execute("COMMIT")
            tkinter.messagebox.showwarning("ADMIN", "ADMIN ADDED SUCCESSFULLY")
            print("\nNew Admin Was Added Successfully !")
            cursor.close()
        else:
            tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!")

def viewAllAdmins():
    if myConnection:
        cursor=myConnection.cursor()
        sql="SELECT * FROM C_ADMINS"
        cursor.execute(sql)
        data=cursor.fetchall()
        if data:
            tkinter.messagebox.showinfo("ADMINS",data)

        else:
            tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")

def deleteUser():
    global user_id,root12
    root12=Tk()
    root12.configure(bg="black")
    label=Label(root12,text="SEARCH USER",font='arial 25 bold',fg="red",bg="black")
    label.pack()
    frame=Frame(root12,height=200,width=-5)
    frame.pack()
    label1=Label(root12,text="ID")
    label1.place(x=10,y=130)
    user_id=tkinter.Entry(root12)
    user_id.place(x=100,y=130)
    b1=Button(root12,text='Submit',command=deleteUser1)
    b1.place(x=100,y=160)
    root12.resizable(False,False)
    root12.mainloop()

def deleteUser1():
    if myConnection:
        cursor=myConnection.cursor()
        c_id=user_id.get()
        sql="SELECT * FROM C_DETAILS WHERE CID= %s"
        cursor.execute(sql,(c_id,))
        data=cursor.fetchall()
        if data:
            sql2="DELETE FROM C_DETAILS WHERE CID= %s"
            myConnection.commit()
            cursor.execute(sql2,(c_id,))
            tkinter.messagebox.showwarning("SUCCESSFULLY", "USER (ID: {}) WAS DELETED".format(c_id))
            cursor.execute("COMMIT")
            cursor.close()
        else:
            tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!")

def adminPage():
    if myConnection:
        cursor=myConnection.cursor()
        c_id=admin_id.get()
        sql="SELECT * FROM C_ADMINS WHERE AD_ID= %s"
        cursor.execute(sql,(c_id,))
        data=cursor.fetchall()
        if data:
            root11=Tk()
            root11.title("RAILWAY ADMIN")
            root11.configure(bg="black")
            label=Label(root11,text="RAILWAY ADMIN",font="arial 40 bold",fg="red",bg="black")
            label.pack()
            frame=Frame(root11,height=470,width=-5)
            frame.pack()
            b2=Button(root11,text="Return Tickets",font="arial 20 bold",bg='light yellow',command=checkTicket)
            b7=Button(root11,text="View all data",font='arial 20 bold',bg='light yellow',command=viewAllData)
            b3=Button(root11,text="Add admin",font="arial 20 bold",bg='light yellow',command=addAdmin)
            b4=Button(root11,text="Delete user",font='arial 20 bold',bg='light yellow',command=deleteUser)
            b5=Button(root11,text="View admins",font='arial 20 bold',bg='light yellow',command=viewAllAdmins)
            b6=Button(root11,text="Exit",font='arial 20 bold',command=root11.destroy,bg='violet')
            b7.place(x=100,y=80)
            b2.place(x=100,y=150)
            b3.place(x=100,y=220)
            b4.place(x=100,y=290)
            b5.place(x=100,y=360)
            b6.place(x=100,y=430)
            root11.resizable(False,False)
            root11.mainloop()

        else:
            tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!")

    

def customerPage():
    root=Tk()
    root.title("RAILWAY")
    test = ImageTk.PhotoImage(file = "C:\\Users\\Ostap\\OneDrive\\Робочий стіл\\unnamed3.jfif")
    label10 = tkinter.Label(image=test)
    label10.image = test
    label10.place(x=0, y=0)
    label=Label(root,text="RAILWAY",font="arial 40 bold",bg="light grey")
    label2=Label(root,text="FOR ANY QUESTIONS - AdminRailway@gmail.com",height = 1,width = 55,font="arial 14 bold",fg = "white",bg="#333",justify=LEFT)
    b1=Button(root,text="Registration",font="arial 20 bold",bg='light yellow',command=registration)
    b2=Button(root,text="Buy Tickets",font="arial 20 bold",bg='light yellow',command=buyTicket)
    b3=Button(root,text="Modify data",font="arial 20 bold",bg='light yellow',command=modification_data)
    b7=Button(root,text="View data by ID",font='arial 20 bold',bg='light yellow',command=search_data)
    b5=Button(root,text="Your Ticket",font='arial 20 bold',bg='light yellow',command=yourTicket)
    b6=Button(root,text="Exit",font='arial 20 bold',command=root.destroy,bg='violet')
    b8=Button(root,text="Admin Menu",font='arial 10 bold',borderwidth=3, relief="solid",bg='light grey',command=checkAdmin)
    label.pack()
    label2.place(x=2,y=645)
    b1.pack(side=LEFT,padx=10)
    b3.pack(side=LEFT,padx=10)
    b2.place(x=10,y=500)
    b7.pack(side=LEFT,padx=10)
    b5.place(x=250,y=500)
    b6.place(x=500,y=500)
    b8.place(x=550,y=10)
    canvas=Canvas(root,height=600,width=-5)
    #canvas.create_text(50, 550, text="HELLO WORLD", fill="black", font=('Helvetica 15 bold'))
    canvas.pack()
    root.resizable(False,False)
    root.mainloop()

myConnection = MYSQLconnectionCheck ()
if myConnection:
    MYSQLconnection ()
customerPage()