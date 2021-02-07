import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def extraçao_dados(fonte_dados):
    dados = pd.read_csv(fonte_dados, delimiter = ';')
    
    plt.figure(figsize = (20, 5))
    plt.bar(dados.nlargest(10, 'imoveis_car')['sigla'], dados.nlargest(10, 'imoveis_car')['imoveis_car'], color = plt.cm.Set2(np.arange(10)))
    plt.title('Os 10 estados com o maior número de imóveis registrados', fontsize = 16, fontweight = 'bold')
    plt.show();
    
    plt.figure(figsize = (20, 5))
    plt.bar(dados.nsmallest(10, 'imoveis_car')['sigla'], dados.nsmallest(10, 'imoveis_car')['imoveis_car'], color = plt.cm.Set1(np.arange(10)))
    plt.title('Os 10 estados com o menor número de imóveis registrados', fontsize = 16, fontweight = 'bold')
    plt.show();
    
    plt.figure(figsize = (20, 5))
    plt.bar(dados.nlargest(10, 'area_car')['sigla'], dados.nlargest(10, 'area_car')['area_car'], color = plt.cm.Set2(np.arange(10)))
    plt.title('Os 10 estados com a maior área dos imóveis registrados', fontsize = 16, fontweight = 'bold')
    plt.show();
    
    plt.figure(figsize = (20, 5))
    plt.bar(dados.nsmallest(10, 'area_car')['sigla'], dados.nsmallest(10, 'area_car')['area_car'], color = plt.cm.Set1(np.arange(10)))
    plt.title('Os 10 estados com a menor área dos imóveis registrados', fontsize = 16, fontweight = 'bold')
    plt.show();
    
    return fonte_dados

def transformaçao_dados(dados):

    #Criação de uma nova coluna com médio de área de cada imóvel cadastrado
    for index, row in dados.iterrows():
        dados.at[index, 'valor_unitario'] = row['area_car'] / row['imoveis_car']
        
    return dados

def carga_dados(dados):

    plt.figure(figsize = (20, 5))
    plt.bar(dados.nlargest(10, 'valor_unitario')['sigla'], dados.nlargest(10, 'valor_unitario')['valor_unitario'], color = plt.cm.Set2(np.arange(10)))
    plt.title('Os 10 estados com o maior média de área por imóvel registrado', fontsize = 16, fontweight = 'bold')
    plt.show();
    
    plt.figure(figsize = (20, 5))
    plt.bar(dados.nsmallest(10, 'valor_unitario')['sigla'], dados.nsmallest(10, 'valor_unitario')['valor_unitario'], color = plt.cm.Set1(np.arange(10)))
    plt.title('Os 10 estados com a menor média de área por imóvel registrado', fontsize = 16, fontweight = 'bold')
    plt.show();
    
    return dados

if __name__ == '__main__':
    #ETL
    
    #Extração
    dados = extraçao_dados('imoveis_sicar_uf_20180531.csv')
    
    #Transformação
    dados_transformados = transformaçao_dados(dados)
    
    #Carga (Load)
    carga_dados = carga_dados(dados_transformados)
