from random import sample

def menu():
    print('|=====================Password Manager==========================')
    print('|Menu Options:\n|\
            1) Generate Key\n|\
            2) Save Key\n|\
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



while True:
    opt = menu()
    if opt == 1:
        psswd = gen_passwd()
        print('[+] The key generated is: ', psswd,'\n')
    elif opt == 0:
        quit()
    else:
        print('[-] Please enter a valid option.')
        continue
    
