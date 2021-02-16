req1.sql
#1 - Quels sont les différents types de titres dans cette base de données ?
SELECT
DISTINCT
titleType
FROM title_basics;

req2.sql
#2 - Combien y a-t-il de titres dans cette base de données ?
SELECT 
COUNT primaryTitle 
FROM title_basics

req3.sql
#3 - En quelle année est sortie le film The Godfather ?
SELECT startYear
FROM title_basics
WHERE primaryTitle=The Godfather
