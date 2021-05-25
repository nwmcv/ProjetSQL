def maxi_in_row(rows,num):
    """
    Fonction: maxi_in_row(rows,num)

     | Cette fonction recherche la largeur maximale parmis les élements d'une colone,
        Cette fonction est utilisé par la fonction affichage()

    ~ parametre: rows -> Une liste de tuples (résultat d'une requète sql)
                 num  -> le numéro de la colone pour laquelle on veux la largeur maximum
    ~ renvoie: une liste avec la largeur maximum de chaque colone
    """
    maxi=0
    for row in rows:
        if len(str(row[num]))>maxi:
            maxi = len(str(row[num]))
    return maxi

def separateur(largeur_colonnes):
    """
    Fonction: separateur(largeur_colonnes)

     | Cette fonction creer une chaine de caractère afin d'afficher proprement le tableau

    ~ parametre: largeur_colonnes -> une liste contenant la largeur maximum de chaque colone liste renvoyé par la fonction maxi_in_row()
    ~ renvoie: sep -> une chaine de caractère modélisant une séparation
    """
    sep = '+'
    for num in largeur_colonnes[:-1]:
        if num == None:
            pass
        else:
            sep += '-'*num + '+'
    return sep + '\n'


def affichage(rows):
    """
    Fonction: affichage(rows)

     | Cette fonction creer une chaine de caractère qui représente un tableau une fois affiché, elle permet de creer une présentation propre d'un requète sql

    ~ parametre: rows -> une liste de tuples, résultat d'une requète sql
    ~ renvoie: finale -> une longue chaine de caractères
    """
    nb_colones = len(rows[0])
    l1=len(str(len(rows)))
    largeur_colonnes = [l1+2]
    largeur_colonnes += [largeur_colonnes.append(maxi_in_row(rows,i)) for i in range(nb_colones)]
    sepa = separateur(largeur_colonnes)
    finale = sepa 
    for i in range(len(rows)):
        finale += '| ' + str(i) + ' '*(l1-len(str(i))) + ' |'
        for k in range(len(rows[i])):
            finale += str(rows[i][k]) + ' '*(largeur_colonnes[k+1]-len(str(rows[i][k])))+'|'
        finale += '\n'+ sepa
    return finale

def num_q(choix_req):
    """
    cette fonction renvoie le numéro de la requète à éxecuter
    """
    l_q = choix_req.split('|')
    numq = int(l_q[0])
    return numq

