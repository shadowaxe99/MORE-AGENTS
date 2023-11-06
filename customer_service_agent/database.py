```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('customer_service_agent.db') # create a database connection to a SQLite database
        print(f'successful connection with sqlite version {sqlite3.version}')
    except Error as e:
        print(e)
    return conn

def close_connection(conn):
    try:
        conn.close()
        print('connection closed')
    except Error as e:
        print(e)

def create_table(conn):
    try:
        sql = '''CREATE TABLE IF NOT EXISTS customer_service (
                    id integer PRIMARY KEY,
                    customer_id text NOT NULL,
                    question text NOT NULL,
                    sentiment text,
                    account_info text
                );'''
        conn.execute(sql)
        print('table created successfully')
    except Error as e:
        print(e)

def main():
    conn = create_connection()
    if conn is not None:
        create_table(conn)
        close_connection(conn)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
```