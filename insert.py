"""Inserting data into a database"""

# import postgresql driver for python
import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="mufasa",
        database="postgres"
    )
    cursor = connection.cursor()
    query = """INSERT INTO public.employee(
            name, department, "employeeId")
    VALUES ('{}', '{}', '{}')""".format("Grace", "Marketing", 345679)
    cursor.execute(query)
    connection.commit()
    print("New Record Added!!")
except(Exception, psycopg2.Error) as error:
    print("Something went wrong", error)