from tkinter import ttk
from tkinter.messagebox import askokcancel,showinfo
import tkinter as tk
from modules.fonctions_bd import *
from modules.affichage_tk import *
import os


def charger_req_dico():
    """
    Fonction charger_req_dico():

     | Cette fonction charge toutes les requètes et les questions et stock dans un dictionnaire

    ~renvoie: req -> un dictionnaire contenant les questions et les requètes
    """
    req = {}
    liste_req=os.listdir(dir_req)
    for fichier in liste_req:
        with open(dir_req+fichier) as requete:
            txt=requete.read()
        list_q_req = txt.split('\n')
        fichier=fichier.split('.')[0].split('req')
        numq=int(fichier[1])
        req[numq] = (list_q_req[0],list_q_req[1])
    return req



def test_req(sql):
    """
    Fonction test_req(sql):

     | Cette fonction test si une requète sql est valide

    ~paramètre: sql -> requète sous forme de chaine de caractères
    ~renvoie: un tuple contenant True si la requète est valide sinon False et l'erreur 
    """
    connect = connexion_bd(dir_db+nom_db)   
    try:
        execute_sql(connect,sql)
    except (TypeError,NameError,sqlite3.Error) as e:
        return (False,e)
    return (True,"")


def Afficher_rep():
    """
    Fonction Afficher_rep():

     | Cette fonction affiche le résultat de la requète sur la fenètre tkinter
    """
    numq = num_q(choix_req.get())
    req_a_executer = dico_req[numq][1]
    conn = connexion_bd(dir_db+nom_db)
    res = execute_sql(conn,req_a_executer)
    text.delete('1.0',tk.END)
    text.insert(1.0,affichage(res))

def modifications():
    """
    Fonction modifications():

     | Cette fonction contient l'affichage d'une nouvelle fenêtre qui permet d'ajouter des requètes

    elle contien la fonction ajouter
    """
    def ajouter():
        if not saisie_q.get():
            askokcancel(title = "erreur question",
                        message = "Veuillez saisir une question",
                        parent = add_q,
                        icon = "error")
        elif not saisie_req.get():
            askokcancel(title = "erreur requète",
                        message = "Veuillez saisir une requète",
                        parent = add_q,
                        icon = "error")
        else:
            test = test_req(saisie_req.get())
            if not test[0]:
                askokcancel(title = "erreur requète",
                            message = "Votre requète contient une erreur :\n\n"+str(test[1]),
                            parent = add_q,
                            icon = "error")
            else:
                maxnum = int(max(charger_req_dico().keys()))+1
                with open(dir_req+"req"+str(maxnum)+".sql","x") as fichier:
                    fichier.write(str(maxnum)+"| "+str(saisie_q.get())+"\n"+str(saisie_req.get()))
                showinfo (title = "Succès",
                          message = "requète ajoutée avec succès !",
                          parent = add_q)



#Création de la fenêtre modifications
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


# Widgets #
    
        # texte
    txt_bienvenu = tk.Label(root, 
                            text = 'Bienvenu !',
                            height = 2,
                            fg = "Black",
                            font = ("Calibri",18))

    texte=" "
    text=tk.Text(cadre_rep, wrap = 'none')
    scroll_x=tk.Scrollbar(text.master, orient="horizontal")
    scroll_x.config(command = text.xview)
    text.configure(xscrollcommand = scroll_x.set)
    scroll_x.pack(side = 'bottom', fill = 'x', anchor = 'w')
    scroll_y = tk.Scrollbar(text.master)
    scroll_y.config(command = text.yview)
    text.configure(yscrollcommand = scroll_y.set)
    scroll_y.pack(side = tk.RIGHT, fill = 'y')
    text.insert("1.0", texte)

        #menu déroulant

    choix_req = tk.StringVar()
    questions = []
    num_questions = sorted(dico_req)
    for i in num_questions:
        questions.append(dico_req[i][0])

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
                        relief = "groove",
                        height = 1,
                        width = 5,
                        fg = "Black",
                        bg = "#dadeff",
                        command = root.destroy)

    b_modif = tk.Button(menu, 
                        text = "modifcations",
                        height = 1,
                        command = modifications)
# Affichage

    b_quit.pack(side = "bottom",pady=10)
    txt_bienvenu.pack()
    menu.pack(fill = "x")
    cadre_rep.pack(expand = 1 ,fill = "both")
    b_affiche_rep.pack(side = "right",pady=10,padx=5)
    b_modif.pack(side = "right",pady=10,padx=5)
    menu_déroulant.pack(side = "left",expand = 1)
    text.pack(side = 'left', expand = 1, fill = "both")
    root.mainloop()