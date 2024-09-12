import sqlite3
import os

directory = "DATABASS"
db_path = r'DATABASS/CT.db'
conn = sqlite3.connect(r'DATABASS/CT.db')
# try:
#       if not os.path.exists(directory):
#             os.makedirs(directory)
#             conn = sqlite3.connect(r'DATABASS/CT.db')
#             # print("Create Folder")
            
#       if os.path.isfile(db_path):
#             # print("have File in folder")
#             pass
#       else:
#             # print("File not found in folder")
#             conn = sqlite3.connect(r'DATABASS/CT.db')
# except OSError:
#       print("Error Create Folder")
            

# # print("เปิดฐานข้อมูลสำเร็จ")
# conn = sqlite3.connect(r'DATABASS/CT.db')
# # conn.execute('''CREATE TABLE USER_LOGIN
# #        (ID INT PRIMARY KEY     NOT NULL,
# #        NAME           TEXT    NOT NULL,
# #        LASTNAME       TEXT    NOT NULL,
# #        EMAIL          TEXT    NOT NULL,
# #        USERNAME       TEXT    NOT NULL,
# #        PASSWORD       TEXT    NOT NULL);''')
# # print("สร้างตารางสำเร็จ :D ")
# # conn.close() 

# cursor = conn.cursor()
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='USER_LOGIN';")
# table_exists = cursor.fetchone()

# if table_exists:
#       print(table_exists)
#       print(" Have Table USER_LOGIN ")
# else:
#       print("Don't Have Table USER_LOGIN ")

# conn.close()
cursor = conn.cursor()
cursor.execute("INSERT INTO USER_LOGIN (ID, NAME, LASTNAME, EMAIL, USERNAME, PASSWORD) VALUES (1, ?, ?, ?, ?, ?)", ("name", "lastname", "email", "username", "password"))
conn.commit()
print("เพิ่มระเบียงข้อมูลสำเร็จ")
conn.close() 
