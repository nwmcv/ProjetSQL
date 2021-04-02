#! user/bin/env python3
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

def debuthtml():
    return "<!DOCTYPE html>\n<meta charset='utf-8'>\n<html>\n<head>\n<style> table, th, td"+str("{border: 1px solid black;  padding: 5px; border-collapse: collapse;}")+ "</style></head>\n<body>"
def finhtml():
    return "\n</body>\n</html>"

def execute_sql(connexion,sql):
    cur = connexion.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    table = "<table>"     
    for row in rows:
        table += "\n<tr><td>" + str(row[0]) + "</td></tr>"
    table +="\n</table>\n"
    return debuthtml() + str(table) +finhtml()
