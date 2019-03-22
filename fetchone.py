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
  FROM public.employee WHERE name = '{}'""".format("Evi")
	cursor.execute(query)
	result = cursor.fetchone()
	if not result:
		print("Sorry Record Not Found!")
	else:
		print(result)
except(Exception, psycopg2.Error) as error:
	print("Something went wrong", error)
