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


button1 = tk.Button(master=frame1 ,text='COMPUTE', command=encryption, bootstyle='light outline').place(relx=0.435, rely=0.73)
button2 = tk.Button(master=frame2 , text='COMPUTE', command=decryption,bootstyle='light outline').place(relx=0.435,rely=0.8)

inputfield1_1 = tk.StringVar()
textfield1_1 = tk.Entry(master=frame1 ,
                        width=20,
                        font='terminal 13 bold',
                        textvariable=inputfield1_1).place(relx=0.279 , rely=0.30)

inputfield2_1 = tk.StringVar()
textfield2_1 = tk.Entry(master=frame2 ,
                        font='terminal 11 bold',
                        textvariable=inputfield2_1).place(relx=0.290 ,rely=0.38)

namelabel1 = tk.Label(master=frame1 ,
                      text='ENCRYPTION',
                      font='Terminal 20' ,
                      )
namelabel1.place(relx=0.270 ,rely=0.10)
namelabel2 = tk.Label(master=frame2 ,
                      text='DECRYPTION' ,
                      font='terminal 20'  ,
                      ).place(relx=0.280 ,rely=0.200)

outputvar1 = tk.StringVar(value='')
outputlabel1 =  tk.Entry(master= frame1,
                         textvariable=outputvar1,
                         font='terminal 11 bold').place(relx= 0,
                                                       rely= 0.48 ,
                                                       width= 1000000,
                                                       height= 50)
outputvar2 = tk.StringVar(value='')
outputlabel2 = tk.Entry(master=frame2 ,
                        textvariable= outputvar2 ,
                        font='terminal 11 bold').place(relx= 0 ,
                                        rely= 0.55 ,
                                        width= 1000000 ,
                                        height= 50)
if __name__ == '__main__':
    object.mainloop()
