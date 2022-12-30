# flake8: noqa
# pylint: disable-all

r"""°°°
# Lista 4 - ICs e Bootstrap
°°°"""
# |%%--%%| <J56h4ZEjIg|hNe2rn41xK>
"""°°°
## Intervalos de Confiança
°°°"""
# |%%--%%| <hNe2rn41xK|wpzwW0k0yu>
r"""°°°
Intervalos de confiança são intervalos calculados a partir de observações que podem variar de amostra para amostra e que com dada frequência (nível de confiança) inclui o parâmetro de interesse real não observável. 

**Por exemplo:** Um intervalo com nível de confiança de 99% para a média de uma variável aleatória significa que ao calcularmos *n* intervalos de confiança tomando como base *n* amostras aleatórias, espera-se que 99% dos intervalos construídos contenham o valor real do parâmetro (média).

Em outras palavras, o nível de confiança seria a proporção de intervalos de confiança construídos em experimentos separados da mesma população e com o mesmo procedimento que contém o parâmetro de interesse real.
°°°"""
# |%%--%%| <wpzwW0k0yu|4VaVVaUMKi>
r"""°°°
Foram ministradas duas maneiras de construírmos intervalos de confiança:

- Probabilisticamente direto dos dados (Forma clássica).
- Via sub-amostragem com reposição (*Bootstrap*).
°°°"""
# |%%--%%| <4VaVVaUMKi|DluHXlrmKm>
r"""°°°
Para o primeiro caso, lembrando do conceito visto em aula, temos (para um IC com 95% de confiança):

$$\begin{align}
0.95 = P(-z \le Z \le z)=P \left(-1.96 \le \frac {\bar X-\mu}{\sigma/\sqrt{n}} \le 1.96 \right) = P \left( \bar X - 1.96 \frac \sigma {\sqrt{n}} \le \mu \le \bar X + 1.96 \frac \sigma {\sqrt{n}}\right).
\end{align}$$
°°°"""
# |%%--%%| <DluHXlrmKm|tavtobexKZ>
r"""°°°
Vamos colocar na prática!
°°°"""
# |%%--%%| <tavtobexKZ|lgEyAOKDd1>
r"""°°°
## Exemplo Inicial
°°°"""
# |%%--%%| <lgEyAOKDd1|L19mWrZiqN>
r"""°°°
Vamos começar construindo um intervalo de confiança pra a média de uma distribuição Normal (Gaussiana) com média $\mu = 0$ e variância $\sigma^2 = 1$.
°°°"""
# |%%--%%| <L19mWrZiqN|3eKKWvYcrM>

from math import inf

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss

plt.rcParams["figure.figsize"] = (10, 8)

np.random.seed(
    0
)  # comando adicionado para reprodutibilidade dos números aleatórios gerados


def confidence_interval(loc, scale, alpha=0.99):
    """Essa função cria uma distribuição Normal com base nos parâmetros fornecidos e constrói um intervalo de confiança para sua média.

    Parameters:
    -----------
    loc (float): Média da distribuição desejada.
    scale (float): Desvio padrão da distribuição desejada.
    alpha (float): Nível de confiança do intervalo. Deve ser um valor entre 0 e 1. Default = 0.99, o que corresponde a 99% de confiança.

    Returns:
    -----------
    X (array): Dados gerados segundo uma distribuição Normal(0,1).
    LI (float): Limite inferior do intervalo calculado.
    LS (float): Limite superior do intervalo calculado.

    """

    # Gerando amostra de uma Normal(0,1) de tamanho N
    N = 1000
    X = np.random.normal(loc=loc, scale=scale, size=N)

    # Criando plot da amostra gerada
    plt.xlabel("Valores", fontsize=12)
    plt.ylabel("Frequências", fontsize=12)
    plt.title("Histograma de amostra de uma Distribuição Normal(0,1)", fontsize=16)

    plt.hist(X, color="#A3333D", alpha=0.9, rwidth=0.85, bins=15)
    plt.show()

    # Calculando intervalo de  95% de confiança para a média manualmente
    LI = X.mean() - 1.96 * (X.std(ddof=1) / np.sqrt(N))  # LI = limite inferior
    LS = X.mean() + 1.96 * (X.std(ddof=1) / np.sqrt(N))  # LS = limite superior
    print("INTERVALO DE CONFIANCA (manual) = [{:.4f}, {:.4f}]".format(LI, LS))

    # Utilizando o valor da confiança como base, utilizamos o pacote scipy.stats
    LI = X.mean() - ss.norm.ppf(alpha + (1 - alpha) / 2).round(2) * (
        X.std(ddof=1) / np.sqrt(N)
    )
    LS = X.mean() + ss.norm.ppf(alpha + (1 - alpha) / 2).round(2) * (
        X.std(ddof=1) / np.sqrt(N)
    )

    # Printando intervalo de confiança
    print("INTERVALO DE CONFIANCA (com scipy)= [{:.4f}, {:.4f}]".format(LI, LS))

    return X, LI, LS


X, LI, LS = confidence_interval(loc=0, scale=1, alpha=0.95)

# |%%--%%| <3eKKWvYcrM|0xegfdTZDN>
r"""°°°
Podemos afirmar que, se pudermos repetir muitas vezes o experimento e coletarmos os dados, aproximadamente em 95% das vezes a média populacional estará no intervalo encontrado.

**Algumas observações interessantes. Note que:**
- A cada vez que executamos o código acima, tanto os intervalos como o histograma dos dados são diferentes. Estamos realizando uma amostra de uma distribuição.
- A medida que o tamanho da amostra (N) cresce, o tamanho do intervalo - para um mesmo nível de confiança - cai. Isso ocorre pois com mais dados temos uma maior certeza de que os valores encontrados de fato representam a população de interesse.
- Os valores dos intervalos de confiança (manual e scipy) só coincidem quando *alpha=0.95*. Essa é a vantagem de se utilizar o pacote. Para valores diferentes de 0.95, deve-se consultar o valor correspondente na distribuição Z.
°°°"""
# |%%--%%| <0xegfdTZDN|CgA2DIxDSy>
r"""°°°
## Dados ENEM 2015.
°°°"""
# |%%--%%| <CgA2DIxDSy|ph19lgJDn2>
r"""°°°
Nos exercícios dessa seção vamos trabalhar com os dados do [ENEM 2015](https://raw.githubusercontent.com/pedroharaujo/ICD_Docencia/master/enem2015.csv).

Importando pandas e carregando dados.
°°°"""
# |%%--%%| <ph19lgJDn2|pOzdIpGs6L>

import pandas as pd

url = "https://raw.githubusercontent.com/pedroharaujo/ICD_Docencia/master/enem2015.csv"
data = pd.read_csv(url)

# |%%--%%| <pOzdIpGs6L|BJ1cGMBxHh>
r"""°°°
Primeiras visualizações do banco de dados do ENEM 2015.
°°°"""
# |%%--%%| <BJ1cGMBxHh|LcsW9RMYIz>

data.head()

# |%%--%%| <LcsW9RMYIz|vz5ksDY1Iv>

data.describe()

# |%%--%%| <vz5ksDY1Iv|lR0q7R7Qsr>
r"""°°°
## Exercício 01
°°°"""
# |%%--%%| <lR0q7R7Qsr|d2BPSH9dJa>
r"""°°°
Altere a função a baixo para retornar o intervalo de confiança para a média da variável 'NOTA_MEDIA_ESCOLA' para escolas com 'DEPENDENCIA_ADMINISTRATIVA' == Estadual.

Nível de confiança: 99%

**Lembrete**: será necessário aplicar os conhecimentos de pandas do módulo anterior para filtrar o DataFrame selecionando apenas os casos de interesse.
°°°"""
# |%%--%%| <d2BPSH9dJa|KaGlRRNNIJ>


def CI(df1: pd.DataFrame):
    df_estadual: pd.DataFrame = df1[df1["DEPENDENCIA_ADMINISTRATIVA"] == "Estadual"]
    X: pd.Series = df_estadual["NOTA_MEDIA_ESCOLA"]
    N: int = X.size
    alpha: float = 0.99
    LI: np.float64 = X.mean() - ss.norm.ppf(alpha + (1 - alpha) / 2).round(2) * (
        X.std(ddof=1) / np.sqrt(N)
    )
    LS: np.float64 = X.mean() + ss.norm.ppf(alpha + (1 - alpha) / 2).round(2) * (
        X.std(ddof=1) / np.sqrt(N)
    )
    # Retorne uma tupla com os limites inferior e superior do intervalo de confiança, respectivamente
    # return (LI, LS)
    # se ocorrer erro de float, tente dar cast na tupla (LI,LS) assim: (np.array(LI), np.array(LS))
    return LI, LS


# |%%--%%| <KaGlRRNNIJ|1uMVWvcdBC>
r"""°°°
Carregando os módulos de testes!
°°°"""
# |%%--%%| <1uMVWvcdBC|0mSifA28lg>

from numpy.testing import assert_equal

# |%%--%%| <0mSifA28lg|y7rDG5p4RU>
r"""°°°
Nosso teste
°°°"""
# |%%--%%| <y7rDG5p4RU|9joxvLbDhx>

(LI, LS) = CI(data)

assert_equal(548.13, LI.round(2))
assert_equal(551.09, LS.round(2))

# |%%--%%| <9joxvLbDhx|OhXgeY9wqN>
r"""°°°
## Exercício 02 (Sem correção automática)
°°°"""
# |%%--%%| <OhXgeY9wqN|0N3h4xd6X8>
r"""°°°
Plote uma CDF da coluna 'TAXA_DE_APROVACAO'.

**Use o statsmodels e crie um objeto `ecdf = ECDF(...)`.**


Esta tarefa não tem correção automática, use o gráfico abaixo para saber se acertou ou não.

![](https://github.com/pedroharaujo/ICD_Docencia/blob/master/ECDF.png?raw=true)
°°°"""
# |%%--%%| <0N3h4xd6X8|bPY7e5Zel9>

# codigo para importar a função ECDF
from statsmodels.distributions.empirical_distribution import ECDF

# |%%--%%| <bPY7e5Zel9|tNVOzB6qfe>

# YOUR CODE HERE
ecdf = ECDF(data["TAXA_DE_APROVACAO"])
plt.plot(ecdf.x, ecdf.y)
plt.title("Empirical CDF for TAXA_DE_APROVACAO")
plt.grid(which="both")
plt.ylabel("% do total")
plt.xlabel("Taxa de Aprovação (%)")
plt.show()

# |%%--%%| <tNVOzB6qfe|onYtG3Q1aA>
r"""°°°
## Bootstrap
°°°"""
# |%%--%%| <onYtG3Q1aA|ZntNg4XIl8>
r"""°°°
Quando falamos em bootstrap deve-se ter em mente que estamos falando de amostragem com reposição.

De maneira simplista, utilizamos bootstrap quando queremos construir um intervalo de confiança para uma variável e dispomos de poucos dados. Ao realizarmos várias sub-amostras **com reposição**, a lei dos grandes números nos garante que estamos aproximando a população de interesse.

Note o destaque para o termo com reposição. É CRUCIAL que as sub-amostras sejam feitas com reposição. Só assim garantimos a aleatoriedade!

Veja o exemplo abaixo.
°°°"""
# |%%--%%| <ZntNg4XIl8|dwt23MrfEd>

col = "TAXA_DE_PARTICIPACAO"
n_sub = 10000  # numero de sub-amostras
size = len(data)  # tamanho do dataframe
values = np.zeros(n_sub)


def bootstrap(n_sub, size, col):
    for i in range(n_sub):
        # replace=TRUE garanta amostras com reposição
        random_state = i  # garante replicabilidade do experimento
        sample = data.sample(size, replace=True, random_state=i)

        # Lembre que podemos utilizar mediana, média ou qualquer outra estatística agregada
        # values[i] = sample[col].median()
        values[i] = sample[col].mean()

    # Gerando valores inferior e superior para um nível de confiança de 95%
    LI = np.percentile(values, 2.5)
    LS = np.percentile(values, 97.5)
    return values, LI, LS


values, LI, LS = bootstrap(n_sub, size, col)
print("Intervalo de Confianca: [{}, {}]".format(LI.round(4), LS.round(4)))

# |%%--%%| <dwt23MrfEd|EqYbxqqSlK>
r"""°°°
## Exercício 03
°°°"""
# |%%--%%| <EqYbxqqSlK|9RQ3MAWMa1>
r"""°°°
Realizando um groupy pela coluna 'DEPENDENCIA_ADMINISTRATIVA' conseguimos observar para quais casos vale a pena utilizarmos bootstrap.
°°°"""
# |%%--%%| <9RQ3MAWMa1|Now0lDO1HT>

data.groupby("DEPENDENCIA_ADMINISTRATIVA").count()

# |%%--%%| <Now0lDO1HT|TveG71Rtmo>
r"""°°°
**A)** Na função abaixo, retorne o número da opção que indica para quais 'DEPENDENCIAS_ADMINISTRATIVAS' é aconselhado utilizar Bootstrap para construção do intervalo de confiança:

- 1) Estadual e Federal.
- 2) Estadual e Municipal.
- 3) Estadual e Privada.
- 4) Federal e Municipal.
- 5) Federal e Privada.
- 6) Municipal e Privada.
°°°"""
# |%%--%%| <TveG71Rtmo|j26mrTBYUr>


def resposta():
    # Pelo groupby, Federal e Municipal são as categorias que possuem menos dados,
    # portanto o bootstrap pode ser mais útil pra elas
    return 4


# |%%--%%| <j26mrTBYUr|MoJAAFwQDX>

assert_equal(4, resposta())

# |%%--%%| <MoJAAFwQDX|83XCFcXWlI>
r"""°°°
**B)** Construa um intervalo de confiança via Bootstrap para a média da variável 'NOTA_MEDIA_ESCOLA' para escolas de 'DEPENDENCIA_ADMINISTRATIVA' **Federal**. Você deve utilizar 5000 amostras e nível de confiança de 90%.

*Nota*: você deve utilizar o argumento random_state=i na função data.sample, como no exemplo inicial da seção de Bootstrap.
°°°"""
# |%%--%%| <83XCFcXWlI|YLdDeTVNh2>


def bootstrap_mean(n_sub: int, alpha: float):

    df_federal: pd.DataFrame = data[data["DEPENDENCIA_ADMINISTRATIVA"] == "Federal"]
    col: str = "NOTA_MEDIA_ESCOLA"
    df_size: int = len(df_federal)
    values: np.ndarray = np.zeros(n_sub)

    for i in range(n_sub):
        sample: pd.DataFrame = df_federal.sample(df_size, replace=True, random_state=i)
        values[i] = sample[col].mean()

    # Gerando valores inferior e superior para um nível de confiança de `alpha`
    LI: np.float64 = np.percentile(values, (100 - alpha * 100) / 2)
    LS: np.float64 = np.percentile(values, 100 - (100 - alpha * 100) / 2)
    # se ocorrer erro de float, tente dar cast na tupla (LI,LS) assim: (np.array(LI), np.array(LS))
    return values, (LI, LS)


# |%%--%%| <YLdDeTVNh2|7A9OfOLwEE>

values, (LI, LS) = bootstrap_mean(n_sub=5000, alpha=0.9)

assert_equal(622.03, LI.round(2))
assert_equal(635.43, LS.round(2))

# |%%--%%| <7A9OfOLwEE|7nE9RSbnFL>
r"""°°°
## Exercício 4
°°°"""
# |%%--%%| <7nE9RSbnFL|7WbsZfbeQL>
r"""°°°
Altere a função abaixo para que retorne a 'DEPENDENCIA_ADMINISTRATIVA' (Federal, Estadual, Municipal ou Privada) cujo intervalo de confiança para *mediana* via *bootstrap* para a variável 'TAXA_DE_PARTICIPACAO' apresente maior amplitude (LS-LI), e qual esse valor. 

Utilize:
- 95% como nível de confiança.
- 5000 como número de sub-amostras.
°°°"""
# |%%--%%| <7WbsZfbeQL|5pfbFJJxoD>


def ci_amplitude():
    col: str = "TAXA_DE_PARTICIPACAO"
    n_sub: int = 5000

    max_amp: np.float64 = np.float64(-inf)
    dependencia_adm = "Federal"
    adm_opts: list[str] = ["Federal", "Estadual", "Municipal", "Privada"]

    for j, opt in enumerate(adm_opts):
        df_opt: pd.DataFrame = data[data["DEPENDENCIA_ADMINISTRATIVA"] == opt]
        df_size: int = len(df_opt)

        values: np.ndarray = np.zeros(n_sub)
        for i in range(n_sub):
            sample: pd.DataFrame = df_opt.sample(df_size, replace=True, random_state=i)
            values[i] = sample[col].median()

        # Gerando valores inferior e superior para um nível de confiança de `alpha`
        LI: np.float64 = np.percentile(values, 2.5)
        LS: np.float64 = np.percentile(values, 97.5)
        amp: np.float64 = LS - LI
        if amp > max_amp:
            max_amp = amp
            dependencia_adm = adm_opts[j]
    # Sua função deve retorar uma tupla como no exemplo
    # exemplo: (dependencia_administrativa, amplitude_do_ic)
    return (dependencia_adm, max_amp)


# |%%--%%| <5pfbFJJxoD|evANQ4MXoQ>

(dep, amp) = ci_amplitude()
assert_equal(dep, "Municipal")
assert_equal(amp.round(2), 11.09)
