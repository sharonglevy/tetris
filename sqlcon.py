#data base creation and managemen with mysql

#First import mysql.connect
import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Bait6213"
)

cursor = db.cursor()

## creating a databse called 'kvndatabase'
## 'execute()' method is used to compile a 'SQL' statement
## below statement is used to create tha 'kvndatabase' database

cursor.execute("CREATE DATABASE kvndatabase")

## executing the statement using 'execute()' method
cursor.execute("SHOW DATABASES")

## 'fetchall()' method fetches all the rows from the last executed statement
databases = cursor.fetchall() ## it returns a list of all databases present

## printing the list of databases
print(databases)

## showing one by one database
for database in databases:
    print(database)

#this code will execute with no mistakes if the database actally exists
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "dbms",
    database = "kvndatabase"
)

## creating a table called 'users' in the 'kvndatabase' database
cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")

#Primary Key:- It is a unique value in the table. It helps to find each row uniquely in the table.
#To create a Primary Key, we use the PRIMARY KEY statement while creating the table.
#The statement INT AUTO_INCREMENT PRIMARY KEY is used to identify each row uniquely with a number starting from 1.

cursor.execute("DROP TABLE users")

## creating the 'users' table again with the 'PRIMARY KEY'
cursor.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user_name VARCHAR(255))")

## 'DESC table_name' is used to get all columns information
cursor.execute("DESC users")

## it will print all the columns as 'tuples' in a list
print(cursor.fetchall())

## defining the Query
query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
## storing values in a variable
values = ("Hafeez", "hafeez")

## executing the query with values
cursor.execute(query, values)

## to make final output we have to run the 'commit()' method of the database object
db.commit()

#To insert multiple rows into the table, we use the executemany() method. 
#It takes a list of tuples containing the data as a second parameter and a query as the first argument.

## defining the Query
query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
## storing values in a variable
values = [
    ("Peter", "peter"),
    ("Amy", "amy"),
    ("Michael", "michael"),
    ("Hennah", "hennah")
]

## executing the query with values
cursor.executemany(query, values)

## to make final output we have to run the 'commit()' method of the database object
db.commit()

#To get all records from a table, we use * in place of column names. Let's get all the data from the users table which we inserted before.
## defining the Query

query = "SELECT * FROM users"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)

#SELECT column_name FROM table_name WHERE condition statement will be used to retrieve the data on some condition.
#WHERE is used to select data on some condition.
## defining the Query
query = "SELECT * FROM users WHERE id = 5"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

#UPDATE keyword is used to update the data of a record or records.
#UPDATE table_name SET column_name = new_value WHERE condition statement is used to update the value of a specific row.

## defining the Query
query = "UPDATE users SET name = 'Kareem' WHERE id = 1"

## executing the query
cursor.execute(query)

## final step to tell the database that we have changed the table data
db.commit()

cursor.close()