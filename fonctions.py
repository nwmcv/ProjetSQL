#coding utf8
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
    for row in rows:
        print(row)

def question(req):
    q=req.split('\n')
    return q[0]

def requete(req):
    q=req.split('\n')
    return q[1]

def question_requete(req):
    q=req.split('\n')
    return q[0],q[1]

def txt_requete(req_path):
    req=open(req_path)
    txt=req.read()
    req.close()
    return txt

#Traduction des fonctions:
database_connexion = connexion_bd
run_sql = execute_sql