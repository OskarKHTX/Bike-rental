import sqlite3 as db

conn = db.connect("users.db")
c = db.Cursor

def createdb():
    c.conn("""CREATE TABLE users
              (username, uid, numberofbikeshourly, numberofbikesdaily, numberofbikesweekly, passwd)""")
    conn.commit()
    conn.close()

def adduser(username, uid, numberofbikeshourly, numberofbikesdaily, numberofbikesweekly, passwd):
    sql = "INSERT INTO users (username, uid, numberofbikeshourly, numberofbikesdaily, numberofbikesweekly, passwd) VALUES (?, ?, ?, ?, ?, ?)";
    conn.execute(sql, (username, uid, numberofbikeshourly, numberofbikesdaily, numberofbikesweekly, passwd))
    conn.commit()
    conn.close()

def login(username, passwd):
    conn1=db.connect("users.db")
    sql = "SELECT * FROM users WHERE username= ? AND passwd= ?";
    conn1.execute(sql, (username ,passwd))
    
    if c.fetchone is not None:
        return True
    else:
        return False
    
adduser(123,123,123,123,123,123)
print(login(123,465))
