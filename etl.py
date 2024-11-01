import pandas as pd
#bibliotecas que o python usa para se comunicas com o SO, com elas podemos usar os comandos do bash
import os
import glob


# Função de extract que le e consolida os jsons

def extrair_dados(path:str) -> pd.DataFrame:
    
    arquivos_json = glob.glob(os.path.join(path, '*.json')) #lista tudo que tá dentro da pasta data com nome terminado em .json
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json] #criando uma lista dos dataframes/arquivos json
    df_total = pd.concat(df_list,ignore_index=True) #UNION dos df. O ignore_index ignora os índices dos df individuais e cria novos no df_total
    
    return(df_total)

# Função que transforma
def calcular_coluna_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    
    df['Total'] = df['Quantidade'] * df['Venda']
    return df
#No pandas, usamos o nome do df e colocamos o nome da coluna que queremos referenciar assim ['nome'], 
# assim conseguimos manipular elas

# Função que dá load em csv ou parquet
def carregar_dados(df: pd.DataFrame, formato_de_saida: list):
    """
    parametro que define se vai ser csv, parquet ou ambos
    """
    for formato in formato_de_saida:
        if formato == 'csv':   
            df.to_csv('dados.csv')
        if formato == 'parquet':
            df.to_parquet('dados.parquet')

#Aqui facilitamos a vida do usuário que vai consumir esse pipeline, pois ele importa só essa função
#  ao invés de todas as outras acima pra gerar o arquivo que ele precisa cfe arquivo pipeline.py
def pipeline_calcular_kpi_de_vendas_consolidado(path: str, formato_de_saida: list):
    data_frame = extrair_dados(path)
    data_frame_calculado = calcular_coluna_total_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)


