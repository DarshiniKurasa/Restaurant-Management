import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()

    # cur.execute("DROP TABLE IF EXISTS supplier")
    # con.commit()

    
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,email TEXT Unique,gender TEXT,contact TEXT unique,dob TEXT,doj TEXT,password TEXT,utype TEXT,address TEXT,salary TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(sid INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text unique,desc text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Category text,name text,price text,qty text,status text)")
    con.commit()
create_db()