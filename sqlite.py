import sqlite3
import json

connection = sqlite3.connect('test.db')
print("Opened Correctly")

# connection.execute(''' 
# CREATE TABLE COMPANY
# (ID INT PRIMARY KEY     NOT NULL,
#  NAME           TEXT    NOT NULL,
#  AGE            INT     NOT NULL,
#  ADDRESS        CHAR(50),
#  SALARY         REAL);
# ''')

# print("Table Created")
# 
# connection.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
# 	  VALUES (1, 'Paul', 32, 'California', 20000.00 )");
# 
# connection.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
# 	  VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
# 
# connection.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
# 	  VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
# 
# connection.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
# 	  VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
# 	  
# connection.commit()
# 
# print("Added Values")

cursor = connection.execute("SELECT id, name, address, salary from COMPANY")

data = cursor.fetchall()

print(json.dumps(data))
print( "Operation done successfully")

connection.close()