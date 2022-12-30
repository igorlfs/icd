import numpy as np

data_list = [3.5, 5, 2, 8, 4.2]
type(data_list)

data = np.array(data_list)
print(data)
print(type(data))

data + 7

X = np.array([[2, 4], [1, 3]])
X

data[0]

X[0, 1]

X = np.random.randn(4, 3)
print(X)

### Indexando

X[0]

X[1]

X[2]

X[:, 0]

X[:, 1]

X[[0, 0, 1]]

X[:, [1, 0]]

### Indexação Booleana

X[[True, False, True, False]]

X[:, [False, True, True]]

### Reshape, Flatten e Ravel

X = np.random.randn(9, 8)

X.reshape((18, 4))

X.reshape(72)

X.flatten()

X.ravel()

np.log(data)

np.mean(data)

data.mean()

np.median(data)

np.median(X)

X.mean()

np.log(X + 10)

X.shape

np.mean(X, axis=0)

np.mean(X, axis=0).shape

np.mean(X, axis=1)

np.mean(X, axis=1).shape

# Lembre-se que eixo 0 é coluna. Eixo 1 é linas.

### Multiplicação de Matrizes

X.shape

X.T.shape

X.T

X @ X.T

X * X

(X * X).shape

(X @ X.T).shape

### Correção Automática

# from numpy.testing import assert_almost_equal
from numpy.testing import assert_equal

from numpy.testing import assert_array_almost_equal
from numpy.testing import assert_array_equal

assert_array_equal(2, 2)

assert_array_equal([1, 2], [1, 2])

assert_array_almost_equal(3.1415, 3.14, 1)


### Funções em Python


def print_something(txt):
    print(f"Você passou o argumento: {txt}")


print_something("DCC 212")


def sum_of_sum_vectors(array_1, array_2):
    return (array_1 + array_2).sum()


x = np.array([1, 2])
y = np.array([1, 2])

sum_of_sum_vectors(x, y)

assert_equal(6, sum_of_sum_vectors(x, y))

### Exercício 01
def inner(array_1, array_2):
    x = np.array(array_1)
    y = np.array(array_2)
    return (x @ y.T).sum()


x1 = np.array([2, 4, 8])
x2 = np.array([10, 100, 1000])
assert_equal(20 + 400 + 8000, inner(x1, x2))

### Exercício 02
def medmult(X_1, X_2):
    return np.mean(X_1 @ X_2)


X = np.array([1, 2, 3, 4]).reshape(2, 2)
Y = np.array([2, 1, 1, 2]).reshape(2, 2)
assert_equal(7.5, medmult(X, Y))
