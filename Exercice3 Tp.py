import tkinter
from tkinter import *

#Exercice 3 
def Commencer():
    global x1,x2,y1,y2,couleur
    ite=0
    i=1
    while x1 < 400 and y1<400:
        can.create_rectangle(x1,y1,x2,y2,fill=couleur)
        i+=1
        ite+=1
        x1+=50
        x2+=50 
        if ite== 8 :
            y1+=50
            y2+=50
            i+=1
            ite=0
            x1=0
            x2=50
            print(i)
        if i%2==0:
            print(i)
            couleur='black'
        else:
            couleur='white'
x1,y1,x2,y2=0,0,50,50
couleur=()
fen=tkinter.Tk()
can=tkinter.Canvas(fen,width=300,heigh=300,bg='ivory')
Commencer()
can.pack(side=TOP,padx=5,pady=5)
fen.mainloop()