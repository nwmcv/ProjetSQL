import sqlite3

def connexion_bd(bd_path):
    """
    Fonction: connexion_bd(bd_path)

     | Cette fonction permet d'établir une connexion avec un base de données

    ~ parametre: bd_path -> Chemin d'accès vers la base de données
    ~ renvoie: La connexion à une base de données
    """
    connexion = None
    try:
        connexion = sqlite3.connect(bd_path)
    except sqlite3.Error as e:
        return e
    return connexion

def execute_sql(connexion,sql):
    """
    Fonction: execute_sql(connexion,sql)

     | Cette fonction permet d'executer du code sql et de renvoyer le résultat

    ~ parametre: connexion -> connexion à une base de données
                 sql       -> une requète sql de type str()
    ~ renvoie: le résultat de la requète sous forme de liste de tuples
    """
    cur = connexion.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows

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