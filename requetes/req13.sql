13| Quels sont les 10 films d’animation ayant reçu plus de 1000 votes les mieux notés ?
SELECT originalTitle FROM title_basics JOIN title_ratings ON title_basics.tconst=title_ratings.tconst WHERE title_basics.genres LIKE '%Animation%' AND title_ratings.numVotes>1000 AND title_basics.titleType='movie' ORDER BY title_ratings.averageRating DESC LIMIT 10; 