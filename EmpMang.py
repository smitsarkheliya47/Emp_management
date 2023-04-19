from tkinter import *
from tkinter import messagebox
import mysql.connector
import smtplib, ssl
import tkinter as tk
import pandas as pd
import qrcode
from PIL import ImageTk,Image
import pandas as pd
from pyqrcode import create
import pyqrcode
 

root = Tk()
root.geometry("700x500")

def management():
    a = s1.get()
    b = s2.get()
    c = s3.get()
    d = s4.get()
    e = s5.get()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="emp_management"
    )

    mycursor = mydb.cursor()
    sql = "insert into details(emp_id,emp_name,salary,address,contact_no) values (%s,%s,%s,%s,%s)"
    val = (a, b, c, d, e)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("record...", "insert succesfully...!!!")


def view():
    top1 = Tk()
    top1.geometry("800x300")
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="emp_management"
    )

    my_conn = db.cursor()
    my_conn.execute("SELECT * FROM details ")
    i = 0
    for details in my_conn:
        for j in range(len(details)):
            e = Entry(top1, width=20, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, details[j])
        i = i+1
    db.commit()
    db.close()
    top1.mainloop()


def delete():

    root1=Tk()
    root1.geometry("500x400")

    def delete1():

        Id=e1.get()

        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="emp_management"
            )
        mycursor=mydb.cursor()
        sql="DELETE FROM details WHERE emp_id=%s"
        val=(Id)
        mycursor.execute(sql,(val,))
        mydb.commit()
        messagebox.showinfo("Record","delete Successfully...!!")
        mydb.close()


    w1 = Label(root1, text="..≛≛.. ENTER EMP_ID AND DELETE HERE ..≛≛..",
           font=("arial", 12, "bold"), bg="powder blue", fg="black")
    w1.grid(row=0,column=2)

    l1=Label(root1,text="EMP ID:➾",font=("arial",16,"bold"))
    l1.grid(row=1,column=1)
    e1=Entry(root1,width=20,bd=5)
    e1.grid(row=1,column=2)
    b1=Button(root1,text="Delete", bg="powder blue", fg="black",width=10,bd=5,font=("arial",16,"bold"),command=delete1)
    b1.grid(row=2,column=2)
    
    root1.mainloop()


def update():

    root2=Tk()
    root2.geometry("700x400")

    def update1():

        Id=s1.get()
        name=s2.get()
        salary=s3.get()
        address=s4.get()
        
        
        connection = mysql.connector.connect(host='localhost',
                                             database='emp_management',
                                             user='root',
                                             password='')

        cur = connection.cursor()
        
        sql="UPDATE details SET emp_name=%s,salary=%s,address=%s  WHERE emp_id=%s"
        val=(name,salary,address,Id)
            
        cur.execute(sql,val)
        connection.commit()
        messagebox.showinfo("Record","Updated Successfully....!!")


    w1 = Label(root2, text="..≛≛.. UPDATE YOUR MANAGEMENT SYSTEM HERE ..≛≛..",
           font=("arial", 12, "bold"), bg="powder blue", fg="black")
    w1.grid(row=0,column=2)

    q1 = Label(root2, text="EMP ID:➾", font=("arial", 12, "bold"))
    q1.grid(row=1, column=1)

    s1 = Entry(root2, font=("arial", 12, "bold"), bd=5, width=24)
    s1.grid(row=1, column=2)

    q2 = Label(root2, text="EMP NAME:➾", font=("arial", 12, "bold"))
    q2.grid(row=2, column=1)

    s2 = Entry(root2, font=("arial", 12, "bold"), bd=5, width=24)
    s2.grid(row=2, column=2)

    q3 = Label(root2, text="EMP SALARY:➾", font=("arial", 12, "bold"))
    q3.grid(row=3, column=1)

    s3 = Entry(root2, font=("arial", 12, "bold"), bd=5, width=24)
    s3.grid(row=3, column=2)

    q4 = Label(root2, text="EMP ADDRESS:➾", font=("arial", 12, "bold"))
    q4.grid(row=4, column=1)

    s4 = Entry(root2, font=("arial", 12, "bold"), bd=5, width=24)
    s4.grid(row=4, column=2)

    q5 = Label(root2, text="CONTACT NO:➾", font=("arial", 12, "bold"))
    q5.grid(row=5, column=1)

    s5 = Entry(root2, font=("arial", 12, "bold"), bd=5, width=24)
    s5.grid(row=5, column=2)

    p4 = Button(root2, text="Update", bd=5, font=(
    'arial', 12, 'bold'), bg="powder blue", fg="black", width=5, command=update1)
    p4.grid(row=8, column=2)

    root2.mainloop()


def csv():
    mydb = mysql.connector.connect(
        host='localhost',
        database='emp_management',
        user='root',
        password='')
        
    mycursor = mydb.cursor()
    sql = "SELECT * FROM details"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    all_id = []
    all_name = []
    all_salary = []
    all_address = []
    all_contact = []
    all_date = []
    for emp_id,emp_name,salary,address,contact_no,date in myresult:
        all_id.append(emp_id)
        all_name.append(emp_name)
        all_salary.append(salary)
        all_address.append(address)
        all_contact.append(contact_no)
        all_date.append(date)

    dic = {'emp_id':all_id,'emp_name':all_name,'salary':all_salary,'address':all_address,'contact_no' :all_contact,'date' :all_date}
    df=pd.DataFrame (dic)
    df_csv=df.to_csv("D:/PYTHON/smit.csv",index=False)
    messagebox.showinfo("Record","CSV File Generate Successfully.......!!")



def email():
    sender_email = "sender@xyz.com"
    receiver_email = "receiver@xyz.com"
    message = """\
    Subject: It Worked!

    Simple Text email from your Python Script."""

    port = 465  
    app_password = input("Enter Password: ")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("sender@xyz.com", app_password)
        server.sendmail(sender_email, receiver_email, message)



def pdf():
      

    stmt = "Select * from details"
    conn = mysql.connector.connect(user="root",
                                   password="",
                                   database="emp_management")
    cursor = conn.cursor()
    cursor.execute(stmt)
    row = cursor.fetchall()
    for i in row:
        try:
            with open(i[0], 'wb') as outfile:
                outfile.write(i[1])
                outfile.close()
                print("Filename Saved as: " + i[0])
        except:
            pass


def qrcodee():
    
    
    global my_image

    l1=Label(Frame1)
    l1.grid(row=10,column=2)
    
    Id=s1.get()
    name=s2.get()
    salary=s3.get()
    address=s4.get()
    contact=s5.get()
    qrdata=pyqrcode.create(f"emp_id:{Id}\n emp_name:{name}\n salary:{salary}\n address:{address}\n contact_no:{contact}")
    my1_qr=qrdata.xbm(scale=2)
    my_image=tk.BitmapImage(data=my1_qr)
    l1.config(image=my_image)

Frame1=Frame(root,height=250,width=350,bg="deep sky blue",bd=1,relief=FLAT)    
Frame1.grid(row=13,column=2)

ll1=Label(Frame1,text="Your QR Generate Here...!!",font=("arial,6,bold"),bg="lightblue",fg="black")
ll1.grid(row=11,column=2)



s1 = IntVar()
s2 = StringVar()
s3 = StringVar()
s4 = StringVar()
s5 = StringVar()

w1 = Label(root, text="..≛≛.. EMPLOYEE MANAGEMENT SYSTEM ..≛≛..",
           font=("arial", 12, "bold"), bg="powder blue", fg="black")
w1.grid(row=0, column=2)

q1 = Label(root, text="EMP ID:➾", font=("arial", 12, "bold"))
q1.grid(row=1, column=1)

s1 = Entry(root, font=("arial", 12, "bold"), bd=9, width=24)
s1.grid(row=1, column=2)

q2 = Label(root, text="EMP NAME:➾", font=("arial", 12, "bold"))
q2.grid(row=2, column=1)

s2 = Entry(root, font=("arial", 12, "bold"), bd=8, width=24)
s2.grid(row=2, column=2)

q3 = Label(root, text="EMP SALARY:➾", font=("arial", 12, "bold"))
q3.grid(row=3, column=1)

s3 = Entry(root, font=("arial", 12, "bold"), bd=8, width=24)
s3.grid(row=3, column=2)

q4 = Label(root, text="EMP ADDRESS:➾", font=("arial", 12, "bold"))
q4.grid(row=4, column=1)

s4 = Entry(root, font=("arial", 12, "bold"), bd=8, width=24)
s4.grid(row=4, column=2)

q5 = Label(root, text="CONTACT NO:➾", font=("arial", 12, "bold"))
q5.grid(row=5, column=1)

s5 = Entry(root, font=("arial", 12, "bold"), bd=8, width=24)
s5.grid(row=5, column=2)

p1 = Button(root, text="Insert", bd=5, font=(
    'arial', 12, 'bold'), bg="powder blue", fg="black", width=5, command=management)
p1.grid(row=7, column=1)

p2 = Button(root, text="View", bd=5, font=(
    'arial', 12, 'bold'), bg="powder blue", fg="black", width=5, command=view)
p2.grid(row=7, column=2)

p3 = Button(root, text="Delet", bd=5, font=(
    'arial', 12, 'bold'), bg="powder blue", fg="black", width=5, command=delete)
p3.grid(row=8, column=1)

p4 = Button(root, text="Update", bd=5, font=(
    'arial', 12, 'bold'), bg="powder blue", fg="black", width=5, command=update)
p4.grid(row=8, column=2)

p5 = Button(root, text="Csv", bd=5, font=(
    'arial', 12, 'bold'), bg="powder blue", fg="black", width=5, command=csv)
p5.grid(row=9,column=1)

p6 = Button(root, text="Email", bd=5, font=(
    'arial', 12, 'bold'), bg="powder blue", fg="black", width=5, command=email)
p6.grid(row=9,column=2)

p7 = Button(root, text="Pdf", bd=5, font=(
    'arial', 12, 'bold'), bg="powder blue", fg="black", width=5, command=pdf)
p7.grid(row=8,column=3)

p8 = Button(root, text="QR code", bd=5, font=(
    'arial', 12, 'bold'), bg="powder blue", fg="black", width=10, command=qrcodee)
p8.grid(row=9,column=3)

root.mainloop()    