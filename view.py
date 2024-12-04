import tkinter as tk
class UserView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        L1 = tk.Label(self.root,text="Username")
        L1.grid(row=0,column=0)
        L2 = tk.Label(self.root,text="Password")
        L2.grid(row=1,column=0)
        self.usernm = tk.Entry()
        self.usernm.grid(row=0,column=1,padx=10,pady=10)
        self.passwd = tk.Entry()
        self.passwd.grid(row=1,column=1,padx=10,pady=10)
        self.L3 = tk.Label(self.root,text="")
        self.L3.grid(row=4,column=1)
        self.btn = tk.Button(self.root,text="Register",bd='5',command=self.create)
        self.btn.grid(row=3,column=1)
        self.btn1 = tk.Button(self.root,text="Login",bd='5',command=self.login)
        self.btn1.grid(row=3,column=2)

    def setController(self,controller):
        self.controller = controller

    def create(self):
        username = self.usernm.get()
        password = self.passwd.get()
        self.controller.create_user(username,password)
    def login(self):
        username = self.usernm.get()
        password = self.passwd.get()
        self.controller.login_user(username,password)
    def run(self):
        self.root.mainloop()