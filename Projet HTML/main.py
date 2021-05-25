#!/usr/bin/env python3
#coding utf-8

#dev : Lukas Houille
#date : 23/03/2021

import os
from fonctions_bd import *

dir_req = "requetes"
dir_rep = "resultats"
bd = "imdb.db"


def charger_req_dico():
    """
    Fonction charger_req_dico():

     | Cette fonction charge toutes les requètes et les questions et stock dans un dictionnaire

    ~renvoie: req -> un dictionnaire contenant les questions et les requètes
    """
    req = {}
    liste_req = os.listdir(dir_req)
    for fichier in liste_req:
        with open("requetes/"+fichier) as requete:
            txt=requete.read()
        list_q_req = txt.split('\n')
        fichier=fichier.split('.')[0].split('req')
        numq=int(fichier[1])
        req[numq] = (list_q_req[0],list_q_req[1])
    return req

def affiche_rep(req):
    conn = connexion_bd("data/imdb.db")
    with open("requetes/"+req,"r") as req:
        sql = req.read().split('\n')[1]
        result = execute_sql(conn, sql)
        return result

def initialisation():
    menu()
    resultats_dispo = os.listdir(dir_rep)
    liste_req = os.listdir(dir_req)
    for req in liste_req:
        if req not in resultats_dispo:
            nom_req = req.split(".sql")[0]
            with open("resultats/"+nom_req+".html" ,"w") as file:
                file.write(affiche_rep(req))



def menu():
    print("Content-type: text/html\n\n")
    print("<meta charset='utf-8'>")
    print("<html>\n<body>")
    print("<div style=\"width: 100%; font-size: 40px; font-weight: bold; text-align: center;\">")
    print("Requetes SQL")
    print("</div>")
    print("<div style=\"text-align: center;\">")
    dico_req = charger_req_dico()
    num_questions = sorted(dico_req.keys())
    print("</div>")
    for n in num_questions:
        print("<a href='resultats/req"+str(n)+".html' target='_blank'>",dico_req[n][0],"</a><br>")



    print("\n</body>\n</html>")

initialisation()