import mysql.connector
import re
class UserModel:
    def __init__(self,db_connection):
        self.db = db_connection
        self.setup_database()
    
    def setup_database(self):
        self.db.cursor.execute("CREATE TABLE IF NOT EXISTS users(id int primary key auto_increment, username varchar(255), password varchar(255))")
        self.db.conn.commit()
        print("Table created")
    
    def create_user(self,username,password):
        self.db.cursor.execute("SELECT * FROM users WHERE username = %s",(username,))
        result =self.db.cursor.fetchall()
        if result:
            return False,"Name already in use. Please select another."
        else:
            print("før password_is_valid")
            if not self.password_is_valid(password):
                return False, "Your password is too weak.\nMinimum six characters, Max 12, at least one letter, one number and one special character"
            else:
                self.db.cursor.execute("INSERT INTO users(username,password) VALUES(%s,%s)",(username,password))
                self.db.conn.commit()
                return True, "User created"
    
    def login_user(self,username,password):
        self.db.cursor.execute("SELECT password FROM users WHERE username = %s",(username,))
        result = self.db.cursor.fetchall()
        if result:
            if result[0][0] == password:
                return True, "You are logged in"
            else:
                return False, "Wrong password"
        else:
            return False, "User not found"
    def password_is_valid(self,password):
        #Minimum six characters, Max 12, at least one letter, one number and one special character
        match = re.match("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{6,12}$",password)
        if match:
            return True
        else:
            return False
