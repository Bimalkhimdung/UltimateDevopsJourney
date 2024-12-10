
import psycopg2
from faker import Faker

fake = Faker()

# this initialize to empty set to keep track of generated email for uniqueness as email is unique
# without this Faker might generate duplicate email 
used_emails = set()

# Connect to database
conn = psycopg2.connect(
    dbname="test_e",
    user="",
    password="",
    host="localhost"
)

# cursor command to execute sql commands

cursor = conn.cursor()

# fetch all ids details form users_user table
cursor.execute("SELECT id FROM users_user")  
user_ids = cursor.fetchall()

# loop through user_id and generate fake username, email, first name, middle name and last name

for user_id in user_ids:
# it checks while the generated new email is in empty used_email or not / if not it, generates new email if present than break out loop
    while True:
     fake_email = fake.email()
     if fake_email not in used_emails:
         used_emails.add(fake_email)
         break

    fake_first_name = fake.first_name()
# used first name function since Faker dose not have middle name function
    fake_middle_name = fake.first_name()
    fake_last_name = fake.last_name()
    fake_username = fake.user_name()
    
    cursor.execute("""
        UPDATE users_user
        SET email = %s, first_name = %s , middle_name = %s , last_name = %s, username = %s
        WHERE id = %s
    """, (fake_email,fake_first_name, fake_middle_name, fake_last_name, fake_username, user_id[0]))

# Commit changes
conn.commit()
cursor.close()
conn.close()

print("Data Duplication  complete!!:)")
