"""Make a connection to a postgresql database"""
# import postgresql driver for python
import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="mufasa",
        database="postgres"
    )
    print(connection)
except(Exception, psycopg2.Error) as error:
    print("Something went Wrong", error)
