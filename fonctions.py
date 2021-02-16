#coding utf8
import sqlite3
import os
import tkinter

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
    for row in rows:
        print(row)


def question_requete(req):
    q=req.split('\n')
    return (q[0],q[1])

def txt_requete(req_path):
    req=open(req_path)
    txt=req.read()
    req.close()
    return txt

def affichage(texte, titre = "Requêtes tables"):
	"""
	Affiche un texte (résultat d'une requête)
	dans une fenêtre tkinter
	Auteurs: M CHOUCHI
	Arguments:
		texte: str du texte à afficher
		titre: str du titre de la fenêtre
	Renvoi:
		rien
	"""
	root = tkinter.Tk()
	root.title(str(titre))
	RWidth=root.winfo_screenwidth() - 100
	RHeight=root.winfo_screenheight() - 100
	root.geometry("%dx%d+50+0"%(RWidth, RHeight))
	text=tkinter.Text(root, wrap = 'none')
	scroll_x=tkinter.Scrollbar(text.master, orient='horizontal', command = text.xview)
	scroll_x.config(command = text.xview)
	text.configure(xscrollcommand = scroll_x.set)
	scroll_x.pack(side = 'bottom', fill = 'x', anchor = 'w')
	scroll_y = tkinter.Scrollbar(text.master)
	scroll_y.config(command = text.yview)
	text.configure(yscrollcommand = scroll_y.set)
	scroll_y.pack(side = tkinter.RIGHT, fill = 'y')
	text.insert("1.0", texte)
	text.pack(side = tkinter.LEFT, expand = True, fill = tkinter.BOTH)
	root.mainloop()


#Traduction des fonctions:
database_connexion = connexion_bd
run_sql = execute_sql