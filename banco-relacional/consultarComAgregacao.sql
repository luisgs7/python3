SELECT 
	regiao as "Região",
	SUM(populacao) as total
FROM estados
	GROUP BY regiao
	ORDER BY total DESC;

SELECT 
	AVG(populacao) as total
FROM estados;