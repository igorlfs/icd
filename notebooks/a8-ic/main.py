r"""°°°
# Simulando a estimativa da prevalência de COVID-19

Primeiro, vamos criar uma população de brasileiros infectados com COVID-19. Para isso, vamos assumir que a probabilidade de um brasileiro estar infectado segue uma distribuição de Bernoulli com média $p$.
°°°"""
# |%%--%%| <ldvRxNKRHd|TeFchmZ6AI>

import matplotlib.pyplot as plt
from scipy.stats import bernoulli

# |%%--%%| <TeFchmZ6AI|1LKaMX0nkU>

p = 0.05
# se seu computador não tem muito memória RAM (<8GB), troque este valor para 20000000 ou menos
tam_pop = 100000000
pop = bernoulli.rvs(p, size=tam_pop)

# |%%--%%| <1LKaMX0nkU|sWlGOjROdS>

res = plt.hist(pop)
p_real = sum(pop) / len(pop)
print(p_real)


# |%%--%%| <sWlGOjROdS|ZlH5sN3Kkn>
"""°°°
Vamos agora extrair uma amostra de tamanho $n$ dessa população.
°°°"""
# |%%--%%| <ZlH5sN3Kkn|iVZY7WcdWP>

import random

# |%%--%%| <iVZY7WcdWP|Oo7vFcK9p8>

n = 1000
amostra = random.sample(list(pop), n)
res = plt.hist(amostra)

# |%%--%%| <Oo7vFcK9p8|5LDELkVIXo>
"""°°°
Agora vamos estimar a média e a variância da população a partir dessa amostra.
°°°"""
# |%%--%%| <5LDELkVIXo|XUwXD10NGo>

p_hat = sum(amostra) / len(amostra)
var_amostra = p_hat * (1 - p_hat)
print(p_hat, var_amostra)

# |%%--%%| <XUwXD10NGo|JzQJJghgJ3>
r"""°°°
Agora podemos definir um intervalo de confiança para a média da população.

Pelo Teorema Central do Limite, sabemos que a distribuição das médias amostrais segue um distribuição Normal com média $\mu$ e variância $\sigma/n$. Então, a função de densidade de probabilidade dessa distribuição é:
°°°"""
# |%%--%%| <JzQJJghgJ3|H6kGsjniG0>

import numpy as np
from scipy.stats import norm

mu_hat = p_hat
sigma_hat = (var_amostra / n) ** 0.5

xs = np.arange(0, 0.1, 0.0001)
fig = plt.figure()
plt.plot(xs, [norm.pdf(x, mu_hat, sigma_hat) for x in xs], "b-")
plt.ylabel(r"$f(\hat{p})$")
plt.xlabel(r"$\hat{p}$")
plt.show()


# |%%--%%| <H6kGsjniG0|06iNbFOUr0>
r"""°°°
A partir dessa distribuição de probabilidade, podemos calcular a probabilidade da média da população $\mu$ estar dentro de um determinado intervalo.

Por exemplo, a probabilidade $P(0.04 \leq \mu \leq 0.06)$ da média $\mu$ estar dentro do intervalo $[0.04, 0.06]$ é a área abaixo da curva acima neste intervalo, que pode ser aproximada pela diferença de CDFs:

$P(0.04 \leq \mu \leq 0.06) = CDF(0.06) - CDF(0.04)$
°°°"""
# |%%--%%| <06iNbFOUr0|0nmxSgFeaf>

p_intervalo = norm.cdf(0.06, mu_hat, sigma_hat) - norm.cdf(0.04, mu_hat, sigma_hat)
print("Probabilidade da média estar no intervalo [0.04, 0.06]:", p_intervalo)

# |%%--%%| <0nmxSgFeaf|aBIQyQaXRJ>
r"""°°°
A partir da função inversa da CDF podemos também calcular um intervalo simétrico ao redor da média amostral em que a probabilidade da média $\mu$ esteja neste intervalo é de $C\%$, por exemplo, $95\%$.

Para isso, e no intuito de construir um intervalo simétrico, vamos colocar metade da probabilidade que queremos (ex: $47.5\%$) à direita da média e metade à esquerda. Dessa forma, precisamos encontrar o valor $x$ (ou $\hat{p}$) que tenha $97.5\%$ dos valores menores que ele ($x_{sup}$) e o valor $x$ que tenha somente $2.5\%$ dos valores menores que ele ($x_{inf}$). Ou seja, entre $x_{inf}$ e $x_{sup}$ concentra-se $95\%$ da densidade da função de probabilidade e essa densidade é simétrica em relação à média amostral.

Para encontrar tais valores usaremos a função inversa da CDF, ou seja, aquela que retorna, para um dada probabilidade $p$, o valor $x$ que possui $p$ valores menores ou iguais a ele. Em Python, felizmente, há uma função pronta que faz quase isso, a `norm.isf` do `scipy.stats`. Embora não seja equivalente a função inversa da CDF, ela é o inverso da CCDF, ou seja, da 1-CDF. Então, ela nos serve se usarmos o complemento `1-p` da probabilidade `p`. Enquanto uma função inversa da CDF (funçao `inverse_normal_cdf` dos slides) retorna o inverso da CDF (ou $P(X \leq x)$, a função `norm.isf` retorna o inverso da função de sobrevivência da normal, que é 1-CDF (ou P(X > x). Assim, se quisermos saber qual é o menor valor $x$ que é maior ou igual a $20\%$ dos valores da distribuição (`inverse_normal_cdf(0.2, mu, sigma)`) , basta encontrar o valor $x$ que é estritamente menor que $80\%$ dos valores da distribuição, ou `norm.isf(1-0.2, mu, sigma)`.

Implementamos essas funções inversas abaixo. Note, inclusive, que já implementamos a função `normal_two_sided_bounds`, que distribui a probabilidade simetricamente e já retorna os valos de $x_{inf}$ e $x_{sup}$.


°°°"""
# |%%--%%| <aBIQyQaXRJ|znqbyO9WVF>


def normal_upper_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z <= z) = probability"""
    return norm.isf(1 - probability, mu, sigma)


def normal_lower_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z >= z) = probability"""
    return norm.isf(probability, mu, sigma)


def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """returns the symmetric (about the mean) bounds
    that contain the specified probability"""
    tail_probability = (1 - probability) / 2
    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    # lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    return lower_bound, upper_bound


# |%%--%%| <znqbyO9WVF|bWc6TSiNoy>
r"""°°°
Então, se quisermos encontrar o intervalo para o qual há $95\%$ de probabilidade da média da população estar nele, podemos fazer:
°°°"""
# |%%--%%| <bWc6TSiNoy|PlSlrjT21r>

confianca = 0.95
p_inf, p_sup = normal_two_sided_bounds(confianca, mu_hat, sigma_hat)
print("Intervalo de confiança: [", p_inf, ",", p_sup, "]")

# |%%--%%| <PlSlrjT21r|VFFW4bh50n>
"""°°°
Usando a aproximação normal, concluímos que estamos "95% confiantes" de que o intervalo acima contém o parâmetro verdadeiro $p$.

Esta é uma afirmação sobre o intervalo, não sobre $p$. Você deve entender isso como a afirmação de que se você repetisse a experiência muitas vezes, 95% das vezes o parâmetro "verdadeiro" (que é o mesmo a cada vez) estaria dentro do intervalo de confiança observado (que pode ser diferente a cada vez).

Vamos testar isso:
°°°"""
# |%%--%%| <VFFW4bh50n|ynQ3JnzybS>

n_amostras = 100  # Too much, man
n = 1000
confianca = 0.95
fora_intervalo = 0
for i in range(n_amostras):
    s_i = random.sample(list(pop), n)
    mu_hat = np.mean(s_i)
    sigma_hat = ((mu_hat * (1 - mu_hat)) / n) ** 0.5
    p_inf, p_sup = normal_two_sided_bounds(confianca, mu_hat, sigma_hat)
    if 0.05 < p_inf or 0.05 > p_sup:
        fora_intervalo += 1
        print("[", p_inf, ",", p_sup, "]")

print("Qtde de intervalos que não contêm a média da população:", fora_intervalo)

# |%%--%%| <ynQ3JnzybS|4voORmSdMt>
r"""°°°
Além disso, como essa é uma distribuição normal, ela segue um comportamento bem definido pelas suas funções de probabilidade.

Assim, podemos calcular, por exemplo, quantos desvios padrões foram somados à (e subtraídos de) $\mu$ para encontrarmos $x_{sup}$ (e $x_{inf}$).

A diferença de entre $x_{sup}$ e $\mu$ nos dá de quanto $\mu$ foi acrescido para chegar em $x_{sup}$. Se dividirmos essa diferença por $\sigma$, encontramos quantos desvios padrões foram acrescidos ao $\mu$ para chegarmos a $x_{sup}$. Por padrão, chamamos esse valor de $z$:

$z = \frac{(x_{sup} - \mu)}{\sigma}$

Vamos calculá-lo agora:
°°°"""
# |%%--%%| <4voORmSdMt|3axl6uIyEY>

z_sup = (p_sup - mu_hat) / sigma_hat
z_inf = (p_inf - mu_hat) / sigma_hat

print("z inferior: %.2f \nz superior: %.2f" % (z_inf, z_sup))

# |%%--%%| <3axl6uIyEY|n7FIoNWmM2>
r"""°°°
Muito provavelmente você já viu esse número antes em fórmulas prontas que calculam o intervalo de confiança para uma estimativa. Em resumo, esses são os valores para os quais você deve multiplicar o desvio padrão de uma **distribuição normal** para encontrar o intervalo ao redor da média que corresponde à $95\%$ da densidade de probabilidade.

Vamos criar agora uma função para realizar amostras de diferentes tamanhos e, com essas amostras, calcular o intervalo de confiança para o valor de $p$.
°°°"""
# |%%--%%| <n7FIoNWmM2|d8qEXBJrRF>


def IC_prevalencia(n, pop, confianca=0.95):

    # amostra de tamanho n:
    amostra = random.sample(list(pop), n)

    # media e variancia da amostra:
    p_hat = sum(amostra) / len(amostra)
    var_amostra = p_hat * (1 - p_hat)

    # media e variancia da distribuição normal que rege a variável aleatória p_hat (TCL):
    mu = p_hat
    sigma = (var_amostra / n) ** 0.5

    p_inf, p_sup = normal_two_sided_bounds(confianca, mu, sigma)

    return p_inf, p_sup


# |%%--%%| <d8qEXBJrRF|vLWGarEqkT>
"""°°°
Com essa função, podemos testar o comportamento do intervalo de confiança quando alteramos o tamanho da amostra (lei dos grandes números) e também o nível de confiança.

Vamos começar pelo tamanho da amostra:
°°°"""
# |%%--%%| <vLWGarEqkT|ROJdJcT2il>

tam_amostras = [100, 1000, 10000, 100000, 1000000]

for n in tam_amostras:
    p_inf, p_sup = IC_prevalencia(n, pop)
    print("n =", n, "IC: [", p_inf, ",", p_sup, "]")

# |%%--%%| <ROJdJcT2il|EDlI5Hfi3F>

confiancas = [0.80, 0.90, 0.95, 0.99, 0.999]
n = 1000

for conf in confiancas:
    p_inf, p_sup = IC_prevalencia(n, pop, conf)
    print("confianca =", conf, "IC: [", p_inf, ",", p_sup, "]")

# |%%--%%| <EDlI5Hfi3F|w0HYDYeyz5>
"""°°°
**Exercício:** troque o valor de $p$ da população para valores menores, como $0.01$ e até mesmo $0.001$ e veja o que acontece com os intervalos acima. Por que isso acontece?
°°°"""
# |%%--%%| <w0HYDYeyz5|Fo9ja7qQWc>
"""°°°
Erro numérico?
°°°"""
# |%%--%%| <Fo9ja7qQWc|ZKvoGBUCig>
