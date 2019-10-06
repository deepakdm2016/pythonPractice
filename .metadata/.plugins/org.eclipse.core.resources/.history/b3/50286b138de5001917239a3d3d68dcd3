import mysql.connector
from mysql.connector import cursor

conn=mysql.connector.connect(host='localhost',database='mydbPython',port=3308,user="root",password="Winvini@2017")

if conn.is_connected():
    print("connected to mydbPython")

cursor=conn.cursor();
cursor.execute('select * from emp')

'''
row=cursor.fetchone()
while row is not None:
    print(row)
    row=cursor.fetchone()
'''

rows=cursor.fetchall()
print("Total number of rows are",cursor.rowcount)
for i in rows:
    print(i)
    
cursor.close()
conn.close()
