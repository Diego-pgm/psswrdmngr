from random import sample
import mysql.connector as sql
from bullet import Password

def menu():
    print('|=====================Password Manager==========================')
    print('Menu Options:\n\
            1) Generate Key\n\
            2) Save Key\n\
            0) Exit Password Manager')
    print('|===============================================================')
    opt = int(input('Choose an option: '))
    return opt

def gen_passwd():
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    numb = '1234567890'
    simb = './!@#$%^&*)(,.?'
    addup = simb + upper + lower + numb
    length = input('[+] How long should the key be?\nlength=')
    psswd = ''.join(sample(addup, int(length)))
    return psswd

def connect_mysql(user, password):
    try:
        db = sql.connect(host='localhost', user=user, password=password, database='manager', auth_plugin="mysql_native_password")
        cursor = db.cursor()
        con = True
    except Exception as e:
        db = sql.connect(host='localhost', user=user, password=password, auth_plugin="mysql_native_password")
        cursor = db.cursor()
        cursor.execute('create database manager')
        db.commit()
        cursor.execute('use manager')
        cursor.execute('create table manager(site varchar(50) not null, name varchar(50) not null, password varchar(50) not null')
        db.commit()
        print("[+] Database setup correctly and table setup correctly.\n")
        con = True
    return db, cursor, con


def insert_mysql(db, cursor, psswd=""):
    pass

try:
    usr = input("Mysql username: ")
    cli = Password(prompt="Mysql password: ", hidden="")
    pwd = cli.launch()
    db, cursor, con = connect_mysql(usr, pwd)
    if con:
        while True: 
            opt = menu()
            if opt == 0:
                quit()
            elif opt == 1:
                psswd = gen_passwd()
                print('[+] The key generated is: ', psswd,'\n')
            elif opt == 2:
                insert_mysql(db, cursor)
            else:
                print('[-] Please enter a valid option.')
                continue
except Exception as e:
    print('Wrong credentials, bye.')
    
