# pylint: disable-all
# pyright: reportUnusedExpression=false

# |%%--%%| <QkGFePR0RZ|5cUtDzAwDO>
"""°°°
# Usiminas: Residência em Ciência de Dados

**Disciplina:** Probabilidade e Análise de Dados com Python

**Professores:** Flávio Figueiredo e Pedro Melo

**Aula 6:** Análise exploratória de dados e visualizações com Seaborn e Plotly 
°°°"""
# |%%--%%| <5cUtDzAwDO|ikyuJe6YhX>
"""°°°
Na aula de hoje, vimos como construir diversos tipos de visualizações utilizando as bibliotecas `seaborn`e `plotly`. Aqui, colocaremos em prática o que aprendemos para gerar e analisar visualizações com essas ferramentas.
°°°"""
# |%%--%%| <ikyuJe6YhX|A8Obbw5vFl>

# import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

import seaborn as sns

# |%%--%%| <A8Obbw5vFl|ZUZ3rdnRlo>
"""°°°
### Questão 1 - Reconstrua o gráfico de pontos mostrado abaixo.

![img1](https://github.com/fccarvalho2/Viz/blob/main/graph.png?raw=true)

**Informações adicionais:** Para este plot, utilizaremos somente os diamantes da melhor classe de cores (D) do conjunto de dados "Diamonds", que já está incluindo na bibloteca `seaborn`. Você precisará utilizar as funções da biblioteca `pandas` para selecionar as linhas que atendem a este critério. Lembre-se de escolher dimensões apropriadas para sua figura.
°°°"""
# |%%--%%| <ZUZ3rdnRlo|63j1y0CyG8>

# Importando e visualizando o conjunto de dados
diamonds = sns.load_dataset("diamonds")
diamonds

# |%%--%%| <63j1y0CyG8|IhMgBhgM7d>

# Selecionando somente os diamantes da melhor classe de cores (D)
diamonds = diamonds[diamonds["color"] == "D"]
diamonds

# |%%--%%| <IhMgBhgM7d|U5b5YHF7Qq>

f, ax = plt.subplots(figsize=(6, 6))
sns.scatterplot(
    x="table", y="price", hue="cut", size="depth", style="clarity", data=diamonds
)

# |%%--%%| <U5b5YHF7Qq|ad98Oxjh2N>
"""°°°
**Pergunta:** Analisando a figura, qual par de variáveis (dentre as mostradas) parece estar mais fortemente associado?
°°°"""
# |%%--%%| <ad98Oxjh2N|fK8U9wDHfv>
"""°°°
**Resposta:** "table" parece estar fortemente associado com "cut": cortes melhores estão com tables menores, de forma consistente ao longo do eixo x.
°°°"""
# |%%--%%| <fK8U9wDHfv|f1iZRc73RW>
"""°°°
### Questão 2 - Reconstrua o violin plot a seguir.


![violin plot](https://github.com/fccarvalho2/Viz/blob/main/graph2.png?raw=true)

**Informações adicionais:** Para este plot, utilizaremos o conjunto de dados "tips" em sua totalidade. Este _dataset_ já está incluindo por padrão na bibloteca `seaborn` e pode ser importado como um dataframe `pandas` utilizando o comando `sns.load_dataset('tips')`.
°°°"""
# |%%--%%| <f1iZRc73RW|2jIgG90Ik8>

# Importando e visualizando o conjunto de dados
tips = sns.load_dataset("tips")
tips

# |%%--%%| <2jIgG90Ik8|0pBxaHMykv>

fig, ax = plt.subplots(figsize=(10, 7))
sns.violinplot(
    data=tips,
    x="day",
    y="tip",
    hue="smoker",
    split=True,
    inner="quartile",
    linewidth=1,
    palette="BrBG_r",
)

# |%%--%%| <0pBxaHMykv|0zjER4dO7A>
"""°°°
Analisando a visualização construída, podemos obter as respostas para algumas perguntas, incluindo, mas não limitando-se a:

1. Fumantes (_smoker_=_Yes_) tendem a pagar melhores gorgetas?
2. Em qual dia da semana as gorgetas são melhores?
3. Em qual dia da semana se observou a maior gorgeta? 

Com base nisso, modifique a visualização acima para responder às seguintes perguntas:

1. Há uma diferença significativa no total das contas (_total_bill_) pagos por homens e mulheres?
2. Os clientes tendem a gastar mais no almoço ou no jantar?
°°°"""
# |%%--%%| <0zjER4dO7A|gudVnapIja>

# total_bill por sexo
fig, ax = plt.subplots(figsize=(10, 7))
sns.violinplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex",
    split=True,
    inner="quartile",
    linewidth=1,
    palette="BrBG_r",
)

# |%%--%%| <gudVnapIja|XoYaXztpNR>

# total_bill por almoço e jantar
import plotly.express as px

#|%%--%%| <XoYaXztpNR|FWG74Z7T1Q>

fig, ax = plt.subplots(figsize=(10, 7))
sns.violinplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="time",
    split=True,
    inner="quartile",
    linewidth=1,
    palette="BrBG_r",
)

# |%%--%%| <FWG74Z7T1Q|AFK0t9w4W2>
"""°°°
### Questão 3 - Construa um  mapa de calor utilizando o conjunto de dados _diamonds_.

**Informações adicionais:** Conjunto de dados muito grandes podem dificultar a criação de visualizações efetivas. Este é o caso do conjunto diamonds, que possui mais de 53 mil entradas. Para situações como esta, a análise de informações estatísticas (como as correlações) dos dados é muito importante durante a etapa de análise exploratória dos dados, e nos ajuda a criar visualizações mais eficientes. Utilizando as bibliotecas `pandas` e `seaborn`, constura um mapa de calor representando as correlações entre as diversas variáveis numéricas deste conjunto de dados.
°°°"""
# |%%--%%| <AFK0t9w4W2|djxZVXjrCh>

sns.heatmap(data=diamonds.corr())

# |%%--%%| <djxZVXjrCh|WdW0oGCWMZ>
"""°°°
**a)** Construa agora uma matriz de _scatterplots_. Qual destas visualizações lhe parece mais efetiva?
°°°"""
# |%%--%%| <WdW0oGCWMZ|B9A86MHlB7>

sns.pairplot(
    data=diamonds,
    hue="cut",
    x_vars=["carat", "depth", "price", "x", "y", "z"],
    y_vars=["carat", "depth", "price", "x", "y", "z"],
)
# Com certeza o heatmap é mais efeitvo. O scatterplot é muito poluído

# |%%--%%| <B9A86MHlB7|Kbu6kiQTlR>
"""°°°
###  Questão 4 [Desafio] - Construindo animações com Plotly

O Gapminder é uma instituição sem afiliações políticas, econômicas ou religiosas, que tem como o objetivo utilizar dados reais para combater a desinformação sistemática sobre diversos aspectos globais importantes como a pobreza e desigualdades sociais. No [site da organização](https://www.gapminder.org/) são disponibilizados diversos recursos como visualizações criativas, quizes, conjuntos de dados de grande utilidade pública, dentre outros.

Uma das visualizações mais famosas criadas e divulgadas pelo Gapminder é o [Bubble chart animado](https://www.gapminder.org/tools/#$chart-type=bubbles&url=v1) que mostra como a renda e a expectativa de vida mudaram ao redor do mundo desde desde o final do século XVIII.

Apesar de bastante impactante e visualmente atraente, esta visualização de aparência complexa é mais fácil de se construir do que inicialmente podemos imaginar. Por isso, propomos aqui o desafio de reconstruir a animação utilizando os dados do gapminder e a biblioteca `plotly`. 

Observação: No gráfico mostrado no Gapminder, o eixo x está em escala logaritmica. Podemos conseguir resultados similares utilizando o parâmetro `log_x=True` na chamada de nossa função. Para ajustar o tamanho do eixo y, podemos usar ` range_y=[15,90]`.
°°°"""
# |%%--%%| <Kbu6kiQTlR|ZXSHzq4N3z>

# Importando e visualizando o conjunto de dados
gapminder = px.data.gapminder()
gapminder

# |%%--%%| <ZXSHzq4N3z|82VfeczkPJ>

fig = px.scatter(
    data_frame=gapminder,
    x="gdpPercap",
    y="lifeExp",
    width=900,
    height=900,
    size="pop",
    size_max=100,  # Aumente o tamanho máximo para facilitar visualização
    color="continent",
    log_x=True,  # Use escala logaritmica
    hover_data=["country"],
    animation_frame="year",
    range_y=[15, 90],
    range_x=[512, 131072],  # Altera eixo x para ficar mais condizente com o original
    title="Evolução da expectativa de vida por renda per capta no mundo",
    labels={
        "gdpPercap": "Renda per Capita",
        "lifeExp": "Expectativa de Vida",
        "continent": "Continente",
        "year": "Ano",
        "pop": "População",
        "country": "País",
    },
)

fig.update_layout(
    xaxis=dict(
        dtick=0.30102999566,  # Atualiza log para base 2
        showgrid=False,  # Remove grade
    ),
    yaxis=dict(
        showgrid=False,  # Remove grade
    ),
    title_x=0.5,  # Centraliza título
)

fig.show()
