import mysql.connector as sql

db = sql.connect(host="localhost", user="diego", password="1234", database="pruebas")
cursor = db.cursor()

def mysql_read(query, cursor):
    cursor.execute(query)
    r = cursor.fetchall()
    return r

def mysql_modify(db, query, cursor):
    cursor.execute(query)
    db.commit()


result = mysql('SELECT * FROM manager', cursor)
print(result)
mysql_modify('INSERT INTO manager values (diego)')
    