import sqlite3 as db


def createdb():
    conn = db.connect("users.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE users
              (username, uid, numberofbikeshourly, numberofbikesdaily, numberofbikes weekly, passwd)""")