import os
import sqlite3

directory = "DATABASS"
db_path = r'DATABASS/CT.db'

class DatabassController:
    def __init__(self):    
        super(DatabassController, self).__init__()
    
    def add_user(self, name, lastname, email, username, password):
        conn = sqlite3.connect(r'DATABASS/CT.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USER_LOGIN")
        rows = cursor.fetchall()
        if not rows:
            cursor.execute("INSERT INTO USER_LOGIN (ID, NAME, LASTNAME, EMAIL, USERNAME, PASSWORD) VALUES (1, ?, ?, ?, ?, ?)", (name, lastname, email, username, password))
        else:
            cursor.execute("SELECT MAX(ID) FROM USER_LOGIN")
            max_id = cursor.fetchone()
            cursor.execute("INSERT INTO USER_LOGIN (ID, NAME, LASTNAME, EMAIL, USERNAME, PASSWORD) VALUES (?, ?, ?, ?, ?, ?)", (max_id[0]+1, name, lastname, email, username, password))
        conn.commit()
        conn.close()
    
    def create_databass(self):
        try:
            if not os.path.exists(directory):
                    os.makedirs(directory)
                    conn = sqlite3.connect(r'DATABASS/CT.db')
            if os.path.isfile(db_path):
                self.check_all_table()
            else:
                    conn = sqlite3.connect(r'DATABASS/CT.db')
        except OSError:
            print("Error Create Folder")
    
    def check_all_table(self):
        self.check_table_userlogin()
        
    def check_table_userlogin(self):
        conn = sqlite3.connect(r'DATABASS/CT.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='USER_LOGIN';")
        table_exists = cursor.fetchone()
        if table_exists:
            pass
        else:
            self.create_table_userlogin()
        conn.close()
        
    def create_table_userlogin(self):
        conn = sqlite3.connect(r'DATABASS/CT.db')
        conn.execute('''CREATE TABLE USER_LOGIN
            (ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT    NOT NULL,
            LASTNAME       TEXT    NOT NULL,
            EMAIL          TEXT    NOT NULL,
            USERNAME       TEXT    NOT NULL,
            PASSWORD       TEXT    NOT NULL);''')
        conn.close() 
        
    def check_user(self, username, password):
        conn = sqlite3.connect(r'DATABASS/CT.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USER_LOGIN WHERE USERNAME = ? AND PASSWORD = ?", (username, password))
        user = cursor.fetchone()
        conn.close()
        return user
    

    def check_user_by_username(self, username):
        conn = sqlite3.connect(r'DATABASS/CT.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USER_LOGIN WHERE USERNAME = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        return user
    
    

