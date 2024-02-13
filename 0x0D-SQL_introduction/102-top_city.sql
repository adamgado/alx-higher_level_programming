-- display top 3 temperature for 2 months in order
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month = '7' OR month = '8' GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
