```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('real_estate_agent.db') # create a database connection to a SQLite database
        print(f'successful connection with sqlite version {sqlite3.version}')
    except Error as e:
        print(e)
    finally:
        if conn:
            return conn

def close_connection(conn):
    conn.close()
    print('connection closed')

def create_table(conn):
    try:
        sql_create_properties_table = """ CREATE TABLE IF NOT EXISTS properties (
                                            id integer PRIMARY KEY,
                                            address text NOT NULL,
                                            price real,
                                            owner text,
                                            status text
                                        ); """
        if conn is not None:
            conn.execute(sql_create_properties_table)
            print('Table created successfully')
        else:
            print("Error! cannot create the database connection.")
    except Error as e:
        print(e)

def main():
    database = r"real_estate_agent.db"
    conn = create_connection()
    if conn is not None:
        create_table(conn)
    else:
        print("Error! cannot create the database connection.")
    close_connection(conn)

if __name__ == '__main__':
    main()
```