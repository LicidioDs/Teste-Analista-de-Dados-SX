USE db_Enem

LOAD DATA LOCAL INFILE '/data/enem_data/enem_data.csv'
INTO TABLE Enem
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(COD_INSCRICAO, ESTADO_CIVIL, NACIONALIDADE, FAIXA_ETARIA, ANO, SEXO, RACA, TIPO_ESCOLA, 
NOTA_CIENCIA_NATUREZA, NOTA_CIENCIA_HUMANA, NOTA_LINGUAGEM_CODIGO, NOTA_MATEMATICA, 
PRESENCA_CN, PRESENCA_CH, PRESENCA_LC, PRESENCA_MT, ESCOLA, REDACAO, Q001, Q002, Q003, 
Q004, Q005, Q006, Q007, Q008, Q009, Q010, Q011, Q012, Q013, Q014, Q015, Q016, Q017, Q018, 
Q019, Q020, Q021, Q022, Q023, Q024, Q025, SOMA_NOTAS, MEDIA_NOTAS, PRESENCAS);
