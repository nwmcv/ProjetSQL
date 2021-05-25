14| Combien de films durent plus de 3 heures ?
SELECT count(primaryTitle) FROM title_basics WHERE titleType='movie' AND runtimeMinutes>180;