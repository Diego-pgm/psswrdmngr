from socket import AI_PASSIVE
import mysql.connector as sql

db = sql.connect(host="localhost", user="diego", password="1234")
cursor = db.cursor()

def mysql_read(cursor, table):
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




create_database(db, cursor)
table = create_table(db, cursor)
mysql_read(cursor, table)
mysql_modify(db, cursor)
mysql_read(cursor, table)
