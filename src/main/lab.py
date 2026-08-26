import os
import sqlite3

"""
SQL sublanguage: DDL (Data Definition Language)

A foreign key is a column in one table that refers to the primary key in another table.

The syntax for creating the songs table with an artist fk is as follows:
CREATE TABLE song (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 song_name varchar(100),
 artist_fk int REFERENCES artist(id)
);

If we try to input an "artist_fk" that isn't in the artist table, an exception will be thrown.
"""

_LAB_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read_sql(filename):
    with open(os.path.join(_LAB_DIR, filename), "r", encoding="utf-8") as f:
        return f.read().strip()


def problem1():
    """
    site_user table:
    |   id  |     firstname        |        lastname        |
    ----------------------------------------------------------
    |1      |'Steve'               |'Garcia'                |
    |2      |'Alexa'               |'Smith'                 |
    |3      |'Steve'               |'Jones'                 |
    |4      |'Brandon'             |'Smith'                 |
    |5      |'Adam'                |'Jones'                 |

    Assignment: create a "post" table that has the following columns:
          post table:
          |   id  |     post        |        user_fk         |
          ----------------------------------------------------
          where the id is an auto-incrementing primary key, post is of type varchar(255), and user_fk is of
          type int, referencing site_user(id).

    Sets up the site_user table, runs the student's CREATE TABLE statement, and returns the open connection so
    the caller can verify both a valid insert and referential integrity. Each call gets a fresh, independent
    in-memory database, so it's safe to call this twice - once per check.
    """
    sql = _read_sql("problem1.sql")

    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    # enables enforcement of FOREIGN KEY constraints, which SQLite keeps off by default
    cur.execute("PRAGMA foreign_keys = ON;")
    cur.execute(
        "CREATE TABLE site_user (id INTEGER PRIMARY KEY AUTOINCREMENT, firstname varchar(100), lastname varchar(100));"
    )
    cur.execute("INSERT INTO site_user (firstname, lastname) VALUES ('Steve', 'Garcia');")
    cur.execute("INSERT INTO site_user (firstname, lastname) VALUES ('Alexa', 'Smith');")
    cur.execute("INSERT INTO site_user (firstname, lastname) VALUES ('Steve', 'Jones');")
    cur.execute("INSERT INTO site_user (firstname, lastname) VALUES ('Brandon', 'Smith');")
    cur.execute("INSERT INTO site_user (firstname, lastname) VALUES ('Adam', 'Jones');")
    conn.commit()

    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(f"problem1: {e}\n")

    return conn
