
import src.AshTextCrypt as A
import sys


print('Welcome to the CLI')

commands = 'Commands : \n\tq: to quit the program \n\tc : view commands\n\te: for encryption\n\td : for decryption\n'

global key
def input_selection(q=None,c=None,e=None,d=None):
    global encflag,decFlag
    if q == 1 :
        sys.exit()
    if c == 1 :
        print(commands,'\n')
    if e == 1 :
        decFlag = False
        encflag = True
        enc()
    if d == 1 :
        decFlag = True
        encflag = False
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
            n = input("Press 'c' : \n")
            inputWrap(n)
def keysetup():
    outer = True
    inner = True
    while outer :
        global key
        key = ''
        i = input('Do you have a key ?(y/n) : ')
        inputWrap(i)
        if i.lower() == 'n' :
            print("Here's your key : ")
            key = A.Crypt.genkey()
            print(key)
            inner = False
            outer = False
        elif i.lower() == 'y':
            while inner:
                print('insert your key here : ')
                kk = input()
                inputWrap(kk)
                if A.Crypt.keyverify(kk) == 1:
                    print('Key selected\n')
                    key = kk
                    inner = False
                    outer = False
                else:
                    print('Enter a valid key !\n')

encflag = True
def enc():
    keysetup()
    while encflag:
        print()
        while True:
            global key
            print("press c to view commands.. ")
            message = input('Encrypt a message : ')
            inputWrap(message)
            a = A.Crypt(message, key=key)
            enc = a.encrypt()
            if (enc[0]) == 1:
                print("Success ! Here's the message : ")
                print('\t',enc[1],'\n')
            else:
                print('Error occurred during the encryption process\n')
decFlag = True
def dec():
    keysetup()
    while decFlag:
        print()
        while True:
            global key
            print("press c to view commands.. ")
            message = input('Decrypt a message : ')
            inputWrap(message)
            a = A.Crypt(message, key=key)
            dec = a.decrypt()
            if (dec[0]) == 1:
                print("Success ! Here's the message : ")
                print('\t',dec[1],'\n')
            else:
                print('Error occurred during the decryption process\n')




if __name__ == '__main__':
    intro()