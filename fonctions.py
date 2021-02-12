#coding utf8
import sqlite3

def connexion_bd(bd_path):
    """
    Fonction: connexion_bd
    : Parametre : bd_path #Chemin d'accès vers la base de données
    :  Renvoie  : la connexion à la base de données
    """
    connexion = None
    try:
        connexion = sqlite3.connect(bd_path)
    except Error as e:
        return e
    
    return connexion

def execute_sql(connexion,sql):
    """
    Fonction: execute_sql
    : Parametres : connexion -> (connexion à une base de données avec sqlite3), sql -> (requete SQL au format str)
    :   Renvoie  : Affiche les différentes lignes de la requete
    """
    cur = connexion.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

database_connexion = connexion_bd
run_sql = execute_sql
