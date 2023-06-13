import AshTextCrypt  as A
import sys


print('Welcome to the container')

commands = 'Commands : \n\tq: to quit the program \n\tc : view commands\n\tk : for key selection\n\te: for encryption\n\td : for decryption'

global key
def input_selection(q=None,c=None,e=None,d=None):
    if q == 1 :
        sys.exit()
    if c == 1 :
        print(commands)
    if e == 1 :
        enc()
    if d == 1 :
        dec()
    else :
        pass

def inputWrap(inp) :
        inp = inp.lower()
        if inp == 'c':
            input_selection(c=1)
            return 'c'
        if inp == 'q' :
            input_selection(q=1)
            return 'q'
        if inp == 'e' :
            input_selection(e=1)
            return 'e'
        if inp == 'd' :
            input_selection(d=1)
            return 'd'
        else :
            return None
def intro():
    intro = True
    while intro:
        print('Program started running..')
        print('To view commands : ')
        while True:
            n = input("Press 'c' : ")
            inputWrap(n)
def keysetup():
    while True :
        global key
        key = ''
        i = input('Do you have a key ?(y/n) : ')
        inputWrap(i)
        if i.lower() == "y" or "n":
            break
        if i == "n":
            print("Here's your key : ")
            key = A.Crypt.genkey()
            print(key)
        else:
            while True:
                print('insert your key here : ')
                kk = input()
                inputWrap(kk)
                if A.Crypt.keyverify(kk) == 1:
                    print('Key selected')
                    key = kk
                else:
                    print('Enter a valid key !')


def enc():
    keysetup()
    while True:
        print()
        while True:
            global key
            print("press c to view commands : ")
            message = input('Enter a message : ')
            inputWrap(message)
            a = A.Crypt(message, key=key)
            enc = a.encrypt()
            if (enc[0]) == 1:
                print(enc[1])
            else:
                print('Error occured during the encryption process')

def dec():
    keysetup()
    while True:
        print()
        while True:
            global key
            print("press c to view commands : ")
            message = input('Enter a message : ')
            inputWrap(message)
            a = A.Crypt(message, key=key)
            dec = a.decrypt()
            if (dec[0]) == 1:
                print(dec[1])
            else:
                print('Error occured during the encryption process')




if __name__ == '__main__':
    intro()