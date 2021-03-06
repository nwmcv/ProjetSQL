import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
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

def test_req(sql):
    connect = connexion_bd(dir_db+nom_db)   
    try:
        execute_sql(connect,sql)
    except (TypeError,NameError,sqlite3.Error) as e:
        return (False,e)
    return (True,"")

def modifications():
    def ajouter():
        if not saisie_q.get():
            askokcancel(title="erreur question",
                        message="Veuillez saisir une question",
                        parent=add_q,
                        icon = "error")
        elif not saisie_req.get():
            askokcancel(title="erreur requète",
                        message="Veuillez saisir une requète",
                        parent=add_q,
                        icon = "error")
        else:
            test = test_req(saisie_req.get())
            if not test[0]:
                askokcancel(title="erreur requète",
                            message="Votre requète contient une erreur :\n\n"+str(test[1]),
                            parent=add_q,
                            icon = "error")
            else:
                pass


    modifications = tk.Tk()
    modifications.title("Modifications")
    modifications.geometry('720x480')
    modifications.minsize(480,360)


    add_q = tk.LabelFrame(modifications,
                          text = "ajouter une question",
                          height = 100,
                          labelanchor = "nw")
    txt_q = tk.Label(add_q, 
                     text = 'écrivez si dessous la question :',
                     height = 1,
                     fg = "Black")

    saisie_q = tk.Entry(add_q,
                        bg = "white",
                        borderwidth = 3)
    txt_req = tk.Label(add_q, 
                       text = 'écrivez si dessous la requète :',
                       height = 1,
                       fg = "Black")
    saisie_req = tk.Entry(add_q,
                          bg = "white",
                          borderwidth = 3)
    b_ajouter = tk.Button(add_q,
                          text = "Ajouter",
                          command = ajouter,
                          width = 5)
    

    add_q.pack(fill = "x")
    txt_q.pack(side = "top",fill = "x")
    saisie_q.pack(side = "top", fill = "x")
    txt_req.pack(side = "top", fill = "x")
    saisie_req.pack(side = "top", fill = "x")
    b_ajouter.pack(side = "top")
    modifications.mainloop()


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

    txt_rep = tk.Label(cadre_rep,
                       textvariable = txt_req,
                       bg = "white")
        #menu déroulant

    choix_req = tk.StringVar()
    questions = [tpl[0] for tpl in dico_req.values()]
    questions = sorted(questions)

    menu_déroulant = ttk.Combobox(menu,
                                  textvariable = choix_req,
                                  values = questions,
                                  width=75)
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

    b_modif = tk.Button(root, 
                        text = "modifcations",
                        height = 1,
                        command = modifications)
# Affichage

    txt_bienvenu.pack()
    menu.pack(fill = "x")
    cadre_rep.pack(expand = 1 ,fill = "both")
    txt_rep.pack()
    b_affiche_rep.pack(side = "right",pady=10,padx=5)
    b_modif.pack(side = "right",pady=10,padx=5)
    b_quit.pack(side = tk.BOTTOM,pady=10)
    menu_déroulant.pack(side = "left",expand = 1)
    root.mainloop()