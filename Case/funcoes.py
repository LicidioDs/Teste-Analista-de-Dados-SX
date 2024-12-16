# Imports
import numpy as np
import pandas as pd
import mysql.connector


# Calcula o percentual de valores ausentes
def func_calc_percentual_valores_ausentes(df):

    # Calcula o total de células no dataset
    totalCells = np.prod(df.shape)

    # Conta o número de valores ausentes por coluna
    missingCount = df.isnull().sum()

    # Calcula o total de valores ausentes
    totalMissing = missingCount.sum()

    # Calcula o percentual de valores ausentes
    print("O dataset tem", round(((totalMissing/totalCells) * 100), 2), "%", "de valores ausentes.")


# Função que calcula o percentual de linhas com valores ausentes
def func_calc_percentual_valores_ausentes_linha(df):

    # Calcula o número total de linhas com valores ausentes
    missing_rows = sum([True for idx,row in df.iterrows() if any(row.isna())])

    # Calcula o número total de linhas
    total_rows = df.shape[0]

    # Calcula a porcentagem de linhas ausentes
    print(round(((missing_rows/total_rows) * 100), 2), "%", "das linhas no conjunto de dados contêm pelo menos um valor ausente.")


# Função para calcular valores ausentes por coluna
def func_calc_percentual_valores_ausentes_coluna(df):
    
    # Total de valores ausentes
    mis_val = df.isnull().sum()

    # Porcentagem de valores ausentes
    mis_val_percent = 100 * mis_val / len(df)

    # Tipo de dado das colunas com valores ausentes
    mis_val_dtype = df.dtypes

    # Cria uma tabela com os resultados
    mis_val_table = pd.concat([mis_val, mis_val_percent, mis_val_dtype], axis=1)

    # Renomear as colunas
    mis_val_table_ren_columns = mis_val_table.rename(
    columns = {0 : 'Valores Ausentes', 1 : '% de Valores Ausentes', 2: 'Dtype'})

    # Classifica a tabela por porcentagem de valores ausentes de forma decrescente e remove colunas sem valores faltantes
    mis_val_table_ren_columns = mis_val_table_ren_columns[mis_val_table_ren_columns.iloc[:,0] != 0].sort_values('% de Valores Ausentes', ascending = False).round(2)

    # Print 
    print ("O dataset tem " + str(df.shape[1]) + " colunas.\n"
        "Encontrado: " + str(mis_val_table_ren_columns.shape[0]) + " colunas que têm valores ausentes.")

    if mis_val_table_ren_columns.shape[0] == 0:
        return

    # Retorna o dataframe com informações ausentes
    return mis_val_table_ren_columns

def convert_to_string(df, columns):
    for col in columns:
        df[col] = df[col].astype("string")


# Função para criar a tabela
def create_table_from_df(df, table_name, conn):
    cursor = conn.cursor()
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
    
    for column in df.columns:
        # Detectar o tipo de dado da coluna
        if df[column].dtype == 'float64':
            dtype = "FLOAT"
        elif df[column].dtype == 'int64':
            dtype = "INT"
        else:
            dtype = "VARCHAR(255)"  # Tipo padrão para texto
        
        create_table_query += f"{column} {dtype}, "
    
    create_table_query = create_table_query.rstrip(", ") + ")"
    cursor.execute(create_table_query)
    conn.commit()
    print(f"Tabela {table_name} criada com sucesso!")


# Função para inserir dados na tabela MySQL
def insert_data_from_df(df, table_name, conn,batch_size=10000):
    cursor = conn.cursor()
    
    # Criar a consulta de inserção
    placeholders = ", ".join(["%s"] * len(df.columns))  # Criar a parte de placeholders
    insert_query = f"INSERT INTO {table_name} ({', '.join(df.columns)}) VALUES ({placeholders})"

    try:
        # Inserir múltiplas linhas de uma vez
        cursor.executemany(insert_query, df.values.tolist())  # Usar executemany para eficiência
        conn.commit()  # Confirmar as alterações no banco
        print(f"Dados inseridos com sucesso na tabela {table_name}!")

    except mysql.connector.Error as err:
        print(f"Erro ao inserir dados: {err}")
        conn.rollback()  # Caso haja erro, desfazer as alterações

    finally:
        # Fechar o cursor após a operação
        cursor.close()


# Classe
class TrataOutlier:

    # Construtor
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def count_outliers(self, Q1, Q3, IQR, columns):
        cut_off = IQR * 1.5
        temp_df = (self.df[columns] < (Q1 - cut_off)) | (self.df[columns] > (Q3 + cut_off))
        return [len(temp_df[temp_df[col] == True]) for col in temp_df]

    def calc_skew(self, columns=None):
        if columns == None:
            columns = self.df.columns
        return [self.df[col].skew() for col in columns]

    def percentage(self, list):
        return [str(round(((value/150001) * 100), 2)) + '%' for value in list]

    def remove_outliers(self, columns):
        for col in columns:
            Q1, Q3 = self.df[col].quantile(0.25), self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            cut_off = IQR * 1.5
            lower, upper = Q1 - cut_off, Q3 + cut_off
            self.df = self.df.drop(self.df[self.df[col] > upper].index)
            self.df = self.df.drop(self.df[self.df[col] < lower].index)

    def replace_outliers_with_fences(self, columns):
        for col in columns:
            Q1, Q3 = self.df[col].quantile(0.25), self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            cut_off = IQR * 1.5
            lower, upper = Q1 - cut_off, Q3 + cut_off

            self.df[col] = np.where(self.df[col] > upper, upper, self.df[col])
            self.df[col] = np.where(self.df[col] < lower, lower, self.df[col])

    def getOverview(self, columns) -> None:
        min = self.df[columns].min()
        Q1 = self.df[columns].quantile(0.25)
        median = self.df[columns].quantile(0.5)
        Q3 = self.df[columns].quantile(0.75)
        max = self.df[columns].max()
        IQR = Q3 - Q1
        skew = self.calc_skew(columns)
        outliers = self.count_outliers(Q1, Q3, IQR, columns)
        cut_off = IQR * 1.5
        lower, upper = Q1 - cut_off, Q3 + cut_off

        new_columns = ['Nome de Coluna', 'Min', 'Q1', 'Median', 'Q3', 'Max', 'IQR', 'Lower fence', 'Upper fence', 'Skew', 'Num_Outliers', 'Percent_Outliers' ]
        
        data = zip([column for column in self.df[columns]], min, Q1, median, Q3, max, IQR, lower, upper, skew, outliers, self.percentage(outliers))

        new_df = pd.DataFrame(data = data, columns = new_columns)
        
        new_df.set_index('Nome de Coluna', inplace = True)
        \
        return new_df.sort_values('Num_Outliers', ascending = False).transpose()
