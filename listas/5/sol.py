# pylint: disable-all

# |%%--%%| <nxfMnbvDFc|tzBWSE8Qw3>
r"""°°°
# Lista 5 - Testes de Hipótese
°°°"""
# |%%--%%| <tzBWSE8Qw3|v5UsORGtlk>
r"""°°°
## Testes A/B
°°°"""
# |%%--%%| <v5UsORGtlk|SbGQFaLRYI>
r"""°°°
Testes A/B são uma metodologia muito utilizada para detectarmos diferenças significativas entre dois grupos, geralmente chamados controle e teste. 

**Exemplo:** Há eficácia na prevenção de morte de uma determinada vacina contra a Covid? 

Para isso, teremos:
- Grupo de controle: placebo.
- Grupo de teste: vacina.

**Solução:** Realizamos amostragem bootstrap de cada grupo e plotamos boxplots das médias encontradas. No final comparamos as médias dos grupos para ver se há diferença significativa entre o número de mortos de cada grupo.

Vamos ver um exemplo prático de como realizar um teste A/B para dados reais.

Começamos importando a biblioteca pandas e carregando os dados do Enem2015. Em seguida, agrupamos pela variável 'DEPENDENCIA_ADMINISTRATIVA' para relembrarmos a distribuição dos dados.
°°°"""
# |%%--%%| <SbGQFaLRYI|Zs3IMAB3AT>

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy.testing import assert_equal

# |%%--%%| <Zs3IMAB3AT|ahU40eyN5g>

url = "https://raw.githubusercontent.com/pedroharaujo/ICD_Docencia/master/enem2015.csv"
data = pd.read_csv(url)

tmp = data.groupby("DEPENDENCIA_ADMINISTRATIVA").count()
tmp.head()

# |%%--%%| <ahU40eyN5g|kwxlQeGrjP>

data.head()
data.info()

# |%%--%%| <kwxlQeGrjP|wVM0vfJHi1>
r"""°°°
Imagine que queremos testar se existe diferença entre as médias da variável 'NOTA_MEDIA_ESCOLA' para escolas com 'DEPENDENCIA_ADMINISTRATIVA' Federal e Municipal. Matematicamente, queremos testar se:

 $$\mu_{Municipal} = \mu_{Federal},$$
 
 onde $\mu$ é a média da variável 'NOTA_MEDIA_ESCOLA'.

 Vamos utilizar os códigos da lista anterior e da aula de testes A/B como base para realização do *bootstrap*.
°°°"""
# |%%--%%| <wVM0vfJHi1|ofGJuRsgPa>


def bootstrap_mean(df1, df2, column, n=10000):
    size1 = len(df1)
    size2 = len(df2)
    values1 = np.zeros(n)
    values2 = np.zeros(n)
    values_diff = np.zeros(n)
    for i in range(n):
        sample1 = df1[column].sample(size1, replace=True, random_state=i)
        sample2 = df2[column].sample(size2, replace=True, random_state=i * 3)
        values1[i] = sample1.mean()
        values2[i] = sample2.mean()
        values_diff[i] = sample1.mean() - sample2.mean()
    return values1, values2, values_diff


federal = data[data["DEPENDENCIA_ADMINISTRATIVA"] == "Federal"]
municipal = data[data["DEPENDENCIA_ADMINISTRATIVA"] == "Municipal"]
col = "NOTA_MEDIA_ESCOLA"
v_fed, v_mun, v_diff = bootstrap_mean(federal, municipal, col)

# |%%--%%| <ofGJuRsgPa|yYUGnjdCgm>
r"""°°°
Em seguida plotamos os boxplots de cada grupo e avaliamos se há intersecção da amplitude dos valores para cada tipo de escola.
°°°"""
# |%%--%%| <yYUGnjdCgm|G5iuEdEPvu>

bp_data = [v_fed, v_mun]

plt.rcParams["figure.figsize"] = (8, 6)
plt.boxplot(
    bp_data, whis=[2.5, 97.5], positions=[1, 2], showfliers=False, showmeans=True
)
plt.xticks([1, 2], ["Municipal", "Federal"], fontsize=10)
plt.ylabel("", fontsize=13)
plt.xlabel("DEPENDENCIA_ADMINISTRATIVA", fontsize=12)
plt.title("Notas Médias das Escolas por Dependência Administrativa", fontsize=14)
plt.show()

# |%%--%%| <G5iuEdEPvu|gvLbTR283V>
r"""°°°
Podemos observar que os boxplots não se cruzam, com evidência de que as médias das `NOTAS_MEDIA_ESCOLA` para escolas Federais são maiores que para escolas com `DEPENDENCIA_ADMINISTRATIVA` Municipal.

Outra maneira de realizarmos essa comparação entre as médias de dois grupos é computarmos a diferença entre as médias a cada amostragem *bootstrap* feita e analisarmos apenas o boxplot das diferenças. O código anterior computa essa diferença na variável `values` e o seguinte plota o boxplot de tais diferenças.
°°°"""
# |%%--%%| <gvLbTR283V|3EVO0XmlOH>

plt.rcParams["figure.figsize"] = (8, 6)

plt.boxplot(v_diff, whis=[2.5, 97.5], showfliers=False, showmeans=True)
plt.xticks([1], ["Valor"], fontsize=10)
plt.ylabel(col, fontsize=12)
plt.xlabel("Diferença Municipal e Federal", fontsize=12)
plt.title("Diferença das Notas Médias das Escolas Municipais e Federais", fontsize=14)
plt.show()

# |%%--%%| <3EVO0XmlOH|fqfZArMFdM>
r"""°°°
Nesse caso, para que as médias sejam consideradas iguais, analisamos se o *boxplot* gerado após o processo de amostragem, contém o valor 0. Como não é o caso, podemos afirmar que existem evidências de que as médias dos grupos comparados são distintas.

Note também, que alteramos o código do boxplot para que os limites sejam relativos aos percentis para um nível de 5% de significância, oque é um valor diferente de como é normalmente calculado os limites de um boxplot.
°°°"""
# |%%--%%| <fqfZArMFdM|9MBRBYt8HG>

print("2.5% PERCENTIL: ", np.percentile(v_diff, 2.5).round(4))
print("97.5% PERCENTIL: ", np.percentile(v_diff, 97.5).round(4))

# |%%--%%| <9MBRBYt8HG|YGOqlkmr4d>
r"""°°°
## Exercício 1
°°°"""
# |%%--%%| <YGOqlkmr4d|H3bm1e4GlH>
r"""°°°
Altere o código abaixo para retornar `True` ou `False` ao comparar se há diferença para as medianas da variável `TAXA_DE_PARTICIPACAO` entre escolas de `DEPENDENCIA_ADMINISTRATIVA` indicadas, a dado nível de significância:

**Exemplo:** Se $\alpha = 0.05$, os percentis serão 2.5 e 97.5.
°°°"""
# |%%--%%| <H3bm1e4GlH|pWq8Rpbow3>


def percent(df1: pd.DataFrame, df2: pd.DataFrame, column: str, alpha: float) -> bool:
    _, _, values_diff = bootstrap_mean(df1, df2, column)
    floor: float = np.percentile(values_diff, alpha * 50)
    ceil: float = np.percentile(values_diff, 100 - (alpha * 50))
    # retorna True se houver diferença e False se não houver diferença entre as medianas testadas
    return floor < 0 and ceil > 0


# |%%--%%| <pWq8Rpbow3|kde3WY9OEB>
r"""°°°
**a)** Privada e Estadual, com $\alpha=0.1$
°°°"""
# |%%--%%| <kde3WY9OEB|DHKtPGilM6>

# col = "TAXA_DE_PARTICIPACAO"
col = "NOTA_MEDIA_ESCOLA"
privada = data[data["DEPENDENCIA_ADMINISTRATIVA"] == "Privada"]
estadual = data[data["DEPENDENCIA_ADMINISTRATIVA"] == "Estadual"]
alpha = 0.1
result = percent(privada, estadual, col, alpha)

assert_equal(result, False)

# |%%--%%| <DHKtPGilM6|kNls4bSzqs>
r"""°°°
**b)** Privada e Municipal, com $\alpha=0.15$
°°°"""
# |%%--%%| <kNls4bSzqs|Tk8unkPuNL>

df1 = data[data["DEPENDENCIA_ADMINISTRATIVA"] == "Privada"]
df2 = data[data["DEPENDENCIA_ADMINISTRATIVA"] == "Municipal"]
alpha = 0.15
result = percent(df1, df2, col, alpha)

assert_equal(result, False)

# |%%--%%| <Tk8unkPuNL|ZJ5miTZveX>
r"""°°°
**c)** Privada e Federal, com $\alpha=0.001$
°°°"""
# |%%--%%| <ZJ5miTZveX|SzU9jdWcQ9>

df1 = data[data["DEPENDENCIA_ADMINISTRATIVA"] == "Privada"]
df2 = data[data["DEPENDENCIA_ADMINISTRATIVA"] == "Federal"]
alpha = 0.001
result = percent(df1, df2, col, alpha)

assert_equal(result, True)

# |%%--%%| <SzU9jdWcQ9|YlRZLn0RcN>
r"""°°°
## Teste de Permutação
°°°"""
# |%%--%%| <YlRZLn0RcN|faMHht1uhH>
r"""°°°
- **Teste via *Bootstrap*:** Geramos várias sub-amostras com base na amostra disponível.
- **Teste de Permutação:** Simulamos a população com base em conhecimentos/suposições da mesma.

**Exemplo:** Suponha que eu jogue uma moeda para o alto 30 vezes e obtenho 23 caras e 7 coroas. Essa moeda pode ser considerada uma moeda honesta?

Sabemos que uma moeda honesta apresenta 50% de chance de cair em cada lado. Logo, em 30 lançamentos o valor esperado seria 15 caras e 15 coroas. Mas a independencia entre um lançamento e outro nos garante que nem sempre isso será verdade. 

Nesse momento que aplica-se teste de permutação.

O lançamento da moeda consistem em uma variável aleatória Bernoulli com média $p = 7/30$ e variância $p(1-p)$.

Queremos testar a hipótese nula de que a moeda é honesta, pois queremos um SINAL caso ela não seja.
°°°"""
# |%%--%%| <faMHht1uhH|GCzni832qI>

# definindo semente para reprodutibilidade
np.random.seed(13)

# criando 100k lançamentos meio a meio (moeda honesta)
pop_size = 10**5
data = np.zeros(pop_size)
data[: int(pop_size / 2)] = 1  # número de caras

# definindo experimento - 1k experimentos com 30 amostras cada
size = 30
simulations = np.zeros(1000)
simulations1 = np.zeros(1000)
for i in range(1000):
    np.random.shuffle(data)
    tmp = data[:size]
    num_k = (tmp == 1).sum()
    prop: float = num_k / size
    simulations[i] = num_k
    simulations1[i] = prop

# histogramas dos resultados - contagem de caras e probabilidade
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 6))

ax1.hist(simulations, color="#A3333D", alpha=0.9, density=False, bins=15, rwidth=0.9)
ax1.set_xlabel("Número de Caras")
ax1.set_ylabel("Frequências")
ax1.set_title("Histograma do Número de Caras")

ax2.hist(simulations1, color="#A3333D", alpha=0.9, density=False, bins=15, rwidth=0.9)
ax2.set_xlabel("Proporção de Caras")
ax2.set_ylabel("Frequências")
ax2.set_title("Histograma da Proporção de Caras")

plt.show()

# |%%--%%| <GCzni832qI|sI7TAZeks2>

alpha = 0.05

count_inf = np.percentile(simulations, (alpha / 2) * 100).round(2)
count_sup = np.percentile(simulations, (1 - alpha / 2) * 100).round(2)
print("COUNT INF: ", count_inf)
print("COUNT SUP: ", count_sup)

prop_inf = np.percentile(simulations1, (alpha / 2) * 100).round(2)
prop_sup = np.percentile(simulations1, (1 - alpha / 2) * 100).round(2)
print("PROP INF:", prop_inf)
print("PROP SUP: ", prop_sup)


# |%%--%%| <sI7TAZeks2|mdfd6i5frd>
r"""°°°
Note que se pegarmos 95% dos valores encontrados ao realizarmos 100k permutações, não estaremos incluindo casos com 23 caras e 7 coroas. Conclui-se que existem evidências que nos levam a rejeitar nossa hipótese nula de que a moeda é honesta a um nível de 5% de significância.

Isso não quer dizer que não possa acontecer de termos 23 caras e 7 coroas, ou vice-versa, apenas que é muito raro.
°°°"""
# |%%--%%| <mdfd6i5frd|ApmHU99wBD>
r"""°°°
## Exercício 2
°°°"""
# |%%--%%| <ApmHU99wBD|fnICaCftuf>
r"""°°°
Você é o agente de um jogador da NBA que pretende receber o salário mais alto possível. Porém, apenas dois times estão interessados no jogador que você representa: Charlotte Hornets e Phoenix Suns. Ele notou que há uma diferença entre os dois times em relação ao salário médio e lhe pediu para checar se essa diferença pode ser explicada pelo acaso ou não.

Você utilizará o seguinte dataframe.
°°°"""
# |%%--%%| <fnICaCftuf|VbY5RddnOd>

df = pd.read_csv(
    "https://media.githubusercontent.com/media/icd-ufmg/material/master/aulas/11-Hipoteses/nba_salaries.csv"
)
df.head()

# |%%--%%| <VbY5RddnOd|rJwlfDhHJQ>

# diferença dos salários médios
df[df["TEAM"].isin(["Charlotte Hornets", "Phoenix Suns"])].groupby("TEAM").mean()

# |%%--%%| <rJwlfDhHJQ|Y4cvgteapP>
r"""°°°
**a)** Qual a estatística de teste?
°°°"""
# |%%--%%| <Y4cvgteapP|xBCuUNXF7i>

data = df[df["TEAM"].isin(["Charlotte Hornets", "Phoenix Suns"])]


def t_obs(data: pd.DataFrame) -> float:
    result: float = (
        data.query("TEAM == 'Phoenix Suns'")[["SALARY"]].mean()
        - data.query("TEAM == 'Charlotte Hornets'")[["SALARY"]].mean()
    )
    return result[0]


# |%%--%%| <xBCuUNXF7i|xmOmvlIbf7>

result = t_obs(data)
assert_equal(round(result, 2), -1.70)

# |%%--%%| <xmOmvlIbf7|0nk4kKKqrt>
r"""°°°
**b)** Agora responda ao jogador: Há diferença de salário significativa entre os clubes?

Utilize um nível de significância de 10%.
°°°"""
# |%%--%%| <0nk4kKKqrt|S9HwZ7aUql>


def difference_of_means(df, group_label) -> float:
    """Takes: data frame,
    column label that indicates the group to which the row belongs
    Returns: Difference of mean birth weights of the two groups"""

    reduced: pd.DataFrame = df[["SALARY", group_label]]
    means_table: pd.DataFrame = reduced.groupby(group_label).mean()
    mean_false: float = means_table.loc["Phoenix Suns"]["SALARY"]
    mean_true: float = means_table.loc["Charlotte Hornets"]["SALARY"]
    return mean_true - mean_false


def one_simulated_difference_of_means(df: pd.DataFrame, column: str) -> float:
    """Returns: Difference between mean maternal ages
    of babies of smokers and non-smokers after shuffling labels"""

    original_and_shuffled: pd.DataFrame = df.copy()
    original_and_shuffled["Shuffled Label"] = np.random.permutation(data[column].values)

    return difference_of_means(original_and_shuffled, "Shuffled Label")


def resposta(data) -> bool:

    repetitions: int = 5000
    differences: np.array = np.zeros(repetitions)
    column: str = "TEAM"

    for i in np.arange(repetitions):
        new_difference: float = one_simulated_difference_of_means(data, column)
        differences[i] = new_difference

    return differences.mean() < 0.1


# |%%--%%| <S9HwZ7aUql|TlL08LAZmY>

result = resposta(data)
assert_equal(result, True)

# |%%--%%| <TlL08LAZmY|2BNxLdgVLg>
r"""°°°
## P-valor e Significância
°°°"""
# |%%--%%| <2BNxLdgVLg|V6BWFxWm16>
r"""°°°
P-valor, ou valor-p, nada mais é do que a probabilidade de obter certo resultado de teste dada uma distribuição, ou seja, é a probabilidade do resultado ser o valor da estatística de teste.

Com o a estatística de teste encontramos uma probabilidade associada, o P-valor.

Já para significância o raciocínio é o oposto. Dado um nível de significância (probabilidade), encontramos o(s) valor(es) associado(s). Para um teste unilateral, teremos um valor e o nível de significância se mantém. Para um teste bilateral teremos dois valores e o nível de significância divide-se em dois. 


Veja o seguinte exemplo, com uma distribuição Normal de média 0 e variância 1.
°°°"""
# |%%--%%| <V6BWFxWm16|38N4yt0mpz>

# Gerando 10k dados de uma distribuição normal
np.random.seed(16)
x = np.random.normal(0, 1, 5000)

# normalizando apenas para deixar mais simétrico
data = (x - x.mean()) / x.std()
plt.hist(data, bins=15, rwidth=0.95)

# calculando percentis para um intervalo de 95% de confiança (5% de significância)
li = np.percentile(data, 2.5)
ls = np.percentile(data, 97.5)

# plotando
plt.fill_between([li, ls], 4, 2000, color="grey", alpha=0.8)
plt.ylim(top=2000)
plt.show()

# |%%--%%| <38N4yt0mpz|fYCrcXOGoy>
r"""°°°
Os limites cinzas são definidos com base no percentil da distribuição. Encontramos esses pontos com base no nível de significância. Um nível de significância de 5% indica que a área cinza contém 95% dos dados enquanto a ára branca contém os demais 5%, sendo 2,5% para baixo e 2,5% para cima.

Quando o interesse for analisar apenas um lado da distribuição, devemos alterar o valor do percentil, como no código abaixo.
°°°"""
# |%%--%%| <fYCrcXOGoy|n4Yg5vpWx1>

# normalizando apenas para deixar mais simétrico
data = (x - x.mean()) / x.std()
plt.hist(data, bins=15, rwidth=0.95)

# calculando percentis para um intervalo de 95% de confiança (5% de significância)
li = np.percentile(data, 5)

# plotando
plt.fill_between([li, 5], 4, 2000, color="grey", alpha=0.8)
plt.ylim(top=2000)
plt.xlim(right=4)
plt.show()

# |%%--%%| <n4Yg5vpWx1|3RGVI9AioT>
r"""°°°
Nesse caso, temos 5% dos dados à esquerda e o restante a direita. Note que o nível de significância se manteve constante, porém o valor de corte se alterou.
°°°"""
# |%%--%%| <3RGVI9AioT|16tg7lJZ2N>
r"""°°°
## Exercício 3
°°°"""
# |%%--%%| <16tg7lJZ2N|mM7TSNr1ZS>
r"""°°°
Neste exercício iremos realizar todas as etapas de um teste de hipóteses. Utilizaremos teste de permutação, porém a metodologia é bem semelhante nos outros casos também, e nos ajuda a mantermos uma linha de raciocínio muito clara e objetiva.


**Exercício:** Utilizaremos um novo conjunto de dados da NBA. Desejamos testar se há uma diferença significativa na altura dos jogadores dos times Cleveland Cavaliers e Golden State Warriors na temporada 2017-18, a um nível de significância de 5%.

**Raciocínio:** 
- 1 - Definir as hipóteses nula e alternativa.
- 2 - Encontrar a estatística de teste.
- 3 - Resampling/Shuffle de acordo com a hipótese nula.
- 4 - Encontrar os valores crítios/calcular o p-valor.
- 5 - Concluir (rejeitar ou não a hipótese).
°°°"""
# |%%--%%| <mM7TSNr1ZS|UdXGrcOPtG>

# preparação do dataset já está pronta
data = pd.read_csv(
    "https://raw.githubusercontent.com/pedroharaujo/ICD_Docencia/master/all_seasons.csv",
    index_col=0,
)
df = data[
    (data["team_abbreviation"].isin(["GSW", "CLE"])) & (data["season"] == "2017-18")
]
df.head()

# |%%--%%| <UdXGrcOPtG|whxmZx7kD7>
r"""°°°
1 - Definir as hipóteses!

$$H_0: \mu_CLE = \mu_{GSW}$$

$$H_1: \mu_{CLE} \neq \mu_{GSW}$$

Ou ainda

$$H_0: \mu_{CLE} - \mu_{GSW} = 0$$

$$H_1: \mu_{CLE} - \mu_{GSW} \neq 0$$

Note que como estamos testando a hipótese alternativa como DIFERENTE, o teste é bilateral. Logo, deveremos dividir o nível de significância em duas regiões cada uma com metade do valor.
°°°"""
# |%%--%%| <whxmZx7kD7|8p9HEdyS1i>
r"""°°°
**2 - Encontre a estatística de teste**

Altere a função abaixo para que retorne a estatística de teste.
°°°"""
# |%%--%%| <8p9HEdyS1i|tXnFeNFj5p>


def t_obs2(data: pd.DataFrame) -> float:
    result: float = (
        data.query("team_abbreviation == 'GSW'")[["player_height"]].mean()
        - data.query("team_abbreviation == 'CLE'")[["player_height"]].mean()
    )
    return result[0]


# |%%--%%| <tXnFeNFj5p|1ioYBb3LOn>

result = t_obs2(df)
assert_equal(round(result, 2), 1.43)

# |%%--%%| <1ioYBb3LOn|3Nb0NN6J2u>
r"""°°°
3 - Resampling/Shuffle

Sempre de acordo com a hipótese nula! Ou seja, se estamos querendo testar se a média de pontos entre os times é igual, devemos remover o fator TIME da equação para podermos comparar.

Como já fizemos isso anteriormente, essa função já será dada aqui. Note que atribuímos uma semente diferente de acordo com o valor de $i$ no *loop*, de forma a deixar o experimento replicável.
°°°"""
# |%%--%%| <3Nb0NN6J2u|ZmSr7E0SY7>


def shuffling(data: pd.DataFrame) -> np.array:
    repetitions: int = 5000
    filtro = data["team_abbreviation"] == "GSW"
    # t_obs = data[filtro]["player_height"].mean() - data[~filtro]["player_height"].mean()
    diffs = np.zeros(repetitions)
    for i in range(repetitions):
        np.random.seed(i)
        np.random.shuffle(filtro.values)
        diffs[i] = (
            data[filtro]["player_height"].mean() - data[~filtro]["player_height"].mean()
        )
    return diffs


diffs = shuffling(df)

# |%%--%%| <ZmSr7E0SY7|2NJlQZlWSQ>
r"""°°°
**4 - Encontrar valores críticos/Calcular o p-valor**

**a)** Altere a função abaixo para que calcule os valores críticos.
°°°"""
# |%%--%%| <2NJlQZlWSQ|bhltKvurnN>


def critical_values(diffs: np.array) -> tuple[float, float]:
    # nível de significância: 5%
    li = np.percentile(diffs, 2.5)
    ls = np.percentile(diffs, 97.5)

    # deve retornar uma tupla com os valores criticos
    # exemplo: (critico_inferior, critico_superior)
    return (li, ls)


# |%%--%%| <bhltKvurnN|qUY8cxfgf3>

(c_inf, c_sup) = critical_values(diffs)
assert_equal(round(c_inf, 2), -4.43)
assert_equal(round(c_sup, 2), 4.2)

# |%%--%%| <qUY8cxfgf3|KWLeN5a8G5>
r"""°°°
**b)** Calcule o p-valor.

Lembrete: o p-valor consiste na área a cima (ou abaixo, a depender do sinal) da estatística de teste. Consiste na probabilidade de valores superiores (ou inferiores) ao da estatística de teste.

Altere a função abaixo para retornar o p-valor, com base na estatística de teste.
°°°"""
# |%%--%%| <KWLeN5a8G5|SgVCCM6ens>


def p_value(t_obs: float, diffs: np.array) -> float:
    total: int = diffs.size
    menor: int = np.count_nonzero(diffs > t_obs)
    ratio: float = menor / total
    # deve retornar o p-valor ou seja,
    # a probabilidade de termos uma diferença maior que a estatística de teste
    return ratio


# |%%--%%| <SgVCCM6ens|GdJEzNttO6>

result: float = t_obs2(df)
foo = p_value(result, diffs)
assert_equal(round(foo, 2), 0.27)

# |%%--%%| <GdJEzNttO6|HJqYNkzGnz>
r"""°°°
**5 - Conclusão**

Altere a função a seguir para retornar o resultado do teste. 

Retorne `True` caso rejeite a hipótese nula e `False` caso não rejeite.
°°°"""
# |%%--%%| <HJqYNkzGnz|IiGfM7mJTP>


def resposta2(diffs: np.array, t_obs: float) -> bool:
    p = p_value(t_obs, diffs)
    # voce pode escolher como quer fazer
    # pode ser com base no p-valor calculado
    # ou com base nos limites calculados e na estatística de teste
    # porém, sua entrada deve ser o vetor diffs e a estatística de teste calculados anteriormente
    return p < 0.05


# |%%--%%| <IiGfM7mJTP|S8G2OjAwn9>

assert_equal(resposta2(diffs, result), False)
