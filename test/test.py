import sqlite3
conn = sqlite3.connect(r'DATABASS/1.db')
print("เปิดฐานข้อมูลสำเร็จ")
# conn.execute('''CREATE TABLE SAVEONE
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        LASTNAME       TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        MESSENGE        CHAR(150));''')
# print("สร้างตารางสำเร็จ :D ")
# conn.close() 

conn.execute("INSERT INTO SAVEONE (ID,NAME,LASTNAME,AGE,MESSENGE ) \
      VALUES (1, 'ต้นตาล','test','12','ทดสอบระบบ :D ')")
conn.execute("INSERT INTO SAVEONE (ID,NAME,LASTNAME,AGE,MESSENGE ) \
      VALUES (2, 'วรรณพงษ์','ddddd','222','ทดสอบระบบ ครับ  :D ')")
conn.commit()
print("เพิ่มระเบียงข้อมูลสำเร็จ")
conn.close() 
