from flask import Blueprint, render_template, request, abort
import pymysql
import os

# Create a Blueprint named 'main'
main = Blueprint('main', __name__)

# Connect to database
DB_CONFIG = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', 'example'),
    'database': os.environ.get('DB_NAME', 'vuln_app'),
    'charset': 'utf8mb4'
}

@main.route('/')
def index():
    conn = pymysql.connect(**DB_CONFIG)
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT id, name, bio FROM users")
            rows = cursor.fetchall()
    except Exception as e:
        print(f"Database error: {e}")
        rows = []
    finally:
        conn.close()
    return render_template('index.html', rows=rows)

@main.route('/search')
def search():
    name = request.args.get('name', '')
    conn = pymysql.connect(**DB_CONFIG)
    try:
        # VULNERABLE: SQL Injection
        sql = f"SELECT id, name, bio FROM users WHERE name LIKE '%{name}%'"
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:  # Use DictCursor here
            cursor.execute(sql)
            rows = cursor.fetchall()
    except Exception as e:
        print(f"Database error: {e}")
        rows = []
    finally:
        conn.close()
    return render_template('search.html', rows=rows, name=name)

@main.route('/show')
def show_file():
    # VULNERABLE: Path Traversal
    filename = request.args.get('file', '')
    path = os.path.join('files', filename)
    
    try:
        if not os.path.exists(path):
            return f"File not found: {path}", 404
            
        return "<pre>" + open(path, 'r', errors='ignore').read() + "</pre>"
    except Exception as e:
        return f"Error: {str(e)}", 500
