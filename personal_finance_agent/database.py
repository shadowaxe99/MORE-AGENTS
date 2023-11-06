```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('personal_finance_agent.db') # create a database connection to a SQLite database
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
    database = r"personal_finance_agent.db"

    sql_create_finances_table = """ CREATE TABLE IF NOT EXISTS finances (
                                        id integer PRIMARY KEY,
                                        user_id integer NOT NULL,
                                        budget real NOT NULL,
                                        expense real NOT NULL,
                                        portfolio_value real NOT NULL,
                                        retirement_plan text
                                    ); """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_finances_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
```