# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 22:10:53 2019
SQL DATABASE STUDY WITH PYTHON (SQLITE3)
@author: omerzulal
"""
import sqlite3
import numpy as np
import time

#%% GENERATE DATABASE AND ITS TABLES
# database name
db_name = "omer_sql.db"

# generates the database and makes a connection, if already generated it just connects to it
conn = sqlite3.connect(db_name)

#rather than creating and writing to a database in the harddrive :memory: will store the database in the RAM
#conn = sqlite3.connect(":memory:") 

# creates a cursor object to communicate with the database
c = conn.cursor()

# the query for creating a table called employees 
query_employees = """
CREATE TABLE if not exists employees (
        first_name text,
        last_name text,
        salary int
)
"""

#pass the query to the cursor object
c.execute(query_employees)

# insert a value into the table (for single line queries use "" and '' for strings)
c.execute("INSERT INTO employees VALUES('omer','eker',140000)")

# query for bringing values from the table
result = c.execute("SELECT * FROM employees").fetchall()
print(result)

#%% ADD ROWS INTO THE TABLE IN A LOOP

#number of rows to add into the database
no_of_rows = int(1e4)

#list of random names to choose
names = ["ahmet","ali","zeliha","zeynep","ayse","mehmet","mustafa","tuba","zulal"]
surnames = ["eker","ertugrul","genc"]

#following loop chooses combines random names, surnames, and salaries and writes into the database
#this could be done with a single line using pandas package
t1 = time.time()
for i in range(no_of_rows):
    name = np.random.choice(names)
    surname = np.random.choice(surnames)
    salary = np.random.randint(15000,350000)
    c.execute("INSERT INTO employees VALUES(?,?,?)",(name,surname,salary))

print("Query Succeeded in %.2f seconds"%(time.time()-t1))

#query the results with some rules
query = """
select * from employees
where salary > 250000 and last_name is not "eker"
order by salary desc
"""

#fetch all result using the query
result = c.execute(query).fetchall()
print(result)

## delete table rows to try the above for loop again
#c.execute("delete from employees")

#commit the the changes to allow the changes in the .db file
conn.commit()

#close the connection to .db file
conn.close()

