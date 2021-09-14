use python_course;

SELECT 
	e.nome AS Estado,
    c.nome AS Cidade,
    regiao as Regiao
FROM estados e, cidades c
WHERE e.id = c.estado_id;


SELECT 
	c.nome AS Cidade,
    e.nome AS Estado,
    regiao AS Regiao
FROM estados AS e 
INNER JOIN cidades c
	on e.id = c.estado_id;
    









