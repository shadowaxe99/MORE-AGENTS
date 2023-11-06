```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('wellness_coach.db') # create a database connection to a SQLite database
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
        sql_create_goals_table = """ CREATE TABLE IF NOT EXISTS goals (
                                        id integer PRIMARY KEY,
                                        user_id integer NOT NULL,
                                        goal text NOT NULL,
                                        start_date text,
                                        end_date text,
                                        status text
                                    ); """

        sql_create_habits_table = """ CREATE TABLE IF NOT EXISTS habits (
                                        id integer PRIMARY KEY,
                                        user_id integer NOT NULL,
                                        habit text NOT NULL,
                                        frequency text,
                                        status text
                                    ); """

        sql_create_workouts_table = """ CREATE TABLE IF NOT EXISTS workouts (
                                        id integer PRIMARY KEY,
                                        user_id integer NOT NULL,
                                        workout_plan text NOT NULL,
                                        date text,
                                        status text
                                    ); """

        sql_create_nutrition_table = """ CREATE TABLE IF NOT EXISTS nutrition (
                                        id integer PRIMARY KEY,
                                        user_id integer NOT NULL,
                                        meal_plan text NOT NULL,
                                        date text,
                                        status text
                                    ); """

        if conn is not None:
            # create goals table
            conn.execute(sql_create_goals_table)
            # create habits table
            conn.execute(sql_create_habits_table)
            # create workouts table
            conn.execute(sql_create_workouts_table)
            # create nutrition table
            conn.execute(sql_create_nutrition_table)
        else:
            print("Error! cannot create the database connection.")
    except Error as e:
        print(e)

def main():
    conn = create_connection()
    if conn is not None:
        create_table(conn)
    else:
        print("Error! cannot create the database connection.")
    close_connection(conn)

if __name__ == '__main__':
    main()
```