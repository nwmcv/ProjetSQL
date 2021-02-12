from fonctions_base_de_donnees import *

if __name__ == '__main__':
    txt=txt_requete('requetes/req1.sql')
    question,req = question_requete(txt)
    print(question)
    print('~~~~~~~~~~~~~~~~~~~~~~~')
    print(req)