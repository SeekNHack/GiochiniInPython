import re
import random
tabella =  [[" "," "," "],[" "," "," "],[" "," "," "]]

r = re.compile("^[1-3][\s|\-|\.|\,][1-3]$")
def stampareTabella():
    stringa = ""
    for i in range(len(tabella)):
        stringa += tabella[i][0] +" | "+ tabella[i][1]+ " | " + tabella[i][2]+"\n"
        if (i<2):
            stringa += "-   -   -\n"
    return stringa


def verificaVittoria(simbolo):
    vittoria = False
    for i in range(len(tabella)): # check delle righe
        if(tabella[i][0] == tabella[i][1] == tabella[i][2] == simbolo):
            vittoria = True
            break
    for j in range(len(tabella)): #check delle colonne
        if(tabella[0][j] == tabella[1][j] == tabella[2][j] == simbolo):
            vittoria = True
            break
    #check delle diagonali
    if ((tabella[0][0] == tabella[1][1] == tabella[2][2] == simbolo) or (tabella[0][2] == tabella[1][1] == tabella[2][0] == simbolo)):
        vittoria = True
    return vittoria


def inserisciSimbolo(simbolo):
    coord = input("Inserisci le coordinate dove vuoi inserire il tuo simbolo: ")
    vannoBene = False
    while(not vannoBene):
        while(not r.match(coord)):
                coord = input("Formato errato, riprova! Esempio: 1,1 : ")
        if(tabella[int(coord[0])-1][int(coord[-1])-1] == " "):
            vannoBene = True
        else:
            coord = ""
    tabella[int(coord[0])-1][int(coord[-1])-1] = simbolo
def autoCompletamento(simbolo):
    if(simbolo == "X"):
        simbolo = "O"
    else:
        simbolo = "X"
    for i in range(len(tabella)):
        for j in range(len(tabella)):
            if (tabella[i][j] == " "):
                tabella[i][j] = simbolo
def gioco():
    turno = False # False giocare X, True giocatore O
    finito = False
    conto = 0
    draw = False
    avversario = False
    while(not finito):
        print(stampareTabella())
        simbolo = "X"
        if(turno):
            simbolo = "O"
        print("Turno del giocatore "+str(int(turno)+1)+"! Posiziona "+simbolo)
        inserisciSimbolo(simbolo)
        conto += 1
        vittoria = verificaVittoria(simbolo)
        print("\n"*30)
        if(conto == 8):
            autoCompletamento(simbolo)
            conto+=1
        if(vittoria):
            finito = True
        elif(conto == 9 and not vittoria):
            draw = True
            finito = True
        else:
            turno = not turno
    print("\n"*30)
    print(stampareTabella())
    if (draw):
        print("Pareggio!")
        input()
        print("\n"*30)
        return -1
    else:
        print("Ha vinto il giocatore "+str(int(turno)+1)+"!")
        input()
        print("\n"*30)
        return int(turno)

vittoria = [0,0] # 1° giocatore 1, il 2° è il giocatore 2
partite = 1
ia = False
print("\n"*30)
print("Benvenuto in Tris!\n")

while(partite != 3 and vittoria[0] != 2 and vittoria[1] != 2):
    tabella = [[" "," "," "],[" "," "," "],[" "," "," "]]
    print("Partita "+str(partite))
    risultato = gioco()
    if (risultato != -1):
        vittoria[risultato] += 1
        partite += 1
if(vittoria[0] >=2):
    print("Vincitore assoluto: Giocatore 1")
elif(vittoria[1]>=2):
    print("Vincitore assoluto: Giocatore 2")
