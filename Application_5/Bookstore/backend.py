import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()


def insert(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    data = cur.fetchall()
    conn.close()
    return data



def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book where title=? or author=? or year=? or isbn=?", (title,author,year,isbn))
    data = cur.fetchall()
    conn.close()
    return data


def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book where id=?",(id,))
    conn.commit()
    conn.close()


def update(id,title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("update book set title=?,author=?,year=?,isbn=? where id=?", (title, author, year, isbn,id))
    conn.commit()
    conn.close()


connect()
# insert("Data Science hands on python", "colt steele", 2016, 9564876523)
# delete(2)
# update(1,"Python Beginner","Jose",2019,8934567234)
# print(view())
# print(search(year=2016))
