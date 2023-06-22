import ttkbootstrap as tk
'''--------------------------------------FRAMING STARTED-------------------------------------------------------------'''

object = tk.Window(themename='vapor')
object.resizable(False ,False)
object.title('AshCrypt')
object.geometry('1500x800')


databaseFrame = tk.Frame(master=object , width=500 , height=800)
databaseFrame.place(x=0 , y=0)

frameFile1 = tk.Frame(master=object , width=500 , height=250)
frameFile1.place(x=500 , y=0)

frameFile2 = tk.Frame(master=object , width=500 , height=250)
frameFile2.place(x=500 , y=250)

textFrame1 = tk.Frame(master=object , width=500 , height=250)
textFrame1.place(x=1000 , y=0)

textFrame2 = tk.Frame(master=object , width=500 , height=250)
textFrame2.place(x=1000 , y=250)

lowerFrame = tk.Frame(master=object, width=1000 ,height=260)
lowerFrame.place(x=500,y=540)


'''--------------------------------------FRAMING DONE--------------------------------------------------------------'''

'''---------------------------------------QR SETUP STARTED-----------------------------------------------------------'''
#
#
# import qrcode
# from typing import Union
#
# def encQR(text : str) -> Union [int,tuple] :
#     try:
#         x = text.strip()
#         qr = qrcode.QRCode(version = 10,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=1)
#         qr.add_data(x)
#         qr.make(fit=True)
#         img = qr.make_image(fill_color = "black", back_color="white")
#         img.save(("encQR.png"))
#         img.show()
#         return 1
#     except Exception as e :
#         return (0,e)
#
# def decQR(text : str) -> Union [int,tuple] :
#     try:
#         x = text.strip()
#         qr = qrcode.QRCode(version = 10,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=20,border=1)
#         qr.add_data(x)
#         qr.make(fit=True)
#         img = qr.make_image(fill_color = "black", back_color="white")
#         img.save(("decQR.png"))
#         img.show()
#         return 1
#
#     except Exception as e :
#         return (0,e)

'''---------------------------------------QR SETUP ENDED-----------------------------------------------------------'''



'''----------------------------------------LOWER FRAME STARTED--------------------------------------------------------'''
# from PIL import ImageTk , Image
# theEncryptedQR = encImageHold.configure(height=220,width=220)
# resizedImageEnc = theEncryptedQR
# photoEncQR = ImageTk.PhotoImage(resizedImageEnc)
# theEncryptedQRLabel = tk.Label(master=lowerFrame,image=photoEncQR)
# theEncryptedQRLabel.place(x=1210 , y=10)



'''----------------------------------------LOWER FRAME ENDED----------------------------------------------------------'''











'''-------------------------------TEXT DECRYPTION/ENCRYPTION STARTED---------------------------------------------------'''



import AshCrypt.AshTextCrypt as AT
import AshCrypt.qr as qr


def encryption():
    m = inputfield1_1.get()
    if AF.CryptFile.keyverify(mainkeyvar.get()) == 1 and keySelectionFlag.get() == 1:
        if len(m) > 200 :
            outputvar1.set('Too Long')
        else :
            if inputfield1_1.get():
                progressbar.start()
                a = AT.Crypt(m, mainkeyvar.get())
                b =  a.encrypt()[1]
                outputvar1.set(b.__str__())
                if var1.get() == 1:
                    qr.tqr(b)


def decryption():
    n =inputfield2_1.get()
    if AF.CryptFile.keyverify(mainkeyvar.get()) == 1 and keySelectionFlag.get() == 1:
        if inputfield2_1.get():
            progressbar2.start()
            a = AT.Crypt(n, mainkeyvar.get())
            b = a.decrypt()[1]
            outputvar2.set(b.__str__())
            if var2.get() == 1:
                if not len(b) > 200:
                    qr.tqr(b)

def func1():
    if var1.get() == 1 :
        label1.config(text='QR ON')
    else:
        label1.config(text='QR OFF')

def func2():
    if var2.get() == 1 :
        label2.config(text='QR ON')
    else:
        label2.config(text='QR OFF')


button1 = tk.Button(master=textFrame1 ,text='ENCRYPT', command=encryption, bootstyle='light outline').place(relx=0.42, rely=0.73)
button2 = tk.Button(master=textFrame2 , text='DECRYPT', command=decryption,bootstyle='light outline').place(relx=0.42,rely=0.8)

inputfield1_1 = tk.StringVar()
textfield1_1 = tk.Entry(master=textFrame1 ,
                        width=20,
                        font='terminal 13 bold',
                        textvariable=inputfield1_1).place(relx=0.279 , rely=0.30)

inputfield2_1 = tk.StringVar(value='')
textfield2_1 = tk.Entry(master=textFrame2 ,
                        font='terminal 11 bold',
                        width=20,
                        textvariable=inputfield2_1).place(relx=0.290 ,rely=0.38)

namelabel1 = tk.Label(master=textFrame1 ,
                      text='ENCRYPTION',
                      font='Calibre 20' ,
                      )
namelabel1.place(relx=0.291 ,rely=0.10)
namelabel2 = tk.Label(master=textFrame2 ,
                      text='DECRYPTION' ,
                      font='Calibre 20'  ,
                      ).place(relx=0.298 ,rely=0.200)

outputvar1 = tk.StringVar(value='')
outputlabel1 =  tk.Entry(master= textFrame1,
                         textvariable=outputvar1,
                         font='terminal 11 bold').place(relx= 0.02,
                                                       rely= 0.48 ,
                                                       width= 480,
                                                       height= 50)
outputvar2 = tk.StringVar(value='')
outputlabel2 = tk.Entry(master=textFrame2 ,
                        textvariable= outputvar2 ,
                        font='terminal 11 bold').place(relx= 0.02,
                                                       rely= 0.55,
                                                       width= 480,
                                                       height= 50)



label1 = tk.Label(master=textFrame1,text='QR',font=('terminal',17))
label1.place(relx=0.2,rely=0.75)
var1 = tk.IntVar()
mytoolbutt3 = tk.Checkbutton(bootstyle='success , round-toggle',
                        master=textFrame1,
                        variable=var1,
                        offvalue=0,
                        command=func1)

mytoolbutt3.place(relx=0.1,rely=0.77)




label2 = tk.Label(master=textFrame2,text='QR',font=('terminal',17))
label2.place(relx=0.2,rely=0.82)
var2 = tk.IntVar()
mytoolbutt6 = tk.Checkbutton(bootstyle='success , round-toggle',
                        master=textFrame2,
                        variable=var2,
                        offvalue=0,
                        command=func2)

mytoolbutt6.place(relx=0.1,rely=0.84)


progressbar = tk.Progressbar(master=textFrame1,mode='indeterminate',style='secondary',length=100,)
progressbar.place(relx=0.05,rely=0.34)

progressbar2 = tk.Progressbar(master=textFrame2,mode='indeterminate',style='secondary',length=100,)
progressbar2.place(relx=0.05,rely=0.42)

'''-------------------------------TEXT DECRYPTION/ENCRYPTION ENDED---------------------------------------------------'''









'''-------------------------------FILE ENCRYPTION/DECRYPTION STARTED--------------------------------------------'''


filepathlabel = tk.Label(master=frameFile1 ,
                      text='FILE PATH',
                      font='Calibre 20' ,
                      )
filepathlabel.place(relx=0.336,rely=0.10)


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

addtodbLabel = tk.Label(master=frameFile1,text='ADD TO DATABASE',font=('Calibre',11))
addtodbLabel.place(relx=0.35,rely=0.908)


def encToggleButtFunc():
    pass

def decToggleButtFunc():
    pass

encfiletoolbuttvar = tk.IntVar()
encfiletoolbutt = tk.Checkbutton(bootstyle='warning , round-toggle',
                        master=frameFile1,
                        variable=encfiletoolbuttvar,
                        offvalue=0,
                        command=encToggleButtFunc)

encfiletoolbutt.place(relx=0.25,rely=0.92)


decfiletoolbuttvar = tk.IntVar()
decfiletoolbutt = tk.Checkbutton(bootstyle='warning , round-toggle',
                        master=frameFile1,
                        variable=decfiletoolbuttvar,
                        offvalue=0,
                        command=decToggleButtFunc)

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
                      font='Calibre 20',
                      bootstyle='secondary',
                      ).place(relx=0.3 ,rely=0.075)


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


'''-------------------------------FILE ENCRYPTION/DECRYPTION ENDED--------------------------------------------'''




'''--------------------------------------DATA BASE FRAME STARTED------------------------------------------------'''


databaseFrame = tk.Frame(master=object,height=800, width=500)
databaseFrame.place(rely=0, relx=0)

console_label = tk.Label(master=databaseFrame, text='DATABASE OUTPUT CONSOLE', font='Terminal 15 bold')
console_label.place( relx=0.09,rely=0.04)

display_text_variable = 'Here is the output...'

db_display_text = tk.ScrolledText(width=34 , height=30, font='Terminal 10 bold')
db_display_text.insert(tk.END,display_text_variable)
db_display_text.place(relx=0.015 ,rely=0.105)

###### FUNCTIONS ######
def show_all_content():
    pass

def show_content():
    pass

def show_all_tables():
    pass
def drop_all_tables():
    pass

def drop_content():
    pass


########## FUNCTIONS DONE ###########

show_all_content_button = tk.Button(master=databaseFrame,text='SHOW ALL TABLE CONTENT',command=show_all_content,bootstyle='light outline')
show_all_content_button.place(relx=0.278,rely=0.75)

show_all_tables_button = tk.Button(master=databaseFrame,text='SHOW ALL TABLES',command=show_all_tables,bootstyle='light outline')
show_all_tables_button.place(relx=0.342,rely=0.81)

drop_all_tables_button = tk.Button(master=databaseFrame,text='DROP ALL TABLES',command=drop_all_tables,bootstyle='light outline')
drop_all_tables_button.place(relx=0.344,rely=0.87)



drop_content_button = tk.Button(master=databaseFrame,text='DROP CONTENT BY ID',command=drop_content,bootstyle='light outline')
drop_content_button.place(relx=0.08,rely=0.93)

content_id_entry_var = tk.StringVar(value=' ID')
content_id_entry = tk.Entry(master=databaseFrame,textvariable=content_id_entry_var,width=3,font='Calibre 11')
content_id_entry.place(relx=0.45,rely=0.93)

show_content_button = tk.Button(master=databaseFrame,text='SHOW CONTENT BY ID',command=show_content,bootstyle='light outline')
show_content_button.place(relx=0.562,rely=0.93)



'''--------------------------------------DATA BASE FRAME ENDED------------------------------------------------'''


'''--------------------------------------CREATING DEMO DB-----------------------------------------------------------------------'''
import AshCrypt.AshDatabase as db
conn = db.Database('test.db')
conn.addtable()
key = '#5482A'
conn.insert('My Accounts', 'some encrypted content of bytes or strings', key)
for e in conn.show_tables():
    print(e)
print(conn.size)
query1 = 'SELECT COUNT(*) AS cc ,content FROM Classified WHERE key = "#5482A" ORDER BY cc DESC '
print(conn.query(query1))


'''---------------------------------------CREATING DEMO DB DONE-----------------------------------------------------------'''
'''----------------------------------------LOWER FRAME STARTED----------------------------------'''



lowerFrame = tk.Frame(master=object, width=1000 ,height=260)
lowerFrame.place(x=500,y=540)           ##### MUST CHANGE ####

def show_db_size():
    pass

def show_last_mod():
    pass

def show_current_IDs():
    pass

def show_cwd():
    pass

import string
def set_db_name():
    global db_blocker
    db_name = db_name_var.get()
    valid_count = 0
    if len(db_name)>0:
        for e in db_name:
            if e in (string.ascii_letters + string.digits + '-' + '.' + '_'):
                valid_count += 1
        if valid_count == len(db_name):
            db_blocker = 1
    else:
        db_blocker = 0



db_blocker = 0
db_name_var = tk.StringVar()
db_name_entry = tk.Entry(master=lowerFrame ,
                        width=22,
                        font='terminal 15 bold',
                        textvariable=db_name_var).place(relx=0.03, rely=0.04)

set_db_button = tk.Button(master=lowerFrame , text='SUBMIT DATABASE NAME', command=set_db_name,bootstyle='secondary outline')
set_db_button.place(relx=0.45,rely=0.048)


db_analysis_label = tk.Label(master=lowerFrame,text='DATABASE', font='Calibre 13 bold')
db_analysis_label.place(relx=0.03,rely=0.21)

database_cwd_label = tk.Label(master=lowerFrame,text='PATH :', font='Calibre 11')
database_cwd_label.place(relx=0.05,rely=0.35)

size_label = tk.Label(master=lowerFrame,text='SIZE (MB) :', font='Calibre 11')
size_label.place(relx=0.05,rely=0.46)


last_mod_label = tk.Label(master=lowerFrame,text='LAST MODIFICATION :', font='Calibre 11')
last_mod_label.place(relx=0.05,rely=0.57)

latest_ID_label = tk.Label(master=lowerFrame,text='LATEST INSERTED ID :', font='Calibre 11')
latest_ID_label.place(relx=0.05,rely=0.68)

'''----------------------------------------LOWER FRAME ENDED----------------------------------'''














if __name__ == '__main__':
    object.mainloop()
