import email
from logging import PlaceHolder
from tkinter import *
root = Tk()
root.geometry("600x600")
root.title("ADV-172 Project")

userlabel = Label(root,text="Username:")
userlabel.place(relx=0.3,rely=0.2,anchor=CENTER)
username = Entry(root)
username.place(relx = 0.6,rely=0.2,anchor=CENTER)
emaillabel = Label(root, text="Email ID:")
emaillabel.place(relx=0.3,rely=0.3)
email_id = Entry(root)
email_id.place(relx=0.6,rely=0.3,anchor=CENTER)
label1 = Label(root)
label1.place(relx=0.5,rely=0.5,anchor=CENTER)

dictionary = {}

class Users():
  
  def __init__(self):
    print("This is class users")

  def addUsers(key,value):
    global dictionary
    dictionary[key] = value
    label1["text"] = dictionary

class getUsers(Users):

  def __init__(self):
    print("Thi is the get users class")

  def getUsers():
    Username = username.get()
    Email_id = email_id.get()
    Users.addUsers(Username,Email_id) 

btn = Button(root, text="Add users details", command=getUsers.getUsers) 
btn.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()