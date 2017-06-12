import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY , Title TEXT , Author TEXT , Name TEXT , Date TEXT )")
    conn.commit()
    conn.close()

def insert(title ,author,name , date):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL, ?,?,?,?)" , (title,author,name,date))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title = "" , author = "" , name = "" , date=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title = ? OR author = ? OR name = ? OR date = ? ",(title , author , name , date))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update(id,title,author,name,date):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET title = ?, author = ?, name = ?, date = ?  WHERE id = ?",(title,author,name,date,id))
    conn.commit()
    conn.close()



connect()
#update(3)
#delete(2)
#delete(4)
#insert("Shoe Dog" , "Phil Knight","-" , "-")
print(view())
#print(search(author = "Phil Knight"))
