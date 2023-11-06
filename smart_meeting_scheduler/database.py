```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:')       
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"pythonsqlite.db"

    sql_create_meetings_table = """ CREATE TABLE IF NOT EXISTS meetings (
                                        id integer PRIMARY KEY,
                                        title text NOT NULL,
                                        start_time text,
                                        end_time text,
                                        priority text
                                    ); """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_meetings_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
```