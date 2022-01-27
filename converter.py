import os

def menu():
    os.system('clear')
    print('=====================Anton Number Converter==========================')
    print('Menu Options:\n\
        1) Binary to Decimal\n\
        2) Decimal to Binary\n\
        3) Binary to Hex\n\
        4) Hex to Binary\n\
        5) Decimal to Hex\n\
        6) Hex to Decimal\n\
        0) Exit')
    opt = int(input('anton> '))
    return opt



def convert(opt):
    os.system('clear')
    result = 0
    if opt == 0:
        quit()
    elif opt == 1:
        num = input('\n[+] Please enter the binary number\nanton> ')
        result = int(num, 2)
        tipo = 'decimal'
        return result, num, tipo 
    elif opt == 2:
        num = input('\n[+] Please enter the decimal number\nanton> ')
        result = bin(int(num))
        tipo = 'binary'
        return result, num, tipo 
    elif opt == 3:
        num = input('\n[+] Please enter the binary number\nanton> ')
        result_dec = int(num,2)
        result = hex(result_dec)
        tipo = 'hexadecimal'
        return result, num, tipo 
    elif opt == 4:
        return
    elif opt == 5:
        return
    elif opt == 6:
        return
    
    
        
while True:
    opt = menu()
    result, num, tipo = convert(opt)
    print('[+] The number {} is {} in {}\n'.format(num, result, tipo))
    input('PRESS ENTER TO CONTINUE')
    