
import tkinter  
import tkinter.ttk as ttk
root = tkinter.Tk ()

#Exercice 1 
print("------------------------------------------")
val=0
def titre():
    zone_texte = tkinter.Label (text = val).grid(column=2,row=0)
def button1 ():
    b = tkinter.Button (root, text=" + ",command=ajouter).grid(column=1,row=1)
def button2():
    b1=tkinter.Button(root,text=" - ",command=soustraire).grid(column=3,row=1)
def ajouter ():
    global val
    val=val+1
    zone_texte = tkinter.Label (text = val).grid(column=2,row=0)
def soustraire():
    global val
    val=val-1
    zone_texte = tkinter.Label (text = val).grid(column=2,row=0)
   
titre()
button2()
button1()
root.mainloop () 