from random import*
from tkinter import*
from random import*

Joueur=0
CasesJoueur1=[['' for i in range(11)] for j in range(11)]
CasesJoueur2=[['' for i in range(11)] for j in range(11)]
BateauJoueur1=[['0' for i in range(11)] for j in range(11)] #Attribue a chaque case jouable du plateau la valeur '0'. Si la case a la valeur '0' alors c'est une case vide.
BateauJoueur2=[['0' for i in range(11)] for j in range(11)] #Cela est fait pour les deux joueurs
Lettre=['A','B','C','D','E','F','G','H','I','J']
Nombre=['1','2','3','4','5','6','7','8','9','10']
NbBateauJ1=17
NbBateauJ2=17
pivoter=0
PremierePrevisualisation=0
Switch=0
fin1=0
fin2=0

################################################################################
#PARTIE FONCTION
################################################################################
def attaque():
    global Joueur , NbBateauJ1 , NbBateauJ2 , fin1 , fin2
    if AttaqueY.get()<=0 or AttaqueY.get()>=11 or AttaqueX.get() not in Lettre:  #Verification que les coordonnées sont bien dans le plateau
        Error('Les coordonnées ne sont pas dans le plateau.')
    elif Joueur==2: #Joueur 2
        x=(Lettre.index(AttaqueX.get()))+1
        y=AttaqueY.get()
        if BateauJoueur1[x][y]=='0':
            #Verification pour savoir si la case est vide ou non. Si la case a la valeur '0' , elle est vide. Si elle a une valeur autre
            #cela correspond soit à un bateau ( chaque bateau a sa propre valeur ) , soit à une case vide déjà touché '7' , soit à un bateau déjà touché '6'.
            PlateauJoueur2.itemconfig(CasesJoueur2[x][y],fill='blue') #colorie la case en bleu si le joueur ne touche rien , en rouge si il touche un bateau.
            message("La frappe fini dans l'eau !")
            BateauJoueur1[x][y]='7'
            fenetrePlateau.after(2000, Plateau1)
        elif BateauJoueur1[x][y]=='7':
            message("Tu as déjà tiré et manqué ta frappe ici ! Réessaie.")
        elif BateauJoueur1[x][y]=='1'or BateauJoueur1[x][y]=='3'or BateauJoueur1[x][y]=='4'or BateauJoueur1[x][y]=='5'or BateauJoueur1[x][y]=='2':
            PlateauJoueur2.itemconfig(CasesJoueur2[x][y],fill='red')
            message("La frappe a touché un bateau!")
            BateauJoueur1[x][y]='6'
            fin2=fin2+1
            fenetrePlateau.after(2000, Plateau1)
            if fin1==17 or fin2==17:
                fenetreCommande2.pack_forget()
                fenetrePlateau.after(2000,fin)
        elif BateauJoueur1[x][y]=='6':
            message("Tu as déjà tiré et touché un bateau ici ! Réessaie.")

    else : #Joueur 1
        x=(Lettre.index(AttaqueX.get()))+1
        y=AttaqueY.get()
        if BateauJoueur2[x][y]=='0':
            PlateauJoueur1.itemconfig(CasesJoueur1[x][y],fill='blue')
            message("La frappe fini dans l'eau !")
            BateauJoueur2[x][y]='7'
            fenetrePlateau.after(2000, Plateau2)
        elif BateauJoueur2[x][y]=='7':
            message("Tu as déjà tiré et manqué ta frappe ici ! Réessaie. ")
        elif BateauJoueur2[x][y]=='1'or BateauJoueur2[x][y]=='3'or BateauJoueur2[x][y]=='4'or BateauJoueur2[x][y]=='5'or BateauJoueur2[x][y]=='2':
            PlateauJoueur1.itemconfig(CasesJoueur1[x][y],fill='red')
            message("La frappe a touché un bateau!")
            BateauJoueur2[x][y]='6'
            fin1=fin1+1
            fenetrePlateau.after(2000, Plateau2)
            if fin1==17 or fin2==17:
                fenetreCommande2.pack_forget()
                fenetrePlateau.after(2000,fin)
        elif BateauJoueur2[x][y]=='6':
            message("Tu as déjà tiré et touché un bateau ici ! Réessaie.")


def Previsualisation1(event):
    global Switch
    if Switch==0:
        Previsualisation2()

def Previsualisation2():
    global Joueur, pivoter, PreX, PreY, PreJoueur, PreNbBateauJ2, PreNbBateauJ1,PreConflit,PrePivoter, PremierePrevisualisation
    Conflit=0
    Previsualisation3()
    if PlacerY.get()<=0 or PlacerY.get()>=11 or PlacerX.get() not in Lettre:
        Error('Les coordonnées ne sont pas dans le plateau.')
    elif Joueur==2:
        y=PlacerY.get()
        x=(Lettre.index(PlacerX.get()))+1
        if NbBateauJ2==0:
            Error((NomJoueur2.get(),", vous avez placé tout vos bateaux"))
        elif NbBateauJ2==17:
            if pivoter==0:
                if y+2>=11 or x+1>10:
                    Conflit=1
                else:
                    for k in range(3):
                        if BateauJoueur2[x][y+k]!='0':
                            Conflit=1
                    for k in range(2):
                        if BateauJoueur2[x+1][+k]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le porte avion.")
                else:
                    for k in range(3):
                            PlateauJoueur2.itemconfig(CasesJoueur2[x][y+k],fill='grey')
                    for k in range (2):
                            PlateauJoueur2.itemconfig(CasesJoueur2[x+1][y+k],fill='grey')
            if pivoter==1:
                if PlacerY.get()+1>=11 or x-2<=0 or x+1>11:
                    Conflit=1
                else:
                    for k in range(3):
                        if BateauJoueur2[x-k][y]!='0':
                            Conflit=1
                    for k in range(2):
                        if BateauJoueur2[x-k][y+1]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le porte avion.")
                else:
                    for k in range(3):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x-k][y],fill='grey')
                    for k in range(2):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x-k][y+1],fill='grey')
            if pivoter==2:
                if y-2<=0 or x-1<=0:
                    Conflit=1
                else:
                    for k in range(3):
                        if BateauJoueur2[x][y-k]!='0':
                            Conflit=1
                    for k in range(2):
                        if BateauJoueur2[x-1][y-k]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le porte avion.")
                else:
                    for k in range(3):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x][y-k],fill='grey')
                    for k in range(2):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x-1][y-k],fill='grey')
            if pivoter==3:
                if y-1<=0 or x+2>=11:
                    Conflit=1
                else:
                    for k in range(3):
                        if BateauJoueur2[x+k][y]!='0':
                            Conflit=1
                    for k in range(2):
                        if BateauJoueur2[x+k][y-1]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le porte avion.")
                else:
                    for k in range(3):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x+k][y],fill='grey')
                    for k in range(2):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x+k][y-1],fill='grey')
        elif NbBateauJ2==12:
            if pivoter==0:
                if y+3>11:
                    Conflit=1
                else:
                    for k in range(4):
                        if BateauJoueur2[x][y+k]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le croiseur")
                else:
                    for k in range(4):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x][y+k],fill='grey')
            if pivoter==1:
                if x-3<=0:
                    Conflit=1
                else:
                    for k in range(4):
                        if BateauJoueur2[x-k][y]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le croiseur")
                else:
                    for k in range(4):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x-k][y],fill='grey')
            if pivoter==2:
                if y-3<=0:
                    Conflit=1
                else:
                    for k in range(4):
                        if BateauJoueur2[x][y-k]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le croiseur")
                else:
                    for k in range(4):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x][y-k],fill='grey')
            if pivoter==3:
                if x+3>11:
                    Conflit=1
                else:
                    for k in range(4):
                        if BateauJoueur2[x+k][y]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le croiseur")
                else:
                    for k in range(4):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x+k][y],fill='grey')
        elif NbBateauJ2==8 or NbBateauJ2==5:
            if pivoter==0:
                if y+2>11:
                    Conflit=1
                else:
                    for k in range(3):
                        if BateauJoueur2[x][y+k]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le sous marin")
                else:
                    for k in range(3):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x][y+k],fill='grey')
            if pivoter==1:
                if x-2<=0:
                    Conflit=1
                else:
                    for k in range(3):
                        if BateauJoueur2[x-k][y]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le sous marin")
                else:
                    for k in range(3):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x-k][y],fill='grey')
            if pivoter==2:
                if y-2<=0:
                    Conflit=1
                else:
                    for k in range(3):
                        if BateauJoueur2[x][y-k]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le sous marin")
                else:
                    for k in range(3):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x][y-k],fill='grey')
            if pivoter==3:
                if x+2>11:
                    Conflit=1
                else:
                    for k in range(3):
                        if BateauJoueur2[x+k][y]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le sous marin")
                else:
                    for k in range(3):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x+k][y],fill='grey')
        elif NbBateauJ2==2:
            if pivoter==0:
                if y+1>11:
                    Conflit=1
                else:
                    for k in range(2):
                        if BateauJoueur2[x][y+k]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le torpilleur")
                else:
                    for k in range(2):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x][y+k],fill='grey')
            if pivoter==1:
                if x-1<=0:
                    Conflit=1
                else:
                    for k in range(2):
                        if BateauJoueur2[x-k][y]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le torpilleur")
                else:
                    for k in range(2):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x-k][y],fill='grey')
            if pivoter==2:
                if y-1<=0:
                    Conflit=1
                else:
                    for k in range(2):
                        if BateauJoueur2[x][y-k]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le torpilleur")
                else:
                    for k in range(2):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x][y-k],fill='grey')
            if pivoter==3:
                if x+1>11:
                    Conflit=1
                else:
                    for k in range(2):
                        if BateauJoueur2[x+k][y]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le torpilleur")
                else:
                    for k in range(2):
                        PlateauJoueur2.itemconfig(CasesJoueur2[x+k][y],fill='grey')


    else:
        y=PlacerY.get()
        x=(Lettre.index(PlacerX.get()))+1
        if NbBateauJ1==0:
            Error((NomJoueur1.get(),", vous avez placé tout vos bateaux"))
        elif NbBateauJ1==17:
            if pivoter==0:
                if PlacerY.get()+2>=11 or x+1>10:
                    Conflit=1
                else:
                    for k in range(3):
                        if BateauJoueur1[x][PlacerY.get()+k]!='0':
                            Conflit=1
                    for k in range(2):
                        if BateauJoueur1[x+1][PlacerY.get()+k]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le porte avion.")
                else:
                    for k in range(3):
                            PlateauJoueur1.itemconfig(CasesJoueur1[x][y+k],fill='grey')
                    for k in range (2):
                            PlateauJoueur1.itemconfig(CasesJoueur1[x+1][y+k],fill='grey')
            if pivoter==1:
                if PlacerY.get()+1>=11 or x-2<=0 or x+1>11:
                    Conflit=1
                else:
                    for k in range(3):
                        if BateauJoueur1[x-k][y]!='0':
                            Conflit=1
                    for k in range(2):
                        if BateauJoueur1[x-k][y+1]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le porte avion.")
                else:
                    for k in range(3):
                        PlateauJoueur1.itemconfig(CasesJoueur1[x-k][y],fill='grey')
                    for k in range(2):
                        PlateauJoueur1.itemconfig(CasesJoueur1[x-k][y+1],fill='grey')
            if pivoter==2:
                if  PlacerY.get()-2<=0 or x-1<=0:
                    Conflit=1
                else:
                    for k in range(3):
                        if BateauJoueur1[x][PlacerY.get()-k]!='0':
                            Conflit=1
                    for k in range(2):
                        if BateauJoueur1[x-1][PlacerY.get()-k]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le porte avion.")
                else:
                    for k in range(3):
                        PlateauJoueur1.itemconfig(CasesJoueur2[x][y-k],fill='grey')
                    for k in range(2):
                        PlateauJoueur1.itemconfig(CasesJoueur2[x-1][y-k],fill='grey')
            if pivoter==3:
                if PlacerY.get()-1<=0 or x+2>=11:
                    Conflit=1
                else:
                    for k in range(3):
                        if BateauJoueur1[x+k][y]!='0':
                            Conflit=1
                    for k in range(2):
                        if BateauJoueur1[x+k][y-1]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le porte avion.")
                else:
                    for k in range(3):
                        PlateauJoueur1.itemconfig(CasesJoueur1[x+k][y],fill='grey')
                    for k in range(2):
                        PlateauJoueur1.itemconfig(CasesJoueur1[x+k][y-1],fill='grey')
        elif NbBateauJ1==12:
            if pivoter==0:
                if y+3>11:
                    Conflit=1
                else:
                    for k in range(4):
                        if BateauJoueur1[x][y+k]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le croiseur")
                else:
                    for k in range(4):
                        PlateauJoueur1.itemconfig(CasesJoueur1[x][y+k],fill='grey')
            if pivoter==1:
                if x-3<=0:
                    Conflit=1
                else:
                    for k in range(4):
                        if BateauJoueur1[x-k][y]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le croiseur")
                else:
                    for k in range(4):
                        PlateauJoueur1.itemconfig(CasesJoueur1[x-k][y],fill='grey')
            if pivoter==2:
                if y-3<=0:
                    Conflit=1
                else:
                    for k in range(4):
                        if BateauJoueur1[x][y-k]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le croiseur")
                else:
                    for k in range(4):
                        PlateauJoueur1.itemconfig(CasesJoueur1[x][y-k],fill='grey')
            if pivoter==3:
                if x+3>11:
                    Conflit=1
                else:
                    for k in range(4):
                        if BateauJoueur1[x+k][y]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le croiseur")
                else:
                    for k in range(4):
                        PlateauJoueur1.itemconfig(CasesJoueur1[x+k][y],fill='grey')
        elif NbBateauJ1==8 or NbBateauJ1==5:
            if pivoter==0:
                if y+2>11:
                    Conflit=1
                else:
                    for k in range(3):
                        if BateauJoueur1[x][y+k]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le croiseur")
                else:
                    for k in range(3):
                        PlateauJoueur1.itemconfig(CasesJoueur1[x][y+k],fill='grey')
            if pivoter==1:
                if x-2<=0:
                    Conflit=1
                else:
                    for k in range(3):
                        if BateauJoueur1[x-k][y]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le croiseur")
                else:
                    for k in range(3):
                        PlateauJoueur1.itemconfig(CasesJoueur1[x-k][y],fill='grey')
            if pivoter==2:
                if y-2<=0:
                    Conflit=1
                else:
                    for k in range(3):
                        if BateauJoueur1[x][y-k]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le croiseur")
                else:
                    for k in range(3):
                        PlateauJoueur1.itemconfig(CasesJoueur1[x][y-k],fill='grey')
            if pivoter==3:
                if x+2>11:
                    Conflit=1
                else:
                    for k in range(3):
                        if BateauJoueur1[x+k][y]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le croiseur")
                else:
                    for k in range(3):
                        PlateauJoueur1.itemconfig(CasesJoueur1[x+k][y],fill='grey')
        elif NbBateauJ1==2:
            if pivoter==0:
                if y+1>11:
                    Conflit=1
                else:
                    for k in range(2):
                        if BateauJoueur1[x][y+k]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le torpilleur")
                else:
                    for k in range(2):
                        PlateauJoueur1.itemconfig(CasesJoueur1[x][y+k],fill='grey')
            if pivoter==1:
                if x-1<=0:
                    Conflit=1
                else:
                    for k in range(2):
                        if BateauJoueur1[x-k][y]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le torpilleur")
                else:
                    for k in range(2):
                        PlateauJoueur1.itemconfig(CasesJoueur1[x-k][y],fill='grey')
            if pivoter==2:
                if y-1<=0:
                    Conflit=1
                else:
                    for k in range(2):
                        if BateauJoueur1[x][y-k]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le torpilleur")
                else:
                    for k in range(2):
                        PlateauJoueur1.itemconfig(CasesJoueur1[x][y-k],fill='grey')
            if pivoter==3:
                if x+1>11:
                    Conflit=1
                else:
                    for k in range(2):
                        if BateauJoueur1[x+k][y]!='0':
                            Conflit=1
                if Conflit==1:
                    Error("Il n'y a pas la place pour le torpilleur")
                else:
                    for k in range(2):
                        PlateauJoueur1.itemconfig(CasesJoueur1[x+k][y],fill='grey')
    PreJoueur,PreX,PreY,PreNbBateauJ1,PreNbBateauJ2,PreConflit,PrePivoter=Joueur,PlacerX.get(),PlacerY.get(),NbBateauJ1,NbBateauJ2,Conflit,pivoter
    PremierePrevisualisation=1


def Previsualisation3():
    global PreX, PreY, PreJoueur, PreNbBateauJ2, PreNbBateauJ1,PreConflit,PrePivoter, PremierePrevisualisation, PreConflit
    if PremierePrevisualisation==1 and PreConflit==0:
        PreConflit=0
        if PreY<=0 or PreY>=11 or PreX not in Lettre:
            LabelError.grid_forget()
        elif PreJoueur==2:
            x=(Lettre.index(PreX))+1
            if PreNbBateauJ2==0:
                Error((NomJoueur2.get(),", vous avez placé tout vos bateaux"))
            elif PreNbBateauJ2==17:
                if PrePivoter==0:
                    for k in range(3):
                        if BateauJoueur2[x][PreY+k]!='0':
                            PreConflit=1
                    for k in range(2):
                        if BateauJoueur2[x+1][PreY+k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(3):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x][PreY+k],fill='white')
                        for k in range (2):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x+1][PreY+k],fill='white')
                if PrePivoter==1:
                    for k in range(3):
                        if BateauJoueur2[x-k][PreY]!='0':
                            PreConflit=1
                    for k in range(2):
                        if BateauJoueur2[x-k][PreY+1]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(3):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x-k][PreY],fill='white')
                        for k in range (2):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x-k][PreY+1],fill='white')
                if PrePivoter==2:
                    for k in range(3):
                        if BateauJoueur2[x][PreY-k]!='0':
                            PreConflit=1
                    for k in range(2):
                        if BateauJoueur2[x-1][PreY-k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(3):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x][PreY-k],fill='white')
                        for k in range (2):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x-1][PreY-k],fill='white')
                if PrePivoter==3:
                    for k in range(3):
                        if BateauJoueur2[x+k][PreY]!='0':
                            PreConflit=1
                    for k in range(2):
                        if BateauJoueur2[x+k][PreY-1]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(3):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x+k][PreY],fill='white')
                        for k in range (2):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x+k][PreY-1],fill='white')
            elif NbBateauJ2==12:
                if PrePivoter==0:
                    for k in range(4):
                        if BateauJoueur2[x][PreY+k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(4):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x][PreY+k],fill='white')
                if PrePivoter==1:
                    for k in range(4):
                        if BateauJoueur2[x-k][PreY]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(4):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x-k][PreY],fill='white')
                if PrePivoter==2:
                    for k in range(4):
                        if BateauJoueur2[x][PreY-k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(4):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x][PreY-k],fill='white')
                if PrePivoter==3:
                    for k in range(4):
                        if BateauJoueur2[x][PreY+k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(4):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x+k][PreY],fill='white')
            elif NbBateauJ2==8 or NbBateauJ2==5:
                if PrePivoter==0:
                    for k in range(3):
                        if BateauJoueur2[x][PreY+k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(3):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x][PreY+k],fill='white')
                if PrePivoter==1:
                    for k in range(3):
                        if BateauJoueur2[x-k][PreY]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(3):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x-k][PreY],fill='white')
                if PrePivoter==2:
                    for k in range(3):
                        if BateauJoueur2[x][PreY-k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(3):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x][PreY-k],fill='white')
                if PrePivoter==3:
                    for k in range(3):
                        if BateauJoueur2[x][PreY+k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(3):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x+k][PreY],fill='white')
            elif NbBateauJ2==2:
                if PrePivoter==0:
                    for k in range(2):
                        if BateauJoueur2[x][PreY+k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(2):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x][PreY+k],fill='white')
                if PrePivoter==1:
                    for k in range(2):
                        if BateauJoueur2[x-k][PreY]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(2):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x-k][PreY],fill='white')
                if PrePivoter==2:
                    for k in range(2):
                        if BateauJoueur2[x][PreY-k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(2):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x][PreY-k],fill='white')
                if PrePivoter==3:
                    for k in range(2):
                        if BateauJoueur2[x][PreY+k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(2):
                                PlateauJoueur2.itemconfig(CasesJoueur2[x+k][PreY],fill='white')

        else:
            x=(Lettre.index(PreX))+1
            if PreNbBateauJ1==0:
                Error((NomJoueur1.get(),", vous avez placé tout vos bateaux"))
            elif PreNbBateauJ1==17:
                if PrePivoter==0:
                    for k in range(3):
                        if BateauJoueur1[x][PreY+k]!='0':
                            PreConflit=1
                    for k in range(2):
                        if BateauJoueur1[x+1][PreY+k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(3):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x][PreY+k],fill='white')
                        for k in range (2):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x+1][PreY+k],fill='white')
                if PrePivoter==1:
                    for k in range(3):
                        if BateauJoueur1[x-k][PreY]!='0':
                            PreConflit=1
                    for k in range(2):
                        if BateauJoueur1[x-k][PreY+1]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(3):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x-k][PreY],fill='white')
                        for k in range (2):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x-k][PreY+1],fill='white')
                if PrePivoter==2:
                    for k in range(3):
                        if BateauJoueur1[x][PreY-k]!='0':
                            PreConflit=1
                    for k in range(2):
                        if BateauJoueur1[x-1][PreY-k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(3):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x][PreY-k],fill='white')
                        for k in range (2):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x-1][PreY-k],fill='white')
                if PrePivoter==3:
                    for k in range(3):
                        if BateauJoueur1[x+k][PreY]!='0':
                            PreConflit=1
                    for k in range(2):
                        if BateauJoueur1[x+k][PreY-1]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(3):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x+k][PreY],fill='white')
                        for k in range (2):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x+k][PreY-1],fill='white')
            elif NbBateauJ1==12:
                if PrePivoter==0:
                    for k in range(4):
                        if BateauJoueur1[x][PreY+k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(4):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x][PreY+k],fill='white')
                if PrePivoter==1:
                    for k in range(4):
                        if BateauJoueur1[x-k][PreY]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(4):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x-k][PreY],fill='white')
                if PrePivoter==2:
                    for k in range(4):
                        if BateauJoueur1[x][PreY-k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(4):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x][PreY-k],fill='white')
                if PrePivoter==3:
                    for k in range(4):
                        if BateauJoueur1[x+k][PreY]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(4):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x+k][PreY],fill='white')
            elif NbBateauJ1==8 or NbBateauJ1==5:
                if PrePivoter==0:
                    for k in range(3):
                        if BateauJoueur1[x][PreY+k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(3):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x][PreY+k],fill='white')
                if PrePivoter==1:
                    for k in range(3):
                        if BateauJoueur1[x-k][PreY]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(3):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x-k][PreY],fill='white')
                if PrePivoter==2:
                    for k in range(3):
                        if BateauJoueur1[x][PreY-k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(3):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x][PreY-k],fill='white')
                if PrePivoter==3:
                    for k in range(3):
                        if BateauJoueur1[x+k][PreY]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(3):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x+k][PreY],fill='white')
            elif NbBateauJ1==2:
                if PrePivoter==0:
                    for k in range(2):
                        if BateauJoueur1[x][PreY+k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(2):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x][PreY+k],fill='white')
                if PrePivoter==1:
                    for k in range(2):
                        if BateauJoueur1[x-k][PreY]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(2):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x-k][PreY],fill='white')
                if PrePivoter==2:
                    for k in range(2):
                        if BateauJoueur1[x][PreY-k]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(2):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x][PreY-k],fill='white')
                if PrePivoter==3:
                    for k in range(2):
                        if BateauJoueur1[x+k][PreY]!='0':
                            PreConflit=1
                    if PreConflit==0:
                        for k in range(2):
                                PlateauJoueur1.itemconfig(CasesJoueur1[x+k][PreY],fill='white')



def Placer():
    global Joueur , NbBateauJ1 , NbBateauJ2
    Conflit=0
    LabelError.pack_forget()
    if PlacerY.get()<=0 or PlacerY.get()>=11 or PlacerX.get() not in Lettre:
        Error('Les coordonnées ne sont pas dans le plateau.')
    elif Joueur==2:
        y=PlacerY.get()
        x=(Lettre.index(PlacerX.get()))+1  #PlacerX.get()+1 car le .index commence à 0
        if NbBateauJ2==0 : #Code pour le joueur 2
            Error((NomJoueur2.get(),", vous avez placé tout vos bateaux"))
        elif BateauJoueur2[x][y]=='0':
            if NbBateauJ2==17:
                if pivoter==0:
                    if y+2>=11 or x+1>10:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur2[x][y+k]!='0':
                                Conflit=1
                        for k in range(2):
                            if BateauJoueur2[x+1][y+k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le porte avion.")
                    else:
                        for k in range(3):
                            PlateauJoueur2.itemconfig(CasesJoueur2[x][y+k],fill='black')
                            BateauJoueur2[x][y+k]='5'
                        for k in range (2):
                            PlateauJoueur2.itemconfig(CasesJoueur2[x+1][y+k],fill='black')
                            BateauJoueur2[x+1][y+k]='5'
                        LabelBateau.config(text='Veuillez placer le : croiseur (4 points de vie)')
                        NbBateauJ2=NbBateauJ2-5
                if pivoter==1:
                    if y+1>=11 or x-2>10:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur2[x-k][y]!='0':
                                Conflit=1
                        for k in range(2):
                            if BateauJoueur2[x-k][y+1]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le porte avion.")
                    else:
                        for k in range(3):
                            PlateauJoueur2.itemconfig(CasesJoueur2[x-k][y],fill='black')
                            BateauJoueur2[x-k][y]='5'
                        for k in range (2):
                            PlateauJoueur2.itemconfig(CasesJoueur2[x-k][y+1],fill='black')
                            BateauJoueur2[x-k][y+1]='5'
                        LabelBateau.config(text='Veuillez placer le : croiseur (4 points de vie)')
                        NbBateauJ2=NbBateauJ2-5
                if pivoter==2:
                    if y-2>=11 or x-1>10:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur2[x][y-k]!='0':
                                Conflit=1
                        for k in range(2):
                            if BateauJoueur2[x-1][y-k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le porte avion.")
                    else:
                        for k in range(3):
                            PlateauJoueur2.itemconfig(CasesJoueur2[x][y-k],fill='black')
                            BateauJoueur2[x][y-k]='5'
                        for k in range (2):
                            PlateauJoueur2.itemconfig(CasesJoueur2[x-1][y-k],fill='black')
                            BateauJoueur2[x-1][y-k]='5'
                        LabelBateau.config(text='Veuillez placer le : croiseur (4 points de vie)')
                        NbBateauJ2=NbBateauJ2-5
                if pivoter==3:
                    if y-1>=11 or x+2>10:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur2[x+k][y]!='0':
                                Conflit=1
                        for k in range(2):
                            if BateauJoueur2[x+k][y-1]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le porte avion.")
                    else:
                        for k in range(3):
                            PlateauJoueur2.itemconfig(CasesJoueur2[x+k][y],fill='black')
                            BateauJoueur2[x+k][y]='5'
                        for k in range (2):
                            PlateauJoueur2.itemconfig(CasesJoueur2[x+k][y-1],fill='black')
                            BateauJoueur2[x+k][y-1]='5'
                        LabelBateau.config(text='Veuillez placer le : croiseur (4 points de vie)')
                        NbBateauJ2=NbBateauJ2-5
            elif NbBateauJ2==12:
                if pivoter==0:
                    if y+3>=11:
                        Conflit=1
                    else:
                        for k in range(4):
                            if BateauJoueur2[x][y+k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le croiseur.")
                    else:
                        for k in range(4) :
                            PlateauJoueur2.itemconfig(CasesJoueur2[x][y+k],fill='black')
                            BateauJoueur2[x][y+k]='4'
                        LabelBateau.config(text='Veuillez placer les : deux sous-marins (3 points de vie chacun)')
                        NbBateauJ2=NbBateauJ2-4
                elif pivoter==1:
                    if x-3<=0:
                        Conflit=1
                    else:
                        for k in range(4):
                            if BateauJoueur2[x-k][y]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le croiseur.")
                    else:
                        for k in range(4) :
                            PlateauJoueur2.itemconfig(CasesJoueur2[x-k][y],fill='black')
                            BateauJoueur2[x-k][y]='4'
                        LabelBateau.config(text='Veuillez placer les : deux sous-marins (3 points de vie chacun)')
                        NbBateauJ2=NbBateauJ2-4
                elif pivoter==2:
                    if y-3<=0:
                        Conflit=1
                    else:
                        for k in range(4):
                            if BateauJoueur2[x][y-k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le croiseur.")
                    else:
                        for k in range(4) :
                            PlateauJoueur2.itemconfig(CasesJoueur2[x][y-k],fill='black')
                            BateauJoueur2[x][y-k]='4'
                        LabelBateau.config(text='Veuillez placer les : deux sous-marins (3 points de vie chacun)')
                        NbBateauJ2=NbBateauJ2-4
                elif pivoter==3:
                    if x+3>11:
                        Conflit=1
                    else:
                        for k in range(4):
                            if BateauJoueur2[x+k][y]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le croiseur.")
                    else:
                        for k in range(4) :
                            PlateauJoueur2.itemconfig(CasesJoueur2[x+k][y],fill='black')
                            BateauJoueur2[x+k][y]='4'
                        LabelBateau.config(text='Veuillez placer les : deux sous-marins (3 points de vie chacun)')
                        NbBateauJ2=NbBateauJ2-4
            elif NbBateauJ2==8:
                if pivoter==0:
                    if y+2>11:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur2[x][y+k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le sous marin.")
                    else:
                        for k in range(3) :
                            PlateauJoueur2.itemconfig(CasesJoueur2[x][y+k],fill='black')
                            BateauJoueur2[x][y+k]='2'
                        NbBateauJ2=NbBateauJ2-3
                elif pivoter==1:
                    if x-2<=0:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur2[x-k][y]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le sous marin.")
                    else:
                        for k in range(3) :
                            PlateauJoueur2.itemconfig(CasesJoueur2[x-k][y],fill='black')
                            BateauJoueur2[x-k][y]='2'
                        NbBateauJ2=NbBateauJ2-3
                elif pivoter==2:
                    if y-2<=0:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur2[x][y-k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le sous marin.")
                    else:
                        for k in range(3) :
                            PlateauJoueur2.itemconfig(CasesJoueur2[x][y-k],fill='black')
                            BateauJoueur2[x][y-k]='2'
                        NbBateauJ2=NbBateauJ2-3
                elif pivoter==3:
                    if x+2>11:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur2[x+k][y]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le sous marin.")
                    else:
                        for k in range(3) :
                            PlateauJoueur2.itemconfig(CasesJoueur2[x+k][y],fill='black')
                            BateauJoueur2[x+k][y]='2'
                        NbBateauJ2=NbBateauJ2-3
            elif NbBateauJ2==5:
                if pivoter==0:
                    if y+2>11:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur2[x][y+k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le sous marin.")
                    else:
                        for k in range(3) :
                            PlateauJoueur2.itemconfig(CasesJoueur2[x][y+k],fill='black')
                            BateauJoueur2[x][y+k]='3'
                        LabelBateau.config(text='Veuillez placer le : torpilleur (2 points de vie)')
                        NbBateauJ2=NbBateauJ2-3
                elif pivoter==1:
                    if x-2<=0:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur2[x-k][y]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le sous marin.")
                    else:
                        for k in range(3) :
                            PlateauJoueur2.itemconfig(CasesJoueur2[x-k][y],fill='black')
                            BateauJoueur2[x-k][y]='3'
                        LabelBateau.config(text='Veuillez placer le : torpilleur (2 points de vie)')
                        NbBateauJ2=NbBateauJ2-3
                elif pivoter==2:
                    if y-2<=0:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur2[x][y-k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le sous marin.")
                    else:
                        for k in range(3) :
                            PlateauJoueur2.itemconfig(CasesJoueur2[x][y-k],fill='black')
                            BateauJoueur2[x][y-k]='3'
                        LabelBateau.config(text='Veuillez placer le : torpilleur (2 points de vie)')
                        NbBateauJ2=NbBateauJ2-3
                elif pivoter==3:
                    if x+2>11:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur2[x+k][y]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le sous marin.")
                    else:
                        for k in range(3) :
                            PlateauJoueur2.itemconfig(CasesJoueur2[x+k][y],fill='black')
                            BateauJoueur2[x+k][y]='3'
                        LabelBateau.config(text='Veuillez placer le : torpilleur (2 points de vie)')
                        NbBateauJ2=NbBateauJ2-3
            elif NbBateauJ2==2:
                if pivoter==0:
                    if y+1>11:
                        Conflit=1
                    else:
                        for k in range(2):
                            if BateauJoueur2[x][y+k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le torpilleur.")
                    else:
                        for k in range(2) :
                            PlateauJoueur2.itemconfig(CasesJoueur2[x][y+k],fill='black')
                            BateauJoueur2[x][y+k]='1'
                        NbBateauJ2=NbBateauJ2-2
                        LabelBateau.pack_forget()
                        fenetrePlateau.after(2000, Plateau1)
                elif pivoter==1:
                    if x-1<=0:
                        Conflit=1
                    else:
                        for k in range(2):
                            if BateauJoueur2[x-k][y]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le torpilleur.")
                    else:
                        for k in range(2) :
                            PlateauJoueur2.itemconfig(CasesJoueur2[x-k][y],fill='black')
                            BateauJoueur2[x-k][y]='1'
                        NbBateauJ2=NbBateauJ2-2
                        LabelBateau.pack_forget()
                        fenetrePlateau.after(2000, Plateau1)
                elif pivoter==2:
                    if y-1<=0:
                        Conflit=1
                    else:
                        for k in range(2):
                            if BateauJoueur2[x][y-k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le torpilleur.")
                    else:
                        for k in range(2) :
                            PlateauJoueur2.itemconfig(CasesJoueur2[x][y-k],fill='black')
                            BateauJoueur2[x][y-k]='1'
                        NbBateauJ2=NbBateauJ2-2
                        LabelBateau.pack_forget()
                        fenetrePlateau.after(2000, Plateau1)
                elif pivoter==3:
                    if x+1>11:
                        Conflit=1
                    else:
                        for k in range(2):
                            if BateauJoueur2[x+k][y]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le torpilleur.")
                    else:
                        for k in range(2) :
                            PlateauJoueur2.itemconfig(CasesJoueur2[x+k][y],fill='black')
                            BateauJoueur2[x+k][y]='1'
                        NbBateauJ2=NbBateauJ2-2
                        LabelBateau.pack_forget()
                        fenetrePlateau.after(2000, Plateau1)

    else:
        y=PlacerY.get()
        x=(Lettre.index(PlacerX.get()))+1  #PlacerX.get()+1 car le .index commence à 0
        if NbBateauJ1==0 : #Code pour le joueur 1
            Error((NomJoueur1.get(),", vous avez placé tout vos bateaux"))
        elif BateauJoueur1[x][y]=='0':
            if NbBateauJ1==17:
                if pivoter==0:
                    if y+2>=11 or x+1>10:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur1[x][y+k]!='0':
                                Conflit=1
                        for k in range(2):
                            if BateauJoueur1[x+1][y+k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le porte avion.")
                    else:
                        for k in range(3):
                            PlateauJoueur1.itemconfig(CasesJoueur1[x][y+k],fill='black')
                            BateauJoueur1[x][y+k]='5'
                        for k in range (2):
                            PlateauJoueur1.itemconfig(CasesJoueur1[x+1][y+k],fill='black')
                            BateauJoueur1[x+1][y+k]='5'
                        LabelBateau.config(text='Veuillez placer le : croiseur (4 points de vie)')
                        NbBateauJ1=NbBateauJ1-5
                if pivoter==1:
                    if y+1>=11 or x-2>10:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur1[x-k][y]!='0':
                                Conflit=1
                        for k in range(2):
                            if BateauJoueur1[x-k][y+1]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le porte avion.")
                    else:
                        for k in range(3):
                            PlateauJoueur1.itemconfig(CasesJoueur1[x-k][y],fill='black')
                            BateauJoueur1[x-k][y]='5'
                        for k in range (2):
                            PlateauJoueur1.itemconfig(CasesJoueur1[x-k][y+1],fill='black')
                            BateauJoueur1[x-k][y+1]='5'
                        LabelBateau.config(text='Veuillez placer le : croiseur (4 points de vie)')
                        NbBateauJ1=NbBateauJ1-5
                if pivoter==2:
                    if y-2>=11 or x-1>10:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur1[x][y-k]!='0':
                                Conflit=1
                        for k in range(2):
                            if BateauJoueur1[x-1][y-k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le porte avion.")
                    else:
                        for k in range(3):
                            PlateauJoueur1.itemconfig(CasesJoueur1[x][y-k],fill='black')
                            BateauJoueur1[x][y-k]='5'
                        for k in range (2):
                            PlateauJoueur1.itemconfig(CasesJoueur1[x-1][y-k],fill='black')
                            BateauJoueur1[x-1][y-k]='5'
                        LabelBateau.config(text='Veuillez placer le : croiseur (4 points de vie)')
                        NbBateauJ1=NbBateauJ1-5
                if pivoter==3:
                    if y-1>=11 or x+2>10:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur1[x+k][y]!='0':
                                Conflit=1
                        for k in range(2):
                            if BateauJoueur1[x+k][y-1]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le porte avion.")
                    else:
                        for k in range(3):
                            PlateauJoueur1.itemconfig(CasesJoueur1[x+k][y],fill='black')
                            BateauJoueur1[x+k][y]='5'
                        for k in range (2):
                            PlateauJoueur1.itemconfig(CasesJoueur1[x+k][y-1],fill='black')
                            BateauJoueur1[x+k][y-1]='5'
                        LabelBateau.config(text='Veuillez placer le : croiseur (4 points de vie)')
                        NbBateauJ1=NbBateauJ1-5
            elif NbBateauJ1==12:
                if pivoter==0:
                    if y+3>=11:
                        Conflit=1
                    else:
                        for k in range(4):
                            if BateauJoueur1[x][y+k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le croiseur.")
                    else:
                        for k in range(4) :
                            PlateauJoueur1.itemconfig(CasesJoueur1[x][y+k],fill='black')
                            BateauJoueur1[x][y+k]='4'
                        LabelBateau.config(text='Veuillez placer les : deux sous-marins (3 points de vie chacun)')
                        NbBateauJ1=NbBateauJ1-4
                elif pivoter==1:
                    if x-3<=0:
                        Conflit=1
                    else:
                        for k in range(4):
                            if BateauJoueur1[x-k][y]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le croiseur.")
                    else:
                        for k in range(4) :
                            PlateauJoueur1.itemconfig(CasesJoueur1[x-k][y],fill='black')
                            BateauJoueur1[x-k][y]='4'
                        LabelBateau.config(text='Veuillez placer les : deux sous-marins (3 points de vie chacun)')
                        NbBateauJ1=NbBateauJ1-4
                elif pivoter==2:
                    if y-3<=0:
                        Conflit=1
                    else:
                        for k in range(4):
                            if BateauJoueur1[x][y-k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le croiseur.")
                    else:
                        for k in range(4) :
                            PlateauJoueur1.itemconfig(CasesJoueur1[x][y-k],fill='black')
                            BateauJoueur1[x][y-k]='4'
                        LabelBateau.config(text='Veuillez placer les : deux sous-marins (3 points de vie chacun)')
                        NbBateauJ1=NbBateauJ1-4
                elif pivoter==3:
                    if x+3>11:
                        Conflit=1
                    else:
                        for k in range(4):
                            if BateauJoueur1[x+k][y]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le croiseur.")
                    else:
                        for k in range(4) :
                            PlateauJoueur1.itemconfig(CasesJoueur1[x+k][y],fill='black')
                            BateauJoueur1[x+k][y]='4'
                        LabelBateau.config(text='Veuillez placer les : deux sous-marins (3 points de vie chacun)')
                        NbBateauJ1=NbBateauJ1-4
            elif NbBateauJ1==8:
                if pivoter==0:
                    if y+2>11:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur1[x][y+k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le sous marin.")
                    else:
                        for k in range(3) :
                            PlateauJoueur1.itemconfig(CasesJoueur1[x][y+k],fill='black')
                            BateauJoueur1[x][y+k]='2'
                        NbBateauJ1=NbBateauJ1-3
                elif pivoter==1:
                    if x-2<=0:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur1[x-k][y]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le sous marin.")
                    else:
                        for k in range(3) :
                            PlateauJoueur1.itemconfig(CasesJoueur1[x-k][y],fill='black')
                            BateauJoueur1[x-k][y]='2'
                        NbBateauJ1=NbBateauJ1-3
                elif pivoter==2:
                    if y-2<=0:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur1[x][y-k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le sous marin.")
                    else:
                        for k in range(3) :
                            PlateauJoueur1.itemconfig(CasesJoueur1[x][y-k],fill='black')
                            BateauJoueur1[x][y-k]='2'
                        NbBateauJ1=NbBateauJ1-3
                elif pivoter==3:
                    if x+2>11:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur1[x+k][y]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le sous marin.")
                    else:
                        for k in range(3) :
                            PlateauJoueur1.itemconfig(CasesJoueur1[x+k][y],fill='black')
                            BateauJoueur1[x+k][y]='2'
                        NbBateauJ1=NbBateauJ1-3
            elif NbBateauJ1==5:
                if pivoter==0:
                    if y+2>11:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur1[x][y+k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le sous marin.")
                    else:
                        for k in range(3) :
                            PlateauJoueur1.itemconfig(CasesJoueur1[x][y+k],fill='black')
                            BateauJoueur1[x][y+k]='3'
                        LabelBateau.config(text='Veuillez placer le : torpilleur (2 points de vie)')
                        NbBateauJ1=NbBateauJ1-3
                elif pivoter==1:
                    if x-2<=0:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur1[x-k][y]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le sous marin.")
                    else:
                        for k in range(3) :
                            PlateauJoueur1.itemconfig(CasesJoueur1[x-k][y],fill='black')
                            BateauJoueur1[x-k][y]='3'
                        LabelBateau.config(text='Veuillez placer le : torpilleur (2 points de vie)')
                        NbBateauJ1=NbBateauJ1-3
                elif pivoter==2:
                    if y-2<=0:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur1[x][y-k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le sous marin.")
                    else:
                        for k in range(3) :
                            PlateauJoueur1.itemconfig(CasesJoueur1[x][y-k],fill='black')
                            BateauJoueur1[x][y-k]='3'
                        LabelBateau.config(text='Veuillez placer le : torpilleur (2 points de vie)')
                        NbBateauJ1=NbBateauJ1-3
                elif pivoter==3:
                    if x+2>11:
                        Conflit=1
                    else:
                        for k in range(3):
                            if BateauJoueur1[x+k][y]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le sous marin.")
                    else:
                        for k in range(3) :
                            PlateauJoueur1.itemconfig(CasesJoueur1[x+k][y],fill='black')
                            BateauJoueur1[x+k][y]='3'
                        LabelBateau.config(text='Veuillez placer le : torpilleur (2 points de vie)')
                        NbBateauJ1=NbBateauJ1-3
            elif NbBateauJ1==2:
                if pivoter==0:
                    if y+1>11:
                        Conflit=1
                    else:
                        for k in range(2):
                            if BateauJoueur1[x][y+k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le torpilleur.")
                    else:
                        for k in range(2) :
                            PlateauJoueur1.itemconfig(CasesJoueur1[x][y+k],fill='black')
                            BateauJoueur1[x][y+k]='1'
                        NbBateauJ1=NbBateauJ1-2
                        LabelBateau.pack_forget()
                        fenetrePlateau.after(2000, Plateau2)
                elif pivoter==1:
                    if x-1<=0:
                        Conflit=1
                    else:
                        for k in range(2):
                            if BateauJoueur1[x-k][y]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le torpilleur.")
                    else:
                        for k in range(2) :
                            PlateauJoueur1.itemconfig(CasesJoueur1[x-k][y],fill='black')
                            BateauJoueur1[x-k][y]='1'
                        NbBateauJ1=NbBateauJ1-2
                        LabelBateau.pack_forget()
                        fenetrePlateau.after(2000, Plateau2)
                elif pivoter==2:
                    if y-1<=0:
                        Conflit=1
                    else:
                        for k in range(2):
                            if BateauJoueur1[x][y-k]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le torpilleur.")
                    else:
                        for k in range(2) :
                            PlateauJoueur1.itemconfig(CasesJoueur1[x][y-k],fill='black')
                            BateauJoueur1[x][y-k]='1'
                        NbBateauJ1=NbBateauJ1-2
                        LabelBateau.pack_forget()
                        fenetrePlateau.after(2000, Plateau2)
                elif pivoter==3:
                    if x+1>11:
                        Conflit=1
                    else:
                        for k in range(2):
                            if BateauJoueur1[x+k][y]!='0':
                                Conflit=1
                    if Conflit==1:
                        Error("Il n'y a pas la place pour le torpilleur.")
                    else:
                        for k in range(2) :
                            PlateauJoueur1.itemconfig(CasesJoueur1[x+k][y],fill='black')
                            BateauJoueur1[x+k][y]='1'
                        NbBateauJ1=NbBateauJ1-2
                        LabelBateau.pack_forget()
                        fenetrePlateau.after(2000, Plateau2)
    if NbBateauJ1==0 and NbBateauJ2==0:
        fenetrePlateau.after(2000,SwitchPlacerAttaquer)

def SwitchPlacerAttaquer():
    global NbBateauJ1, NbBateauJ2, Switch
    fenetreCommande1.pack_forget()
    fenetreCommande2.pack()
    for x in range(1,11):
       for y in range(1,11):
            PlateauJoueur1.itemconfig(CasesJoueur1[x][y],fill='white')
            PlateauJoueur2.itemconfig(CasesJoueur2[x][y],fill='white')
    NbBateauJ1,NbBateauJ2=17,17
    BoutonAfficher.pack(side=BOTTOM)
    Switch=1

def Pivoter():
    global pivoter
    pivoter=pivoter+1
    if pivoter==4:
        pivoter=0
    Previsualisation2()

def Debut():
    global Joueur, PreJoueur
    fenetreDebut.pack_forget()
    fenetrePlateau.pack()
    Joueur=randint(1,2)
    if Joueur==1:
        Plateau1()
    else:
        Plateau2()
    fenetreCommande1.pack()

def fin():
    global fin1, fin2
    BoutonAfficher.pack_forget()
    if fin1==17 or fin2==17:
        if fin1==-17:
            LabelGagnant.config(text=('Bravo !',NomJoueur2.get(),'a gagné la partie !'))
            LabelGagnant.pack()
        else :
            LabelGagnant.config(text=('Bravo !',NomJoueur1.get(),'a gagné la partie !'))
            LabelGagnant.pack()
    fenetrePlateau.pack_forget()
    fenetreCommande2.pack_forget()
    fenetreFin.pack()

def Plateau1():
    global Joueur
    Joueur=1
    if Switch==1:
        LabelJoueur1.pack_forget()
        LabelJoueur2.pack(side=TOP)
    else:
        LabelJoueur2.pack_forget()
        LabelJoueur1.pack(side=TOP)
    PlateauJoueur2.pack_forget()
    PlateauJoueur1.pack()
    LabelJoueur1.config(text=NomJoueur1.get())
    LabelBateau.config(text="Veuillez placer le : porte avion ( 5 points de vie )")

def Plateau2():
    global Joueur
    Joueur=2
    if Switch==1:
        LabelJoueur2.pack_forget()
        LabelJoueur1.pack(side=TOP)
    else:
        LabelJoueur1.pack_forget()
        LabelJoueur2.pack(side=TOP)
    PlateauJoueur1.pack_forget()
    PlateauJoueur2.pack()
    LabelJoueur2.config(text=NomJoueur2.get())
    LabelBateau.config(text="Veuillez placer le : porte avion ( 5 points de vie )")


def Error(text):
    LabelError.config(text=text)
    LabelError.grid(column=0,row=4,columnspan=2)
    LabelError.after(3000, LabelError.grid_forget)

def message(text):
    LabelMessage.config(text=text,fg='blue')
    LabelMessage.pack()
    LabelMessage.after(2000,LabelMessage.pack_forget)

def AfficherPart1():
    if Joueur==1:
        for x in range (1,11):
            for y in range(1,11):
                if BateauJoueur1[x][y]!='0' and BateauJoueur1[x][y]!='6' and BateauJoueur1[x][y]!='7':
                    PlateauJoueur1.itemconfig(CasesJoueur1[x][y],fill='black')
    elif Joueur==2:
        for x in range(1,11):
            for y in range(1,11):
                if BateauJoueur2[x][y]!='0' and BateauJoueur2[x][y]!='6' and BateauJoueur2[x][y]!='7':
                    PlateauJoueur2.itemconfig(CasesJoueur2[x][y],fill='black')
    fenetrePlateau.after(3000,AfficherPart2)

def AfficherPart2():
    if Joueur==1:
        for x in range (1,11):
            for y in range(1,11):
                if BateauJoueur1[x][y]!='0' and BateauJoueur1[x][y]!='6' and BateauJoueur1[x][y]!='7':
                    PlateauJoueur1.itemconfig(CasesJoueur1[x][y],fill='white')
    elif Joueur==2:
        for x in range(1,11):
            for y in range(1,11):
                if BateauJoueur2[x][y]!='0' and BateauJoueur2[x][y]!='6' and BateauJoueur2[x][y]!='7':
                    PlateauJoueur2.itemconfig(CasesJoueur2[x][y],fill='white')



################################################################################
#PROGRAMME
################################################################################

#FENETRE PRINCIPALE

fenetre=Tk()
fenetre.title("Bataille Navale")
fenetre.configure(bg="#FFFFFF")

BoutonQuitter=Button(fenetre,text="Quitter",command=fenetre.destroy)
BoutonQuitter.pack(side=BOTTOM)

#Fenetre de début de partie

fenetreDebut=LabelFrame(fenetre,bg='#FFFFFF')
fenetreDebut.pack()

NomJoueur1=StringVar()
NomJoueur1.set('Nom du Joueur 1')
EntryJoueur1=Entry(fenetreDebut,textvariable=NomJoueur1)
EntryJoueur1.pack(side=LEFT)

NomJoueur2=StringVar()
NomJoueur2.set('Nom du Joueur 2')
EntryJoueur2=Entry(fenetreDebut,textvariable=NomJoueur2)
EntryJoueur2.pack(side=RIGHT)

BouttonDebut=Button(fenetreDebut,text='Commencer la partie.',command=Debut)
BouttonDebut.pack(side=BOTTOM)

#Fenetre de fin de partie

fenetreFin=LabelFrame(fenetre,bg='#FFFFFF')

LabelGagnant=Label(fenetreFin,text='',fg='red')
LabelGagnant.pack()

#Plateau

fenetrePlateau=LabelFrame(fenetre,bg='#FFFFFF',text='Plateau')

LabelJoueur1=Label(fenetrePlateau,bg='lightgrey',fg='blue',text=NomJoueur1.get())
LabelJoueur2=Label(fenetrePlateau,bg='lightgrey',fg='blue',text=NomJoueur2.get())

PlateauJoueur1=Canvas(fenetrePlateau,bg='green',width=547,height=547)
PlateauJoueur2=Canvas(fenetrePlateau,bg='yellow',width=547,height=547)

BoutonAfficher=Button(fenetre,text='Afficher les bateaux pendant 3 secondes.',command=AfficherPart1)

#Création des deux plateaux
for x in range(11):
    for y in range(11):
        x1=x*50
        y1=y*50
        CasesJoueur1[x][y]=PlateauJoueur1.create_rectangle(x1+2,y1+2,x1+48,y1+48,fill='white')  #Creation des cases blanches pour chacun des plateaux.
        CasesJoueur2[x][y]=PlateauJoueur2.create_rectangle(x1+2,y1+2,x1+48,y1+48,fill='white')
for x in range(11):
    PlateauJoueur1.itemconfig(CasesJoueur1[x][0],fill='lightgrey')      #Creation des cases grises pour chacun des plateaux
    PlateauJoueur2.itemconfig(CasesJoueur2[x][0],fill='lightgrey')
for y in range(11):
    PlateauJoueur1.itemconfig(CasesJoueur1[0][y],fill='lightgrey')
    PlateauJoueur2.itemconfig(CasesJoueur2[0][y],fill='lightgrey')

for i in range(1,11):
    i1=i*50
    PlateauJoueur1.create_text(i1+25,25,text=Lettre[i-1],font=('Arial', '24', 'bold'))      #Création des lettres et chiffres aux extrêmitées des plateaux
    PlateauJoueur2.create_text(i1+25,25,text=Lettre[i-1],font=('Arial', '24', 'bold'))
    PlateauJoueur1.create_text(25,i1+25,text=Nombre[i-1],font=('Arial', '24', 'bold'))
    PlateauJoueur2.create_text(25,i1+25,text=Nombre[i-1],font=('Arial', '24', 'bold'))

#Commandes

fenetreCommande1=LabelFrame(fenetre,bg='lightgrey',text='Commandes')
fenetreCommande2=LabelFrame(fenetre,bg='lightgrey',text='Commandes')

LabelAttaque=Label(fenetreCommande2,text="Coordonnées de l'attaque.")
LabelAttaque.grid(column=0,row=0)

LabelMajuscule2=Label(fenetreCommande2,text='Les lettres doivent être en majuscule.')
LabelMajuscule2.grid(column=1,row=0)

AttaqueX=StringVar()
EntryAttaqueX=Entry(fenetreCommande2,textvariable=AttaqueX)
EntryAttaqueX.grid(column=0,row=1,columnspan=1)

AttaqueY=IntVar()
EntryAttaqueY=Entry(fenetreCommande2,textvariable=AttaqueY)
EntryAttaqueY.grid(column=1,row=1,columnspan=1)

BoutonAttaque=Button(fenetreCommande2,text='Attaquez !',command=attaque)
BoutonAttaque.grid(column=0,row=2,columnspan=2)

LabelPlacer=Label(fenetreCommande1,text="Placez vos bateaux.")
LabelPlacer.grid(column=0,row=0)

LabelMajuscule1=Label(fenetreCommande1,text='Les lettres doivent être en majuscule.')
LabelMajuscule1.grid(column=1,row=0)

PlacerX=StringVar()
EntryPlacerX=Entry(fenetreCommande1,textvariable=PlacerX)
EntryPlacerX.bind('<KeyRelease>', Previsualisation1)
EntryPlacerX.grid(column=0,row=1,columnspan=1)


PlacerY=IntVar()
EntryPlacerY=Entry(fenetreCommande1,textvariable=PlacerY)
EntryPlacerY.bind('<KeyRelease>', Previsualisation1)
EntryPlacerY.grid(column=1,row=1,columnspan=1)

BoutonPlacer=Button(fenetreCommande1,text="Placer",command=Placer)
BoutonPlacer.grid(column=0,row=2,columnspan=1)

BoutonPivoter=Button(fenetreCommande1,text="Pivoter",command=Pivoter)
BoutonPivoter.bind('<ButtonRelease>',Previsualisation1)
BoutonPivoter.grid(column=1,row=2,columnspan=1)

################################################################################
#Label
LabelError=Label(fenetreCommande1,text='',fg='red')

LabelBateau=Label(fenetreCommande1,text="Veuillez placer le porte avion (5 points de vie)",fg='blue')
LabelBateau.grid(column=0,row=3,columnspan=2)

LabelMessage=Label(fenetre,text='',fg='black')

################################################################################

fenetre.mainloop()