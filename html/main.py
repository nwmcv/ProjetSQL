#!/usr/bin/env python3
#coding utf-8

#dev : Lukas Houille
#date : 23/03/2021

import os
from fonctions_bd import *

liste_requetes = os.listdir('requetes/')
def charger_req_dico():
    """
    Fonction charger_req_dico():

     | Cette fonction charge toutes les requètes et les questions et stock dans un dictionnaire

    ~renvoie: req -> un dictionnaire contenant les questions et les requètes
    """
    req = {}
    liste_req=os.listdir("requetes/")
    for fichier in liste_req:
        with open("requetes/"+fichier) as requete:
            txt=requete.read()
        list_q_req = txt.split('\n')
        fichier=fichier.split('.')[0].split('req')
        numq=int(fichier[1])
        req[numq] = (list_q_req[0],list_q_req[1])
    return req

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
print("<form methode='get'>")
for n in num_questions:
    print("<input type='radio' id='",str(n),"' name='questions' value='",n,"'>")
    print("<label for='",str(n),"'>",dico_req[n][0],"</label><br>")

print("<button type=button onclick='displayRadioValue()'>executer</button>")
print("</form>")



print("<div id='result'></div>")

print("<script>")
print("function displayRadioValue() {")
print("var element = document.getElementsByName('questions');")
print("for(i = 0; i < element.length; i++) {")
print("if(element[i].checked)")
print("document.getElementById('result').innerHTML")
print("= 'Num q: '+element[i].value;}}")
print("</script>")


print("\n</body>\n</html>")