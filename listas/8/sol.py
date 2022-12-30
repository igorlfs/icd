r"""°°°
# Lista 8 - Verossimilhança
°°°"""
# |%%--%%| <kKoaNHkHrJ|xWZSO3o4Vh>
r"""°°°
## Introdução
°°°"""
# |%%--%%| <xWZSO3o4Vh|Cm98qhNOKZ>

# -*- coding: utf8

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy.testing import assert_equal
from scipy import stats as ss

import seaborn as sns

plt.rcParams["figure.figsize"] = (18, 10)
plt.rcParams["axes.labelsize"] = 10
plt.rcParams["axes.titlesize"] = 10
plt.rcParams["legend.fontsize"] = 10
plt.rcParams["xtick.labelsize"] = 10
plt.rcParams["ytick.labelsize"] = 10
plt.rcParams["lines.linewidth"] = 4

# |%%--%%| <Cm98qhNOKZ|LjpIGjt6lu>

plt.ion()
plt.style.use("seaborn-colorblind")
plt.rcParams["figure.figsize"] = (12, 8)

# |%%--%%| <LjpIGjt6lu|EcfykAtZ2x>


def despine(ax=None):
    if ax is None:
        ax = plt.gca()
    # Hide the right and top spines
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position("left")
    ax.xaxis.set_ticks_position("bottom")


# |%%--%%| <EcfykAtZ2x|98B3kfSOkQ>
r"""°°°
Continuando da aula passada. Vamos ver mais uma forma de entender um modelo de regressão linear. Lembre-se até agora falamos de correlação e covariância cobrindo os seguintes tópicos:

1. Covariância
1. Coeficiente de Pearson (Covariância Normalizada)
1. Coeficiente de Pearson como sendo a fração do desvio de y capturado por x
1. Mínimos Quadrados

Todos os passos acima chegam no mesmo local de traçar a "melhor" reta no gráfico de dispersão. Melhor aqui significa a reta que que minimiza o erro abaixo:

$$\Theta = [\alpha, \beta]$$
$$L(\Theta) = \sum_i (y_i - \hat{y}_i)^2$$
$$L(\Theta) = \sum_i (y_i - (\beta x_i + \alpha))^2$$

Chegamos em:

\begin{align}
 \alpha & = \bar{y} - \beta\,\bar{x}, \\[5pt]
  \beta &= \frac{ \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) }{ \sum_{i=1}^n (x_i - \bar{x})^2 } \\[6pt]
            &= \frac{ \operatorname{Cov}(x, y) }{ \operatorname{Var}(x) } \\[5pt]
            &= r_{xy} \frac{s_y}{s_x}. \\[6pt]
\end{align}
°°°"""
# |%%--%%| <98B3kfSOkQ|9Sup765d40>
r"""°°°
## Visão probabílistica
°°°"""
# |%%--%%| <9Sup765d40|V522plqnzz>
r"""°°°
Vamos aprender uma última forma de pensar na regressão. Em particular, vamos fazer uso de uma visão probabílistica. Para tal, exploraremos o caso dos apartamentos de BH abaixo.

Inicialmente, vamos observar os dados além do resultado da melhor regressão.
°°°"""
# |%%--%%| <V522plqnzz|JmQIckYna4>

df = pd.read_csv(
    "https://raw.githubusercontent.com/pedroharaujo/ICD_Docencia/master/aptosBH.txt",
    index_col=0,
)
df["preco"] = df["preco"] / 1000

plt.scatter(df["area"], df["preco"], edgecolors="k", s=80, alpha=0.6)

plt.title("Preço de Apartamentos em BH")
plt.ylabel(r"Preço * $10^3$ (R\$)")
plt.xlabel(r"Área ($M^2$)")
despine()

# |%%--%%| <JmQIckYna4|Zs90RAwivM>
r"""°°°
O seaborn tem uma função regplot que plota a melhor reta além de um intervalo de confiança.
°°°"""
# |%%--%%| <Zs90RAwivM|r6dnhuAdZT>

sns.regplot(
    x="area",
    y="preco",
    data=df,
    n_boot=10000,
    line_kws={"color": "magenta", "lw": 4},
    scatter_kws={"edgecolor": "k", "s": 80, "alpha": 0.8},
)
plt.title("Preco de Apartamentos em BH")
plt.ylabel(r"Preço * $10^3$ (R\$)")
plt.xlabel(r"Área ($M^2$)")
despine()

# |%%--%%| <r6dnhuAdZT|oLlLgr7fDX>
r"""°°°
A reta pode ser recuperada usando scipy.
°°°"""
# |%%--%%| <oLlLgr7fDX|zk24rTcRDL>

model = ss.linregress(df["area"], df["preco"])
model

# |%%--%%| <zk24rTcRDL|xUwR4PzJlE>
r"""°°°
Usando esta reta podemos prever o preço de um apartamento usando apenas a área do mesmo.
°°°"""
# |%%--%%| <xUwR4PzJlE|3JyJ8mVbYo>

beta = model.slope
alpha = model.intercept
novo_apt_area = 225
preco = beta * novo_apt_area + alpha
preco

# |%%--%%| <3JyJ8mVbYo|FRM7BARDK5>
r"""°°°
Ou seja, quando um apartamento de 225$m^2$ entra no mercado o mesmo custa em torno de 1M de reais.
°°°"""
# |%%--%%| <FRM7BARDK5|VE8QQjkNV8>
r"""°°°
## Erros Normais
°°°"""
# |%%--%%| <VE8QQjkNV8|jIoCtVoLvg>
r"""°°°
Agora, será que conseguimos chegar no mesmo pensando na regressão como um modelo probabilístico?

Ao invés de focar no valor quadrático do erro, vamos pensar no caso ideal. Qual seria o valor ideal do erro da minha regressão? ZERO! Porém, isso é possível somente quando temos relações lineares perfeitas (ex: x = altura em cm, y = altura em polegadas), o que não é o caso geral.

Nesse caso, vamos assumir que:
$$\epsilon_i \sim Normal(0, \sigma^2)$$

Isto é, cada um dos erros vem de uma distribuição normal com média 0. Ou seja, a média dos erros ainda vai ser uma normal centrada em 0. Além disso, o desvio padrão dos erros poderão ser estimados através dos dados após a regressão.

°°°"""
# |%%--%%| <jIoCtVoLvg|SK9D9TfmsX>
r"""°°°
## Verossimilhança
°°°"""
# |%%--%%| <SK9D9TfmsX|az8IMSxja5>
r"""°°°
Na regressão, queremos prever o valor de $y$ em função de $x$. No exemplo mostrado acima, queremos prever o preço de compra de um apartamento em BH em função da área.

Estamos assumindo que:
$$\epsilon_i = x_i - \beta x_i - \alpha$$

Ou seja, um erro na estimativa de um ponto não depende de outros.

Temos uma função de densidade de probabilidade para os erros:
$$\epsilon_i \sim Normal(0, \sigma^2)$$

Observe a função de densidade da Normal:
$$p(x|\mu, \sigma^2) = \frac{1}{\sqrt{\sigma^2 2 \pi}} e^{-\frac{(x-\mu)^2}{2 \sigma^2}}$$

Logo:
$$p(\epsilon_i|\mu, \sigma^2) = \frac{1}{\sqrt{\sigma^2 2 \pi}} e^{-\frac{(\epsilon_i-\mu)^2}{2 \sigma^2}}$$

Como no nosso modelo a média é zero, ficamos com:
$$p(\epsilon_i|\mu=0, \sigma^2) = \frac{1}{\sqrt{\sigma^2 2 \pi}} e^{-\frac{\epsilon_i^2}{2 \sigma^2}}$$
$$p(\epsilon_i|\sigma^2, \alpha, \beta) = \frac{1}{\sqrt{\sigma^2 2 \pi}} e^{-\frac{(y_i - \beta x_i - \alpha)^2}{2 \sigma^2}}$$

A probabilidade mostrada acima é a probabilidade de uma observação (observar o erro $\epsilon_i$) dado os parâmetros $\sigma^2$, $\alpha$ e $\beta$!  
Isto é uma **verossimilhança**!

O gráfico abaixo mostra a distribuição de probabilidade para erros vindos de uma distribuição normal com média igual a zero e desvio padrão igual a um.
°°°"""
# |%%--%%| <az8IMSxja5|QXMJcr9hw1>

x = np.linspace(-5, 5, 100)
plt.plot(x, ss.distributions.norm.pdf(x, scale=1))
plt.xlabel(r"$\epsilon_i$")
plt.ylabel(r"$p(\epsilon_i \mid \mu=0, \sigma=1)$")

despine()

# |%%--%%| <QXMJcr9hw1|6hgW3CvDT9>
r"""°°°
Um modelo estatístico na mais é do que um conjunto de hipóteses que se supõem válidas para a distribuição de probabilidades das variáveis aleatórias medidas na amostra.

Em particular, aqui estamos falando de modelos paramétricos, onde assumimos que o erro é uma normal e assumimos uma função de densidade (como mostrado no gráfico acima).

Vamos focar numa base de 3 pontos. Além do mais, vamos assumir uma reta qualquer, dessa forma, o desvio padrão dos erros podem ser estimados através dos dados após a regressão. Se os erros vem de uma distribuição normal com função de densidade já conhecida, qual dos três erros abaixo é o mais verossímil? 

Observe:
$$p(\epsilon_i|\sigma^2, \alpha, \beta) = \frac{1}{\sqrt{\sigma^2 2 \pi}} e^{-\frac{(y_i - \beta x_i - \alpha)^2}{2 \sigma^2}}$$

Quanto menor o erro, maior a probabilidade, sendo assim, o segundo erro é o mais verossímil.


°°°"""
# |%%--%%| <6hgW3CvDT9|GvC4DFkdPJ>

beta = 1
alpha = 1

fig = plt.figure(figsize=(36, 10))

x = np.array([2, 8, 5])
y = np.array([0, 1, 3])

plt.subplot(121)
plt.scatter(x, y, edgecolors="k", s=80, alpha=0.6)
plt.title("3 Pontinhos")
plt.ylabel(r"Y")
plt.xlabel(r"X")

y_bar = x * beta + alpha
plt.plot(x, y_bar, color="magenta")

y_min = [min(y_i, y_bar_i) for y_i, y_bar_i in zip(y, y_bar)]
y_max = [max(y_i, y_bar_i) for y_i, y_bar_i in zip(y, y_bar)]
plt.vlines(x, ymin=y_min, ymax=y_max, color="magenta", lw=1)

despine()

plt.subplot(122)
plt.title("PDF da Normal")
ei_x = np.linspace(-10, 10, 100)
sigma = (y - y_bar).std(ddof=1)
plt.plot(ei_x, ss.distributions.norm.pdf(ei_x, scale=sigma))
plt.xlabel(r"$\epsilon_i$")
plt.ylabel(r"$p(\epsilon_i \mid \mu=0, \sigma={})$".format(np.round(sigma, 2)))
despine()

# |%%--%%| <GvC4DFkdPJ|FBBFSFpYc3>
r"""°°°
Observe o exemplo considerando agora todos os pontos do exemplo de predição de preço de apartamentos em BH.
°°°"""
# |%%--%%| <FBBFSFpYc3|OFMdQVFzCG>

beta = 3.535719156333653
alpha = 200.52361368989432

fig = plt.figure(figsize=(36, 16))

x = df["area"]
y = df["preco"]

plt.subplot(121)
plt.scatter(x, y, edgecolors="k", s=80, alpha=0.6)
plt.title("Preco de Apartamentos em BH")
plt.ylabel(r"Preço * $10^3$ (R\$)")
plt.xlabel(r"Área ($M^2$)")

y_bar = x * beta + alpha
plt.plot(x, y_bar, color="magenta")

y_min = [min(y_i, y_bar_i) for y_i, y_bar_i in zip(y, y_bar)]
y_max = [max(y_i, y_bar_i) for y_i, y_bar_i in zip(y, y_bar)]
plt.vlines(x, ymin=y_min, ymax=y_max, color="magenta", lw=1)

despine()

plt.subplot(122)
plt.title("PDF da Normal")
ei_x = np.linspace(-1000, 1000, 100)
sigma = (y - y_bar).std(ddof=1)
plt.plot(ei_x, ss.distributions.norm.pdf(ei_x, scale=sigma))
plt.xlabel(r"$\epsilon_i$")
plt.ylabel(r"$p(\epsilon_i \mid \mu=0, \sigma={})$".format(np.round(sigma, 2)))
despine()

# |%%--%%| <OFMdQVFzCG|4M97h47RgO>
r"""°°°
## Erros Independentes
°°°"""
# |%%--%%| <4M97h47RgO|PbBU3ycqc3>
r"""°°°
Nos exemplos acima discutimos sobre qual erro é o mais verossímil... Mas como podemos calcular a verossimilhança de todos os erros?

Ao assumir **independência**, estamos dizendo que:
$$p(E|\sigma^2, \alpha, \beta) = \prod_i p(\epsilon_i|\sigma^2, \alpha, \beta) = \prod_i p(\epsilon_i|\theta)$$
onde $E = \{e_1, e_2, ..., e_n\}$ e $\theta = \{\sigma^2, \alpha, \beta\}$


Acabamos de definir nossa primeira função de verossimilhança. Como podemos proceder agora? Maximizando a mesma! Ou seja, queremos os parâmetros ($\theta$) que melhor se ajustam os nossos dados. 
Porém, maximizar produtórios é chato... O mundo das somas é mais bacana do que o mundo da multiplicação.
°°°"""
# |%%--%%| <PbBU3ycqc3|WMjraDOnAf>
r"""°°°
## Log-verossimilhança
°°°"""
# |%%--%%| <WMjraDOnAf|zi0gqGWhDm>
r"""°°°
Como o log é uma função monotonicamente crescente, maximizar o log(f(x)) é equivalente a maximizar f(x). Portanto vamos trabalhar no log.

Ao invés de maximizar a função de **verossimilhança** $L(\theta)$, vamos maximizar a função de **log-verossimilhança** $l(\theta)$:

$$L(\theta) = \prod_i p(\epsilon_i|\theta)$$
$$log(L(E|\theta)) = log(\prod_i p(\epsilon_i|\theta))$$
$$l(\epsilon_i|\theta) = \sum_i log(p(\epsilon_i|\theta))$$
uma vez que $log(A*B) = log(A) + log(B)$.

Substituindo os parâmetros $\sigma^2$, $\alpha$, $\beta$ nas funções e fazendo algumas manipulações, temos que a verossimilhança e a log-verossimilhança são dadas por:

$$L(E|\theta) = \prod_i \frac{1}{\sqrt{\sigma^2 2 \pi}} e^{-\frac{(y_i - \beta x_i - \alpha)^2}{2 \sigma^2}}$$

$$l(E|\theta) = -nlog(\sqrt{2\pi}) -nlog(\sigma) - \frac{\sum_i (y_i - \beta x_i - \alpha)^2}{2 \sigma^2}$$
°°°"""
# |%%--%%| <zi0gqGWhDm|XDjtdUlzga>
r"""°°°
* A partir da fórmula da verossimilhança, dada por:
$$L(E|\theta) = \prod_i \frac{1}{\sqrt{\sigma^2 2 \pi}} e^{-\frac{(y_i - \beta x_i - \alpha)^2}{2 \sigma^2}}$$
verifique que a expressão da log-verossimilhança é dada por:
$$l(E|\theta) = -nlog(\sqrt{2\pi}) -nlog(\sigma) - \frac{\sum_i (y_i - \beta x_i - \alpha)^2}{2 \sigma^2}$$
°°°"""
# |%%--%%| <XDjtdUlzga|FiMciogiXM>
r"""°°°
$$L(E|\theta) = \prod_i \frac{1}{\sqrt{\sigma^2 2 \pi}} e^{-\frac{(y_i - \beta x_i - \alpha)^2}{2 \sigma^2}}$$
$$log(L(E|\theta)) = log(\prod_i \frac{1}{\sqrt{\sigma^2 2 \pi}} e^{-\frac{(y_i - \beta x_i - \alpha)^2}{2 \sigma^2}})$$
$$l(\epsilon_i|\theta) = \sum_i log(\frac{1}{\sqrt{\sigma^2 2 \pi}} e^{-\frac{(y_i - \beta x_i - \alpha)^2}{2 \sigma^2}})$$
uma vez que $log(A*B) = log(A) + log(B)$.
$$l(\epsilon_i|\theta) = \sum_i log(\frac{1}{\sqrt{\sigma^2 2 \pi}}) + \sum_i log(e^{-\frac{(y_i - \beta x_i - \alpha)^2}{2 \sigma^2}})$$
$$l(\epsilon_i|\theta) = n log(\frac{1}{\sqrt{\sigma^2 2 \pi}}) + \sum_i log(e^{-\frac{(y_i - \beta x_i - \alpha)^2}{2 \sigma^2}})$$
$$l(\epsilon_i|\theta) = n log(\frac{1}{\sqrt{\sigma^2 2 \pi}}) - \frac{\sum_i (y_i - \beta x_i - \alpha)^2}{2 \sigma^2}$$
uma vez que $log(A^x) = x log(A)$ e $log(e) = 1$.
$$l(\epsilon_i|\theta) = - n log(\sqrt{\sigma^2 2 \pi}) - \frac{\sum_i (y_i - \beta x_i - \alpha)^2}{2 \sigma^2}$$
uma vez que $log(\frac{1}{x}) = - log(x)$.
$$l(\epsilon_i|\theta) = - n log(\sqrt{2 \pi}) - n log(\sqrt{\sigma}) - \frac{\sum_i (y_i - \beta x_i - \alpha)^2}{2 \sigma^2}$$
°°°"""
# |%%--%%| <FiMciogiXM|GF3BgmIP3I>
r"""°°°
Maximizar a log verossimilhança implica em achar os parâmetros que melhor se ajustam aos dados. Além disso, lembre-se que maximizar é achar o local onde a derivada é zero.

Para isso, devemos resolver as derivadas em relação a cada um dos parâmetros: $\sigma$, $\alpha$ e $\beta$. 

$$\alpha = \bar{y} - \beta \bar{x}$$
$$\beta = \frac{ \sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y}) }{ \sum_{i=1}^n (x_i - \bar{x})^2 }$$
$$\sigma^2 = \frac{\sum_i (y_i - \beta x_i - \alpha)^2}{n}$$

Observe que ao maximizar $\sigma$, chegamos no estimador da variância. Além disso, o $\sigma$ não impacta os valores de $\alpha$ e $\beta$, mas é útil para entendermos os erros do estimador (é a variância dos erros afinal).

Por fim, note que maximizar a verossimilhança da regressão é o mesmo que minimizar os erros quadrados.

°°°"""
# |%%--%%| <GF3BgmIP3I|blI757mEMg>
r"""°°°
## Estimação da Máxima Verossimilhança e Mínimos Quadrados
°°°"""
# |%%--%%| <blI757mEMg|7tATz70Y8r>
r"""°°°
Por que escolher os mínimos quadrados? Uma justificativa envolve a estimativa de máxima verossimilhança.

Imagine que temos uma amostra de dados $v_1, \cdots, v_n$ que vem de uma distribuição que depende de algum parâmetro desconhecido $\theta$:

$$p(v_1, \cdots, v_n~|~\theta)$$

Se não conhecêssemos theta, poderíamos nos virar e pensar nessa quantidade como a probabilidade de $\theta$ dada a amostra:

$$L(\theta~|~v_1, \cdots, v_n)$$

Sob essa abordagem, o mais provável $\theta$ é o valor que maximiza essa função de verossimilhança; isto é, o valor que torna os dados observados os mais prováveis. No caso de uma distribuição contínua, na qual temos uma função de distribuição de probabilidade e não uma função de massa de probabilidade, podemos fazer a mesma coisa.

De volta à regressão. Uma suposição que muitas vezes é feita sobre o modelo de regressão simples é que os erros de regressão são normalmente distribuídos com média $0$ e algum desvio padrão (conhecido) $\sigma$. Se esse for o caso, a probabilidade baseada em ver um par $(x_i, y_i)$ é:

$$L(\alpha, \beta~|~x_i, y_i, \sigma) = \frac{1}{\sqrt{2\pi\sigma}}\exp{\big(\frac{-(y_i-\alpha-\beta x_i)^2}{2\sigma^2}\big)}$$

A probabilidade baseada em todo o conjunto de dados é o produto das probabilidades individuais, que é maior precisamente quando alfa e beta são escolhidos para minimizar a soma dos erros quadrados. Ou seja, nesse caso (e com essas suposições), minimizar a soma dos erros quadrados é equivalente a maximizar a probabilidade dos dados observados.
°°°"""
# |%%--%%| <7tATz70Y8r|UM7rwvpFgs>
r"""°°°
## Qualidade da regressão
°°°"""
# |%%--%%| <UM7rwvpFgs|OFypOaTyoR>
r"""°°°
Após encontrar os parâmetros do modelo que melhor se ajustam aos dados (minimizam os erros quadrados, maximizam a verossimilhança), devemos avaliar a qualidade do ajuste. A qualidade da regressão pode ser analisada através de gráficos ou métricas, como o R-quadrado, estudado anteriormente.

°°°"""
# |%%--%%| <OFypOaTyoR|4K9Ao74Zhp>
r"""°°°
## Gráfico residual
°°°"""
# |%%--%%| <4K9Ao74Zhp|fQvpxh5ily>
r"""°°°
O gráfico residual é uma forma de visualizar os erros versus a variável preditora para verificar a pressuposição de que os erros são aleatoriamente distribuídos e têm variância constante. De maneira ideal, os pontos devem cair aleatoriamente em ambos os lados de 0, sem padrões reconhecíveis nos pontos. Como os erros são centrados em zero, ao plotar valor de x pelo erro queremos pontos igualmente dispersados  positivos e negativos.
Lembre-se da PDF da distribuição normal. A mediana e a média são iguais, ou seja, 50% dos erros se concentram acima de 0 e 50% abaixo.

Observe o gráfico residual para o exemplo de prever o preço de um apartamento usando apenas a área do mesmo. No eixo-x temos a área do aparatamento e no eixo-y o erro. O gráfico não parece ter um padrão (é o que queremos) já que os erros estão espalhados em ambos os lados da linha tracejada que marca o erro igual a 0. Entretanto, os erros aparentam ser piores quando a área dos apartamentos (variável x) aumenta.

°°°"""
# |%%--%%| <fQvpxh5ily|cT6vA85Jdt>

sns.residplot(
    x="area",
    y="preco",
    data=df,
    line_kws={"color": "magenta", "lw": 4},
    scatter_kws={"edgecolor": "k", "s": 80, "alpha": 0.8},
)
plt.ylabel(r"$\epsilon_i$")
plt.xlabel(r"Área ($M^2$)")
despine()

# |%%--%%| <cT6vA85Jdt|kmSyEbVugh>
r"""°°°
## QQ Plot
°°°"""
# |%%--%%| <kmSyEbVugh|zeIzNnZ7SH>
r"""°°°
Por fim, outra forma de verificar se o modelo é bom se chama QQ Plot.
Esse gráfico é útil para checar a adequação da distribuição de frequência dos dados à uma distribuição de probabilidades. No caso dos modelos de regressão, o QQ Plot é usado para verificar se os erros apresentam distribuição normal.

Uma forma de construir o QQ Plot consiste em ordenar os erros (eixo-y), comparando com o local esperado do mesmo no modelo (distribuição normal). Nesse caso, a mediana fica no centro do plot. O erro mediano é zero caso a normal seja verdadeira!

Outra forma de construir o QQ Plot consiste em pegar o valor z-norm que leva para a probabilidade de cada um dos erros ordenados no modelo e plotar os erros ordenados no eixo-y e os valores z-normalizados no eixo-x. O gráfico abaixo apresenta o QQ Plot do exemplo de prever o preço de um apartamento usando apenas a área do mesmo.

Idealmente quanto mais próximo de uma reta melhor, uma vez que a reta quer dizer que os erros são perfeitamente normais. Sendo assim, na regressão perfeita observamos uma linha reta no QQ plot.
°°°"""
# |%%--%%| <zeIzNnZ7SH|mrTSw2930r>

ss.probplot(y - y_bar, plot=plt.gca())

# |%%--%%| <mrTSw2930r|voVRLAVGO0>
r"""°°°
## Exercícios - Outros datasets
°°°"""
# |%%--%%| <voVRLAVGO0|GyMLXWHQ8k>
r"""°°°
### Enunciado
°°°"""
# |%%--%%| <GyMLXWHQ8k|TyEuHOrKeG>
r"""°°°
Abaixo estão listados algumas conjuntos de dados contendo relações entre variáveis:

**Supernovas**: Atualmente, uma das teorias mais aceitas sobre a formação do universo, diz que o universo está em constante expansão. Supernovas são estrelas que explodiram e morreram recentemente. Os dados contêm registros dessas supernovas. Cada linha na tabela corresponde a uma supernova próxima da Terra observada por astrônomos, indicando o quão longe da Terra a supernova estava e o quão rápido ela se afastava.

**Stocks and Unemployment**: A Bolsa está diretamente ligada à economia do país e do mundo. Quando ela desaba, isso pode ter consequências negativas até no dia a dia de quem nem sabe como a Bolsa funciona. Por exemplo, o desemprego pode aumentar e a inflação, acelerar, tornando os produtos no supermercado mais caros. Com base nisso, os dados apresentam a evolução no preço de uma ação e a taxa de desemprego em determinado período.

**Stocks and Interest**: Além de relacionar o valor de ações na Bolsa com o índice de desemprego, é possível correlacionar o valor das ações e outros indicadores. Os dados apresentam a evolução no preço de uma ação e a taxa de juros em determinado período.


**Dugongs**: Os dados incluem informações de peixe-bois. Cada linha contém o comprimento e a idade de indivíduos. A base de dados é muito utilizada para fazer predições do comprimento desses animais de acordo com a idade.
°°°"""
# |%%--%%| <TyEuHOrKeG|cnPNYxZl3y>
r"""°°°
- **Exercício:** Para cada um dos datasets você deverá:

    1. Carregar os dados do arquivo.  
    2. Fazer uma regressão linear.  
    3. Avaliar a qualidade do modelo através do cálculo do $R^2$ e dos gráficos de erros: Gráfico residual e QQ Plot.  
    4. Verificar se os erros são independentes. Para isso, conte quantos erros são maiores e quantos são menores do que zero. 

Antes de realizar o exercício, é útil você definir as seguintes funções com base nos parâmetros citados em cada uma:

Note que após definir as funções pedidas corretamente até o fim do primeiro dataset, os demais irão executar sem erros, não precisando ser alterados.
°°°"""
# |%%--%%| <cnPNYxZl3y|DIiBBkKzIO>


def predict(alpha: float, beta: float, x_i: float):
    return beta * x_i + alpha


def error(alpha: float, beta: float, x: float, y: float):
    return y - predict(alpha, beta, x)


def sum_of_squared_errors(alpha, beta, x, y):
    return


def total_sum_of_squares(y):
    return


def r_squared(alpha, beta, x, y):
    sq_res = sum((y - (beta * x + alpha)) ** 2)
    y_mean = y.mean()
    sq_tot = sum((y - y_mean) ** 2)
    return 1 - sq_res / sq_tot


# |%%--%%| <DIiBBkKzIO|tJpvvFWEgi>
r"""°°°
### 1. Supernovas
°°°"""
# |%%--%%| <tJpvvFWEgi|1wlaMN7y1k>
r"""°°°
#### 1.1 Carregar os dados
°°°"""
# |%%--%%| <1wlaMN7y1k|M9GdAbesUA>

df = pd.read_csv(
    "https://raw.githubusercontent.com/pedroharaujo/ICD_Docencia/master/close_novas.csv"
)
x = df["Distance (million parsecs)"]
y = df["Speed (parsecs/year)"]

# |%%--%%| <M9GdAbesUA|6V7zo9H9Vs>
r"""°°°
#### 1.2 Regressão Linear
°°°"""
# |%%--%%| <6V7zo9H9Vs|SvumvWubo0>


def linear_regression(x, y):
    covariance = np.cov(x, y)
    beta: float = covariance[1][0] / covariance[0][0]
    x_mean: float = x.mean()
    y_mean: float = y.mean()
    alpha: float = y_mean - beta * x_mean
    return alpha, beta


# |%%--%%| <SvumvWubo0|LoWn2vxsxV>

(a1, b1) = linear_regression(x, y)
assert_equal(round(a1, 6), 0.000167)
assert_equal(round(b1, 6), 0.000068)

# |%%--%%| <LoWn2vxsxV|TPoNjg9LFj>
r"""°°°
#### 1.3 Avaliação do Modelo via R²
°°°"""
# |%%--%%| <TPoNjg9LFj|THhL6eeR1s>

# avaliacao do Rsquared
r2 = r_squared(a1, b1, x, y)
assert_equal(round(r2, 4), 0.9645)

# |%%--%%| <THhL6eeR1s|mo8bsciFb2>

# avaliacao via grafico dos residuos (sem correcao automatica)

# seu codigo aqui
# gabarito a seguir
sns.residplot(
    x="Distance (million parsecs)",
    y="Speed (parsecs/year)",
    data=df,
    line_kws={"color": "magenta", "lw": 4},
    scatter_kws={"edgecolor": "k", "s": 80, "alpha": 0.8},
)
plt.ylabel(r"$\epsilon_i$")
despine()
# que coincidêndia, ficou igual ao gabarito!


# |%%--%%| <mo8bsciFb2|6UvnMnfpOi>

# GABARITO GRAFICO
# sns.residplot(x='Distance (million parsecs)', y='Speed (parsecs/year)', data=df,
#               line_kws={'color':'magenta', 'lw':4},
#               scatter_kws={'edgecolor':'k', 's':80, 'alpha':0.8})
# plt.ylabel(r'$\epsilon_i$')
# despine()
# plt.show()

# |%%--%%| <6UvnMnfpOi|F4XVOaEaln>
r"""°°°
#### 1.4 Verificando se os erros são independentes
°°°"""
# |%%--%%| <F4XVOaEaln|qeumsDbaFQ>


def error_verification(alpha, beta, x, y):
    pos: int = 0
    neg: int = 0
    for (i, j) in zip(x, y):
        if error(alpha, beta, i, j) > 0:
            pos += 1
        else:
            neg += 1
    return (pos, neg)


# |%%--%%| <qeumsDbaFQ|XHC2EB19Tr>

(maiores, menores) = error_verification(a1, b1, x, y)
assert_equal(maiores, 78)
assert_equal(menores, 78)

# |%%--%%| <XHC2EB19Tr|GqLSpKZ8He>

# avaliacao via grafico dos residuos (sem correcao automatica)

# seu codigo aqui
# gabarito a seguir
ss.probplot(y - y.mean(), plot=plt)
despine()
# estou craque nisso

# |%%--%%| <GqLSpKZ8He|77BFPmjMjQ>

# ss.probplot(y - y.mean(), plot=plt)
# despine()
# plt.show()

# |%%--%%| <77BFPmjMjQ|JbL62eUy5N>
r"""°°°
### 2. Stocks anad Unemployment
°°°"""
# |%%--%%| <JbL62eUy5N|m2Mn72QkNj>
r"""°°°
#### 2.1 Carregar os dados
°°°"""
# |%%--%%| <m2Mn72QkNj|ka3Q5u5Kda>

df = pd.read_csv(
    "https://raw.githubusercontent.com/pedroharaujo/ICD_Docencia/master/stocks_unemployment.csv"
)
x = df["Unemployment_Rate"]
y = df["Stock_Index_Price"]

# |%%--%%| <ka3Q5u5Kda|3Uls4Yab8s>
r"""°°°
#### 2.2 Regressão Linear
°°°"""
# |%%--%%| <3Uls4Yab8s|nf6KhPWIaF>

(a2, b2) = linear_regression(x, y)
assert_equal(round(a2, 6), 4471.339321)
assert_equal(round(b2, 6), -588.962076)

# |%%--%%| <nf6KhPWIaF|2Xo4XMfaAK>
r"""°°°
#### 2.3 Avaliação do Modelo via R²
°°°"""
# |%%--%%| <2Xo4XMfaAK|KhafPGkD0p>

# avaliacao do Rsquared
r2 = r_squared(a2, b2, x, y)
assert_equal(round(r2, 4), 0.8507)

# |%%--%%| <KhafPGkD0p|nY4XztxlCV>

# avaliacao via grafico dos residuos (sem correcao automatica)

# seu codigo aqui
# gabarito a seguir
sns.residplot(
    x="Unemployment_Rate",
    y="Stock_Index_Price",
    data=df,
    line_kws={"color": "magenta", "lw": 4},
    scatter_kws={"edgecolor": "k", "s": 80, "alpha": 0.8},
)
plt.ylabel(r"$\epsilon_i$")
despine()


# |%%--%%| <nY4XztxlCV|Y24IpRJCFf>

# GABARITO GRAFICO
# sns.residplot(x='Unemployment_Rate', y='Stock_Index_Price', data=df,
#               line_kws={'color':'magenta', 'lw':4},
#               scatter_kws={'edgecolor':'k', 's':80, 'alpha':0.8})
# plt.ylabel(r'$\epsilon_i$')
# despine()
# plt.show()

# |%%--%%| <Y24IpRJCFf|Czm9vJw4Uc>
r"""°°°
#### 2.4 Verificando se os erros são independentes
°°°"""
# |%%--%%| <Czm9vJw4Uc|EC8YHsp0B4>

(maiores, menores) = error_verification(a2, b2, x, y)
assert_equal(maiores, 13)
assert_equal(menores, 11)

# |%%--%%| <EC8YHsp0B4|hCt1Rjs1Sh>

# avaliacao via grafico dos residuos (sem correcao automatica)

# seu codigo aqui
# gabarito a seguir
ss.probplot(y - y.mean(), plot=plt)
despine()

# |%%--%%| <hCt1Rjs1Sh|cplx47Ex6l>

# ss.probplot(y - y.mean(), plot=plt)
# despine()
# plt.show()

# |%%--%%| <cplx47Ex6l|f43Aqpuufu>
r"""°°°
### 3. Stocks and Interest
°°°"""
# |%%--%%| <f43Aqpuufu|RJ81x4XjFD>
r"""°°°
#### 3.1 Carregar os dados
°°°"""
# |%%--%%| <RJ81x4XjFD|VZAxFuSj1B>

df = pd.read_csv(
    "https://raw.githubusercontent.com/pedroharaujo/ICD_Docencia/master/stocks_interest.csv"
)
x = df["Interest_Rate"]
y = df["Stock_Index_Price"]

# |%%--%%| <VZAxFuSj1B|jwPLvelCFV>
r"""°°°
#### 3.2 Regressão Linear
°°°"""
# |%%--%%| <jwPLvelCFV|YbBipHZm3d>

(a3, b3) = linear_regression(x, y)
assert_equal(round(a3, 6), -99.464319)
assert_equal(round(b3, 6), 564.203892)

# |%%--%%| <YbBipHZm3d|a06FO6WNXd>
r"""°°°
#### 3.3 Avaliação do Modelo via R²
°°°"""
# |%%--%%| <a06FO6WNXd|elqeEjlO1i>

# avaliacao do Rsquared
r2 = r_squared(a3, b3, x, y)
assert_equal(round(r2, 4), 0.8757)

# |%%--%%| <elqeEjlO1i|gubRb2pXI7>

# avaliacao via grafico dos residuos (sem correcao automatica)

# seu codigo aqui
# gabarito a seguir
sns.residplot(
    x="Interest_Rate",
    y="Stock_Index_Price",
    data=df,
    line_kws={"color": "magenta", "lw": 4},
    scatter_kws={"edgecolor": "k", "s": 80, "alpha": 0.8},
)
plt.ylabel(r"$\epsilon_i$")
despine()


# |%%--%%| <gubRb2pXI7|2TQRkDRfkD>

# GABARITO GRAFICO
# sns.residplot(x='Interest_Rate', y='Stock_Index_Price', data=df,
#               line_kws={'color':'magenta', 'lw':4},
#               scatter_kws={'edgecolor':'k', 's':80, 'alpha':0.8})
# plt.ylabel(r'$\epsilon_i$')
# despine()
# plt.show()

# |%%--%%| <2TQRkDRfkD|Vd55lqa9tJ>
r"""°°°
#### 3.4 Verificando se os erros são independentes
°°°"""
# |%%--%%| <Vd55lqa9tJ|MA1nWWZ0eY>

(maiores, menores) = error_verification(a3, b3, x, y)
assert_equal(maiores, 12)
assert_equal(menores, 12)

# |%%--%%| <MA1nWWZ0eY|JukhOmdVok>

# avaliacao via grafico dos residuos (sem correcao automatica)

# seu codigo aqui
# gabarito a seguir
ss.probplot(y - y.mean(), plot=plt)
despine()

# |%%--%%| <JukhOmdVok|OO1p8NyHfv>

# ss.probplot(y - y.mean(), plot=plt)
# despine()
# plt.show()

# |%%--%%| <OO1p8NyHfv|wiXv7fbCJ5>
r"""°°°
### 4. Dugongs
°°°"""
# |%%--%%| <wiXv7fbCJ5|980gXaroz6>
r"""°°°
#### 4.1 Carregar os dados
°°°"""
# |%%--%%| <980gXaroz6|6iZMCLya31>

df = pd.read_csv(
    "https://raw.githubusercontent.com/pedroharaujo/ICD_Docencia/master/dugongs.csv"
)
x = df["Age"]
y = df["Length"]

# |%%--%%| <6iZMCLya31|Jzo4YREHKN>
r"""°°°
#### 4.2 Regressão Linear
°°°"""
# |%%--%%| <Jzo4YREHKN|M5CY8TrLTR>

(a4, b4) = linear_regression(x, y)
assert_equal(round(a4, 6), 2.018286)
assert_equal(round(b4, 6), 0.028955)

# |%%--%%| <M5CY8TrLTR|LtQOEj5TyH>
r"""°°°
#### 4.3 Avaliação do Modelo via R²
°°°"""
# |%%--%%| <LtQOEj5TyH|dC9NWfxTZi>

# avaliacao do Rsquared
r2 = r_squared(a4, b4, x, y)
assert_equal(round(r2, 4), 0.6883)

# |%%--%%| <dC9NWfxTZi|maAAxkQ6xP>

# avaliacao via grafico dos residuos (sem correcao automatica)

# seu codigo aqui
# gabarito a seguir
sns.residplot(
    x="Age",
    y="Length",
    data=df,
    line_kws={"color": "magenta", "lw": 4},
    scatter_kws={"edgecolor": "k", "s": 80, "alpha": 0.8},
)
plt.ylabel(r"$\epsilon_i$")
despine()


# |%%--%%| <maAAxkQ6xP|LKtkF2a3HZ>

# GABARITO GRAFICO
# sns.residplot(x='Age', y='Length', data=df,
#               line_kws={'color':'magenta', 'lw':4},
#               scatter_kws={'edgecolor':'k', 's':80, 'alpha':0.8})
# plt.ylabel(r'$\epsilon_i$')
# despine()
# plt.show()

# |%%--%%| <LKtkF2a3HZ|yLKsboNWNk>
r"""°°°
#### 4.4 Verificando se os erros são independentes
°°°"""
# |%%--%%| <yLKsboNWNk|QaTk1mUrEG>

(maiores, menores) = error_verification(a4, b4, x, y)
assert_equal(maiores, 16)
assert_equal(menores, 11)

# |%%--%%| <QaTk1mUrEG|vl9QLJ3CqH>

# avaliacao via grafico dos residuos (sem correcao automatica)
# seu codigo aqui
# gabarito a seguir
ss.probplot(y - y.mean(), plot=plt)
despine()

# |%%--%%| <vl9QLJ3CqH|hYTDRBk526>

# ss.probplot(y - y.mean(), plot=plt)
# despine()
# plt.show()

# |%%--%%| <hYTDRBk526|TMhNJhyJvN>
r"""°°°
## Estimador de Máxima Verossimilhança
°°°"""
# |%%--%%| <TMhNJhyJvN|RSKDwJd51f>
r"""°°°
Conforme vimos, a verossimilhança representa a probabilidade dos nossos dados $X$ (ou erros $E$) condicionados em um modelo. O modelo aqui são os parâmetros $\theta$ e a função de probabilidade $p$.

$$X = \{x_1, x_2, ..., x_n\}$$

$$p(X|\theta) = \prod_i p(x_i|\theta)$$

No modelo que estudamos:

$\epsilon_i \sim Normal(0, \sigma^2)$  

$p(\epsilon_i|\sigma^2, \alpha, \beta) = \frac{1}{\sqrt{\sigma^2 2 \pi}} e^{-\frac{(y_i - \beta x_i - \alpha)^2}{2 \sigma^2}}$  

$E = \{e_1, e_2, ..., e_n\}$ e $\theta = \{\sigma^2, \alpha, \beta\}$  

$p(E|\theta) = \prod_i p(\epsilon_i|\theta)$

Entretanto, podemos estimar os parâmetros de qualquer modelo probabilístico.
°°°"""
# |%%--%%| <RSKDwJd51f|7du6D44t5c>
r"""°°°
Imagine o seguinte caso, em que observamos variáveis categóricas $X$. $X$ corresponde ao efeito do remédio em um grupo de pessoas, onde cada $x_i$ assume valo igual a 1, caso o remédio tenha funcionado e 0 caso contrário. Por exemplo: $X = \{1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0\}$

Podemos modelar estes dados a partir de uma distribuição [Bernoulli](https://en.wikipedia.org/wiki/Bernoulli_distribution). Ou seja,  $x_i \sim Bernoulli(\theta)$ onde $\theta$ representa a probabilidade do remédio funcionar para o paciente (probabilidade de sucesso).

* Derive o estimador de máxima verossimilhança para a distribuição Bernoulli.
°°°"""
# |%%--%%| <7du6D44t5c|MnKIPhG4wP>
r"""°°°
$$x_i \sim Bernoulli(\theta)$$

$$p(x_i|\theta) = \theta^{x_i} (1-\theta)^{(1 - x_i)}$$

Estimador de máxima verossimilhança:

$$L(X|\theta) = \prod_i p(x_i|\theta) = \prod_i \theta^{x_i} (1-\theta)^{(1 - x_i)} = \theta^{\sum_i x_i} (1-\theta)^{\sum_i (1 - x_i)}$$
lembrando que $a^x b^y * a^z b^w = a^{x+z} b^{y+w}$


Estimador de máxima log-verossimilhança:

$$l(X|\theta) = log(\prod_i p(x_i|\theta)) = \sum_i log(\theta^{x_i} (1-\theta)^{(1 - x_i)}) = \sum_i x_i log(\theta) + \sum_i (1-x_i) log(1-\theta)$$
lembrando que $log(ab) = log(a) + log(b)$ e $log(a^x) = xlog(a)$
°°°"""
# |%%--%%| <MnKIPhG4wP|b7k4p8otHO>
r"""°°°
* Após derivar o estimador de máxima verossimilhança para a distribuição Bernoulli encontre o valor de $\theta$ que maximiza a verossimilhança.
°°°"""
# |%%--%%| <b7k4p8otHO|Fg1BCIcox6>
r"""°°°
Assumimos que as observações são independentes, maximizar a log da verossimilhança corresponde a derivar essa função, encontrando o seu ponto de máximo. Igualando a derivada da log-verossimilhança encontramos os parâmetros ótimos:

$$\frac{\partial l(X|\theta)}{\theta} = \frac{\partial (\sum_i x_i log(\theta) + \sum_i (1-x_i) log(1-\theta))}{\partial \theta} = \frac{\sum_i x_i}{\theta} - \frac{\sum_i (1-x_i)}{(1-\theta)}$$
Lembrando que $\frac{\partial log(a)}{\partial a} = \frac{1}{a}$ e $\frac{\partial log(1-a)}{\partial a} = \frac{1}{(1-a)}$

Igualando a derivada a zero, encontramos o valor de $\theta$ que maximiza a log-verossimilhança:

$$\frac{\sum_i x_i}{\theta} - \frac{\sum_i (1-x_i)}{(1-\theta)} = 0$$
$$(1-\theta) \sum_i x_i = \theta \sum_i (1-x_i)$$
$$\sum_i x_i - \theta \sum_i x_i = n\theta - \theta \sum_i x_i$$
$$\sum_i x_i = n\theta$$
$$\theta = \frac{\sum_i x_i}{n}$$

°°°"""
