"""PostgreSQL Operations"""

import psycopg2

# create table


def create_table():
    conn = psycopg2.connect("dbname='test' user='postgres'  password='3682' host='localhost'  port='5432' ")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


# insert table

def insert_table(item, quantity, price):
    conn = psycopg2.connect("dbname='test' user='postgres'  password='3682' host='localhost'  port='5432' ")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()


# select data

def select_data():
    conn = psycopg2.connect("dbname='test' user='postgres'  password='3682' host='localhost'  port='5432' ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    data = cur.fetchall()
    conn.close()
    return data


# delete data


def delete_data(item):
    conn = psycopg2.connect("dbname='test' user='postgres'  password='3682' host='localhost'  port='5432' ")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


# update data

def update_data(item, quantity, price):
    conn = psycopg2.connect("dbname='test' user='postgres'  password='3682' host='localhost'  port='5432' ")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


# create_table()
# insert_table("kiwi",1,25)
# delete_data("mobile")
# update_data("kiwi",1,50)
# print(select_data())
