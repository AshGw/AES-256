import ttkbootstrap as tk
from AshTextCrypt import *
import qr

key = 'c3066e464350e68a144d6be3e35c879eac1b9f360139443ee3d9e1960725d6a4d3379af0a35b6a07d083ecc29c4ba03767ad6d48b8e9c20d319dd459da52a91a'

def encryption():
    m = inputfield1_1.get()
    if len(m) > 200 :
        outputvar1.set('Too Long')
    else :
        a = Crypt(m, key)
        b =  a.encrypt()[1]
        outputvar1.set(b.__str__())
        qr.tqr(b)

def decryption():
    n =inputfield2_1.get()
    a = Crypt(n, key)
    b = a.decrypt()[1]
    outputvar2.set(b.__str__())



object = tk.Window(themename='vapor')
object.resizable(False ,False)
object.title('AshCrypt')
object.geometry('500x540')

frame1 = tk.Frame(master=object , width=500 , height=250)
frame1.place(x=0 , y=0)
frame2 = tk.Frame(master=object , width=500 , height=250)
frame2.place(x=0 , y=250)


button1 = tk.Button(master=frame1 ,text='compute', command=encryption).place(relx=0.43, rely=0.8)
button2 = tk.Button(master=frame2 , text='compute', command=decryption).place(relx=0.43,rely=0.8)

inputfield1_1 = tk.StringVar()
textfield1_1 = tk.Entry(master=frame1 ,
                        width=20,
                        font='Calibre 9 bold',
                        textvariable=inputfield1_1).place(relx=0.3333 , rely=0.33)

inputfield2_1 = tk.StringVar()
textfield2_1 = tk.Entry(master=frame2 ,
                        width=20,
                        textvariable=inputfield2_1).place(relx=0.3333 ,rely=0.35)

namelabel1 = tk.Label(master=frame1 ,
                      text='Encryption',
                      font='Calibre 20 bold' ,
                      ).place(relx=0.33 ,rely=0.10)
namelabel2 = tk.Label(master=frame2 ,
                      text='Decryption' ,
                      font='Calibre 20 bold'  ,
                      ).place(relx=0.335 ,rely=0.14)

outputvar1 = tk.StringVar(value='')
outputlabel1 =  tk.Entry(master= frame1,
                         textvariable=outputvar1,
                         font='Calibre 7 bold').place(relx= 0,
                                                       rely= 0.53 ,
                                                       width= 1000000,
                                                       height= 50)
outputvar2 = tk.StringVar(value='')
outputlabel2 = tk.Entry(master=frame2 ,
                        textvariable= outputvar2 ,
                        font='Calibre 11 bold').place(relx= 0 ,
                                        rely= 0.55 ,
                                        width= 1000000 ,
                                        height= 50)
if __name__ == '__main__':
    object.mainloop()
