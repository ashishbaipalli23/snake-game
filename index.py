from tkinter import *
from PIL import Image,ImageTk
import random
import jinna
from tkinter import messagebox as ms
root = Tk()

root.config(bg='#ccf381')
root.geometry('500x650')
root.title('Anaconda')


l1 = Label(root,text= "WELCOME TO ANACONDA",fg='black',bg='#ccf381',font=('Helvetica',20))
e = Entry(root,bd=2,fg='blue')


l2 = Label(root,text='ENTER NAME :',font=('Helvetica',12),fg='black',bg='#ccf381')

var=StringVar()
#var.set("EASY")

drop=OptionMenu(root,var,'EASY','MEDIUM','HARD')


l3 = Label(root,text='CHOOSE LEVEL:',font=('Helvetica',12),fg='black',bg='#ccf381')


    
#define function
def mygame():
    global a
    a = var.get()  
    #print(a)   
    h=e.get()
    if len(h) == 0:
        ms.showerror('error!!','enter name field')
    else:  
        
        #Label(root,text=a).pack()    
        jinna.play()
   
  

btn = Button(root,text='START',bg="#4831d4",command=mygame)
#displaying wedgets
l1.pack()
l2.pack()
e.pack(pady=9)
#l3.pack(pady=9)
#drop.pack(pady=8,ipadx=4)

btn.pack(ipadx=16,ipady=3)





root.mainloop()