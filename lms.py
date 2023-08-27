#-----------------
#FOR MySQL
#-----------------
'''create database db;

create table books(bid varchar(20) primary key, title varchar(30),
  author varchar(30), status varchar(30));

create table books_issued(bid varchar(20) primary
  key, issuedto varchar(30));'''
#-----------------------------------------------------------------------------------



#importing necessary modules
import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

#creating connection between MySQL and py
mypass = "root"
mydatabase="db" 
con = mysql.connector.connect (port="3306",host="localhost",user="root",password="root",database=mydatabase)
curs = con.cursor()

#creating GUI with Tkinter
root = Tk()
root.title("Library Management System")
root.minsize(width=500,height=600)
root.geometry("600x500")
root.config(bg="black")


headingFrame1 = Frame(root,bg="red",bd=7)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="  Welcome to \n the Royal Library!!!", bg='yellow', fg='black', font=('Harlow Solid Italic',21))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#FUNCTIONS
def bookRegister():
    
    bid = bookid.get()
    title = booktitle.get()
    author = bookauthor.get()
    status = bookstatus.get()
    status = status.lower()
    
    insertBooks = "insert into "+books+" values ('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(bid)
    print(title)
    print(author)
    print(status)
    root.destroy()

def addBook(): 
    
    global bookid ,booktitle, bookauthor, bookstatus, Canvas1, con, cur, books, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
 
    con =mysql.connector.connect( host="localhost",user="root",password="root",database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    books = "books" 

    Canvas1 = Canvas(root)
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#3639ff",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='orange', fg='black', font=('arial bold',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white',font=('arial bold',15))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookid = Entry(labelFrame)
    bookid.place(relx=0.32,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white',font=('arial bold',15))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    booktitle = Entry(labelFrame)
    booktitle.place(relx=0.32,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white',font=('arial bold',15))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookauthor = Entry(labelFrame)
    bookauthor.place(relx=0.32,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Book Status
    lb4 = Label(labelFrame,text="Avail/Issued: ", bg='black', fg='white',font=('arial bold',14))
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookstatus = Entry(labelFrame)
    bookstatus.place(relx=0.32,rely=0.65, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    subbutton = Button(root,text="SUBMIT",bg='#d1ccc0', fg='red',font=('arial bold',15),command=bookRegister)
    subbutton.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitbutton = Button(root,text="Quit",bg='#d1ccc0', fg='red',font=('arial bold',15), command=root.destroy)
    quitbutton.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()   

def View(): 
    books = "books"
    root = tk.Tk()
    root.title("Library")
    root.minsize(width=755,height=600)
    root.geometry("250x400")

    mypass = "root"
    mydatabase="db"

    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#FFFFFF")
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(root,bg="blue",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    headingLabel = Label(headingFrame1, text="View Books",bg='orange', fg='black', font=('arial bold',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='white')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    lb2 = Label(labelFrame,text="BOOK ID", bg='white', fg='black',font=('arial bold',15))
    lb2.place(relx=0,rely=0.45)
    lb2 = Label(labelFrame,text="TITLE", bg='white', fg='black',font=('arial bold',15))
    lb2.place(relx=0.28,rely=0.45)
    lb2 = Label(labelFrame,text="AUTHOR", bg='white', fg='black',font=('arial bold',15))
    lb2.place(relx=0.568,rely=0.45)
    lb2 = Label(labelFrame,text="STATUS", bg='white', fg='black',font=('arial bold',15))
    lb2.place(relx=0.85,rely=0.45)

    con =mysql.connector.connect( host="localhost",user="root",password="root",database=mydatabase)
    cur = con.cursor()
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#FFFFFF")
    Canvas1.pack(expand=True,fill=BOTH)


    cur.execute("SELECT * FROM books")
    i=0 
    for student in cur: 
     for j in range(len(student)):
        e = Entry(Canvas1,width=20, fg='red',bg="black",bd=3,font=('arial bold',12)) 
        e.grid(row=i, column=j) 
        e.insert(END, student[j])
     i=i+1
    Canvas1.mainloop()


   
def BookDeleter():
    
    books="books"
    bid = bookid.get()

    mypass = "root"
    mydatabase="db"

    con =mysql.connector.connect( host="localhost",user="root",password="root",database=mydatabase)
    cur = con.cursor()
    
    deleteSql = "delete from "+books+" where bid = '"+bid+"'"
    
    cur.execute(deleteSql)
    con.commit()
    messagebox.showinfo('Success',"Book Record Deleted Successfully")
        
   
    print(bid)
    bookid.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global bookid,booktitle,bookauthor,bookstatus,Canvas1,con,cur,books,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas1 = Canvas(root)
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='orange', fg='black', font=('arial bold',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='white')
    labelFrame.place(relx=0.25,rely=0.3,relwidth=0.5,relheight=0.1)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID: ", bg='white', fg='black',font=('arial bold',15))
    lb2.place(relx=0.0001,rely=0.285)
        
    bookid = Entry(labelFrame)
    bookid.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    #Submit Button
    subbutton = Button(root,text="SUBMIT",bg='#d1ccc0', fg='red',font=('arial bold',15),command=BookDeleter)
    subbutton.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitbutton = Button(root,text="Quit",bg='#d1ccc0', fg='red',font=('arial bold',15), command=root.destroy)
    quitbutton.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


def members():

    global bookid,booktitle,bookauthor,bookstatus,Canvas1,con,cur,books,root
    
    root = Tk()
    root.title("Members")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas1 = Canvas(root)
    Canvas1.config(bg="white")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#3639ff",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Members", bg='orange', fg='black', font=('arial bold',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    #member ID
    lb1 = Label(labelFrame,text="Member ID : ", bg='black', fg='white',font=('arial bold',15))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookid = Entry(labelFrame)
    bookid.place(relx=0.32,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Name         : ", bg='black', fg='white',font=('arial bold',15))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    booktitle = Entry(labelFrame)
    booktitle.place(relx=0.32,rely=0.35, relwidth=0.62, relheight=0.08)
        
    #Book id (bid)
    lb3 = Label(labelFrame,text="Book ID      : ", bg='black', fg='white',font=('arial bold',15))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookauthor = Entry(labelFrame)
    bookauthor.place(relx=0.32,rely=0.50, relwidth=0.62, relheight=0.08)
    
    subbutton = Button(root,text="SUBMIT",bg='#d1ccc0', fg='red',font=('arial bold',15),command=memAdder)
    subbutton.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitbutton = Button(root,text="Quit",bg='#d1ccc0', fg='red',font=('arial bold',15), command=root.destroy)
    quitbutton.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
def memAdder():    
    mid = bookid.get()
    name = booktitle.get()
    bid = bookauthor.get()
    
    mypass = "root"
    mydatabase="db"

    con =mysql.connector.connect( host="localhost",user="root",password="root",database=mydatabase)
    cur = con.cursor()

    insertmembers = "insert into members values ('"+mid+"','"+name+"','"+bid+"')"
    cur.execute(insertmembers)
    con.commit()
    root.destroy()


def ViewMem(): 
    members = "members"
    root = tk.Tk()
    root.title("Members List")
    root.minsize(width=500,height=800)
    root.geometry("250x400")
    Canvas1 = Canvas(root)
    Canvas1.config(width="500",height="200",bg="black")
    Canvas1.pack(side=TOP)

    mypass = "root"
    mydatabase="db"

    headingFrame1 = Frame(root,bg="blue",bd=5)
    headingFrame1.place(relx=0.25,rely=0.05,relwidth=0.5,relheight=0.13)
    
    headingLabel = Label(headingFrame1, text="View Members",bg='orange', fg='black', font=('arial bold',20))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    con =mysql.connector.connect( host="localhost",user="root",password="root",database=mydatabase)
    cur = con.cursor()

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#FFFFFF")
    Canvas1.pack(expand=True,fill=BOTH)


    cur.execute("SELECT * FROM members")
    i=0 
    for student in cur: 
     for j in range(len(student)):
        e = Entry(Canvas1,width=20, fg='red',bg="black",bd=3,font=('arial bold',12)) 
        e.grid(row=i, column=j) 
        e.insert(END, student[j])
     i=i+1
    Canvas1.mainloop()

def DelMem():
    global mid
    
    con =mysql.connector.connect( host="localhost",user="root",password="root",database=mydatabase)
    cur = con.cursor()
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#FFFFFF")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#3639ff",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='orange', fg='black', font=('arial bold',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='white')
    labelFrame.place(relx=0.25,rely=0.3,relwidth=0.5,relheight=0.1)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Member ID:", bg='white', fg='black',font=('arial bold',15))
    lb2.place(relx=0.001,rely=0.285)
        
    mid = Entry(labelFrame)
    mid.place(relx=0.4,rely=0.4, relwidth=0.62)

    #Submit Button
    subbutton = Button(root,text="SUBMIT",bg='#d1ccc0', fg='red',font=('arial bold',15),command=MemberDeleter)
    subbutton.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitbutton = Button(root,text="Quit",bg='#d1ccc0', fg='red',font=('arial bold',15), command=root.destroy)
    quitbutton.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def MemberDeleter():
    
    tablename="members"
    memID = mid.get()

    mypass = "root"
    mydatabase="db"

    con =mysql.connector.connect( host="localhost",user="root",password="root",database=mydatabase)
    cur = con.cursor()
    
    deleteSql = "delete from "+tablename+" where mid = '"+memID+"'"
    
    cur.execute(deleteSql)
    con.commit()
    messagebox.showinfo('Success',"Member Record Deleted Successfully")
        
   
#########BUTTONS##########

button1 = Button(root,text="ADD BOOK",bg='orange', fg='black',font=('arial bold',25),command=addBook)
button1.place(x=120,y=170, relwidth=0.6,relheight=0.12)
    
button2 = Button(root,text="DELETE BOOK",bg='orange', fg='black',font=('arial bold',23), command=delete)
button2.place(x=120,y=330, relwidth=0.6,relheight=0.12)
    
button3 = Button(root,text="VIEW BOOKS",bg='orange', fg='black',font=('arial bold',25), command=View)
button3.place(x=120,y=410, relwidth=0.6,relheight=0.12)

button4 = Button(root,text="ADD MEMBERS",bg='orange', fg='black',font=('arial bold',25), command=members)
button4.place(x=120,y=250, relwidth=0.6,relheight=0.12)

button5 = Button(root,text="VIEW MEMBERS",bg='orange', fg='black',font=('arial bold',25), command=ViewMem)
button5.place(x=120,y=490, relwidth=0.6,relheight=0.12)

button6 = Button(root,text="DELETE \n MEMBERS",bg='orange', fg='black',font=('arial bold',11), command=DelMem)
button6.place(x=482,y=490, relwidth=0.25,relheight=0.12)
    
root.mainloop()








