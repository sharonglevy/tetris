#Create Database for KVN
import mysql.connector as mysql
import MySQLdb as mdb

def main():
	needs = input("what do you need to do? type: 'new line', 'create table' or 'create database', 'drop table'")
	if needs == "new line":
		new_line()
	elif needs == "drop table":
		drop()
	try:
		create_database
	except:
		create_table
	finally:
		print("finalized")

def create_database():
	db = mysql.connect(
	host = "localhost",
	user = "root",
	passwd = "Bait6213"
	)

	cursor = db.cursor()

	cursor.execute("CREATE DATABASE KVN_database")

def create_table():
	db = mysql.connect(
	host = "localhost",
	user = "root",
	passwd = "dbms",
	database = "KVN_database"
	)
	cursor = db.cursor()

	cursor.execute("CREATE TABLE KVN_usersTable (id INT(300) NOT NULL AUTO_INCREMENT PRIMARY KEY, Email VARCHAR(30), EID VARCHAR(15), Location VARCHAR(20), PhoneNumber VARCHAR(20), Registered VARCHAR(5), Authorized VARCHAR(6))")

def new_line():
	data = input("enter data as follows: Email, EID, Location, PhoneNumber, Registered, Authorized")

def drop():
	nametab = input("name of the table to drop? ")
	db = mysql.connect(
	host = "localhost",
	user = "root",
	passwd = "Bait6213",
	database = "KVN_database"
	)
	cursor = db.cursor()

	#sql = "DROP TABLE %s"
	#cursor.execute(sql, (nametab,))
	t = (nametab,)
	cursor.execute("DROP TABLE %s", t)

main()