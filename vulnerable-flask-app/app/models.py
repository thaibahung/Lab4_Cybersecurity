from flask import current_app
import pymysql

def get_db_connection():
    return pymysql.connect(
        host=current_app.config['DB_HOST'],
        user=current_app.config['DB_USER'],
        password=current_app.config['DB_PASSWORD'],
        database=current_app.config['DB_NAME'],
        cursorclass=pymysql.cursors.DictCursor
    )

def get_user_by_name(name):
    conn = get_db_connection()
    try:
        # UNSAFE: vulnerable to SQL Injection
        sql = f"SELECT id, name, bio FROM users WHERE name = '{name}'"
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        conn.close()

def get_file_contents(filename):
    # UNSAFE: vulnerable to File Inclusion
    path = f"./files/{filename}"
    with open(path, 'r', errors='ignore') as file:
        return file.read()