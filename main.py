import mysql.connector
import tkinter as tk
from view import *
from model import *
from controller import *

class Connection():
    _instance = None
    conn = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self.conn is None:
            try:
                self.conn = mysql.connector.connect(
                    host='localhost',
                    database='testdb',
                    user='Hannibal',
                    password='Mnbvcxz123'
                    )
                if self.conn.is_connected():
                    db_Info = self.conn.get_server_info()
                    print("Connected to mysql server version: ",db_Info)
                    self.cursor = self.conn.cursor()
                    self.cursor.execute("SELECT database();")
                    record = self.cursor.fetchone()
                    print("You are connected to database: ",record)
            except mysql.connector.Error as e:
                print("Error while connecting to MySQL: ",e)
        else:
            print("Connection already exists")


if __name__ == "__main__":
    db_connection = Connection()
    user_model = UserModel(db_connection)
    view = UserView()
    controller = UserController(view,user_model)
    view.setController(controller)
    view.run()



