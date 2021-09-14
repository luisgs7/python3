SELECT e.nome, c.nome 
FROM empresas AS e, empresas_unidades AS eu, cidades AS c
WHERE e.id = eu.empresa_id
AND c.id = eu.cidade_id
AND sede;