import ttkbootstrap as tk

##########################################################################################


object = tk.Window(themename='vapor')
object.resizable(False ,False)
object.title('AshCrypt')
object.geometry('500x540')

frameFile1 = tk.Frame(master=object , width=500 , height=250)
frameFile1.place(x=0 , y=0)
frameFile2 = tk.Frame(master=object , width=500 , height=250)
frameFile2.place(x=0 , y=250)

##############################################################################

filepathlabel = tk.Label(master=frameFile1 ,
                      text='FILE PATH',
                      font='Terminal 20' ,
                      )
filepathlabel.place(relx=0.293 ,rely=0.10)


resultvarfile = tk.StringVar(value='                  ..RESULT..')
resultLabelfile =  tk.Label(master= frameFile1,
                         textvariable=resultvarfile,
                         font='terminal 13 bold').place(
                                                       rely= 0.55 ,
                                                       )

import AshCrypt.AshFileCrypt as AF

fileaccessSemo = 1
def encFile():
    global fileaccessSemo
    if fileaccessSemo == 1 :
        fileaccessSemo -= 1
        if AF.CryptFile.keyverify(mainkeyvar.get()) == 1 and keySelectionFlag.get() == 1:
            filename = filenameStringVar.get()
            key = mainkeyvar.get()
            target = AF.CryptFile(filename, key)
            a = target.encrypt()
            if a == 1:
                resultvarfile.set('            Encrypted Successfully')
            if a == 2:
                resultvarfile.set('            ERROR : File is Empty')
            if a == 3:
                resultvarfile.set("          ERROR : File Doesn't Exist")
            if a == 0:
                resultvarfile.set("               ERROR : Can't Encrypt")
            elif a == 4:
                resultvarfile.set('                 ERROR : Unknown')
            fileaccessSemo += 1

def decfile():
    global fileaccessSemo
    if fileaccessSemo == 1:
        fileaccessSemo -= 1
        if AF.CryptFile.keyverify(mainkeyvar.get()) == 1 and keySelectionFlag.get() == 1:
            filename = filenameStringVar.get()
            key = mainkeyvar.get()
            target = AF.CryptFile(filename, key)
            a = target.decrypt()
            if a == 1:
                resultvarfile.set('            Decrypted Successfully')
            if a == 2:
                resultvarfile.set('            ERROR : File is Empty')
            if a == 3:
                resultvarfile.set("          ERROR : File Doesn't Exist")
            if a == 0:
                resultvarfile.set("             ERROR : Can't Decrypt")
            elif a == 4:
                resultvarfile.set('                ERROR : Unknown')
            fileaccessSemo += 1





encryptionfilebutton = tk.Button(master=frameFile1 ,text='ENCRYPT FILE', command=encFile, bootstyle='warning outline').place(relx=0.25, rely=0.73)
decryptionfilebutton = tk.Button(master=frameFile1 , text='DECRYPT FILE', command=decfile,bootstyle='warning outline').place(relx=0.55,rely=0.73)

filenameStringVar = tk.StringVar(value='')
filenametext = tk.Entry(master=frameFile1 ,
                        width=22,
                        font='terminal 15 bold',
                        textvariable=filenameStringVar).place(relx=0.1, rely=0.30)

#################################################################################"

addtodbLabel = tk.Label(master=frameFile1,text='ADD TO DATABASE',font=('terminal',11))
addtodbLabel.place(relx=0.36,rely=0.91)


def func1():
    if encfiletoolbuttvar.get() == 1 :
        x = 8*8
    else:
        x = 8-8
def func2():
    if decfiletoolbuttvar.get() == 1 :
        ###
        x = 2
    else:
        x = 5


encfiletoolbuttvar = tk.IntVar()
encfiletoolbutt = tk.Checkbutton(bootstyle='warning , round-toggle',
                        master=frameFile1,
                        variable=encfiletoolbuttvar,
                        offvalue=0,
                        command=func1)

encfiletoolbutt.place(relx=0.25,rely=0.92)


decfiletoolbuttvar = tk.IntVar()
decfiletoolbutt = tk.Checkbutton(bootstyle='warning , round-toggle',
                        master=frameFile1,
                        variable=decfiletoolbuttvar,
                        offvalue=0,
                        command=func2)

decfiletoolbutt.place(relx=0.717,rely=0.92)

#####################################################################################


keySelectionFlag = tk.IntVar(value=0)
def mainKeyWrapper():
    if AF.CryptFile.keyverify(mainkeyvar.get()) == 1 :
        keyrefGen()
        keyselectionvar.set('       SELECTED')
        keySelectionFlag.set(1)
    else :
        keyselectionvar.set('     NOT SELECTED')



mainkeyLabel = tk.Label(master=frameFile2 ,
                      text='MAIN KEY' ,
                      font='terminal 20',
                      bootstyle='secondary',
                      ).place(relx=0.195 ,rely=0.100)


mainkeyvar = tk.StringVar()
mainkeyEntry = tk.Entry(master=frameFile2 ,
                        font='terminal 15 bold',
                        textvariable=mainkeyvar,
                        width=22
                        ).place(relx=0.1 ,rely=0.29)


import string
import secrets
def keyrefGen():
    ref = '#'
    for _ in range(6):
        character = secrets.choice(string.ascii_letters + string.digits + '$' + '?' + '&' + '@' + '!' + '-' + '+')
        ref += character
    outputKeyref.set(ref)



outputKeyref = tk.StringVar(value='#XXXXXX')
keyrefLabel = tk.Label(master=frameFile2,textvariable=outputKeyref,bootstyle='secondary',font=('terminal',12))
keyrefLabel.place(relx=0.712,rely=0.12)

keySelectButton = tk.Button(master=frameFile2 ,text='SELECT KEY', command=mainKeyWrapper, bootstyle='secondary outline').place(relx=0.6725, rely=0.5)


keyselectionvar = tk.StringVar(value='   KEY NOT SELECTED')
keyselectionLabel = tk.Label(master=frameFile2 ,
                        textvariable= keyselectionvar ,
                        bootstyle='secondary',
                        font='terminal 11 bold').place(relx= 0.15 ,
                                        rely= 0.465,
                                        height= 50)

###########################################################################################

def genSideKey():
    keyGenVar.set(AF.CryptFile.genkey())


keyGenVar = tk.StringVar(value='')
keyGenEntry = tk.Entry(master=frameFile2 ,
                        font='terminal 15 bold',
                        textvariable=keyGenVar,
                        width=14,
                        show='').place(relx=0.1 ,rely=0.69)

keyButton = tk.Button(master=frameFile2 ,text='GENERATE', command=genSideKey, bootstyle='success outline').place(relx=0.675, rely=0.7)


###########################################################################################"


if __name__ == '__main__':
    object.mainloop()

