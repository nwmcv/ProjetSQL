from fonctions_base_de_donnees import *

d=connexion_bd("imdb.db")
execute_sql(d, "SELECT DISTINCT titleType FROM title_basics;")
