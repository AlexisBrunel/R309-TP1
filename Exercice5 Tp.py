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
        print(x1,y1)
        if ite== 8 :
            y1+=50
            y2+=50
            i+=1
            ite=0
            x1=0
            x2=50
        if i%2==0:
            couleur='grey'
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
    
    

fen=Tk()
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
    #Empecher le pion de sortir de la grille
    if x <=0 or x>=400 or y <=0 or y>=400 : #Empeche la photo de sortir 
        if x<=0 :
            x=1
        elif x>=400 :
            x=399
        if y<=0:
            y=1
        elif y>=400:
            y=399
    #Formatage des coordonnées en String pour récupérer les dizaines et les centaines
    cooX = str(x)
    cooY = str(y)
    #Utilisation de ternaire
    centX = cooX[:1] if len(cooX)==3 else "0" #Centaine X
    dizX = int(cooX[1:]) if len(cooX)==3 else int(cooX) #Dizaine X
    centY = cooY[:1] if len(cooY)==3 else "0" #Centaine Y
    dizY = int(cooY[1:]) if len(cooY)==3 else int(cooY) #Dizaine Y
    
    #Mise en place des Pas de la piece
    if dizX < 50:
        dizX = 25
    elif dizX >= 50:
        dizX = 75
    if dizY < 50:
        dizY = 25
    elif dizY >= 50:
        dizY = 75
    #Reformatage Complet des Coordonnées String en Int
    cooX = int(centX+str(dizX))
    cooY = int(centY+str(dizY))
    #Affichage de l'image aux bonnes Coordonnées
    my_img = can.create_image(cooX, cooY,  image=photo)
    

can=Canvas(fen,width=400,heigh=400,bg='ivory')
can.pack(side=TOP,padx=5,pady=5)
photo=reine()
Commencer()
can.bind('<B1-Motion>',drag)
fen.mainloop() 