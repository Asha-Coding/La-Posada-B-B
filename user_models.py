from connection import get_db
from passlib.hash import pbkdf2_sha256 as pw


def create_user_table():
    connection = get_db()
    sql = connection.cursor()
    sql.execute(
        """
         CREATE TABLE IF NOT EXISTS users (
               "id" INTEGER PRIMARY KEY AUTOINCREMENT,
               "name" TEXT,
               "phone" TEXT,
               "check_in" TEXT,
               "check_out" TEXT,
               "identity" TEXT,
               "guests" INTEGER
         )
         """
    )
    connection.commit()


def insert_user(name, phone, check_in, check_out, identity, guests):
    connection = get_db()
    sql = connection.cursor()
    try:
        sql.execute(
            """
            INSERT INTO users (name, phone, check_in, check_out, identity, guests) VALUES (?, ?, ?, ?, ?, ?)
            """, [name, phone, check_in, check_out, identity, guests])
        connection.commit()
    except Exception as e:
        print("Error inserting user:", e)  # You might want to log this instead


def find_user_by_identity(identity):
    connection = get_db()
    sql = connection.cursor()
    data = sql.execute(
        """ SELECT * FROM users WHERE identity = ? """, [identity])
    user = data.fetchone()
    if user:
        return user



def get_user(identity, name):
    user = find_user_by_identity(identity)
    if user:
        stored_name = user[1]  # This is now the plain name
        print(name, stored_name)
        if name == stored_name:  # Check if the plain name matches
            return user
