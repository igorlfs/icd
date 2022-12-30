"""°°°
---
layout: page
title: Tabelas e Tipos de Dados
nav_order: 2
---

[<img src="./colab_favicon_small.png" style="float: right;">](https://colab.research.google.com/github/icd-ufmg/icd-ufmg.github.io/blob/master/_lessons/02-tabelas.ipynb)


# Tabelas e Tipos de Dados

{: .no_toc .mb-2 }

Um breve resumo de alguns comandos python.
{: .fs-6 .fw-300 }

{: .no_toc .text-delta }
Resultados Esperados

1. Aprender o básico de Pandas
1. Entender diferentes tipos de dados
1. Básico de filtros e seleções
1. Aplicação de filtros básicos para gerar insights nos dados de dados tabulares



---
**Sumário**
1. TOC
{:toc}
---
°°°"""
# |%%--%%| <0tywUjwZRz|7GxlQzjIv2>
"""°°°
## Introdução

Neste notebook vamos explorar um pouco de dados tabulares. A principal biblioteca para leitura de dados tabulares em Python se chama **pandas**. A mesma é bastante poderosa implementando uma série de operações de bancos de dados (e.g., groupby e join). Nossa discussão será focada em algumas das funções principais do pandas que vamos explorar no curso. Existe uma série ampla de funcionalidades que a biblioteca (além de outras) vai trazer. 

Caso necessite de algo além da aula, busque na documentação da biblioteca. Por fim, durante esta aula, também vamos aprender um pouco de bash.
°°°"""
# |%%--%%| <7GxlQzjIv2|HYX6cmTYPU>
"""°°°
### Imports básicos

A maioria dos nossos notebooks vai iniciar com os imports abaixo.
1. pandas: dados tabulates
1. matplotlib: gráficos e plots

A chamada `plt.ion` habilita gráficos do matplotlib no notebook diretamente. Caso necesse salvar alguma figura, chame `plt.savefig` após seu plot.
°°°"""
# |%%--%%| <HYX6cmTYPU|WpfSM2A6r1>

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.ion()

# |%%--%%| <WpfSM2A6r1|aenkNPt6zj>
"""°°°
## Series

Existem dois tipos base de dados em pandas. O primeiro, Series, representa uma coluna de dados. Um combinação de Series vira um DataFrame (mais abaixo). Diferente de um vetor `numpy`, a Series de panda captura uma coluna de dados (ou vetor) indexado. Isto é, podemos nomear cada um dos valores.
°°°"""
# |%%--%%| <aenkNPt6zj|bz5OHg0dNa>

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=["a", "b", "c", "d"])

# |%%--%%| <bz5OHg0dNa|ga4NaD4zXZ>

data

# |%%--%%| <ga4NaD4zXZ|vqqMDYkgPx>
"""°°°
Note que podemos usar como um vetor:
°°°"""
# |%%--%%| <vqqMDYkgPx|mZHiRHLgsB>

data[3]

# |%%--%%| <mZHiRHLgsB|lwaPUyRPNy>
"""°°°
Podemos também acessar os valores pelas suas posições na série e pelos índices através das funções `loc` e `iloc`:
°°°"""
# |%%--%%| <lwaPUyRPNy|BHWKlZe3a1>

data.index

# |%%--%%| <BHWKlZe3a1|xNs0quZdrP>
"""°°°
1. `series.loc[índice]` - valor indexado pelo índice correspondente.
1. `series.iloc[int]` - i-ésimo elemento da Series.
°°°"""
# |%%--%%| <xNs0quZdrP|I0P4vIjjzt>

data.loc["a"]

# |%%--%%| <I0P4vIjjzt|LJ01kEc3rY>

data.loc["b"]

# |%%--%%| <LJ01kEc3rY|MXM0knXwdD>
"""°°°
Com `iloc` acessamos por número da linha, como em um vetor tradicional.
°°°"""
# |%%--%%| <MXM0knXwdD|s5QAJwXlSh>

data.iloc[0]

# |%%--%%| <s5QAJwXlSh|z8JyU1wEK4>

data[0]

# |%%--%%| <z8JyU1wEK4|rLFmijLZK9>
"""°°°
## Data Frames

Ao combinar várias Series com um índice comum, criamos um **DataFrame**. Não é tão comum gerar os mesmos na mão como estamos fazendo, geralmente carregamos DataFrames de arquivos `.csv`, `.json` ou até de sistemas de bancos de dados `mariadb`. De qualquer forma, use os exemplos abaixo para entender a estrutura de um dataframe.
°°°"""
# |%%--%%| <rLFmijLZK9|Hgl0712io3>
"""°°°
Lembre-se que {}/dict é um dicionário (ou mapa) em Python. Podemos criar uma série a partir de um dicionário
index->value
°°°"""
# |%%--%%| <Hgl0712io3|TvxlfMjHsq>

area_dict = {
    "California": 423967,
    "Texas": 695662,
    "New York": 141297,
    "Florida": 170312,
    "Illinois": 149995,
}

# |%%--%%| <TvxlfMjHsq|zzAMAsOD1K>

area_dict["California"]

# |%%--%%| <zzAMAsOD1K|WlZGBT4XZO>
"""°°°
A linha abaixo lista todas as chaves.
°°°"""
# |%%--%%| <WlZGBT4XZO|2fb60Lz3Zm>

list(area_dict.keys())

# |%%--%%| <2fb60Lz3Zm|gL042nRJRM>
"""°°°
Agora todas as colunas
°°°"""
# |%%--%%| <gL042nRJRM|ViAi2ZP0BJ>

list(area_dict.values())

# |%%--%%| <ViAi2ZP0BJ|AVTeP1excw>
"""°°°
Acessando um valor.
°°°"""
# |%%--%%| <AVTeP1excw|1hsbWE9vWX>

area_dict["California"]

# |%%--%%| <1hsbWE9vWX|IcsloGzRwn>
"""°°°
Podemos criar a série a partir do dicionário, cada chave vira um elemento do índice. Os valores viram os dados do vetor.
°°°"""
# |%%--%%| <IcsloGzRwn|XJSFsOMvok>

area = pd.Series(area_dict)
area

# |%%--%%| <XJSFsOMvok|TmvQXWDIza>
"""°°°
Agora, vamos criar outro dicionário com a população dos estados.
°°°"""
# |%%--%%| <TmvQXWDIza|v6XhPfFLtc>

pop_dict = {
    "California": 38332521,
    "Texas": 26448193,
    "New York": 19651127,
    "Florida": 19552860,
    "Illinois": 12882135,
}
pop = pd.Series(pop_dict)
pop

# |%%--%%| <v6XhPfFLtc|FHMbwQJsSj>
"""°°°
Por fim, observe que o DataFrame é uma combinação de Series: `area` + `pop`. Cada uma das Series torna-se uma coluna da tabela de dados (ou DataFrame).
°°°"""
# |%%--%%| <FHMbwQJsSj|bF4vRS6Kv0>

data = pd.DataFrame({"area": area, "pop": pop})
data

# |%%--%%| <bF4vRS6Kv0|B3pXTPHos8>
"""°°°
Agora o uso de `.loc e .iloc` deve ficar mais claro:
°°°"""
# |%%--%%| <B3pXTPHos8|2TYcyisKrE>

data.loc["California"]

# |%%--%%| <2TYcyisKrE|6og1zIxANA>

data.loc[["California", "Texas"]]

# |%%--%%| <6og1zIxANA|2fde2sDnac>

df_texas_cali = data.loc[["California", "Texas"]]

# |%%--%%| <2fde2sDnac|R6zTBmbKI0>

df_texas_cali

# |%%--%%| <R6zTBmbKI0|oiunaTOLzq>
"""°°°
Note que o uso de `iloc` retorna a i-ésima linha. O problema é que nem sempre nos dataframes esta ordem vai fazer sentido. O `iloc` acaba sendo mais interessante para iteração (e.g., passar por todas as linhas.)
°°°"""
# |%%--%%| <oiunaTOLzq|CBxRzZmBYz>

data.iloc[0]

# |%%--%%| <CBxRzZmBYz|XxVBeO1IY3>

data.iloc[[0, 2]]

# |%%--%%| <XxVBeO1IY3|lWY5bImUy1>
"""°°°
## Slicing
°°°"""
# |%%--%%| <lWY5bImUy1|ELn5OJqHvW>
"""°°°
Agora, podemos realizar *slicing* no DataFrame. Slicing é uma operação Python que retorna sub-listas/sub-vetores. Caso não conheça, tente executar o exemplo abaixo:
°°°"""
# |%%--%%| <ELn5OJqHvW|5AJ6j1TEBf>

vec = []
vec = [7, 1, 3, 5, 9]
print(vec[0])
print(vec[1])
print(vec[2])

# Agora, l[ini:fim] retorna uma sublista iniciando na posição ini e terminando na posição fim-1
print(vec[1:4])

# |%%--%%| <5AJ6j1TEBf|vaXG0K3ojs>
"""°°°
Voltando para o nosso **dataframe**, podemos realizar o slicing usando o `.iloc`.
°°°"""
# |%%--%%| <vaXG0K3ojs|IILCzJBmwp>

data.iloc[2:4]

# |%%--%%| <IILCzJBmwp|uvV2RIxt6M>
"""°°°
## Modificando DataFrames
°°°"""
# |%%--%%| <uvV2RIxt6M|VlGA6XkJcU>
"""°°°
Series e DataFrames são objetos mutáveis em Python. Podemos adicionar novas colunas em DataFrama facilmente da mesma forma que adicionamos novos valores em um mapa. Por fim, podemos também mudar o valor de linhas específicas e adicionar novas linhas.
°°°"""
# |%%--%%| <VlGA6XkJcU|SMMyaoY7sY>

data

# |%%--%%| <SMMyaoY7sY|UtOzz30NG8>

data["density"] = data["pop"] / data["area"]
data.loc["Texas"]

# |%%--%%| <UtOzz30NG8|xMiIzUyqFT>

data

# |%%--%%| <xMiIzUyqFT|hy4QOx4c6W>

data

# |%%--%%| <hy4QOx4c6W|nOcadA38Ak>

df = data

# |%%--%%| <nOcadA38Ak|2s6QOhFq3e>

df.index

# |%%--%%| <2s6QOhFq3e|BpGYZLcfY9>
"""°°°
## Arquivos

Antes de explorar DataFrames criados a partir de arquivos, vamos ver como um notebook é um shell bastante poderoso. Ao usar uma exclamação (!) no notebook Jupyter, conseguimos executar comandos do shell do sistema. Em particular, aqui estamos executando o comando ls para indentificar os dados da pasta atual.

Tudo que executamos com `!` é um comando do terminal do unix. Então, este notebook só deve executar as linhas abaixo em um computador `Windows`.
°°°"""
# |%%--%%| <BpGYZLcfY9|pwzX3Qit8r>

# !dir

# |%%--%%| <pwzX3Qit8r|RjTyLa1GWH>
"""°°°
## Baby Names

É bem mais comum fazer uso de DataFrames que já existem em arquivos. No entanto, é importante ressaltar que nem sempre esses arquivos já estão prontos para o cientista de dados. Em várias ocasiões, você vai ter que coletar e organizar os mesmos. Limpeza e coleta de dados é uma parte fundamental do seu trabalho. Durante o curso, boa parte dos notebooks já vão ter dados prontos.

Primeiro, vamos abrir o arquivo csv que temos no nosso diretório:
°°°"""
# |%%--%%| <RjTyLa1GWH|5J67h1ecdo>

df = pd.read_csv("baby.csv")
df

# |%%--%%| <5J67h1ecdo|0WXAuGH6IM>

df.describe()

# |%%--%%| <0WXAuGH6IM|FsqFSg3h0M>
"""°°°
Podemos também carregar outro conjunto de dados sobre bebês, que contém informações sobre os seus nomes. A versão completa está disponível publicamente pela Internet:
°°°"""
# |%%--%%| <FsqFSg3h0M|sZsvjc6GRB>

df = pd.read_csv(
    "https://media.githubusercontent.com/media/icd-ufmg/material/master/aulas/03-Tabelas-e-Tipos-de-Dados/baby.csv"
)
df = df.drop("Id", axis="columns")  # remove a coluna id, não serve para nada
df

# |%%--%%| <sZsvjc6GRB|LzKWllLNoX>

df.info()

# |%%--%%| <LzKWllLNoX|kA74aAI6EK>
"""°°°
O método `head` do notebook retorna as primeiras `n` linhas do mesmo. Use tal método para entender seus dados. **Sempre olhe para seus dados.** Note como as linhas abaixo usa o `loc` e `iloc` para entender um pouco a estrutura dos mesmos.
°°°"""
# |%%--%%| <kA74aAI6EK|KnY9ZZYvfU>

df.head()

# |%%--%%| <KnY9ZZYvfU|Fr5b2bx2JC>

df.head(6)

# |%%--%%| <Fr5b2bx2JC|46syTQGbKc>

df[10:15]

# |%%--%%| <46syTQGbKc|pPsapJdVcB>

df.iloc[0:6]

# |%%--%%| <pPsapJdVcB|Ehy36eLhGk>

df[["Name", "Gender"]].head(6)

# |%%--%%| <Ehy36eLhGk|qRIgKC2qXK>
"""°°°
## Groupby

Vamos responder algumas perguntas com a função groupby. Lembrando a ideia é separar os dados com base em valores comuns, ou seja, agrupar por nomes e realizar alguma operação. O comando abaixo agrupa todos os recem-náscidos por nome. Imagine a mesma fazendo uma operação equivalente ao laço abaixo:

```python
buckets = {}                    # Mapa de dados
names = set(df['Name'])         # Conjunto de nomes únicos
for idx, row in df.iterrows():  # Para cada linha dos dados
    name = row['Name']
    if name not in buckets:
        buckets[name] = []      # Uma lista para cada nome
    buckets[name].append(row)   # Separa a linha para cada nome
```

O código acima é bastante lento!!! O groupby é optimizado. Com base na linha abaixo, o mesmo nem retorna nehum resultado ainda. Apenas um objeto onde podemos fazer agregações.
°°°"""
# |%%--%%| <qRIgKC2qXK|uKwfBAB3ck>

gb = df.groupby("Name")
type(gb)

# |%%--%%| <uKwfBAB3ck|7trubo06Fv>
"""°°°
Agora posso agregar todos os nomes com alguma operação. Por exemplo, posso somar a quantidade de vezes que cada nome ocorre. Em Python, seria o seguinte código.

```python
sum_ = {}                       # Mapa de dados
for name in buckets:            # Para cada nomee
    sum_[name] = 0
    for row in buckets[name]:   # Para cada linha com aquele nome, aggregate (some)
        sum_[name] += row['Count']
```
°°°"""
# |%%--%%| <7trubo06Fv|vSbJn3J91Y>
"""°°°
Observe o resultado da agregação abaixo. Qual o problema com a coluna `Year`??
°°°"""
# |%%--%%| <vSbJn3J91Y|cD29gL73AR>

gb.mean()

# |%%--%%| <cD29gL73AR|6UV9vkIAv9>
"""°°°
Não faz tanto sentido somar o ano, embora seja um número aqui representa uma categoria. Vamos somar as contagens apenas.
°°°"""
# |%%--%%| <6UV9vkIAv9|QMKuKG34qb>

gb.sum()["Count"]

# |%%--%%| <QMKuKG34qb|RUF414gDwp>
"""°°°
E ordenar...
°°°"""
# |%%--%%| <RUF414gDwp|PqpsnUKxM2>

gb.sum()["Count"].sort_values()

# |%%--%%| <PqpsnUKxM2|AygzAfuARk>
"""°°°
É comum, embora mais chato de ler, fazer tudo em uma única chamada. Isto é uma prática que vem do mundo SQL. A chamada abaixo seria o mesmo de:

```sql
SELECT Name, SUM(Count)
FROM baby_table
GROUPBY Name
ORDERBY SUM(Count)
```
°°°"""
# |%%--%%| <AygzAfuARk|EiDrMEqWPy>

df.groupby("Name").sum().sort_values(by="Count")["Count"]

# |%%--%%| <EiDrMEqWPy|KPmMybgqSO>
"""°°°
Use `[::-1]` para inverter a ordem:
°°°"""
# |%%--%%| <KPmMybgqSO|ou5jRN5VpA>

df.groupby("Name").sum().sort_values(by="Count")["Count"][::-1]

# |%%--%%| <ou5jRN5VpA|rgYafca6ET>
"""°°°
Podemos agrupar por múltiplas colunas:
°°°"""
# |%%--%%| <rgYafca6ET|1ZOhT9xazh>

df.groupby(["Name", "Year"]).sum()

# |%%--%%| <1ZOhT9xazh|tWtvMHHqfK>
"""°°°
## NBA Salaries e Indexação Booleana

Por fim, vamos explorar alguns dados da NBA para entender a indexação booleana. Vamos carregar os dados da mesma forma que carregamos os dados dos nomes de crianças.
°°°"""
# |%%--%%| <tWtvMHHqfK|DncD4VgZg1>

df = pd.read_csv(
    "https://media.githubusercontent.com/media/icd-ufmg/material/master/aulas/03-Tabelas-e-Tipos-de-Dados/nba_salaries.csv"
)
df.head()

# |%%--%%| <DncD4VgZg1|FRHTnVRiaC>
"""°°°
Por fim, vamos indexar nosso DataFrame por booleanos. A linha abaixo pega um vetor de booleanos onde o nome do time é `Houston Rockets`.
°°°"""
# |%%--%%| <FRHTnVRiaC|4hiBqNfmrF>

df["TEAM"] == "Houston Rockets"

# |%%--%%| <4hiBqNfmrF|UjoFhT2hX6>
"""°°°
Podemos usar tal vetor para filtrar nosso DataFrame. A linha abaixo é o mesmo de um:

```sql
SELECT *
FROM table
WHERE TEAM = 'Houston Rockets'
```
°°°"""
# |%%--%%| <UjoFhT2hX6|9KNv5L76Om>

filtro = df["TEAM"] == "Houston Rockets"
df[filtro]

# |%%--%%| <9KNv5L76Om|zMrrzI7TvZ>

df[df["TEAM"] == "Houston Rockets"]

# |%%--%%| <zMrrzI7TvZ|SQhoGCMTkH>
"""°°°
Assim como pegar os salários maior do que um certo valor!
°°°"""
# |%%--%%| <SQhoGCMTkH|PKkX68ZfvP>

df[df["SALARY"] > 2]

# |%%--%%| <PKkX68ZfvP|t9NQip7KPz>
"""°°°
## Exercícios

Abaixo temos algumas chamadas em pandas. Tente explicar cada uma delas.
°°°"""
# |%%--%%| <t9NQip7KPz|El1jQM4RQS>

df[["POSITION", "SALARY"]].groupby("POSITION").mean()

# |%%--%%| <El1jQM4RQS|5K0C3gsOq5>

df[["TEAM", "SALARY"]].groupby("TEAM").mean().sort_values("SALARY")

# |%%--%%| <5K0C3gsOq5|n7EQ0CR87e>
"""°°°
## Merge

Agora, vamos explorar algumas chamadas que fazem opereações de merge.
°°°"""
# |%%--%%| <n7EQ0CR87e|Pm0zBIKh4S>

people = pd.DataFrame(
    [
        ["Joey", "blue", 42, "M"],
        ["Weiwei", "blue", 50, "F"],
        ["Joey", "green", 8, "M"],
        ["Karina", "green", np.nan, "F"],
        ["Fernando", "pink", 9, "M"],
        ["Nhi", "blue", 3, "F"],
        ["Sam", "pink", np.nan, "M"],
    ],
    columns=["Name", "Color", "Age", "Gender"],
)
people

# |%%--%%| <Pm0zBIKh4S|2Fv6ttqIKq>

email = pd.DataFrame(
    [
        ["Deb", "deborah_nolan@berkeley.edu"],
        ["Sam", np.nan],
        ["John", "doe@nope.com"],
        ["Joey", "jegonzal@cs.berkeley.edu"],
        ["Weiwei", "weiwzhang@berkeley.edu"],
        ["Weiwei", np.nan],
        ["Karina", "kgoot@berkeley.edu"],
    ],
    columns=["User Name", "Email"],
)
email

# |%%--%%| <2Fv6ttqIKq|DwOl85rixm>

people.merge(email, how="inner", left_on="Name", right_on="User Name")

# |%%--%%| <DwOl85rixm|7LTw04Ccsw>
