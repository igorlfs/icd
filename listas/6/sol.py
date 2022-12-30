# pylint: disable-all

# |%%--%%| <eQuib9dJSo|ZVOWBFXR1g>
"""°°°
# Lista 6 - Teorema Central do Limite, ICs e Testes de Hipóteses
°°°"""
# |%%--%%| <ZVOWBFXR1g|jcK4eoEJ1L>
"""°°°
## Teorema Central do Limite e Distribuição Normal
°°°"""
# |%%--%%| <jcK4eoEJ1L|O6CdZIeDer>
"""°°°
**Conceito:** A distribuição das médias de variáveis aleatórias independentes e identicamente distribuídas tendo a uma Normal.

Vamos fazer um experimento clássico para demonstrar na prática.

- Geraremos $n$ amostras de tamanho 100 de uma distribuição qualquer (utilizaremos uma Uniforme, mas funciona para qualquer distribuição).
- Calcularemos suas médias.
- Plotamos um histograma.
- Variaremos o tamanho de $n$ e repetiremos.

Vamos usar:
- $n=10$
- $n=20$
- $n=50$
- $n=100$
- $n=1000$
°°°"""
# |%%--%%| <O6CdZIeDer|vIyUTsPVlT>

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy.testing import assert_equal

# |%%--%%| <vIyUTsPVlT|4z5uHoQaZc>

np.random.seed(23)  # seed para reprodutibilidade


size = 100

medias = []
for n in [10, 20, 50, 100, 1000]:
    for _ in range(n):
        data = np.random.uniform(1, 1000, size)
        medias.append(data.mean())
    plt.hist(medias, bins=15, rwidth=0.95)
    plt.title("N={}".format(n))
    plt.show()

# |%%--%%| <4z5uHoQaZc|paY2FL83D5>
"""°°°
Note que a medida que aumentamos o número de médias amostradas ($n$), o histograma se modifica cada vez mais próximo de uma distribuição Normal.

**Está demonstrado o princípio do Teorema Central do Limite!**

Ao demonstrar o TCL, mostramos indiretamente porque a distribuição Normal é tão importante. Vamos agora, revisar e explorar a Normal um pouco mais.

Se as médias de variáveis aleatórias apresentam distribuição próxima a Normal, como podemos estimar probabilidades e fazer testes com base na Normal?

Uma distribuição Normal é definida por dois parâmetros:
- Média ($\mu$).
- Desvio padrão ($\sigma$), ou variância ($\sigma^2$).

Tendo esses valores de uma população e uma amostra com $n$ elementos, podemos normalizá-la de forma que os valores resultantes possuem um distribuição Normal Gaussiana, ou seja, com $\mu=0$ e $\sigma^2=1$, denotada por Normal(0,1), ou ainda, N(0,1). Para fazer isso, utilizamos:

$$ Z = \frac {\bar X-\mu}{\sigma/\sqrt{n}}, $$

onde:
- $\bar{X}$: é a média encontrada em uma amostra de tamanho $n$.
- $\mu$: é a média da população da qual realizamos a amostra.
- $\sigma^2$: é a variância da população da qual realizamos a amostra.

Assim, temos:

$$Z \thicksim Normal(0,1)$$

Lembre-se que também sabemos que a variância do estimador da média é:

$$Var(\hat{\mu}) = \frac{\sigma^2}{n}$$

Assim:

$$\bar{X} \thicksim Normal(\mu, \frac{\sigma^2}{n})$$

A Normal Gaussiana é de extrema importância, pois serve de base para definirmos probabilidades. Vamos ver um exemplo.
°°°"""
# |%%--%%| <paY2FL83D5|6SqqmRJkzM>
"""°°°
**Exemplo:**Dado que a população de homens de um país apresenta pesos distribuídos normalmente com média de 173lb e desvio-padrão de 30lb. Como podemos determinar a probabilidade de um homem escolhido aleatoriamente pesar mais de 180lb?

Nesse caso, temos:
- $\mu = 173$
- $\sigma = 30$
- $n = 1$

Vamos encontrar o valor de Z.
°°°"""
# |%%--%%| <6SqqmRJkzM|2YTcwjyueJ>


def z_obs(x, mu, sigma, n):
    z = (x - mu) / (sigma / np.sqrt(n))
    return z.round(2)


z_obs(180, 173, 30, 1)

# |%%--%%| <2YTcwjyueJ|NaMXisAeLH>
"""°°°
Sabemos que $z$ é um valor de uma distribuição Normal com média 0 e variância 1.

Vamos então encontrar a probabilidade de obtermos um valor maior que $z$.

Para isso, estatísticos usam uma tabela com as probabilidades bem definidas. Cientistas de dados fazem assim:
°°°"""
# |%%--%%| <NaMXisAeLH|9h9BYOcuoc>

import scipy.stats as ss

print(ss.distributions.norm.sf(0.23))

# |%%--%%| <9h9BYOcuoc|g07NJ1v13z>
"""°°°
Isso nos diz que a probabilidade de obtermos um valor maior que o valor de $z$ encontrado (0.23), na distribuição Normal(0,1) é 0.4090!

Logo, a probabilidade de um homem selecionado aleatoriamente pesar mais que 180lb é 0.4090!
°°°"""
# |%%--%%| <g07NJ1v13z|lZQWJCxhDo>
"""°°°
E se quisermos calcular a probabilidade do peso médio de 36 homens selecionados aleatoriamente ser maior que 180lb?

A ideia é a mesma.
°°°"""
# |%%--%%| <lZQWJCxhDo|zRpxoV5vEY>

print(z_obs(180, 173, 30, 36))
print(ss.distributions.norm.sf(z_obs(180, 173, 30, 36)))

# |%%--%%| <zRpxoV5vEY|NLLiyPkRHw>
"""°°°
Concluímos que há uma probabilidade de 0.4090 de UM indivíduo pesar mais que 180, porém a probabilidade da média do peso de 36 homens é de apenas 0.0808.

**É muito mais fácil um indivíduo se afastar da média, do que um grupo com 36 indivíduos.**

Note que escancaramos a influência do tamanho da amostra. Para uma mesma distribuição com os mesmos parâmetros, aumentar o tamanho da amostra significa se afastar da média na distribuição Z (note que o valor de $z$ para o caso com $n=36$ é superior ao caso com $n=1$ e a média da distribuição de Z é 0), porém significa que a probabilidade da média dos pesos ser superior a 180lb é muito menor.
°°°"""
# |%%--%%| <NLLiyPkRHw|xE6BamQqhM>
"""°°°
## Exercício 1
°°°"""
# |%%--%%| <xE6BamQqhM|W1UOl5ZF20>
"""°°°
Sabendo que os preços de bolsas de uma marca de grife seguem uma distribuição Normal com média 1100 reais e desvio-padrão de 420, altere o código abaixo para retornar a probabilidade de uma bolsa selecionada aleatoriamente custar mais que 1400 reais.
°°°"""
# |%%--%%| <W1UOl5ZF20|iDKfE0K90o>


def prob(x: float, mu: float, sigma: float, n: int) -> float:
    # a probabilidade de uma bolsa custar mais que 1400 -> P(X>1400)
    z: float = (x - mu) / (sigma / np.sqrt(n))
    probability: float = ss.distributions.norm.sf(z)
    return probability


# |%%--%%| <iDKfE0K90o|udmr1yY1fq>

p = prob(1400, 1100, 420, 1)
assert_equal(0.2375, p.round(4))

# |%%--%%| <udmr1yY1fq|SoFWVrTlql>
"""°°°
## Intervalos de Confiança
°°°"""
# |%%--%%| <SoFWVrTlql|GILtAMkWbc>
"""°°°
Vimos duas maneiras de construirmos intervalos de confiança para variáveis aleatórias:

- Usando o teorema central do limite.
- Usando *Bootstrap*.

Com baso no TCL e nas propriedades da distribuição Normal podemos definir intervalos de confiança. Basta definirmos o nível de confiança associado ao nosso intervalo e manipularmos a equação do TCL utilizada para encontrar $z$ de forma a isolar $\mu$ (parâmetro de interesse).

$$\begin{align}
0.95 = P(-z \le Z \le z)=P \left(-1.96 \le \frac {\bar X-\mu}{\sigma/\sqrt{n}} \le 1.96 \right) = P \left( \bar X - 1.96 \frac \sigma {\sqrt{n}} \le \mu \le \bar X + 1.96 \frac \sigma {\sqrt{n}}\right),
\end{align}$$

onde 1.96 é o valor de $z$ associado ao nível de confiança escolhido. Basicamente é o inverso do que estávamos fazendo. Ao invés de encontrarmos a probabilidade associada a um valor $z$, encontramos o valor $z$ associado a uma probabilidade pré-definida (nível de confiança).
°°°"""
# |%%--%%| <GILtAMkWbc|mXpyqVOxNo>
"""°°°
## Exercício 2
°°°"""
# |%%--%%| <mXpyqVOxNo|u0g87YM4BA>
"""°°°
**a) Qual a temperatura média do corpo humano?**

Os dados a seguir foram obtidos por pesquisadores da Universidade de Maryland que mediram 106 temperaturas do corpo humano. Construa um intervalo de 95% de confiança para a média. Utilize a equação a cima.
°°°"""
# |%%--%%| <u0g87YM4BA|bcRIN07Pcl>

data = np.array(
    [
        98.6,
        98.6,
        98.0,
        98.0,
        99.0,
        98.4,
        98.4,
        98.4,
        98.4,
        98.6,
        98.6,
        98.8,
        98.6,
        97.0,
        97.0,
        98.8,
        97.6,
        97.7,
        98.8,
        98.0,
        98.0,
        98.3,
        98.5,
        97.3,
        98.7,
        97.4,
        98.9,
        98.6,
        99.5,
        97.5,
        97.3,
        97.6,
        98.2,
        99.6,
        98.7,
        99.4,
        98.2,
        98.0,
        98.6,
        98.6,
        97.2,
        98.4,
        98.6,
        98.2,
        98.0,
        97.8,
        98.0,
        98.4,
        98.6,
        98.6,
        97.8,
        99.0,
        96.5,
        97.6,
        98.0,
        96.9,
        97.6,
        97.1,
        97.9,
        98.4,
        97.3,
        98.0,
        97.5,
        97.6,
        98.2,
        98.5,
        98.8,
        98.7,
        97.8,
        98.0,
        97.1,
        97.4,
        99.4,
        98.4,
        98.6,
        98.4,
        98.5,
        98.6,
        98.3,
        98.7,
        98.8,
        99.1,
        98.6,
        97.9,
        98.8,
        98.0,
        98.7,
        98.5,
        98.9,
        98.4,
        98.6,
        97.1,
        97.9,
        98.8,
        98.7,
        97.6,
        98.2,
        99.2,
        97.8,
        98.0,
        98.4,
        97.8,
        98.4,
        97.4,
        98.0,
        97.0,
    ]
)

# |%%--%%| <bcRIN07Pcl|LiTeG56e5i>


def ic(data: np.array) -> tuple:
    # altere a função para retornar uma tupla (LI, LS) com os limites do intervalo de confiança
    N: int = 10000
    medias: np.array = np.zeros(N)
    for i in range(N):
        mean: float = np.random.choice(data, 100).mean()
        medias[i] = mean
    li: float = np.percentile(medias, 2.5)
    ls: float = np.percentile(medias, 97.5)
    return (li, ls)


# |%%--%%| <LiTeG56e5i|27RI04QcKh>

(LI, LS) = ic(data)
assert_equal(98.08, LI.round(2))
assert_equal(98.32, LS.round(2))

# |%%--%%| <27RI04QcKh|BMcrpJhMCV>
"""°°°
**b) Bootstrap**

Suponha que você tenha apenas as 15 primeiras observações das temperaturas corporais. Um intervalo de confiança com poucos dados pode não ser muito aconselhável, pois não há garantias de que a sua amostra seja de fato representativa da sua população. Para contornar esse tipo de empecilho, é comum utilizarmos técnicas de amostragem que garantam estimativas confiáveis que reflitam a população de interesse. Uma das maneiras de realizarmos esse processo de amostragem é chamado de *Bootstrap* e consiste em realizar sub-amostras da amostra disponível, com reposição. Assim gera-se várias novas amostras com elementos que podem se repetir nessas novas amostras, mesmo que isso não ocorra na amostra original.

Nessa lista, não daremos muito enfoque na explicação do *Bootstrap*, apenas na revisão. Caso precise relembrar o método, sugerimos a revisão das aulas e listas de exercícios com *Bootstrap*.

ALTERE A FUNÇÃO ABAIXO PARA RETORNAR UM INTERVALO DE 95% DE CONFIANÇA PARA AS TEMPERATURAS CORPORAIS DOS 15 PRIMEIROS INDIVÍDUOS. UTILIZE 5000 SUB-AMOSTRAS DE TAMANHO IGUAL AO TAMANHO ORIGINAL (15).
°°°"""
# |%%--%%| <BMcrpJhMCV|4mqBCnioCM>

df = data[:15]


def bootstrap_mean(df: np.array):
    # OS PARÂMETROS INICIAIS PODEM SER ALTERADOS A SEU GOSTO
    # SUA FUNÇÃO DEVE RETORNAR UMA TUPLA COM OS LIMITES DO IC
    # (LI, LS)
    num_repetitions: int = 5000
    means: np.array = np.zeros(num_repetitions)
    for i in np.arange(num_repetitions):
        np.random.seed(i)
        mean: float = np.random.choice(df, size=df.size).mean()
        means[i] = mean
    li: float = np.percentile(means, 2.5)
    ls: float = np.percentile(means, 97.5)
    return (li, ls)


# |%%--%%| <4mqBCnioCM|DqjTvkrwhO>

(LI, LS) = bootstrap_mean(df)
assert_equal(97.97, LI.round(2))
assert_equal(98.55, LS.round(2))

# |%%--%%| <DqjTvkrwhO|pcozp42PIC>
"""°°°
## Testes de Hipóteses
°°°"""
# |%%--%%| <pcozp42PIC|61GNQ8OfaN>
"""°°°
Até o momento, vimos como realizar testes de hipóteses através de algumas metodologias diferentes. Podemos citar:

- Testes A/B: comparamos intervalos de confiança para o estimador da média (mediana), ou da diferença de médias e analisamos o boxplot. Nesse caso, a criação de intervalos de confiança pode ser via *bootstrap* ou via TLC.
- Testes de Permutação: embaralhamos a amostra retirando a influência de uma variável categórica e comparamos se a média se mantém.

Utilizando o conhecimento sobre testes de hipóteses, resolva as questões com o dataset a seguir.
°°°"""
# |%%--%%| <61GNQ8OfaN|34eZv5g06r>

import numpy as np
import pandas as pd

data = pd.read_csv(
    "https://raw.githubusercontent.com/rashida048/Datasets/master/home_data.csv",
    nrows=100,
)
data.head()

# |%%--%%| <34eZv5g06r|VC9dunD8YO>
"""°°°
## Exercício 3
°°°"""
# |%%--%%| <VC9dunD8YO|5lqlyA7NHw>
"""°°°
Uma corretora de imóveis desconfia que exista uma diferença entre os preços médios de casas de acordo com o número de pisos (`floors`). Ela deseja comparar casas totalmente térreas (1 piso) e casas com mais de 1 piso. Realize um teste de permutação, respondendo as questões. 

1 - Definida as hipóteses:

$$H_0: \mu_{T} = \mu_{\bar{T}}$$

$$H_1: \mu_{T} \neq \mu_{\bar{T}}$$


°°°"""
# |%%--%%| <5lqlyA7NHw|RM4xTQTL0M>
"""°°°
**2 - Qual a estatística de teste?**
°°°"""
# |%%--%%| <RM4xTQTL0M|iCL3MsgDVD>


def t_obs(data: pd.DataFrame) -> float:
    filter: pd.DataFrame = data["floors"] == 1
    # deve retornar um valor apenas
    # os filtros aplicados sobre data devem estar dentro da função
    return data[filter]["price"].mean() - data[~filter]["price"].mean()


# |%%--%%| <iCL3MsgDVD|TQ8E4isGRs>

tobs = t_obs(data)
assert_equal(-53396.48, round(tobs, 2))

# |%%--%%| <TQ8E4isGRs|q9jiTCBxyZ>
"""°°°
**3 - Faça o processo de shuffling e responda: Há diferença de preço significativa entre casas térreas e casas com mais de um andar?**
°°°"""
# |%%--%%| <q9jiTCBxyZ|E2a4k1Fs1j>


def shuffling(data: pd.DataFrame):
    # realiza permutações entre os dados de maneira aleatória
    # atribuindo um preço a uma casa independente do número de andares
    # deve retornar uma tupla com os valores críticos
    filter: pd.DataFrame = data["floors"] == 1
    repetitions: int = 5000
    diffs = np.zeros(repetitions)
    for i in range(repetitions):
        np.random.seed(i)
        np.random.shuffle(filter.values)
        diffs[i] = data[filter]["price"].mean() - data[~filter]["price"].mean()
    li = np.percentile(diffs, 2.5)
    ls = np.percentile(diffs, 97.5)
    return (li, ls)


# |%%--%%| <E2a4k1Fs1j|MMA0Pvcsxp>


def get_diffs() -> np.array:
    filter: pd.DataFrame = data["floors"] == 1
    repetitions: int = 5000
    diffs = np.zeros(repetitions)
    for i in range(repetitions):
        np.random.seed(i)
        np.random.shuffle(filter.values)
        diffs[i] = data[filter]["price"].mean() - data[~filter]["price"].mean()
    return diffs


# |%%--%%| <MMA0Pvcsxp|cZddshcfUR>

(c_inf, c_sup) = shuffling(data)
assert_equal(round(c_inf, 2), -119308.36)
assert_equal(round(c_sup, 2), 120417.14)

# |%%--%%| <cZddshcfUR|QfU5OfSTU7>
"""°°°
Por fim, conclua: Há diferença entre os preços de casas térreas e casas não térreas?
°°°"""
# |%%--%%| <QfU5OfSTU7|YxenhwWWjn>


def p_value(t_obs: float, diffs: np.array) -> float:
    total: int = diffs.size
    menor: int = np.count_nonzero(diffs > t_obs)
    ratio: float = menor / total
    # deve retornar o p-valor ou seja,
    # a probabilidade de termos uma diferença maior que a estatística de teste
    return ratio


def resposta():
    diffs = get_diffs()
    p = p_value(tobs, diffs)
    # deve retornar True caso exista diferença e False caso contrário
    return p <= 0.05


# |%%--%%| <YxenhwWWjn|6y9VqgMpvO>

assert_equal(resposta(), False)
