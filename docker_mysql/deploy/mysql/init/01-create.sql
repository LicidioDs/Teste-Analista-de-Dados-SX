-- Criar banco de dados
CREATE DATABASE db_Enem;

-- Criar usuário
CREATE USER 'dbadmin'@'%' IDENTIFIED BY 'dbadmin123';

-- Conceder permissões ao usuário
GRANT ALL PRIVILEGES ON db_Enem.* TO 'dbadmin'@'%';

-- Usar o banco de dados
USE db_Enem;

-- Criar a tabela Enem
CREATE TABLE IF NOT EXISTS db_Enem.Enem (
    COD_INSCRICAO VARCHAR(50) PRIMARY KEY,
    ESTADO_CIVIL VARCHAR(50),
    NACIONALIDADE VARCHAR(50),
    FAIXA_ETARIA VARCHAR(50),
    ANO INT,
    SEXO VARCHAR(10),
    RACA VARCHAR(50),
    TIPO_ESCOLA VARCHAR(50),
    NOTA_CIENCIA_NATUREZA DECIMAL(5,2),
    NOTA_CIENCIA_HUMANA DECIMAL(5,2),
    NOTA_LINGUAGEM_CODIGO DECIMAL(5,2),
    NOTA_MATEMATICA DECIMAL(5,2),
    PRESENCA_CN INT,
    PRESENCA_CH INT,
    PRESENCA_LC INT,
    PRESENCA_MT INT,
    ESCOLA VARCHAR(50),
    REDACAO VARCHAR(50),
    Q001 VARCHAR(50),
    Q002 VARCHAR(50),
    Q003 VARCHAR(50),
    Q004 VARCHAR(50),
    Q005 VARCHAR(50),
    Q006 VARCHAR(50),
    Q007 VARCHAR(50),
    Q008 VARCHAR(50),
    Q009 VARCHAR(50),
    Q010 VARCHAR(50),
    Q011 VARCHAR(50),
    Q012 VARCHAR(50),
    Q013 VARCHAR(50),
    Q014 VARCHAR(50),
    Q015 VARCHAR(50),
    Q016 VARCHAR(50),
    Q017 VARCHAR(50),
    Q018 VARCHAR(50),
    Q019 VARCHAR(50),
    Q020 VARCHAR(50),
    Q021 VARCHAR(50),
    Q022 VARCHAR(50),
    Q023 VARCHAR(50),
    Q024 VARCHAR(50),
    Q025 VARCHAR(50),
    SOMA_NOTAS DECIMAL(10,2),
    MEDIA_NOTAS DECIMAL(5,2),
    PRESENCAS INT
);
