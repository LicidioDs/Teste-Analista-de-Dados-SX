# Projeto de Análise de Dados - ENEM 2020

Este projeto tem como objetivo a análise dos dados do Exame Nacional do Ensino Médio (ENEM) 2020. Foram utilizadas ferramentas de Python e Power BI para processar e visualizar os dados. O foco principal foi o desenvolvimento de um processo de ETL para carregar os dados do arquivo CSV para um banco de dados MySQL e gerar indicadores e visualizações para análise do desempenho dos alunos.

## Ferramentas Utilizadas

- **Python**: Para processamento dos dados e execução do ETL.
- **MySQL**: Para armazenamento e consulta dos dados.
- **Power BI**: Para visualização e análise gráfica dos dados.
- **Docker**: Utilizado para configurar o ambiente de banco de dados MySQL em container.

## Objetivos do Projeto

- Realizar a extração, transformação e carga (ETL) dos dados do ENEM 2020.
- Levantar indicadores-chave a partir dos dados.
- Gerar visualizações gráficas que ajudem a analisar o desempenho dos alunos nas provas.
- Responder a perguntas chave sobre as médias de notas, ausências, inscritos e outras variáveis importantes.

## Etapas do Projeto

### 1. Preparação do Ambiente

Foi realizado um fork do repositório original e configurado o ambiente de desenvolvimento utilizando o Docker para criar um container com o MySQL. O banco de dados foi configurado para receber os dados extraídos do arquivo CSV.

### 2. ETL (Extração, Transformação e Carga)

Utilizando Python, foi desenvolvido um processo ETL para:

- **Extração**: Leitura do arquivo `MICRODADOS_ENEM_2020.csv`, disponível para download no seguinte link:
  - [Download do arquivo ENEM 2020](https://download.inep.gov.br/microdados/microdados_enem_2020.zip)
  
- **Transformação**: Limpeza e transformação dos dados para garantir que estivessem no formato adequado para análise.

- **Carga**: Inserção dos dados no banco de dados MySQL rodando em um container Docker.

### 3. Geração de Indicadores

Após carregar os dados no MySQL, foram calculados os seguintes indicadores:

- Escola com a maior média de notas.
- Aluno com a maior média de notas e o valor dessa média.
- Média geral de notas.
- Porcentagem de ausentes.
- Número total de inscritos.
- Média por disciplina, sexo e etnia.

### 4. Visualizações Gráficas (Data Viz)

Foi utilizado o **Power BI** para criar visualizações interativas a fim de facilitar a análise dos dados:

- **Média de Notas por Disciplina**: Visualização das médias de notas em cada disciplina.
- **Distribuição das Notas**: Gráficos para comparar a distribuição das notas por sexo, etnia e escola.
- **Desempenho de Alunos**: Gráficos para analisar a relação entre variáveis como sexo, etnia e o desempenho dos alunos.
- **Notas de Redação e Provas**: Análise do desempenho nas 4 provas (Ciências da Natureza, Ciências Humanas, Linguagens e Matemática) em comparação com as notas de redação.

Você pode visualizar as análises gráficas feitas no Power BI através do seguinte link:
- [Visualizações no Power BI](https://app.powerbi.com/view?r=eyJrIjoiYzEzNjIyMTctZmI2OC00NTgzLWFlYWItOWI5MDBiN2NmMWQ0IiwidCI6ImY3ZTFkMzEwLTQ1ZjgtNDlmYS05MTVjLWZlNzM5NzU1NmU0MSJ9)

### 5. Análise de Correlação

Foram realizadas algumas análises de correlação entre as variáveis, como:

- Correlação entre as notas das 4 provas (Ciências da Natureza, Ciências Humanas, Linguagens e Matemática).
- Correlação entre o desempenho nas provas e variáveis socioeconômicas (como sexo e etnia).

## Como Reproduzir Este Projeto

### 1. Download dos Dados

É necessário realizar o download das bases de dados especificadas nos seguintes caminhos:

- A base pode ser baixada clicando no seguinte link:  
  - [Download do arquivo ENEM 2020](https://download.inep.gov.br/microdados/microdados_enem_2020.zip)
  
Após descompactar a pasta, o arquivo com a base estará no diretório:
