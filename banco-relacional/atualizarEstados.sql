UPDATE estados
SET nome = "Maranhão"
WHERE sigla = "MA";

SELECT est.nome FROM estados as est WHERE sigla = "MA";

UPDATE estados
SET nome = "Paraná",
	populacao = 11.32
WHERE sigla = "PR";

SELECT 
	est.nome, sigla, populacao
FROM estados as est
WHERE sigla = "PR";






