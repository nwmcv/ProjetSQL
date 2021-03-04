#coding utf-8
import tkinter as tk
from tkinter import ttk
import os
import sqlite3

def connexion_bd(bd_path):
    """
    Fonction: connexion_bd
    : parametre : bd_path #Chemin d'accès vers la base de données
    """
    connexion = None
    try:
        connexion = sqlite3.connect(bd_path)
    except Error as e:
        return e
    return connexion

def execute_sql(connexion,sql):
    cur = connexion.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows


def charger_req_dico():
    req = {}
    liste_req=os.listdir(dir_req)
    liste_req.remove('alire.md')
    for fichier in liste_req:
        requete=open(dir_req+fichier)
        txt=requete.read()
        requete.close()
        list_q_req = txt.split('\n')
        numq=list_q_req[0][0]
        req[numq] = (list_q_req[0],list_q_req[1])
        
    return req

def Afficher_rep():
    numq = choix_req.get()[0]
    req_a_executer = dico_req[numq][1]
    conn = connexion_bd(dir_db+nom_db)
    res = execute_sql(conn,req_a_executer)
    txt_req.set(res)

dir_req = "requetes/"
dir_db = "DATA/"
nom_db = "imdb.db"

if __name__=="__main__":

    dico_req=charger_req_dico()


#Création de la fenêtre
    root = tk.Tk()
    root.title("Réponses questions SQL")
    root.geometry('720x480')
    root.minsize(480,360)

    menu = tk.LabelFrame(root,
                        text = "choix question",
                        height = 100,
                        labelanchor = "nw")

    cadre_rep = tk.LabelFrame(root,
                              bg = "white")

    txt_req = tk.StringVar()

# Widgets #
    
        # texte
    txt_bienvenu = tk.Label(root, 
                            text = 'Bienvenu !',
                            height = 2,
                            fg = "Black",
                            font = ("Calibri",18))

    txt_rep = tk.Label(cadre_rep,textvariable = txt_req,bg = "white")
        #menu déroulant

    choix_req = tk.StringVar()
    questions = [tpl[0] for tpl in dico_req.values()]
    questions = sorted(questions)

    menu_déroulant = ttk.Combobox(menu,
                              textvariable = choix_req,
                              values = questions,
                              width=75
                              )
    menu_déroulant.current(0)

        # boutons
    b_affiche_rep = tk.Button(menu,
                            text = "afficher la réponse",
                            height = 1,
                            command = Afficher_rep)

    b_quit = tk.Button(root, 
                        text = "Quitter",
                        relief = tk.GROOVE,
                        height = 1,
                        width = 5,
                        fg = "Black",
                        bg = "#dadeff",
                        command = root.destroy)

# Affichage

    txt_bienvenu.pack()
    menu.pack(fill = "x")
    cadre_rep.pack(expand = 1 ,fill = "both")
    txt_rep.pack()
    b_affiche_rep.pack(side = "right",pady=10,padx=5)
    b_quit.pack(side = tk.BOTTOM,pady=10)
    menu_déroulant.pack(side = "left",expand = 1)
    root.mainloop()
