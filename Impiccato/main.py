import random
import sys



def selezionaParola():
    file = open(".\\paroleitaliane\\parole.txt","r").readlines()
    rand = random.randint(0,59999)
    parola = file[rand]

    while len(parola)<=2:
            rand = random.randint(0,59999)
            parola = file[rand]
    return parola[:-1]



def creaWordlist(parola):
    lung = len(parola)
    wordlist = (parola[0]+" "+"_ "*(len(parola)-2)+parola[-1]).split(" ")
    for i in range(len(parola)):
        if parola[i] == parola[0]:
            wordlist[i] = parola[0]
        elif parola[i] == parola[-1]:
            wordlist[i] = parola[-1]
    return wordlist

def stampaParola(wordlist):
    string = ""
    for i in range(len(wordlist)):
        string += wordlist[i]+" "
    return string

def hovinto(wordlist):
    if "_" in wordlist:
        vittoria = False
    else:
        vittoria = True
    return vittoria

parola = selezionaParola()
wordlist = creaWordlist(parola)
print("\n"*30)
print("Benvenuto!")
vittoria = False
if(parola[0]!=parola[-1]):
    lettere = [parola[0],parola[-1]]
else:
    lettere = [parola[0]]
parole = []
diff = int(input("Difficoltà: 1 Facile, 2 Medio, 3 Difficile: "))
while diff<1 or diff>3:
    print("Numero non valido!")
    diff = int(input("Seleziona la difficoltà: 1 Facile, 2 Medio, 3 Difficile: "))
vite = 7
if diff==1:
    vite = 10
elif diff==3:
    vite = 5

while(not(vittoria)):
    print("Hai "+str(vite)+" vite!\n")
    print("Lettere usate: "+stampaParola(lettere)+"\n")
    print("Parole usate: "+stampaParola(parole)+"\n")

    print(stampaParola(wordlist)+"\n")
    char = input("Inserisci una lettera: ").lower()
    while char in lettere:
        print("Lettera già inserita!")
        char = input("Inserisci una lettera: ").lower()
    if len(char)>1:
        if parola==char:
            vittoria=True
            break
        parole.append(char)
    else:
        lettere.append(char)

    if char in parola:
        for i in range(len(parola)):
            if char==parola[i]:
                wordlist[i] = parola[i]
                vittoria = hovinto(wordlist)
        print("\n"*30)
    else:
        if vite <= 1:
            print("Hai perso!\n")
            print("La parola era: "+parola)
            exit()
        vite -= 1
        print("La lettera non c'è!")
        print("\n"*30)
print("Hai vinto!")
print("La parola era: "+parola)
print("Ti erano rimaste ben "+str(vite)+" vite")
