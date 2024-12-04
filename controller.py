import tkinter as tk
class UserController:

    def __init__(self,view,model):
        self.view = view
        self.model = model
    
    def create_user(self,username,password):
        success, message = self.model.create_user(username,password)
        self.view.L3.config(text=message)
        if success:
            print("User created")
        else:
            print("Error: Could not create user")
    
    def login_user(self,username,password):
        success, message = self.model.login_user(username,password)
        self.view.L3.config(text=message)
        if success:
            print("User logged in")
        else:
            print("Error: Could not login user")
