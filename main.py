#!/usr/bin/python3

from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import LEFT
from tkinter import RIGHT
from tkinter import Entry
from tkinter import StringVar
import socket

# now that I tested the code I have to create a client

msg = "Connect with the target"

def sockBtnCallBack(textField,portField,msgToShow):

    print("You've entered : ",textField.get(),portField.get())
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#    sock.bind((textField.get(),int(portField.get())))
    sock.connect((textField.get(),int(portField.get())))
    msgToShow.set("Connected with the target")
    
#    sock.listen()
    



    sock.sendall(b"Hello world from python3 server")
    data = sock.recv(1024)
    print("Server recieved from client: ",data)
    sock.close()

def main():
    root = Tk() # Creating the root
    msgToShow = StringVar()
    msgToShow.set("Waiting for the connection....")

    root.title("VirtualKeyboard configuration")
    root.geometry("300x400")
    root.configure(bg = 'black') # there is a another way of doing same thing root['bg'] = "red"

    labelAddress = Label(root,text ="Enter the target address")
    labelAddress.place(x=50,y=20)
    
    textField = Entry(root,bd = 2)
    textField.place(x = 50, y = 50)

    labelPort = Label(root,text="Enter the target port:")
    labelPort.place(x = 50, y = 90)

    portField = Entry(root,bd = 2)
    portField.place(x = 50,y=120)

    
    
    connStatus = Label(root,textvariable=msgToShow)
    connStatus.place(x = 50,y = 220)
    
    btn = Button (root,text="Connect",justify="center",command = lambda:sockBtnCallBack(textField,portField,msgToShow))
    btn.place(x= 100,y=170)


   

    root.mainloop()

if __name__ == "__main__":
    main()
