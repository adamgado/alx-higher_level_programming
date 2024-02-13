-- list all records with score 10 or more from second_table
SELECT score, name FROM second_table WHERE `score` >= 10 ORDER BY score DESC;
