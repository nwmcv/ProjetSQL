#coding utf8
from fonctions import *
import os

def Menu():
    action=int(input('\n Que voulez Vous faire ?: \n\n --1/Executer une requète \n --2/Ajouter une requète \n --3/modifer les requetes \n --4/supprimer une requete \n --5/Arreter le programme \n :'))
    if action in [1,2,3,4,5]:
        if action == 1:
            Executer()
        elif action == 2:
            Ajouter()
        elif action == 3:
            modifier()
        elif action == 4:
            supprimer()
        elif action == 5:
            print('Sortie ...')
    else:
        print("\n ~~~~~~~~~~~~~ \n L'entrée n'est pas valide veuillez taper un des 5 chiffres \n ~~~~~~~~~~~~~\n")
        input('appuiez sur entrer pour continuer')
        Menu()

def Executer():
    q_a_executer = {}
    choix_q=choix_req()
    req_dispo=req_existe(choix_q)
    if not req_dispo:
        print("\n le numéro ",choix_q," n'existe pas\n")
        input("appuiez sur entrer pour continuer")
        return Executer()
    else:
        q_a_executer[choix_q] = tpl_question_req('requetes/'+nom_req+str(choix_q)+'.sql')
        titre='requete '+str(choix_q)
        connexion = connexion_bd(database)
        tab_resultats=execute_sql(connexion,q_a_executer[choix_q][1])
        print(tab_resultats)


        

def Ajouter():
    pass

def modifier():
    pass

def supprimer():
    pass

def choix_req():
    print("quels questions choisissez vous ?\n")
    alire = open(fichier_req)
    texte_req = alire.read()
    alire.close()
    questions_req = questions(texte_req)
    for q in questions_req:
        print(q)
    num_q = str(input("veuillez saisir le numéro d'une questions choisie: "))
    try:
        int(num_q)
        return num_q
    except ValueError:
        print("\n Les valeurs entrées doivent être des entiers !\n")
        input("taper entrer pour continuer : ")
        return choix_req()

def questions(alire):
    alire=alire.split('#')
    questions=[]
    for i in range(1,len(alire)):
        q=alire[i].split('\n')
        questions.append(q[0])
    return questions

def req_existe(num):
    liste_req=os.listdir('requetes')
    req=''
    liste_req.remove('alire.md')
    req=nom_req+str(num)+'.sql'
    return req in liste_req



nom_req='req'
fichier_req='requetes/alire.md'
database='data/imdb.db'

if __name__ == '__main__':
    Menu()