from AshCrypt import AshFileCrypt as AF
from AshCrypt import AshTextCrypt as A
import sys


print('Welcome to the CLI')

commands = 'Commands : \n\tq: to quit the program \n\tc : view commands\n\te: for encryption\n\td : for decryption\n' \
           '\tef : to encrypt a file\n\tdf : to decrypt a file\n'

global key
def input_selection(q=None,c=None,e=None,d=None,ef=None,df=None):
    global encflag,decFlag,file_decFlag,file_encFlag
    if q == 1 :
        sys.exit()
    if c == 1 :
        print(commands)
    if e == 1 :
        file_decFlag = False
        file_encFlag = False
        decFlag = False
        encflag = True
        enc()
    if d == 1 :
        file_decFlag = False
        file_encFlag = False
        encflag = False
        decFlag = True
        dec()
    if ef == 1 :
        decFlag = False
        encflag = False
        file_decFlag = False
        file_encFlag = True
        file_enc()
    if df == 1 :
        encflag = False
        decFlag = True
        file_encFlag = False
        file_decFlag = True
        file_dec()
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
        if inp == 'ef' :
            input_selection(ef=1)
            return 'ef'
        if inp == 'df' :
            input_selection(df=1)
            return 'df'
        else :
            return None
def intro():
    intro = True
    while intro:
        print('Program started running..')
        print('Press c to view commands : ')
        while True:
            n = input("Press..\n")
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

file_encFlag = True


file_decFlag = True
def file_dec():
    keysetup()
    while file_decFlag :
        print()
        global key
        pre = input("running file decryption mode , press the known commands or 'Enter' to continue.. : ")
        print()
        inputWrap(pre)
        if pre == '' :
            print("You can use the commands AFTER entering the file name.. ")
            filename = input('Enter full file name to be Decrypted : ')
            target = AF.CryptFile(filename, key)
            a = target.decrypt()
            if a == 1:
                print('File successfully decrypted ')
            if a == 2:
                print('Cannot decrypt the file  when it is already empty')
            if a == 3:
                print(f'The file named : "{filename}" does not exists , try specifying the whole sys path')
            if a == 0:
                print('Error in the decryption process. Check if the the file is distorted or it might just be '
                      'decrypted already')
            elif a == 4 :
                print('Unknown Error has occurred\n')


def file_enc():
    keysetup()
    while file_encFlag :
        print()
        global key
        pre = input("running file encryption mode, press the known commands or 'Enter' to continue.. : ")
        print()
        inputWrap(pre)
        if pre == '' :
            print("You can use the commands AFTER entering the file name.. ")
            filename = input('Enter full file name to be Encrypted : ')
            target = AF.CryptFile(filename, key)
            a = target.encrypt()
            if a == 1:
                print('File successfully encrypted ')
            if a == 2:
                print('Cannot encrypt the file  when it is already empty')
            if a == 3:
                print(f'The file named : "{filename}" does not exists , try specifying the whole sys path')
            if a == 0:
                print('Error in the encryption process. Check if the the file is distorted')
            elif a == 4 :
                print('Unknown Error has occurred\n')



if __name__ == '__main__':
    intro()