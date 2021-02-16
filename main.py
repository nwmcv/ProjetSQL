from fonctions import *
import os

def Menu():
    action=int(input('Que voulez Vous faire ?: \n --1/Executer une requète \n --2/Ajouter une requète \n 3/Exit \n :'))
    if action not in [1,2,3,4,5]:
        print("la valeur entrés n'est pas valide\n")
        Menu()
    elif action == 1:
        Executer()
    elif action == 2:
        Ajouter()
    elif action == 3:
        modifier()
    elif action == 4:
        supprimer()
    elif action == 5:
        print('Sortie ...')

def Executer():
    q_a_executer = {}
    liste_choix_req=choix_req()
    error,num_error=req_existe(liste_choix_req)
    if error==True:
        print("\n le numéro ",num_error," n'existe pas\n")
        input("appuiez sur entrer pour continuer")
        return Executer()
    else:
        for num in (liste_choix_req):
            reqpath='requetes/'+nom_req+str(num)+'.sql'
            txt_req=txt_requete(reqpath)
            q_a_executer[num]=question_requete(txt_req)
        


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
    num_q = str(input("veuillez saisir le numéro des questions choisies separé d'un espace : "))
    num_q = num_q.split(' ')
    liste_choix=[]
    for i in range(len(num_q)):
        try:
            int(num_q[i])
            liste_choix.append(num_q[i])
        except ValueError:
            print("\n Les valeurs entrées doivent être des entiers !\n")
            input("taper entrer pour continuer : ")
            return choix_req()
    return num_q

def questions(alire):
    alire=alire.split('#')
    questions=[]
    for i in range(1,len(alire)):
        q=alire[i].split('\n')
        questions.append(q[0])
    return questions

def req_existe(list_num):
    liste_req=os.listdir('requetes')
    req=''
    for i in range(len(list_num)):
        req=nom_req+str(list_num[i])+'.sql'
        if req not in liste_req:
            return True,liste_req[i]
    return False,None


nom_req='req'
fichier_req='requetes/alire.md'


if __name__ == '__main__':
    Menu()