```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('travel_planning_assistant.db') # create a database connection to a SQLite database
        print(f'successful connection with sqlite version {sqlite3.version}')
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
    database = r"travel_planning_assistant.db"

    sql_create_destinations_table = """ CREATE TABLE IF NOT EXISTS destinations (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        country text,
                                        description text
                                    ); """

    sql_create_bookings_table = """CREATE TABLE IF NOT EXISTS bookings (
                                    id integer PRIMARY KEY,
                                    user_id integer NOT NULL,
                                    destination_id integer NOT NULL,
                                    start_date text,
                                    end_date text,
                                    FOREIGN KEY (destination_id) REFERENCES destinations (id)
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_destinations_table)
        create_table(conn, sql_create_bookings_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
```