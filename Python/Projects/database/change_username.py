import psycopg2
from faker import Faker
from slugify import slugify
import getpass

fake = Faker()

# Database connection setup
db_name = input("Enter your database name here: ")
db_user = input("Enter your database username here: ")
db_pass = getpass.getpass("Enter your database password here: ")
db_host = input("Enter database host [Enter for default localhost]: ") or "localhost"

def connect_to_db():
    return psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_pass,
        host=db_host,
        port="5432"
    )

# function to fetch data from db
def fetch_all(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()
#function to  update table

def update_table(cursor, query, values):
    cursor.execute(query, values)

#function to generate unique values
def generate_unique_value(existing_set, generator_func):
    while True:
        value = generator_func()
        if value not in existing_set:
            existing_set.add(value)
            return value
def update_superuser(conn):
    with conn.cursor() as cursor:
        superusers = fetch_all(cursor, "SELECT id FROM users_user WHERE is_superuser = TRUE")
        for (user_id,) in superusers:
            try:
                update_table(
                    cursor,
                    """
                    UPDATE users_user
                    SET username = %s, password = %s
                    WHERE id = %s
                    """,
                    ('aayulogic123', 'pbkdf2_sha256$260000$V8oiIdp0Wk6xKkzDcTyTRC$cvyOom6vxU3kV9RaWP1WRm7Mjg2e9zIepNnJWxsAJJ0=', user_id)
                )
                print(f"Superuser with user_id: {user_id} updated successfully.")
            except psycopg2.Error as e:
                print(f"Failed to update superuser {user_id}: {e}")        


if __name__ == "__main__":
    try:
        with connect_to_db() as conn:
            update_superuser(conn)
            print("All tables have been updated with fake data")
    except psycopg2.Error as e:
        print(f"Database error: {e}")