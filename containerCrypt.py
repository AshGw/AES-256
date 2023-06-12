import AshTextCrypt  as A
import sys


print('Welcome to the container')

commands = 'Commands : \n\tq: to quit the program \n\tc : view commands\n\tb : back to the enc/dec menu selection' \
           '\n\tk : for key selection\n\te: for encryption\n\td : for decryption'

key = ''
def input_selection(q=None,c=None,b=None,k=None,e=None,d=None):
    if q == 1 :
        sys.exit()
    if b == 1 :
        encdec()
    if c == 1 :
        print(commands)
    else :
        pass

def inputWrap(inp) :
        inp = inp.lower()
        if inp == 'c':
            input_selection(c=1)
            return 'c'
        if inp == 'b' :
            input_selection(b=1)
            return 'b'
        if inp == 'q' :
            input_selection(q=1)
            return 'q'
        else :
            return None
def intro():
    intro = True
    while intro:
        print('Program started running..')
        print('To view commands : ')
        while True:
            n = input("Press 'c' : ")
            a = inputWrap(n)
            if a == 'c':
                print()
                break

def keysetup():
    while True :
        global key
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
                global key
                print('insert your key here : ')
                kk = input()
                inputWrap(kk)
                if A.Crypt.keyverify(kk) == 1:
                    print('Key selected')
                    key = kk
                else:
                    print('Enter a valid key !')


def encdec():
    while True:
        print()
        while True:
            global key
            print("press c to view commands : ")
            message = input('Enter a message : ')
            a = A.Crypt(message, key=key)
            enc = a.encrypt()
            if (enc[0]) == 1:
                print(enc[1])
            else:
                print('Error occured during the encryption process')




if __name__ == '__main__':
    intro()
    keysetup()
    encdec()