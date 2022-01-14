import mysql.connector as sql
import pandas as pd

db = sql.connect(host="localhost", user="diego", password="1234", auth_plugin="mysql_native_password")
cursor = db.cursor()

def mysql_print(db):
    df = pd.read_sql("select * from prueba", db)
    print(df)


def mysql_read(cursor, table="prueba"):
    query = 'SELECT * FROM ' + table 
    cursor.execute(query)
    r = cursor.fetchall()
    print('Results: \n', r)

def mysql_modify(db, cursor):
    query = 'INSERT INTO prueba (name, email) values ("diego", "diego@hotmail.com")'
    cursor.execute(query)
    db.commit()

def create_database(db, cursor):
    try:
        query = 'CREATE database pruebas'
        cursor.execute(query)
        db.commit()
        query = 'USE pruebas'
        cursor.execute(query)
    except Exception as e:
        query = 'use pruebas'
        cursor.execute(query)


def create_table(db, cursor):
    table_name = input('What should the table name be: ')
    try:
        query = 'create table ' + table_name + '(name varchar(20) not null, email varchar(30) not null)'
        cursor.execute(query)
        db.commit()
    except Exception as e:
        print('[-] Table already exists')
        query = 'SHOW tables'
        cursor.execute(query)
        r = cursor.fetchall()
        print('The tables are:',r)
    return table_name


def delete_user(db, cursor, table_name="prueba"):
    username=input('Please insert the username you want to delete')
    query = 'delete from {} where name="{}"'.format(table_name, username) 
    cursor.execute(query)
    db.commit()
    print('User {} deleted successfully'.format(username))

create_database(db, cursor)
#table = create_table(db, cursor)
mysql_read(cursor)
mysql_modify(db, cursor)
mysql_read(cursor)
mysql_print(db)
delete_user(db, cursor)