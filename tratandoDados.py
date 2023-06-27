import pandas as pd
import matplotlib.pyplot as plt

# Estou importando um dataframe que baixei aqui https://www.kaggle.com/datasets/krishnaraj30/movies-and-tv-shows
dataframe = pd.read_csv('series.csv')

dataframe_transformado = dataframe.copy()

# Preenchendo os valores ausentes nas colunas 'duration', 'genre', 'rating' e 'directors' pois são as colunas que estão faltando
dataframe_transformado['duration'] = dataframe_transformado['duration'].fillna('Desconhecido')
dataframe_transformado['genre'] = dataframe_transformado['genre'].fillna('Desconhecido')
dataframe_transformado['rating'] = dataframe_transformado['rating'].fillna(0)
dataframe_transformado['directors'] = dataframe_transformado['directors'].fillna('Desconhecido')

# Agrupando por título e juntando as informações
dataframe_transformado = dataframe_transformado.groupby('title').agg({
    'ranking': 'first',
    'year': 'first',
    'duration': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else None,
    'genre': lambda x: ', '.join(set(x)),
    'rating': 'mean',
    'directors': lambda x: ', '.join(set(x)),
    'votes': 'sum'
}).reset_index()

# Gráfico
generos = dataframe_transformado['genre'].str.split(', ', expand=True).stack().value_counts()
generos.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Gênero')
plt.ylabel('Quantidade')
plt.title('Quantidade de Títulos por Gênero')
plt.savefig('grafico.png', dpi=300)  # Salvar o gráfico como uma imagem PNG
plt.show()


dataframe_transformado.to_csv('dataframe_transformado.csv', index=False)

#TODO criar uma nova coluna classificando por genero. 
# Pegar um genero especifico, comparar com todos que tem esse genero, e dar uma classificação. 
# Ainda nao pensei em caso o filme tenha mais de 1 genero


