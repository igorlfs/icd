import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import bernoulli

# |%%--%%| <FZlXtYobbK|EPwLcZ6Kqi>

sample_size = 100
p = 0.26
sample = bernoulli.rvs(p, size=sample_size)
print("Number of Black jurors:", sum(sample))

# |%%--%%| <EPwLcZ6Kqi|W6N4uKBrMn>


def one_simulated_count(p=0.26, sample_size=100):
    return sum(bernoulli.rvs(p, size=sample_size))


# |%%--%%| <W6N4uKBrMn|zwxE9My7mh>

print("Number of Black jurors:", one_simulated_count())

# |%%--%%| <zwxE9My7mh|nNyaoxqPu2>

counts = []
repetitions = 10000
for i in np.arange(repetitions):
    counts.append(one_simulated_count())

# |%%--%%| <nNyaoxqPu2|uFyRXsHea3>

bins = np.arange(5.5, 46.6, 1)
plt.hist(counts, bins=bins)
plt.axvline(x=8, color="r")

# |%%--%%| <uFyRXsHea3|b7jh6BGqBI>

eight_or_less = [x for x in counts if x <= 8]
print("Number of panels with 8 or less Black jurors:", len(eight_or_less))

# |%%--%%| <b7jh6BGqBI|zYoojMRQPR>
"""°°°
## Usando a Binomial
°°°"""
# |%%--%%| <zYoojMRQPR|bmTR4YJnO7>

from scipy.stats import binom

# |%%--%%| <bmTR4YJnO7|8tZeIDUTxv>

r = binom.rvs(sample_size, p, size=repetitions)

# |%%--%%| <8tZeIDUTxv|Uf26xa3Upj>

bins = np.arange(5.5, 46.6, 1)
plt.hist(counts, bins=bins)
plt.axvline(x=8, color="r")

# |%%--%%| <Uf26xa3Upj|nuKrpdhykF>

prob = binom.cdf(8, 100, 0.26)
print(prob)

# |%%--%%| <nuKrpdhykF|VjImqMC2NE>

eight_or_less = [x for x in counts if x <= 8]
print("Number of panels with 8 or less Black jurors:", len(eight_or_less))

# |%%--%%| <VjImqMC2NE|B2B8icNVNW>
"""°°°
# Múltiplas categorias
°°°"""
# |%%--%%| <B2B8icNVNW|8rUAd4vXPs>

jury = pd.DataFrame(
    {
        "Ethnicity": ["Asian/PI", "Black/AA", "Caucasian", "Hispanic", "Other"],
        "Eligible": [0.15, 0.18, 0.54, 0.12, 0.01],
        "Panels": [0.26, 0.08, 0.54, 0.08, 0.04],
    }
)


jury

# |%%--%%| <8rUAd4vXPs|1vuUh8ruLC>

ax = jury.set_index("Ethnicity").plot.bar(rot=0)

# |%%--%%| <1vuUh8ruLC|uqLhsRYZgL>
"""°°°
## Comparação com painéis selecionados aleatoriamente
°°°"""
# |%%--%%| <uqLhsRYZgL|TvweGCf6sy>

from scipy.stats import multinomial

# |%%--%%| <TvweGCf6sy|65flpbZWxU>


def sample_proportions(n, p):
    r = multinomial.rvs(n, p)
    return r / n


# |%%--%%| <65flpbZWxU|V2SUfBGVpu>

random_prop = sample_proportions(1453, jury["Eligible"].values)
random_prop

# |%%--%%| <V2SUfBGVpu|U1vBqu6vvi>

jury_with_sample = jury.copy()
jury_with_sample["Random Sample"] = random_prop

# |%%--%%| <U1vBqu6vvi|LWUU2ooCsq>

jury_with_sample

# |%%--%%| <LWUU2ooCsq|fE69CP3Lvz>

ax = jury_with_sample.set_index("Ethnicity").plot.bar(rot=0)

# |%%--%%| <fE69CP3Lvz|moeASK5MdU>
"""°°°
### Cálculo da diferença entre proporções
°°°"""
# |%%--%%| <moeASK5MdU|0bHobefHAY>

jury_with_diffs = jury.copy()
jury_with_diffs["Difference"] = jury["Panels"] - jury["Eligible"]
jury_with_diffs

# |%%--%%| <0bHobefHAY|A3JIo9bsS1>

jury_with_diffs["Absolute Difference"] = jury_with_diffs["Difference"].abs()
jury_with_diffs

# |%%--%%| <A3JIo9bsS1|SpcJpxspiX>

jury_with_diffs["Absolute Difference"].sum() / 2

# |%%--%%| <SpcJpxspiX|ZyTsWn8FMm>


def total_variation_distance(distribution_1, distribution_2):
    return sum(np.abs(distribution_1 - distribution_2)) / 2


# |%%--%%| <ZyTsWn8FMm|8U3wdD8SFh>

tvd_real = total_variation_distance(jury["Panels"], jury["Eligible"])
print("total variation distance: ", tvd_real)

# |%%--%%| <8U3wdD8SFh|ZRkoPflIsZ>

eligible_population = jury["Eligible"].values
sample_distribution = sample_proportions(1453, eligible_population)
total_variation_distance(sample_distribution, eligible_population)

# |%%--%%| <ZRkoPflIsZ|TMZvzMooYt>
"""°°°
### Simulando um valor da estatística
°°°"""
# |%%--%%| <TMZvzMooYt|iqFuNwWkt6>

# Simulate one simulated value of
# the total variation distance between
# the distribution of a sample selected at random
# and the distribution of the eligible population


def one_simulated_tvd():
    sample_distribution = sample_proportions(1453, eligible_population)
    return total_variation_distance(sample_distribution, eligible_population)


# |%%--%%| <iqFuNwWkt6|ALbXuj2O22>
"""°°°
### Simulando vários valores da estatística
°°°"""
# |%%--%%| <ALbXuj2O22|22j5AIjLRu>

tvds = []
repetitions = 50000
for i in np.arange(repetitions):
    tvds.append(one_simulated_tvd())

# |%%--%%| <22j5AIjLRu|YqEqpwk3He>

tvds

# |%%--%%| <YqEqpwk3He|8OriOVML7d>

bins = np.arange(0, 0.18, 0.005)
plt.hist(tvds, bins=bins)
plt.xlabel("TVD")
plt.title("Predição considerando seleção aleatória")
plt.axvline(x=tvd_real, color="r")

# |%%--%%| <8OriOVML7d|bU25BEPQZL>

lista_maiores = [a for a in tvds if a >= 0.14]

# |%%--%%| <bU25BEPQZL|kgbnHaYiDP>

len(lista_maiores)

# |%%--%%| <kgbnHaYiDP|4CPW2T06Sh>
"""°°°
# Decisões e Incertezas
°°°"""
# |%%--%%| <4CPW2T06Sh|ObHGcGUjsQ>

705 / 929

# |%%--%%| <ObHGcGUjsQ|cViSPcysLH>

observed_statistic = abs(100 * (705 / 929) - 75)
observed_statistic

# |%%--%%| <cViSPcysLH|GRpdbA0GzQ>

mendel_proportions = [0.75, 0.25]
mendel_proportion_purple = mendel_proportions[0]
sample_size = 929

# |%%--%%| <GRpdbA0GzQ|tSHhjjdkKc>


def one_simulated_distance():
    sample_proportion_purple = sample_proportions(sample_size, mendel_proportions)[0]
    return 100 * abs(sample_proportion_purple - mendel_proportion_purple)


# |%%--%%| <tSHhjjdkKc|LgO6uKCQT4>

repetitions = 10000
distances = []
for i in np.arange(repetitions):
    distances = np.append(distances, one_simulated_distance())

# |%%--%%| <LgO6uKCQT4|GIDfdVaoaJ>

plt.hist(distances)
plt.xlabel("Distance entre a % da Amostra e 75%")
plt.title("Predição feita pela hipótese nula")
plt.axvline(x=observed_statistic, color="r")


# |%%--%%| <GIDfdVaoaJ|kmH5rn29Qg>

different_observed_statistic = 3.2
plt.hist(distances)
plt.xlabel("Distance entre a % da Amostra e 75%")
plt.title("Predição feita pela hipótese nula")
plt.axvline(x=different_observed_statistic, color="m")


# |%%--%%| <kmH5rn29Qg|iY91TBrXOM>

np.count_nonzero(distances >= different_observed_statistic) / repetitions

# |%%--%%| <iY91TBrXOM|ZIWcsXtbZa>
"""°°°
**Exercício 1:** Qual é valor para a estatística observada?
°°°"""
# |%%--%%| <ZIWcsXtbZa|Hlh4jl2TqI>

np.count_nonzero(distances >= observed_statistic) / repetitions

# |%%--%%| <Hlh4jl2TqI|k4FQFcxXef>
"""°°°
**Exercício 2:** Como usar a distribuição binomial para verificar se o número de plantas com flores brancas observado é um valor extremo?
°°°"""
# |%%--%%| <k4FQFcxXef|OzGkW0DC6d>

k = 905
n = 929
p = 0.75

prob = 1 - binom.cdf(k, 929, 0.75)
print(prob)

# |%%--%%| <OzGkW0DC6d|M9CQOES6HM>
"""°°°
# Probabilidades de Erro
°°°"""
# |%%--%%| <M9CQOES6HM|kN1SlNqC3q>


def simula_moeda(p, n):
    return sum(bernoulli.rvs(p, size=n))


# |%%--%%| <kN1SlNqC3q|wHevtsgmwq>

repetitions = 5000
num_tosses = 2000
p = 0.5

difs = list()
for i in range(repetitions):
    s = np.abs(simula_moeda(p, num_tosses) - 1000)
    difs.append(s)

plt.hist(difs)

# |%%--%%| <wHevtsgmwq|u8zEoVFOSv>

from statsmodels.distributions.empirical_distribution import ECDF

ecdf = ECDF(difs)
plt.plot(ecdf.x, ecdf.y)

# |%%--%%| <u8zEoVFOSv|AXeOhxPob6>

values = ecdf.x[::-1]
limiar = values[0]

for x in values[1:]:
    if 1 - ecdf(x) > 0.05:
        break
    limiar = x
print(limiar, 1 - ecdf(limiar))


# |%%--%%| <AXeOhxPob6|M2bERrVaEQ>
