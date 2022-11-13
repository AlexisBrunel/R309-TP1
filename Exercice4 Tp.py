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
        if i%2==0:
            couleur='black'
        else:
            couleur='white'
        
x1,y1,x2,y2=0,0,50,50
couleur= 'white'

# Fonction pour modifier la taille de l'image 
def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()
    newPhotoImage = PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x*oldWidth/newWidth)
            yOld = int(y*oldHeight/newHeight)
            rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage

def reine ():
   
    photo=PhotoImage(file='img/reine.png')
    photo=resizeImage(photo,45,45)
    return photo
    
    


'''def mousepointer():
        sourisx=fen.winfo_pointerx()
        sourisy=fen.winfo_pointery()
        print(sourisx)
        print(sourisy)'''

def drag(event):
    global photo
    photo = PhotoImage(file = "img/reine.png") 
    photo=resizeImage(photo,45,45)
    x=event.x
    y=event.y
    #Impossible de sortir 
    if x <=0 or x>=400 or y <=0 or y>=400 : #Empeche la photo de sortir 
        if x<0 :
            x=0
        elif x>400 :
            x=400
        if y<0:
            y=0
        elif y>400:
            y=400
    my_img = can.create_image(x, y,  image=photo)
    
    
    
   
    
    
    
fen=tkinter.Tk()
can=tkinter.Canvas(fen,width=400,heigh=400,bg='ivory')
can.pack(side=TOP,padx=5,pady=5)
photo=reine()
Commencer()
can.bind('<B1-Motion>',drag)
fen.mainloop()