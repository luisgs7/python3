ALTER TABLE empresas MODIFY cnpj VARCHAR(14);

INSERT INTO empresas
	(nome, cnpj)
VALUES 
	('Empresa-01', 9857483928283),
    ('Empresa-02', 0984760938473),
    ('Empresa-03', 0009847382627);


desc empresas;
desc prefeitos;
    
INSERT INTO empresas_unidades
    (empresa_id, cidade_id, sede)
VALUES
	(1, 6, 1),
    (1, 7, 0),
	(2, 6, 0),
	(2, 7, 1);









