import pandas as pd
import matplotlib.pyplot as plt

# Estou importando um dataframe que baixei aqui https://www.kaggle.com/datasets/krishnaraj30/movies-and-tv-shows
dataframe = pd.read_csv('series.csv')

# aqui vou gravar o tanto de linha que tinha antes de eu fazer o tratamento, para ter um parametro
total_linhas_antes = len(dataframe)

# Aqui estou verificando se as colunas que eu considero importante não são vazias ou nulas
colunas_obrigatorias = ['title', 'year', 'genre', 'rating', 'votes', 'duration']
linhas_nulas = dataframe[colunas_obrigatorias].isnull().any(axis=1)
dataframe_limpo = dataframe[~linhas_nulas]

# Aqui vou tirar todas as oujtras colunas, que por enquanto não vou usar elas. E nesse dataframe que eu importei nao estão completas
colunas_indesejadas = set(dataframe.columns) - set(colunas_obrigatorias)
dataframe_limpo = dataframe_limpo.drop(columns=colunas_indesejadas)

# Decidi fazer isso pois nao entendi o motivo de ter tanta serie repetida nesse dataframe. 
# Nao é uma boa solução mas nao sabia como decidir o que era pra manter ou nao
dataframe_limpo = dataframe_limpo.sort_values('votes', ascending=False).drop_duplicates(subset='title')

# Aqui separo os genenores e vou contando para gerar o grafico no final
generos = dataframe_limpo['genre'].str.split(', ', expand=True).stack().value_counts()

# Gráfico
generos.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Gênero')
plt.ylabel('Quantidade')
plt.title('Quantidade de Títulos por Gênero')
plt.show()