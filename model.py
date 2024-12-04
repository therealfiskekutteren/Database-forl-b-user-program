import mysql.connector
class UserModel:
    def __init__(self,db_connection):
        self.db = db_connection
        self.setup_database()
    
    def setup_database(self):
        self.db.cursor.execute("CREATE TABLE IF NOT EXISTS users((id int primary key auto_increment, name varchar(255), password varchar(255))")
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
                return False, "Your password is too weak."
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
