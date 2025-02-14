import sqlite3
from os import getcwd

cwd = getcwd()
database_path = f"{cwd}/database/database.sqlite"


def sql_exec(query, params=()):
    con = sqlite3.connect(database_path)
    cur = con.cursor()
    cur.execute(query, params)
    return cur, con
