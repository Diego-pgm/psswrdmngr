from random import sample
import mysql.connector as sql
from bullet import Password

def menu():
    print('=====================Anton Password Manager==========================')
    print('Menu Options:\n\
            1) Generate password\n\
            2) Add user:password\n\
            0) Exit Password Manager')
    opt = int(input('anton> '))
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
        db = sql.connect(host='localhost', user=user, password=password, database='manager', auth_plugin="mysql_native_password") # Set auth_plugin because ubuntu...
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


def insert_mysql(db, cursor, psswd):
    res = input('[-] Use a password generated by Anton (Y/n): ')
    if (res == 'y') or (res == 'yes') or (res == "Y"):
        site = input('anton> Please insert app name: ')
        uname = input('anton> Please insert the username: ')
    elif (res == 'n') or (res == 'no') or (res == "No"):
        site = input('Please insert app name: ')
        uname = input('Please insert the username/email: ')
        psswd = input('Please insert the password: ')
    query = 'insert into manager values ("{}", "{}", "{}")'.format(site, uname,psswd)
    #print(query)
    quest = input('Are you sure you want to add: \n \
                    Site: {}\n \
                    Username/Email: {}\n \
                    Password: {}\n \
                    anton> (Y/n): '.format(site, uname,psswd))
    if (quest == 'y') or (quest == "yes") or (quest=="Y"):
        cursor.execute(query)
        db.commit()
    else:
        pass

try:
    psswd = ""
    usr = input("Mysql username: ")
    cli = Password(prompt="Mysql password: ", hidden="")
    pwd = cli.launch()
    db, cursor, con = connect_mysql(usr, pwd)
except Exception as e:
    print('Wrong credentials, bye.')
if con:
    while True: 
        opt = menu()
        if opt == 0:
            quit()
        elif opt == 1:
            psswd = gen_passwd()
            print('[+] The password generated is: ', psswd,'\n')
        elif opt == 2:
            insert_mysql(db, cursor, psswd)
        else:
            print('[-] Please enter a valid option.')
            continue