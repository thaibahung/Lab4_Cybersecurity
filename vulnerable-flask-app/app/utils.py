def get_user_by_name(name):
    import pymysql
    from config import DB_CONFIG

    conn = pymysql.connect(**DB_CONFIG)
    try:
        # UNSAFE: vulnerable to SQL Injection
        sql = f"SELECT id, name, bio FROM users WHERE name = '{name}'"
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        conn.close()

def read_file(file_path):
    # UNSAFE: vulnerable to File Inclusion
    with open(file_path, 'r', errors='ignore') as file:
        return file.read()