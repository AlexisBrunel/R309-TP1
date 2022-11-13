import tkinter
def verif():
    saisie=val.get()
    if "@" not in saisie or   "." not in saisie or " " in saisie :
        rep =tkinter.Label().grid(column=0,row=4)
    else :
        user_button['state']=tkinter.NORMAL
        user_button['command']=root.destroy
        user_button['bg']='green'
        print("Vous allez être enregistré avec:",saisie)
def valid():
    rep = tkinter.Label(root).grid(column=0,row=5)
    root.quit
root = tkinter.Tk ()
val= tkinter.StringVar()
val.trace("w", lambda name, index, mode, val=val: verif())
user = tkinter.Label(root, text = "Veuillez entrer votre Email:",bg='yellow').grid(column=0,row=0)
user_Entry = tkinter.Entry(root,bg="orange",textvariable=val).grid(column=0,row=2)
user_button=tkinter.Button(root,text="Valider",command=valid,state=tkinter.DISABLED,bg='red')
user_button.grid(column=0,row=5)
root.mainloop () 