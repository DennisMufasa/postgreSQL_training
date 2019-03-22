"""Fetch a single record from database"""
import psycopg2

try:
	con = psycopg2.connect(
		host="localhost",
		user="postgres",
		password="mufasa",
		database="postgres")
	print(con)
	cursor = con.cursor()
	query = """SELECT name, department, "employeeId"
  FROM public.employee"""
	cursor.execute(query)
	result = cursor.fetchall()
	if not result:
		print("Sorry Record Not Found!")
	else:
		for i in result:
			print(i)
except(Exception, psycopg2.Error) as error:
	print("Something went wrong", error)
