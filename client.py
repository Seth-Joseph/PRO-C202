import socket
from threading import Thread
from tkinter import *

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port =8000
client.connect((ip_address,port))
print('Client connected.')

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.withdraw()
        
        self.login = Toplevel()
        self.login.title('Login')
        self.login.resizable(width=False,height=False)
        self.login.configure(width=775,height=550,bg='#36393F')

        self.heading = Label(self.login,text='Login',font='Helvetica 24 bold',justify=CENTER,bg='#36393F',fg='#FFF')
        self.heading.place(relx=0.5, rely=0.3,anchor=CENTER )

        self.labelName = Label(self.login,text='NICKNAME: ',font='Helvetica 12 bold',justify=CENTER,bg='#36393F',fg='#727479')
        self.labelName.place(anchor=CENTER,relx=0.4,rely=0.45)

        self.entryName = Entry(self.login,font='Helvetica 14 bold',bg='#202225',fg='#FFF',bd=0,width=27)
        self.entryName.place(anchor=CENTER,relx=0.53,rely=0.5,height=35)
        
        self.loginBtn = Button(self.login,text="Login",font='Helvetica 14 bold',bg='#5865F2',fg='#FFF',justify=CENTER,width=24,bd=0,command=lambda: self.goAhead(self.entryName.get()))
        self.loginBtn.place(anchor=CENTER,relx=0.53,rely=0.6)
        self.window.mainloop()

    def goAhead(self,name):
        self.login.destroy()
        self.name = name
        rcv = Thread(target=self.recieve)
        rcv.start()
    
    def recieve(self):
        while True:
            try:
                msg = client.recv(2048).decode('utf-8')
                if msg == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    print('failed')
                    pass
            except:
                print('Connection error.')
                client.close()
                break

g1 = GUI()