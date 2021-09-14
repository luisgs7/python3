SELECT * FROM estados WHERE id = 25;

INSERT INTO cidades (nome, area, estado_id)
VALUES ('Campinas', 795.0, 25); 

INSERT INTO cidades (nome, area, estado_id)
VALUES ('Niterói', 133.9, 19); 

INSERT INTO cidades (nome, area, estado_id)
VALUES ('Caruaru', 920.6, (SELECT id FROM estados WHERE sigla = 'PE')); 

INSERT INTO cidades (nome, area, estado_id)
VALUES ('Juazeiro do Norte', 248.62, 
	(SELECT id FROM estados WHERE sigla = 'CE')
    ); 

DELETE FROM cidades 
WHERE id = 3;



