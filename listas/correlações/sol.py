import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# |%%--%%| <xVQzaVwn6M|fXdO1alhfq>
r"""°°°
## Paradoxo de Simpson

Uma surpresa não incomum ao analisar dados é o Paradoxo de Simpson, no qual as correlações podem ser enganosas (ou *misleading*) quando variáveis confusas (ou *confounding variables*) são ignoradas.

Por exemplo, imagine que você pode identificar todos os membros  do *DataSciencester* como cientistas de dados da Costa Leste ou cientistas de dados da Costa Oeste. Você decide examinar quais cientistas de dados são mais amigáveis:


|Costa|# de membros|# médio de amigos|
| :-: | :-: | :-: |
|Oeste|101|8.2|
|Leste|103|6.5|

Certamente parece que os cientistas de dados da Costa Oeste são mais amigáveis do que os cientistas de dados da Costa Leste. Seus colegas de trabalho avançam todos os tipos de teorias sobre por que isso pode ser: talvez seja o sol, ou o café, ou os produtos orgânicos, ou a vibração descontraída do Pacífico?

Ao brincar com os dados, você descobre algo muito estranho. Se você olhar apenas para pessoas com PhDs, os cientistas de dados da Costa Leste têm mais amigos, em média. E se você olhar apenas para pessoas sem PhDs, os cientistas de dados da Costa Leste também têm mais amigos em média!


|Costa|PhD?|# de membros|# médio de amigos|
| :-: | :-: | :-: | :-: |
|Oeste|Sim|35|3.1|
|Leste|Sim|70|3.2|
|Oeste|Não|66|10.9|
|Leste|Não|33|13.4|

Depois de contabilizar se os usuários tem PhDs ou não, a correlação vai na direção oposta! Separar os dados somente entre Costa Leste e Costa Oeste escondeu o fato de que há muito mais cientistas de dados na Costa Leste com PhD (proporcionalmente) que na Costa Oeste.

Esse fenômeno surge no mundo real com alguma regularidade. A questão-chave é que a correlação está medindo a relação entre suas duas variáveis **sendo tudo o mais igual**. Se suas classes de dados são atribuídas aleatoriamente, como elas podem ser em um experimento bem projetado, "tudo o mais sendo igual" pode não ser uma suposição terrível. Mas quando há um padrão mais profundo para atribuições de classe, "tudo o mais sendo igual" pode ser uma suposição terrível. Nesse exemplo, se a proporção de cientistas de dados com PhD fosse igual na Costa Leste e Costa Oeste, então "ter PhD" deixaria de ser um fator de confusão para a variável "número médio de amigos".

Assim, a única maneira real de evitar fatores de confusão é conhecer seus dados e fazer o que puder para garantir que você tenha verificado tais fatores. Obviamente, isso nem sempre é possível. Se você não tivesse nos seus dados o nível educacional desses 200 cientistas de dados, você poderia simplesmente concluir que havia algo inerentemente mais sociável na Costa Oeste.
°°°"""
# |%%--%%| <fXdO1alhfq|74H7F1JHAW>
r"""°°°
O Paradoxo de Simpson também pode ser observado na taxa de sobrevivência do [naufrágio do RMS Titanic](https://en.wikipedia.org/wiki/RMS_Titanic). Havia uma estimativa de 2.224 passageiros e tripulantes a bordo, e mais de 1.500 morreram, tornando-se um dos mais mortais desastres marítimos comerciais em tempos de paz da história moderna. Dados sobre os passageiros podem ser baixados [aqui](https://ww2.amstat.org/publications/jse/v3n3/datasets.dawson.html). Este conjunto de dados foi processado por mim e transformado em um arquivo [csv](https://www.dropbox.com/s/vk8jf0wyczqxkvv/survival_titanic.csv?dl=0), que é muito mais fácil de tratar que um arquivo texto. Informações sobre ele podem ser lidas [aqui](https://www.dropbox.com/s/xpjw74khyqx9ww4/survival_titanic.README.txt?dl=0). 

Embora muitas outras informações existam sobre os passageiros, aqui vamos trabalhar com apenas quatro:

1) Se o passageiro sobreviveu;
2) A classe do seu bilhete (primeira, segunda ou terceira) ou se ele era membro da tripulação;
3) O sexo do passageiro;
4) E se ele era um adulto ou uma criança.

Primeiro, vamos carregar os dados:
°°°"""
# |%%--%%| <74H7F1JHAW|vaeBtGuP5v>

import pandas as pd

df = pd.read_csv(
    "https://media.githubusercontent.com/media/icd-ufmg/material/master/aulas/15-Correlacao/survival_titanic.csv"
)
df

# |%%--%%| <vaeBtGuP5v|WZ5hma4jX4>
r"""°°°
Se você leu o arquivo explicativo, viu que os dados estão organizados da seguinte maneira:

|Coluna|Descrição|Valores|
| :-: | :-: | :-: |
|0|Classe| 0 = tripulação, 1 = primeira, 2 = segunda, 3 = terceira|
|1|Idade|1 = adulto, 0 = criança|
|2|Sexo|1 = masculino, 0 = feminino|
|3|Sobreviveu?|1 = sim, 0 = não|
°°°"""
# |%%--%%| <WZ5hma4jX4|gHfb2qEcHU>
r"""°°°
Agora vamos montar uma tabela de contigência na mão. Para tal, vamos calcular a fração de pessoas que sobreviveram por classe. Podemos aplicar o group-by na classe e tirar a média. Lembrando que a média de 1s e 0s captura uma fração.

**Exercício 1**: use a função `groupby` do `Pandas` para calcular e exibir essa fração.
°°°"""
# |%%--%%| <gHfb2qEcHU|1J36txDeNB>

# Seu código aqui:

colunas = ["Survived", "class"]  # completar
coluna_groupby = "class"  # completar
df[colunas].groupby(coluna_groupby).mean()

# |%%--%%| <1J36txDeNB|Z28MyLMmU9>
r"""°°°
Aparentemente, a classe dos tripulantes (classe 0) é aquela com menor taxa de sobrevivência. Para verificar se o Paradoxo de Simpson ocorre, vamos quebrar a análise pelas outras duas colunas, idade (`Age`) e sexo (`Sex`). Para isso, basta agrupar a taxa de sobrevivência pelas duas colunas de interesse.

Primeiro, vamos quebrar pela idade.

**Exercício 2**: use a função `groupby` do `Pandas` para calcular e exibir essa fração quebrada por idade (`Age`).
°°°"""
# |%%--%%| <Z28MyLMmU9|MvxQOcqJAa>

# Seu código aqui:

colunas = ["Survived", "Age", "class"]  # completar
colunas_groupby = ["Age", "class"]  # completar
df[colunas].groupby(colunas_groupby).mean()

# |%%--%%| <MvxQOcqJAa|PUNAkWBJ1r>
r"""°°°
A única coisa que podemos ver aqui é que a taxa de sobrevivência de crianças é significativamente maior. Talvez se tivéssemos uma quantidade significativa de crianças, poderíamos observar o Paradoxo de Simpson.

Vamos agora quebrar por sexo.

**Exercício 3**: use a função `groupby` do `Pandas` para calcular e exibir essa fração quebrada por sexo (`Sex`).
°°°"""
# |%%--%%| <PUNAkWBJ1r|PQDQKdxolH>

# Seu código aqui:
colunas = ["Survived", "Sex", "class"]  # completar
colunas_groupby = ["Sex", "class"]  # completar
df[colunas].groupby(colunas_groupby).mean()

# |%%--%%| <PQDQKdxolH|PXJvVWWUz7>
r"""°°°
Quebrando a análise por sexo, podemos ver também que a taxa de sobrevivência de mulheres foi significativamente maior que a taxa de sobrevivência de homens. Além disso, por haver muito mais mulheres na terceira classe que na tripulação, isso mascarou o primeiro resultado, que indicava que membros da tripulação sobreviveram menos que os membros da terceira classe. Podemos ver agora que os membros da tripulação sobreviveram mais que os membros da terceira classe, o que configura o Paradoxo de Simpson.

**Exercício 4**: Para você confiar ainda mais nessa análise, observe a quantidade de pessoas de cada sexo por classe e note que há uma proporção muito menor de mulheres na classe `0` que na classe `3`.
°°°"""
# |%%--%%| <PXJvVWWUz7|sj9y9TJBDy>

# Seu código aqui:
filter: pd.DataFrame = df["Sex"] == 0
num_of_women = df[filter]["Sex"].count()
num_of_0 = df[filter]["class"][df["class"] == 0].count()
num_of_3 = df[filter]["class"][df["class"] == 3].count()
ratio_0 = num_of_0 / num_of_women
ratio_3 = num_of_3 / num_of_women
print(ratio_0, ratio_3)


# |%%--%%| <sj9y9TJBDy|5GWntJkeXL>
r"""°°°
## Valores-p de Correlações

Alguns pacotes, como o `scipy`, também calculam **valores-p** (ou *p-values*) de correlações. Esse valor-p refere-se à probabilidade da correlação ser explicada pela hipótese **H0** abaixo em detrimento da hipótese **H1**:

- **H0**: A correlação observada pode ser fruto do acaso, ou seja, é estatisticamente explicada por uma permutações aleatórias nos dados.
- **H1**: A correlação observada não é fruto do acaso, ou seja, permutações dos dados não podem gerar dados correlacionados dessa maneira.

°°°"""
# |%%--%%| <5GWntJkeXL|QUfaeOzZZJ>
r"""°°°
**Exercício 5**: Crie uma função que recebe dois *arrays numpy* e retorna a correlação de Pearson entre eles.
°°°"""
# |%%--%%| <QUfaeOzZZJ|GefCFWhwd0>

import numpy as np

# |%%--%%| <GefCFWhwd0|hvC3YFjKVS>

# seu codigo aqui:
def correlation(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.corrcoef(x, y)[1][0]


# |%%--%%| <hvC3YFjKVS|MIUeV3Q2vt>
r"""°°°

Observe como os dados abaixo tem uma correlação quase que perfeita!
°°°"""
# |%%--%%| <MIUeV3Q2vt|z6YM3RiudD>

x = np.array([7.1, 7.1, 7.2, 8.3, 9.4])
y = np.array([2.8, 2.9, 2.8, 2.6, 3.5])
plt.scatter(x, y, edgecolor="k", alpha=0.6, s=80)
print("correlação entre x e y:", correlation(x, y))

# |%%--%%| <z6YM3RiudD|dG4vsJltn5>
r"""°°°
No entanto, se permutarmos esses dados 10000 vezes...
°°°"""
# |%%--%%| <dG4vsJltn5|Nn5aBWTNk8>

# copia x para x_perm
x_perm = x.copy()
# vamos guardar os valores das correlações
perm_corr = []
for _ in range(10000):
    # permuta o vetor x
    np.random.shuffle(x_perm)
    # calcula a correlação e guarda no vetor perm_corr
    perm_corr.append(correlation(x_perm, y))


# |%%--%%| <Nn5aBWTNk8|8bSvL752v5>
r"""°°°
Temos agora 10000 valores de correlações, que foram calculadas a partir de permutações do vetor `x` original. Será que apenas o `x` original era correlacionado com `y`?
°°°"""
# |%%--%%| <8bSvL752v5|2IXHJngQ8c>

plt.hist(perm_corr, edgecolor="k")
plt.xlabel("Correlação na Permutação")
plt.ylabel("Quantidade de Permutações")
plt.vlines(correlation(x, y), 0, 2000, color="r")
plt.text(correlation(x, y), 2000, "Observado")


# |%%--%%| <2IXHJngQ8c|C7e9Mula7c>
r"""°°°
Podemos calcular agora quantos desses valores de correlações, gerados ao acaso, são maiores ou iguais ao valor observado:
°°°"""
# |%%--%%| <C7e9Mula7c|tHoclXw2Jh>

valor_p = sum(perm_corr > correlation(x, y)) / len(perm_corr)
print("valor_p", valor_p)

# |%%--%%| <tHoclXw2Jh|TqF3UBftno>
r"""°°°
Vamos calcular a correlação e o valor-p a partir do `scipy`:
°°°"""
# |%%--%%| <TqF3UBftno|5a3d7NRUU9>

from scipy import stats as ss

# |%%--%%| <5a3d7NRUU9|iFB0dgWRlX>

c, p = ss.pearsonr(x, y)
print(c, p)

# |%%--%%| <iFB0dgWRlX|6m5ZhOu3vG>
r"""°°°
A conclusão é que, de fato, a correlação entre x e y pode ser uma correlação espúria, ou seja, vinda do acaso. O valor-p indica que há uma alta probabilidade de conseguirmos uma correlção tão alta quanto a observada.
°°°"""
# |%%--%%| <6m5ZhOu3vG|uDJOzKGS7T>
r"""°°°
## Algumas Outras Advertências Correlacionais

Uma correlação de zero indica que não há relação linear entre as duas variáveis. No entanto, outros tipos de relacionamentos podem existir. Por exemplo, se:

`x = [-2, -1, 0, 1, 2]`

`y = [ 2, 1, 0, 1, 2]`

então `x` e `y` têm correlação zero. Mas eles certamente têm um relacionamento - cada elemento de `y` é igual ao valor absoluto do elemento correspondente de `x`. O que eles não têm é um relacionamento em que saber como `x_i` se compara à média de `x` (`mean(x)`) nos fornece informações sobre como `y_i` se compara à média de `y` (`mean(y)`). Esse é o tipo de relacionamento que a correlação procura.

Além disso, a correlação não informa nada sobre o tamanho do relacionamento. As variáveis:

`x = [-2, 1, 0, 1, 2]`

`y = [99.98, 99.99, 100, 100.01, 100.02]`

são perfeitamente correlacionados, mas (dependendo do que você está medindo) é bem possível que esse relacionamento não seja tão interessante.
°°°"""
# |%%--%%| <uDJOzKGS7T|G44cwAT8NM>
r"""°°°
## Correlação e Causalidade

Você provavelmente já ouviu, em algum momento, que "correlação não é causalidade", provavelmente por alguém que olha dados que representam um desafio para partes de sua visão de mundo que ele estava relutante em questionar. No entanto, este é um ponto importante - se `x` e `y` estão fortemente correlacionados, isso pode significar que `x` causa `y`, `y` causa `x`, que cada um causa o outro, que algum terceiro fator causa ambos, ou pode não significar nada.

Considere a relação entre `numero_amigos` e `minutos_diarios`. É possível que ter mais amigos no site faça com que os usuários do *DataSciencester* passem mais tempo no site. Este pode ser o caso se cada amigo publicar uma certa quantidade de conteúdo por dia, o que significa que quanto mais amigos você tiver, mais tempo levará para se manter atualizado a respeito das publicações deles.

No entanto, também é possível que quanto mais tempo você gasta discutindo nos fóruns do *DataSciencester*, mais você encontra e faz amizade com pessoas que pensam como você. Ou seja, passar mais tempo no site faz com que os usuários tenham mais amigos.

Uma terceira possibilidade é que os usuários mais apaixonados por ciência dos dados passem mais tempo no site (porque acham isso a coisa mais interessante do dia) e façam mais ativamente amigos que gostam de ciência de dados (porque não querem se associar a ninguém mais).

Uma maneira de se sentir mais confiante sobre a causalidade é conduzir estudos randomizados. Se você puder dividir seus usuários aleatoriamente em dois grupos com dados demográficos semelhantes e dar a um dos grupos uma experiência levemente diferente, então você poderá muitas vezes dizer que essa leve experiência está causando os diferentes resultados.

Por exemplo, se você não se importa em ser acusado de fazer experiências com seus usuários, você pode escolher aleatoriamente um subconjunto de usuários e mostrar a eles apenas uma fração de seus amigos. Se esse subconjunto subsequentemente passou menos tempo no site, isso lhe daria alguma confiança de que ter mais amigos causa mais tempo no site.
°°°"""
# |%%--%%| <G44cwAT8NM|cisMVpEKi8>
r"""°°°
## Para explorações futuras

* [`SciPy`](https://www.scipy.org/), [`pandas`](https://pandas.pydata.org/) e [`StatsModels`](https://www.statsmodels.org/stable/index.html) vêm com uma ampla variedade de funções estatísticas.

* Estatísticas são *importantes*. (Ou talvez as estatísticas *sejam* importantes?) Se você quer ser um bom cientista de dados, seria uma boa idéia ler um livro de estatísticas. Muitos estão disponíveis gratuitamente online. Dois exemplos:
 - [*OpenIntro Statistics*](https://www.openintro.org/stat/textbook.php)
 - [*OpenStax Introductory Statistics*](https://openstax.org/details/introductory-statistics)
°°°"""
# |%%--%%| <cisMVpEKi8|1qEUJUARph>
r"""°°°
## Dados Reais

Nesta aula vamos utilizados dados de preços de carros híbridos. Nos EUA, um carro híbrido pode rodar tanto em eletricidade quanto em combustível. A tabela contém as vendas de 1997 até 2003.

Uma máxima dessa aula será: **Sempre visualize seus dados**. 

As colunas são:

1. **vehicle:** modelo do carro
1. **year:** ano de manufatura
1. **msrp:** preço sugerido em 2013 e em USDs
1. **acceleration:** aceleração em km por hora por segundo
1. **mpg:** economia de combustível em milhas por galão
1. **class:** a classe do modelo

### Olhando para os Dados

Vamos iniciar olhando para cada coluna dos dados.
°°°"""
# |%%--%%| <1qEUJUARph|bWENAwhbgX>

df = pd.read_csv(
    "https://media.githubusercontent.com/media/icd-ufmg/material/master/aulas/15-Correlacao/hybrid.csv"
)
df["msrp"] = df["msrp"] / 1000
df.head()

# |%%--%%| <bWENAwhbgX|bHsKru1ITO>
r"""°°°
A coluna MSRP é o preço médio de venda. Cada linha da tabela é um carro. 

Vamos ver o histograma da aceleração:
°°°"""
# |%%--%%| <bHsKru1ITO|0wSdtrjcxL>

plt.hist(df["acceleration"], bins=20, edgecolor="k")
plt.title("Histograma de Aceleração")
plt.xlabel("Aceleração em Milhas por Hora")
plt.ylabel("Num. Carros")

# |%%--%%| <0wSdtrjcxL|YbsBoiOYpd>
r"""°°°
Agora vamos ver o histograma do preço sugerido:
°°°"""
# |%%--%%| <YbsBoiOYpd|IWVHUOPwAI>

plt.hist(df["msrp"], bins=20, edgecolor="k")
plt.title("Histograma de Modelos por Ano")
plt.xlabel("Preço em Mil. Dólar")
plt.ylabel("Num. Carros")


# |%%--%%| <IWVHUOPwAI|cBdXXC2m8p>
r"""°°°
Os gráficos acima nos dão uma visão geral dos dados. Note que, como esperado, cada coluna tem uma faixa diferente de valores no eixo-x. Além do mais, a concentração (lado esquerdo/direito) diferente entre as colunas. Como que podemos comparar as colunas? Cada uma está representada em uma unidade diferente.

Vamos fazer os gráficos de dispersão.

### Dispersão

Começamos com o gráfico que compara aceleração com o preço:
°°°"""
# |%%--%%| <cBdXXC2m8p|aWVi4fpSX4>

plt.scatter(df["acceleration"], df["msrp"], edgecolor="k", alpha=0.6, s=80)
plt.xlabel("MSRP")
plt.ylabel("Acc.")
plt.title("Consumo vs Acc")

# |%%--%%| <aWVi4fpSX4|fFoEYxGBBe>
r"""°°°
Tudo indica que há uma correlação entre os dois valores.

**Exercício 6**: calcule a correlação entre aceleração e preço. Indique se a correlação é significativa ou não através do seu valor-p.
°°°"""
# |%%--%%| <fFoEYxGBBe|hGqcEWEVNS>

# Seu código aqui:
statistic, pvalue = ss.pearsonr(df["acceleration"], df["msrp"])
print(statistic, pvalue)
# o valor-p é muito próximo de 0, o que significa que é muito improvável obter esses dados ao acaso, então a correlação é significativa

# |%%--%%| <hGqcEWEVNS|UJtVCpk2hu>
r"""°°°
Finalmente, o pairplot no Seaborn permite que você veja gráficos de dispersão e histogramas para várias colunas em uma tabela. Aqui brincamos com algumas das palavras-chave para produzir um gráfico de pares mais sofisticado e fácil de ler que incorpora linhas de mistura alfa e regressão linear para os gráficos de dispersão.
°°°"""
# |%%--%%| <UJtVCpk2hu|Z0Dx3fK3EX>

import seaborn as sns

fig = sns.pairplot(
    df[["msrp", "acceleration", "mpg", "class", "year"]],
    kind="reg",
    plot_kws={"line_kws": {"color": "red"}, "scatter_kws": {"alpha": 0.1}},
).fig

fig.savefig("out.png")

# |%%--%%| <Z0Dx3fK3EX|mjTz4tjspm>
r"""°°°
Você pode também calcular a matriz de correlações entre todas as colunas de um `DataFrame` usando a função `corr`:
°°°"""
# |%%--%%| <mjTz4tjspm|qH3yvXNgtt>

df.corr()

# |%%--%%| <qH3yvXNgtt|66mbChy5S4>
r"""°°°
Essa função calcula a correlação de `Pearson`, mas você pode calcular a de `Spearman`.
°°°"""
# |%%--%%| <66mbChy5S4|SMxdCmKYNx>

df.corr(method="spearman")

# |%%--%%| <SMxdCmKYNx|1PyPua9TWD>
r"""°°°
# Exercício Final

O professor disponibilizou uma planilha com as notas finais dos alunos que cursaram a disciplina *Programação e Desenvolvimento de Software - 1* da UFMG [neste link](https://drive.google.com/file/d/1Bm5mKv5FHHfaFycuVufV8FBWnk1Dh267/view?usp=sharing). Faça o download desse arquivo para realizar este exercício.


A planilha contém as seguintes informações:

- **Aluno**: código anonimizado do número de matrícula do aluno.
- **Praticas**: pontuação (no intervalo entre 0 e 5) obtida pelo aluno nas atividades práticas semanais. É uma forma de quantificar a *quantidade de horas* dedicada para a disciplina.
- **Ano**: ano em que a disciplina foi cursada.

### Objetivos do exercício:

1) Verificar se há correlação entre os pontos obtidos nas atividades práticas e a nota final.
2) Verificar se há diferenças entre as correlação do ano 2020 com a do ano 2021.
2) Verificar se as correlações mudam ao remover os alunos que desistiram do curso.

**Importante**: não se esqueça de lidar com os valores faltantes!
°°°"""
# |%%--%%| <1PyPua9TWD|atz9y4l2Cg>

df_alunos = pd.read_csv("notas_pds1.csv", delimiter=",", header="infer")
df_alunos.head()

# |%%--%%| <atz9y4l2Cg|6Za0oXUL5A>
r"""°°°
Verifique se há valores faltantes com a função `info()`.
°°°"""
# |%%--%%| <6Za0oXUL5A|QhTPreSt6L>

# Seu código aqui:
df_alunos.info()


# |%%--%%| <QhTPreSt6L|AHx9ajeItI>
r"""°°°
Troque os valores nulos por `0`.
°°°"""
# |%%--%%| <AHx9ajeItI|2qhAjRWRNr>

# Seu código aqui:
df_alunos = df_alunos.fillna(0)

# |%%--%%| <2qhAjRWRNr|norxQKu6KA>

df_alunos

# |%%--%%| <norxQKu6KA|BBf8w3YQJF>
r"""°°°
Os valores das colunas `Aluno`, `Praticas` e `Nota` estão com o tipo `object` e também com o caractere `,` separando a parte inteira da parte decimal. Substitua as `,` por `.` usando a função `str.replace` do `Pandas` e, depois, use a função `astype(float)` para converter os tipos para `float`.
°°°"""
# |%%--%%| <BBf8w3YQJF|oM4IZjHAdn>

# Seu código aqui:
df_alunos["Praticas"] = df_alunos["Praticas"].str.replace(",", ".").astype(float)
df_alunos["Nota"] = df_alunos["Nota"].str.replace(",", ".").astype(float)
df_alunos = df_alunos.fillna(0)

# |%%--%%| <oM4IZjHAdn|Eu3Xl2nozH>
r"""°°°
Calcule a correção entre a coluna `Praticas` e `Nota` usando a função `corr` do Pandas.
°°°"""
# |%%--%%| <Eu3Xl2nozH|0Oo2kXnK0C>

# Seu código aqui:
df_alunos.corr(numeric_only=True)["Praticas"]["Nota"]

# |%%--%%| <0Oo2kXnK0C|ZDMley8ODJ>
r"""°°°
Por fim, encontre as colunas que correspondem aos alunos que fizeram a disciplina em 2020 e também em 2021. Use a expressão `idx_ano = df["coluna"] == ano` para encontrar esses índices. Depois, calcule a correção nesses anos.
°°°"""
# |%%--%%| <ZDMley8ODJ|pQMbxQFfdM>

# Seu código aqui:
idx_2020 = df_alunos["Ano"] == 2020
idx_2021 = df_alunos["Ano"] == 2021

corr_2020 = df_alunos[idx_2020].corr(numeric_only=True)["Praticas"]["Nota"]
corr_2021 = df_alunos[idx_2021].corr(numeric_only=True)["Praticas"]["Nota"]
print(corr_2020, corr_2021)


# |%%--%%| <pQMbxQFfdM|dXE1j1aeG6>
r"""°°°
Como exercício final, remova todos os alunos desistentes e calcule as correlações novamente. Os alunos desistentes são aqueles que ficaram com `Nota` menor que `1`. Para isso, use a função `drop` do Pandas.
°°°"""
# |%%--%%| <dXE1j1aeG6|0sHrRx1qdp>

# Seu código aqui:
idx_desistentes = df_alunos["Nota"] < 1
df_nao_desistentes = df_alunos.drop(df_alunos.loc[idx_desistentes].index)
df_nao_desistentes.corr(numeric_only=True)["Praticas"]["Nota"]
