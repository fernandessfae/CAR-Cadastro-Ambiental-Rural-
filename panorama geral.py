import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = pd.read_csv('imoveis_sicar_uf_20180531.csv', delimiter = ';')

#10 maiores e menores estados com número de imóveis registrados
plt.figure(figsize = (20, 5))
plt.bar(dados.nlargest(10, 'imoveis_car')['sigla'], dados.nlargest(10, 'imoveis_car')['imoveis_car'], color = plt.cm.Set2(np.arange(10)))
plt.title('Os 10 estados com o maior número de imóveis registrados', fontsize = 16, fontweight = 'bold')
plt.show()

plt.figure(figsize = (20, 5))
plt.bar(dados.nsmallest(10, 'imoveis_car')['sigla'], dados.nsmallest(10, 'imoveis_car')['imoveis_car'], color = plt.cm.Set1(np.arange(10)))
plt.title('Os 10 estados com o menor número de imóveis registrados', fontsize = 16, fontweight = 'bold')
plt.show()

#10 maiores e menores estados com área total de imóveis registrados
plt.figure(figsize = (20, 5))
plt.bar(dados.nlargest(10, 'area_car')['sigla'], dados.nlargest(10, 'area_car')['area_car'], color = plt.cm.Set2(np.arange(10)))
plt.title('Os 10 estados com a maior área dos imóveis registrados', fontsize = 16, fontweight = 'bold')
plt.show()

plt.figure(figsize = (20, 5))
plt.bar(dados.nsmallest(10, 'area_car')['sigla'], dados.nsmallest(10, 'area_car')['area_car'], color = plt.cm.Set1(np.arange(10)))
plt.title('Os 10 estados com a menor área dos imóveis registrados', fontsize = 16, fontweight = 'bold')
plt.show()

#Criação de uma nova coluna com médio de área de cada imóvel cadastrado
for index, row in dados.iterrows():
    dados.at[index, 'valor_unitario'] = row['area_car'] / row['imoveis_car']

plt.figure(figsize = (20, 5))
plt.bar(dados.nlargest(10, 'valor_unitario')['sigla'], dados.nlargest(10, 'valor_unitario')['valor_unitario'], color = plt.cm.Set2(np.arange(10)))
plt.title('Os 10 estados com o maior média de área por imóvel registrado', fontsize = 16, fontweight = 'bold')
plt.show()

plt.figure(figsize = (20, 5))
plt.bar(dados.nsmallest(10, 'valor_unitario')['sigla'], dados.nsmallest(10, 'valor_unitario')['valor_unitario'], color = plt.cm.Set1(np.arange(10)))
plt.title('Os 10 estados com a menor média de área por imóvel registrado', fontsize = 16, fontweight = 'bold')
plt.show()