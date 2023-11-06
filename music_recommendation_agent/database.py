```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('music_recommendation_agent.db') # create a database connection to a SQLite database
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
    database = r"music_recommendation_agent.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        email text NOT NULL UNIQUE
                                    ); """

    sql_create_music_table = """CREATE TABLE IF NOT EXISTS music (
                                    id integer PRIMARY KEY,
                                    title text NOT NULL,
                                    artist text NOT NULL,
                                    genre text NOT NULL,
                                    release_date text
                                );"""

    sql_create_playlists_table = """CREATE TABLE IF NOT EXISTS playlists (
                                    id integer PRIMARY KEY,
                                    user_id integer NOT NULL,
                                    music_id integer NOT NULL,
                                    FOREIGN KEY (user_id) REFERENCES users (id),
                                    FOREIGN KEY (music_id) REFERENCES music (id)
                                );"""

    conn = create_connection()

    if conn is not None:
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_music_table)
        create_table(conn, sql_create_playlists_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
```