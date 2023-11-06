```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('tutoring_agent.db') # create a database connection to a SQLite database
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
    database = r"tutoring_agent.db"

    sql_create_students_table = """ CREATE TABLE IF NOT EXISTS students (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        grade_level text
                                    ); """

    sql_create_tutors_table = """CREATE TABLE IF NOT EXISTS tutors (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    subject text
                                );"""

    sql_create_sessions_table = """CREATE TABLE IF NOT EXISTS sessions (
                                    id integer PRIMARY KEY,
                                    student_id integer NOT NULL,
                                    tutor_id integer NOT NULL,
                                    session_date text NOT NULL,
                                    session_duration integer,
                                    FOREIGN KEY (student_id) REFERENCES students (id),
                                    FOREIGN KEY (tutor_id) REFERENCES tutors (id)
                                );"""

    conn = create_connection()

    if conn is not None:
        create_table(conn, sql_create_students_table)
        create_table(conn, sql_create_tutors_table)
        create_table(conn, sql_create_sessions_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
```