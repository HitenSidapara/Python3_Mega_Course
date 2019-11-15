import sqlite3


class Database():

    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()


    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,isbn))
        self.conn.commit()


    def view(self):
        self.cur.execute("SELECT * FROM book")
        data = self.cur.fetchall()
        return data


    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book where title=? or author=? or year=? or isbn=?", (title,author,year,isbn))
        data = self.cur.fetchall()
        return data


    def delete(self,id):
        self.cur.execute("DELETE FROM book where id=?",(id,))
        self.conn.commit()


    def update(self,id,title,author,year,isbn):
        self.cur.execute("update book set title=?,author=?,year=?,isbn=? where id=?", (title, author, year, isbn,id))
        self.conn.commit()


    def __del__(self):
        self.conn.close()


# insert("Data Science hands on python", "colt steele", 2016, 9564876523)
# delete(2)
# update(1,"Python Beginner","Jose",2019,8934567234)
# print(view())
# print(search(year=2016))
