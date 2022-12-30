# -*- coding: utf8

import matplotlib.pyplot as plt
from numpy.testing import assert_equal, assert_array_almost_equal
import numpy as np
import pandas as pd
import seaborn as sns

plt.rcParams["figure.figsize"] = (18, 10)
plt.rcParams["axes.labelsize"] = 12
plt.rcParams["axes.titlesize"] = 12
plt.rcParams["legend.fontsize"] = 12
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12
plt.rcParams["lines.linewidth"] = 4

# |%%--%%| <MLT1Y4KJJv|5ujknf3qTH>

plt.ion()
plt.style.use("seaborn-colorblind")
plt.rcParams["figure.figsize"] = (12, 8)

# |%%--%%| <5ujknf3qTH|WgPNQcX5mv>


def despine(ax=None):
    if ax is None:
        ax = plt.gca()
    # Hide the right and top spines
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position("left")
    ax.xaxis.set_ticks_position("bottom")


# |%%--%%| <WgPNQcX5mv|orujzluXzH>

df = pd.read_csv(
    "https://raw.githubusercontent.com/pedroharaujo/ICD_Docencia/master/aptosBH.txt",
    index_col=0,
)
df.head()

# |%%--%%| <orujzluXzH|qxhzxksxTw>

sns.pairplot(df, diag_kws={"edgecolor": "k"}, plot_kws={"alpha": 0.5, "edgecolor": "k"})

# |%%--%%| <qxhzxksxTw|490ki39iI3>

y = df["preco"]
X = df[["area", "quartos", "suites", "vagas"]]
X["intercepto"] = 1
X = X[["intercepto", "area", "quartos", "suites", "vagas"]]
X.head()

# |%%--%%| <490ki39iI3|kSg1dqX22Z>

y.shape

# |%%--%%| <kSg1dqX22Z|aFRNiFh00u>

X.shape

# |%%--%%| <aFRNiFh00u|MLuTUAtBQt>

X = X.values
y = y.values  # pegar a matrix
X

# |%%--%%| <MLuTUAtBQt|1yFKYOoMd4>


def derivadas_regressao_media_old(theta, X, y):
    return -2 * ((y - X @ theta) * X.T).mean(axis=1)


# |%%--%%| <1yFKYOoMd4|RC6JlJMjAl>


def derivadas_regressao(theta, X, y):
    return -2 * ((y - X @ theta) @ X)


# |%%--%%| <RC6JlJMjAl|8MALeULNcR>


def derivadas_regressao_media(theta, X, y):
    return -2 * ((y - X @ theta) @ X) / len(y)


# |%%--%%| <8MALeULNcR|7et9S3jnLs>

df = pd.read_csv(
    "https://raw.githubusercontent.com/pedroharaujo/ICD_Docencia/master/hybrid.csv"
)
df.head()

# |%%--%%| <7et9S3jnLs|WlUBZWMotN>

import seaborn as sns

sns.pairplot(df, diag_kws={"edgecolor": "k"}, plot_kws={"alpha": 0.5, "edgecolor": "k"})

# |%%--%%| <WlUBZWMotN|kZHrib8nEf>

# SELECIONE AS COLUNAS
X = df[["year", "acceleration", "mpg"]]
y = df["msrp"]

# NORMALIZE OS DADOS
X = (X - X.mean()) / X.std(ddof=1)
y = (y - y.mean()) / y.std(ddof=1)

# ACRESCENTE INTERCEPTO
inter: np.ndarray = np.ones(y.size)
X.insert(0, "Intercepto", inter, True)

# EXTRAIA MATRIZES COM .VALUES
X = X.values
y = y.values

# |%%--%%| <kZHrib8nEf|q6ZDEFD2eD>


def gradients(theta, X, y):
    # x : matriz nxm
    # y : array nx1
    # theta : array mx1
    return -2 * ((y - X @ theta) @ X) / len(y)


# |%%--%%| <q6ZDEFD2eD|8TUtqJ4NU5>


def descent(theta0, X, y, learning_rate=0.005, tolerance=0.0000001):
    old_err_sq = np.inf
    i = 0
    while True:
        grad = gradients(theta0, X, y)
        theta_novo = theta0 - learning_rate * grad
        err_sq = ((X.dot(theta_novo) - y) ** 2).mean()

        if np.abs(old_err_sq - err_sq) <= tolerance:
            break
        theta0 = theta_novo
        old_err_sq = err_sq

        i += 1
        if i == 9999999:
            break
    return theta_novo


# |%%--%%| <8TUtqJ4NU5|s1aruAgleV>

_teste_param0 = np.array([1000, 1, 1, 1])
theta = descent(_teste_param0, X, y)
assert_array_almost_equal(
    np.round(theta, 4), np.round([0.00201339, -0.04349112, 0.59055261, -0.23979036], 4)
)

# |%%--%%| <s1aruAgleV|a422RRMxJs>


def sst(y):
    return ((y - y.mean()) ** 2).sum()


def predict(X, theta):
    return X @ theta.T


def sse(X, y, theta):
    return y.T @ y - (y.T @ X @ np.linalg.inv(X.T @ X) @ X.T @ y)


def rsquared(X, y, theta):
    return 1 - (sse(X, y, theta) / sst(y))


# |%%--%%| <a422RRMxJs|EYGTRoFpCx>

rs = rsquared(X, y, theta)
assert_equal(np.round(rs, 4), np.round(0.5288887684860548, 4))

# |%%--%%| <EYGTRoFpCx|NWwTqql3Ua>

from scipy.stats import zscore

# |%%--%%| <NWwTqql3Ua|BCmWJRKS0K>

y = df["msrp"]
X = df[["year", "acceleration", "mpg"]]

# TIRE O LOG DA VARIAVEL MPG
aux = X.copy()
for i in range(len(y)):
    aux.iloc[i, 2] = np.log(aux.iloc[i, 2])
X = aux

# Z-NORMALIZE OS DADOS
X = X.apply(zscore)

# ADICIONE O INTERCEPTO
inter: np.ndarray = np.ones(y.size)
X.insert(0, "Intercepto", inter, True)

# DEFINA X e Y UTILIZANDO .VALUES
X = X.values
y = y.values

# |%%--%%| <BCmWJRKS0K|BQRtWLYtiM>

_teste_param0 = np.array([1000, 1, 1, 1])
theta = descent(_teste_param0, X, y)
rs1 = rsquared(X, y, theta)
assert_equal(np.round(rs1, 4), np.round(0.5543728866213389, 4))

# |%%--%%| <BQRtWLYtiM|t1rz8wglzr>

df = pd.read_csv(
    "https://raw.githubusercontent.com/pedroharaujo/ICD_Docencia/master/chemical_reaction.csv"
)
df.head()

# |%%--%%| <t1rz8wglzr|wRBOZUuP33>

from sklearn.linear_model import LinearRegression

df = pd.read_csv(
    "https://raw.githubusercontent.com/pedroharaujo/ICD_Docencia/master/chemical_reaction.csv",
    index_col=0,
)

X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values

lm = LinearRegression()
lm.fit(X, y)

print("Coeficientes: {}".format(lm.coef_))
print("Intercept: {}".format(lm.intercept_))
print("R^2: {}".format(lm.score(X, y)))

# |%%--%%| <wRBOZUuP33|1eCovCCmkr>

import statsmodels.api as sm

X = sm.add_constant(X)  # adding a constant

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)

# |%%--%%| <1eCovCCmkr|GSXADIyEO9>

df = pd.read_csv(
    "https://raw.githubusercontent.com/pedroharaujo/ICD_Docencia/master/skills_and_overall_sample_20k.csv",
    index_col=0,
)
df.head()

# |%%--%%| <GSXADIyEO9|yNm26M9C5r>

from sklearn.linear_model import LinearRegression

X = df.iloc[:, 1:33].values
y = df.iloc[:, 33].values

lm = LinearRegression()
lm.fit(X, y)

print("Coeficientes: {}".format(lm.coef_))
print("Intercept: {}".format(lm.intercept_))
print("R^2: {}".format(lm.score(X, y)))

# |%%--%%| <yNm26M9C5r|0SHXEv5Uyr>

import statsmodels.api as sm

X = sm.add_constant(X)  # adding a constant

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)

# |%%--%%| <0SHXEv5Uyr|ktiRai6tkf>
