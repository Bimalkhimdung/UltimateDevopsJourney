import psycopg2

db_connection = psycopg2.connect(
        dbname = "",
        user = "",
        password = "",
        host = "localhost"
)

# create object to connect to db
#choice = input(" Do you want to create User (Y\N) ??\n")
db_name = input("Enter database name\n")
db_user = input("Enter database user\n")

cursor = db_connection.cursor()

cursor.execute( """
        CREATE DATABASE   


"""


)
