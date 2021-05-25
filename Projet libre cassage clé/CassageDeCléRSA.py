#coding utf-8
# 25/05/2021
# Houille Lukas

import time

##### class #####
class colors:
    """
    classe colors
    cette classe provient d'internet 
    c'est simplement une classe pour modifier plus facilement les couleurs d'affichage sans importer de modules.
    """
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

##### Fonctions #####
def main():
    """
    Fonction main()
    Cette fonction permet les premieres entrees de l'utilisateur et d'utiliser les differentes autres fonctions
    Parametre: None
    """
    n = input("entrez la clé RSA que vous souhaitez decomposer : ")
    try:
        if int(n) < (9999991 ** 2): #Nombre choisi en fonction des nombres premiers disponibles dans le fichier
            choix = input("Avec quelle methode souhaitez vous utiliser pour casser cette clé :\n1 -> brutForce\n2 -> brutForceOptimise\n3 -> comparer les deux\n: ")
        else:
            choix = 2
        if n or choix == "exit":
            pass
        else:
            execute(int(n),int(choix))
    except ValueError as e:
        print(colors.fg.red+"veuillez entrer un nombre entier ou exit"+colors.reset)
        continuer()
        main()

def affichage(p,q,t2="None"):
    """
    Fonction affichage
    Cette Fonction permet un belle affichage du résultat
    Parmetres: p, q (deux nombres), t2 (le temps mis par le programme)
    Renvoie: 
    """
    print("temps d'execution : ",t2,"secondes")
    print(colors.fg.red,"P=",colors.reset,p,colors.fg.red," Q=",colors.reset,q)

def execute(n,choix = 1):
    """
    Fonction execute
    Cette Fonction permet de casser la clé et de mesurer le temps en fonction de la methode choisie par l'utilisateur
    Elle permet aussi l'affichage du resultat
    parametres: n (cle RSA), choix
    renvoie:
    """
    if choix == 1:
        t1 = time.time()
        p,q = cassage_cle_brut(n)
        t2 = time.time() - t1
        affichage(p,q,t2)
        continuer()
    elif choix == 2:
        t1 = time.time()
        p,q = cassage_cle_opti(n)
        t2 = time.time() - t1
        affichage(p,q,t2)
        continuer()
    elif choix == 3:
        t1 = time.time()
        p1,q1 = cassage_cle_brut(n)
        t2 = time.time() - t1
        t1 = time.time()
        p2,q2 = cassage_cle_opti(n)
        t3 = time.time() - t1
        print("\nAvec la methode brute:")
        affichage(p1,q1,t2)
        print("\nAvec la methode optimise")
        affichage(p2,q2,t3)
        continuer()
    else:
        print("faites un autre choix")

def continuer():
    """
    Fonction pour marquer des pauses dans l'execution du programme attendre que l'utlisateur soit pret
    """
    input("tapez entrer pour continuer:\n")
    main()

def cassage_cle_opti(nb):
    """
    Fonction cassage_cle_opti
    Cette fonction décompose la cle RSA en ses deux facteurs premier avec une methode brut force optimise
    Parametre: nb (Une cle RSA)
    Renvoie: p,q, les deux facteurs premier qui constitue la cle
    """
    if nb % 2 == 0:
        return 2, nb//2
    sqr = int(nb**0.5)
    if sqr % 2 == 0:
        sqr += 1
    i = 0
    while i < sqr:
        if nb % (sqr - i) == 0:
            return sqr-i, nb//(sqr-i)
        else:
            i += 2

def cassage_cle_brut(nb):
    """
    Fonction cassage_cle_brut
    Cette fonction decompose la cle RSA en ses deux facteurs premier avec une methode brut force
    Parametre: nb (Une cle RSA)
    Renvoie: p,q, deux entiers facteurs premier qui constitue la cle
    """
    with open("nbpremier.txt") as nbs:
        liste_nb = nbs.read().split('\n')
    for i in liste_nb:
        if i!= '':
            n=int(i)
        if nb%n==0:
            if nb//n!=0:
                return n,nb//n

if __name__ == "__main__":
    print(colors.fg.red+"Bienvenue, tapez exit pour sortir du programme\n"+colors.reset)
    main()
