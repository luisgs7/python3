SELECT * FROM prefeitos;
SELECT * FROM cidades;

SELECT * FROM cidades AS c INNER JOIN prefeitos AS p ON c.id = p.cidade_id;
 
SELECT * FROM cidades AS c LEFT OUTER JOIN prefeitos AS p ON c.id = p.cidade_id;

SELECT * FROM cidades AS c RIGHT JOIN prefeitos AS p ON c.id = p.cidade_id;


SELECT * FROM cidades AS c LEFT OUTER JOIN prefeitos AS p ON c.id = p.cidade_id
UNION
SELECT * FROM cidades AS c RIGHT JOIN prefeitos AS p ON c.id = p.cidade_id;

