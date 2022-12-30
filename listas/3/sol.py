"""°°°
# Lista 03 - Análise Exploratória de Dados

Continuando da última lista, vamos agora realizar um pouco dos passos da análise exploratória de dados. Em particular, vamos passar pelos passos de:

1. Carregamento dos dados
1. Limpeza dos dados
1. Análise exploratória com gráficos e estatísticas simples

## Imports Básicos

As células abaixo apenas configuram nosso notebook para ficar mais parecido com os das aulas
°°°"""
# |%%--%%| <CRNE5hpoui|1bIsRFlv12>

from numpy.testing import assert_almost_equal
from numpy.testing import assert_equal

# from numpy.testing import assert_array_almost_equal
# from numpy.testing import assert_array_equal

# |%%--%%| <1bIsRFlv12|HESHofO0G1>

# import numpy as np
# import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# |%%--%%| <HESHofO0G1|3Z3QweN52C>

# plt.rcParams['figure.figsize']  = (16, 10)
# plt.rcParams['axes.labelsize']  = 20
# plt.rcParams['axes.titlesize']  = 20
# plt.rcParams['legend.fontsize'] = 20
# plt.rcParams['xtick.labelsize'] = 20
# plt.rcParams['ytick.labelsize'] = 20
# plt.rcParams['lines.linewidth'] = 4

# |%%--%%| <3Z3QweN52C|DbCEJeQA47>

plt.ion()
plt.style.use("seaborn-colorblind")

# |%%--%%| <DbCEJeQA47|UxmMuhD8EG>
"""°°°
## Notas dos Alunos (Tutorial)

Como falamos na última lista, em muitos cenários do mundo real, os dados são carregados de fontes como arquivos. Vamos substituir o DataFrame das notas dos alunos pelo conteúdo de um arquivo de texto. 
°°°"""
# |%%--%%| <UxmMuhD8EG|gVWAttmMDh>

df = pd.read_csv(
    "https://raw.githubusercontent.com/icd-ufmg/icd-ufmg.github.io/master/listas/l3/grades.csv",
    sep=",",
    header=0,
)
df.head()

# |%%--%%| <gVWAttmMDh|w36JjIxMCZ>
"""°°°
O método `read_csv` do `DataFrame` é usado para carregar dados de arquivos de texto. Como você pode ver no código de exemplo, você pode especificar opções como o delimitador de coluna e qual linha (se houver) contém cabeçalhos de coluna (neste caso, o delimitador é uma vírgula e a primeira linha contém os nomes das colunas).

Além do mais, a chamada `head` imprime as primeiras cinco linhas da nossa tabela.
°°°"""
# |%%--%%| <w36JjIxMCZ|GYujpCDQVp>
"""°°°
### Dados Faltantes

Um dos problemas mais comuns com os quais os cientistas de dados precisam lidar são dados incompletos ou ausentes. Como podemos saber que o DataFrame contém valores ausentes? Você pode usar o método `isnull` para tal tarefa.
°°°"""
# |%%--%%| <GYujpCDQVp|STVbxQPchB>

df.isnull()

# |%%--%%| <STVbxQPchB|nkLtHteOSD>
"""°°°
Obseve como a última linha falta com o número de horas estudadas. Nas dúas últimas, faltam as notas. Caso você deseja saber a quantidade de dados faltantes, basta somar os `True`s da tabela acima. Aqui é importante saber que Python tratta `True` de forma similar ao número 1. Portanto, basta você somar a tabela inteira para pegar tal quantidade de dados faltantes.
°°°"""
# |%%--%%| <nkLtHteOSD|IoOwKNCYV9>

df.isnull().sum()

# |%%--%%| <IoOwKNCYV9|vH7zyk3CwJ>
"""°°°
Lembrando que a chamada `iloc` pega uma linha com base no número da mesma, vamos observar a última linha da tabela de dados. Observe como os valores faltantes viram `NaN`s. Além do mais, lembre-se que podemos indexar de trás para frente com o -1. -1 é a última linha, -2 a penúltima. Para entender a lógica, em um vetor de tamanho `n`, `n-1` é o último elemento. Indexar `-1` indica `n-1`.
°°°"""
# |%%--%%| <vH7zyk3CwJ|gyZFn52Dxw>

df.iloc[-1]

# |%%--%%| <gyZFn52Dxw|X1WEgVpw2t>
"""°°°
A penúltima.
°°°"""
# |%%--%%| <X1WEgVpw2t|Cprb1fFgH9>

df.iloc[-2]

# |%%--%%| <Cprb1fFgH9|Vq65NqKhDo>
"""°°°
Agora que encontramos os valores faltantes, o que podemos fazer a respeito deles?

#### fillna

Uma abordagem comum é imputar valores de substituição. Por exemplo, se o número de horas de estudo está faltando, podemos simplesmente supor que o aluno estudou por um período médio de tempo e substituir o valor faltante com as horas de estudo médias. Para fazer isso, podemos usar o método fillna, como este:
°°°"""
# |%%--%%| <Vq65NqKhDo|7H7pV6LgjR>

# df["StudyHours"].mean()
df["StudyHours"].fillna(df["StudyHours"].mean())

# |%%--%%| <7H7pV6LgjR|9CaDjF1lm9>
"""°°°
Observe que a última linha foi alterada! Porém, o DataFrame original não foi.
°°°"""
# |%%--%%| <9CaDjF1lm9|br6evnI080>

df.iloc[-1]

# |%%--%%| <br6evnI080|6rn8N8GrXr>
"""°°°
Para alterar, podemos trocar a coluna. Abaixo faço tal operação em uma cópia dos dados. Realizei tal escolha apenas para não mudar a tabela original.
°°°"""
# |%%--%%| <6rn8N8GrXr|xmWg8coY2h>

df_novo = df.copy()  # criar uma cópia apenas para o exemplo
df_novo["StudyHours"] = df_novo["StudyHours"].fillna(df_novo["StudyHours"].mean())
df_novo.iloc[-1]

# |%%--%%| <xmWg8coY2h|QTLKCIZxZx>
"""°°°
Observe como não mudamos nada das notas. O `fillna` pode receber uma série indexada para alterar várias colunas. Primeiramente, observe como a chamada `mean` pega a média de todas as colunas.
°°°"""
# |%%--%%| <QTLKCIZxZx|ADz4P2KiXT>

df.mean()

# |%%--%%| <ADz4P2KiXT|s9cfd31TtH>
"""°°°
O `fillna` então vai pegar o índice dessa série, o nome da coluna, e utilizar como chave para quais colunas imputar. O valor da série indica o valor que será imputado. Observe como os novos dados abaixo estão sem NaNs.
°°°"""
# |%%--%%| <s9cfd31TtH|prK42ut8hM>

df_novo = df.fillna(df.mean())
df_novo

# |%%--%%| <prK42ut8hM|TRvYsuPzlP>

df_novo.isnull().sum()

# |%%--%%| <TRvYsuPzlP|Ps51FMQBhY>
"""°°°
#### dropna

Outra opção é simplesmente remover todas as linhas com dados faltantes. Para tal, fazemos uso da chamada `dropna`.
°°°"""
# |%%--%%| <Ps51FMQBhY|WUxC8Z7sbq>

df_novo = df.dropna()
df_novo.shape

# |%%--%%| <WUxC8Z7sbq|9VnJ9NqLJ1>

df.shape

# |%%--%%| <9VnJ9NqLJ1|fAVITZoOxy>
"""°°°
Observe como o novo DataFrame tem duas linhas a menos do que o anterior. A escolha de como limpar dados faltantes depende do tipo de análise que você vai realizar. Aqui, vamos seguir com o drop no `df`.
°°°"""
# |%%--%%| <fAVITZoOxy|KAXTFcvl4Y>

df.dropna(inplace=True)  # on inplace=True altera o dataframe atual, não retorna um novo
df

# |%%--%%| <KAXTFcvl4Y|9EVPEYMsBt>
"""°°°
### Explorando Dados

Lembre-se que você pode indexar DataFrames com vetores booleanos. Por exemplo, para pegas as notas de Skye podemos primeiramente achar a discente nos dados:
°°°"""
# |%%--%%| <9EVPEYMsBt|KRxskFkMFB>

df["Name"] == "Skye"

# |%%--%%| <KRxskFkMFB|AlulpLEPVc>
"""°°°
Obserne como acima temos uma entrada verdadeira. Esta, é justamente a linha onde temos o nome `Skye`. Ao indexar o DataFrame com tal linha, pegamos a nota da discente.
°°°"""
# |%%--%%| <AlulpLEPVc|h2sgfIF8T5>

idx = df["Name"] == "Skye"
df[idx]

# |%%--%%| <h2sgfIF8T5|PUBUz31sFR>
"""°°°
Outra forma de fazer a mesma operação é com o método **query**. O query faz consultados usando uma línguagem similar aos bancos de dados. Um exemplo:
°°°"""
# |%%--%%| <PUBUz31sFR|mVjJz289YS>

df.query('Name == "Skye"')

# |%%--%%| <mVjJz289YS|c97PKTlOAa>
"""°°°
Podemos também pegar todas as notas acima de 60. Ou seja, os alunos aprovados.
°°°"""
# |%%--%%| <c97PKTlOAa|x5SwRDPMZd>

df.query("Grade >= 60")

# |%%--%%| <x5SwRDPMZd|dX3JN6Sx0X>
"""°°°
Como também os alunos que passaram estudando relativamente pouco.  No nosso caso, vamos focar em alunos que estudaram menos do que 14horas.
°°°"""
# |%%--%%| <dX3JN6Sx0X|6zVDCdr2oH>

df.query("Grade >= 60 and StudyHours <= 14")

# |%%--%%| <6zVDCdr2oH|IttWpO0oWn>
"""°°°
Todo retorno, ou do índice booleano ou da query são outros DataFrames. Então, podemos chamar métodos como tirar a média dos alunos.
°°°"""
# |%%--%%| <IttWpO0oWn|3eydca9t31>

above_60_low_hours = df.query("Grade >= 60 and StudyHours <= 14")
type(above_60_low_hours)

# |%%--%%| <3eydca9t31|F1yXAUV5hN>

above_60_low_hours.mean()

# |%%--%%| <F1yXAUV5hN|HbjTxjUtg6>
"""°°°
Podemos também buscar os alunos que estão acima da média!
°°°"""
# |%%--%%| <HbjTxjUtg6|lhMfJOIfuV>

mean = df["Grade"].mean()
df[df["Grade"] >= mean]

# |%%--%%| <lhMfJOIfuV|frq943L48Y>
"""°°°
ou, via query.
°°°"""
# |%%--%%| <frq943L48Y|fS9Pp9twGi>

df.query(f"Grade >= {mean}")

# |%%--%%| <fS9Pp9twGi|WIvtd5GQfZ>
"""°°°
Os DataFrames são incrivelmente versáteis e facilitam a manipulação de dados. Muitas operações DataFrame retornam uma nova cópia do DataFrame; portanto, se quiser modificar um DataFrame, mas manter a variável existente, você precisará atribuir o resultado da operação à variável existente. Por exemplo, o código a seguir classifica os dados do aluno em ordem decrescente de nota e atribui o DataFrame classificado resultante à variável `df_students`. 
°°°"""
# |%%--%%| <WIvtd5GQfZ|rgr92YOy3k>

# Re-ordena os dados por nota
df_students = df.sort_values("Grade", ascending=False)
df_students

# |%%--%%| <rgr92YOy3k|bgKlT0XmzH>
"""°°°
### Visualizando dados com Matplotlib

Os DataFrames fornecem uma ótima maneira de explorar e analisar dados tabulares, mas uma imagem vale mil palavras. A biblioteca [Matplotlib](matplotlib.org) fornece a base para a plotagem de visualizações de dados.

Vamos começar com um histograma de notas. Observe como também colocamos uma linha preta em cada barra `edgecolor='k'` e setamos rótulos ao X e Y (para sabermos qual eixo mostra quais dados).
°°°"""
# |%%--%%| <bgKlT0XmzH|qtmicyhQ0O>

plt.hist(df_students["Grade"], edgecolor="k")
plt.xlabel("Grade")
plt.ylabel("Num. Students")
plt.show()

# |%%--%%| <qtmicyhQ0O|mjb3vcOZeW>
"""°°°
Observe como as notas concentram em 50. Às vezes é mais simples interpretar a função cumulativa dos dados.  Vamos fazer este gráfico de uma forma diferente da que vimos em sala de aula. Alterando um pouco a chamada `hist` podemos pegar a cumulativa.
°°°"""
# |%%--%%| <mjb3vcOZeW|Hc2hpTv9vQ>

plt.hist(df_students["Grade"], edgecolor="k", cumulative=True)
plt.xlabel("Grade - x")
plt.ylabel("Num. Students with Grade <= x")
plt.show()

# |%%--%%| <Hc2hpTv9vQ|c4WAdMU14o>
"""°°°
Agora, `density=True` transforma este plot em uma função cumulativa de probabilidade.
°°°"""
# |%%--%%| <c4WAdMU14o|14x06LmiJf>

plt.hist(df_students["Grade"], edgecolor="k", cumulative=True, density=True)
plt.xlabel("Grade - x")
plt.ylabel("Frac. Students with Grade <= x")
plt.show()

# |%%--%%| <14x06LmiJf|Ng6PBhJ1ag>
"""°°°
Observe que 50% dos alunos (0.5 no eixo-y) tem nota menor ou igual à mais ou menos 47~50 (eixo-x). Isto pode ser verificado com a chamada median abaixo. Outro exemplo, tente entender no gráfico, 20% dos alunos (eixo-y) tem nota menor ou igual à mais ou menos 30.
°°°"""
# |%%--%%| <Ng6PBhJ1ag|jCDkLmTlUe>

df_students["Grade"].median()

# |%%--%%| <jCDkLmTlUe|gb6EBQvmEd>
"""°°°
Até agora, você usou métodos do Matplotlib.pyplot para plotar gráficos. No entanto, muitos pacotes, incluindo Pandas, fornecem métodos que abstraem as funções Matplotlib simplificando sua vida. Por exemplo, o DataFrame fornece seus próprios métodos para plotar dados, conforme mostrado no exemplo a seguir para plotar um gráfico de barras de horas de estudo. 
°°°"""
# |%%--%%| <gb6EBQvmEd|iuGoYGiXai>

# df_students.plot.bar(x="Name", y="Grade", edgecolor="k")
plt.show()

# |%%--%%| <iuGoYGiXai|OK1GxFFuDG>
"""°°°
Ou o mesmo histograma de antes.
°°°"""
# |%%--%%| <OK1GxFFuDG|t8AHgz76Bg>

df_students.plot.hist(y="Grade", edgecolor="k")
plt.xlabel("Grade - x")
plt.ylabel("Num. Students")
plt.show()

# |%%--%%| <t8AHgz76Bg|hLN4xgloXj>
"""°°°
Como também uma versão contínua do histograma. Esta é chamada de Kernel Density Estimation (vimos rapidamente em sala de aula).
°°°"""
# |%%--%%| <hLN4xgloXj|cV7pglq85I>

# requer scipy
df_students.plot.kde(y="Grade")
plt.xlabel("Grade - x")
plt.ylabel("Density")
plt.show()

# |%%--%%| <cV7pglq85I|EA9hWANEGT>
"""°°°
### Estatísticas

#### Medidas de tendência central

Para entender melhor a distribuição, podemos examinar as chamadas medidas de tendência central; que é uma maneira sofisticada de descrever estatísticas que representam o "meio" dos dados. O objetivo disso é tentar encontrar um valor "típico". Maneiras comuns de definir o meio dos dados incluem:
  * A média: uma média simples baseada na soma de todos os valores no conjunto de amostra e, em seguida, na divisão do total pelo número de amostras.
  * A mediana: o valor no meio do intervalo de todos os valores de amostra.
  * A moda: o valor de ocorrência mais comum no conjunto de amostra.

Vamos calcular esses valores, junto com os valores mínimo e máximo para comparação, e mostrá-los no histograma. Primeiramente, observe como podemos pegar tais valores direto do DataFrame.
°°°"""
# |%%--%%| <EA9hWANEGT|wLFjW4W6kv>

df.mean()

# |%%--%%| <wLFjW4W6kv|uO8cznWsPt>

df.median()

# |%%--%%| <uO8cznWsPt|7284qFZm99>
"""°°°
Ou, descrever o DataFrame como um todo. Aqui pegamos a média, mínimo, máximo e quartis (mais abaixo) dos dados.
°°°"""
# |%%--%%| <7284qFZm99|ZxGxxpAYbt>

df.describe()

# |%%--%%| <ZxGxxpAYbt|M6293J8zHK>
"""°°°
Além disso, podemos focar em um vetor de dados específico.
°°°"""
# |%%--%%| <M6293J8zHK|eCnjyYb0JV>

data = df["Grade"]


min_ = data.min()
max_ = data.max()
mean = data.mean()
median = data.median()
mode = data.mode()[0]

print(min_, max_, mean, median, mode, sep=", ")

# |%%--%%| <eCnjyYb0JV|5BQUxiVZq2>
"""°°°
Abaixo plotamos cada estatística em linhas verticais.
°°°"""
# |%%--%%| <5BQUxiVZq2|qqSMOQfUus>

# Histograma
plt.hist(data, edgecolor="k")
plt.xlabel("Grade")
plt.ylabel("Num. Students")

# Linhas para cada estatística
plt.axvline(x=min_, color="gray", linestyle="dashed", linewidth=2, label="min")
plt.axvline(x=mean, color="cyan", linestyle="dashed", linewidth=2, label="mean")
plt.axvline(x=median, color="red", linestyle="dashed", linewidth=2, label="median")
plt.axvline(x=mode, color="yellow", linestyle="dashed", linewidth=2, label="mode")
plt.axvline(x=max_, color="gray", linestyle="dashed", linewidth=2, label="max")

# Adiciona uma legenda
plt.legend()
plt.show()

# |%%--%%| <qqSMOQfUus|Da1PYvr66w>
"""°°°
### Medidas de variância

Portanto, agora temos uma boa ideia de onde estão as estatísticas centrais dos dados. No entanto, há outro aspecto das distribuições que devemos examinar: quanta variabilidade existe nos dados?

As estatísticas típicas que medem a variabilidade nos dados incluem:

* Intervalo: a diferença entre o máximo e o mínimo. Não há função incorporada para isso, mas é fácil calcular usando as funções mín e máx.
* Variância: a média da diferença quadrática da média. Você pode usar a função var integrada para encontrar isso.
* Desvio padrão: a raiz quadrada da variância. Você pode usar a função std embutida para encontrar isso. 
°°°"""
# |%%--%%| <Da1PYvr66w|CQXGbYLfVT>

for col_name in ["Grade", "StudyHours"]:
    col = df_students[col_name]
    rng = col.max() - col.min()
    var = col.var(ddof=1)
    std = col.std(ddof=1)
    print(
        "\n{}:\n - Range: {:.2f}\n - Variance: {:.2f}\n - Std.Dev: {:.2f}".format(
            col_name, rng, var, std
        )
    )

# |%%--%%| <CQXGbYLfVT|BhhLuJSIZA>
"""°°°
#### Quartis

Na estatística descritiva, um quartil é qualquer um dos três valores que divide o conjunto ordenado de dados em quatro partes iguais, e assim cada parte representa 1/4 da amostra ou população.

Assim, no caso duma amostra ordenada,
  * primeiro quartil (designado por Q1/4) = quartil inferior = é o valor aos 25% da amostra ordenada = 25º percentil
  * segundo quartil (designado por Q2/4) = mediana = é o valor até ao qual se encontra 50% da amostra ordenada = 50º percentil, ou 5º decil.
  * terceiro quartil (designado por Q3/4) = quartil superior = valor a partir do qual se encontram 25% dos valores mais elevados = valor aos 75% da amostra ordenada = 75º percentil
  * à diferença entre os quartis superior e inferior chama-se amplitude inter-quartil.
  
Observe como os quartis estão presentes na sumarização dos dados. São as linhas 25%, 50% (mediana) e 75%.
°°°"""
# |%%--%%| <BhhLuJSIZA|ThTRvcwSrb>

df.describe()

# |%%--%%| <ThTRvcwSrb|jntbGZ3MkJ>
"""°°°
#### Comparando Dados

Por fim, vamos comparar o tempo de estudo entre os alunos que passaram ou não. Para tal, vamos definir qualquer nota >= 60 como sendo uma aprovação. Depois disso, vamos alterar o DataFrame para conter tal informação.

Primeiro criando a série com tal informação.
°°°"""
# |%%--%%| <jntbGZ3MkJ|tVEh7CsnSs>

passed = df["Grade"] >= 60
passed

# |%%--%%| <tVEh7CsnSs|5qYK0YEeZq>
"""°°°
Agora, alterando o DataFrame.
°°°"""
# |%%--%%| <5qYK0YEeZq|glTkmtfUol>

df["Passed"] = passed
df

# |%%--%%| <glTkmtfUol|GEw0VlQbPz>
"""°°°
Agora, vamos entender o tempo de dedicação dos alunos que passam e dos que não passam. Podemos fazer uso do Boxplot para tal comparativo. Na estatística descritiva, o boxplot é uma ferramenta gráfica para representar a variação de dados observados de uma variável numérica por meio de quartis.

A "caixa" mostra o primeiro e terceiro quartil. A linha no meio mostra o segundo, a mediana. Portanto, a caixa se estende dos valores dos quartil de Q1 a Q3 dos dados, com uma linha na mediana (Q2). Os bigodes se estendem das bordas da caixa para mostrar a extensão dos dados. Por padrão, eles estendem não mais do que 1,5 * IQR (IQR = Q3 - Q1) das bordas da caixa, terminando no ponto de dados mais distante dentro desse intervalo. Valores fora desta faix são plotados como pontos separados. 
°°°"""
# |%%--%%| <GEw0VlQbPz|1Po2lLM3Wf>

df.boxplot(column="StudyHours", by="Passed", grid=False)
plt.show()

# |%%--%%| <1Po2lLM3Wf|QukOoicuGQ>
"""°°°
Observe que, como esperado, alunos que passam estudam mais. Os quartis, portanto a distribuição dos dados, são mais altos. Para observar os valores podemos fazer um groupby.

Abaixo eu agrupo os dados por passou ou não. Depois, pego as horas de estudo. Por fim, observo as estatíticas.
°°°"""
# |%%--%%| <QukOoicuGQ|jzzsYE3PEu>

df.groupby("Passed")["StudyHours"].describe()

# |%%--%%| <jzzsYE3PEu|mxXxJK4nUM>
"""°°°
Observe como 25% (primeiro quartil) dos alunos que não passam, estudam menos do que 8,25 horas. Para os que passam, este valor é de 13,125. Agora pense no complemento dos 25%. 75% dos alunos que passam estudam pelo menos 13h! Isso é bem maior do que as 8h dos que não passam!
°°°"""
# |%%--%%| <mxXxJK4nUM|4DkFnpmHeE>
"""°°°
### Correlacionando Dados

Por fim, podemos correlacional o tempo de estudo com a nota.
°°°"""
# |%%--%%| <4DkFnpmHeE|4cxbZ6liYG>

plt.scatter(df.StudyHours, df.Grade, edgecolor="k", alpha=0.75)
plt.xlabel("Hours")
plt.ylabel("Grade")
plt.show()

# |%%--%%| <4cxbZ6liYG|5BzhCrm7PU>
"""°°°
## Exercícios (Flight Data)

Eu espero que o tutorial acima tenha sido uma boa revisão de análise exploratória de dados. Agora é com você! Nesta lista, você explorará um conjunto de dados do mundo real contendo dados de voos do Departamento de Transporte dos EUA.

Vamos começar carregando e visualizando os dados. 
°°°"""
# |%%--%%| <5BzhCrm7PU|gKTZegPct8>

df = pd.read_csv(
    "https://raw.githubusercontent.com/icd-ufmg/icd-ufmg.github.io/master/listas/l3/flights.csv"
)

# |%%--%%| <gKTZegPct8|RmtHaYOANk>
"""°°°
O conjunto de dados contém observações de voos domésticos dos EUA em 2013 e consiste nos seguintes campos:
* Ano: o ano do voo (todos os registros são de 2013)
* Mês: o mês do voo
* Dia do mês: o dia do mês em que o voo partiu
* DayOfWeek: o dia da semana em que o voo partiu - de 1 (segunda-feira) a 7 (domingo)
* Transportadora: a abreviatura de duas letras da companhia aérea.
* OriginAirportID: Um identificador numérico exclusivo para o aeroporto de partida
* Nome do aeroporto de origem: o nome completo do aeroporto de partida
* OriginCity: a cidade do aeroporto de partida
* Estado de origem: o estado do aeroporto de partida
* DestAirportID: Um identificador numérico único para o aeroporto de destino
* DestAirportName: o nome completo do aeroporto de destino
* DestCity: a cidade do aeroporto de destino
* DestState: o estado do aeroporto de destino
* CRSDepTime: a hora de partida programada
* DepDelay: o número de minutos de atraso na partida (o voo que saiu antes do horário tem um valor negativo)
* DelDelay15: Um indicador binário de que a partida foi atrasada por mais de 15 minutos (e, portanto, considerada "atrasada")
* CRSArrTime: a hora de chegada programada
* ArrDelay: o número de minutos de atraso na chegada (o voo que chegou antes do horário tem um valor negativo)
* ArrDelay15: Um indicador binário de que a chegada foi atrasada em mais de 15 minutos (e, portanto, considerada "atrasada")
* Cancelado: um indicador binário de que o voo foi cancelado 
°°°"""
# |%%--%%| <RmtHaYOANk|HjpofskG32>

df.head()

# |%%--%%| <HjpofskG32|z11g0lQbHg>
"""°°°
### Exercício 1

Conte a quantidade de dados faltantes na tabela. Isto é, em TODAS as células. O método retorna apenas um número.
°°°"""
# |%%--%%| <z11g0lQbHg|UEsdSTsti6>


def count_missing(df) -> int:
    return df.isnull().sum().sum()


# |%%--%%| <UEsdSTsti6|Ju0HcbboiO>

assert_equal(2761, count_missing(df))

# |%%--%%| <Ju0HcbboiO|Sy3pWPHJfq>
"""°°°
### Exercício 2

Crie um novo DataFrame sem as linhas com dados faltantes
°°°"""
# |%%--%%| <Sy3pWPHJfq|LvAyh3AExk>


def drop_missing(df):
    return df.dropna()


df_new = drop_missing(df)

# |%%--%%| <LvAyh3AExk|hfamIrMXaz>

assert_equal(269179, drop_missing(df).shape[0])

# |%%--%%| <hfamIrMXaz|Xs0V1u77Nk>
"""°°°
### Exercício 3

Retorne a mediana de TODAS as colunas numéricas do DataFrame
°°°"""
# |%%--%%| <Xs0V1u77Nk|9SBRTZKGUs>


def all_median(df):
    return df.median(numeric_only=True)


# |%%--%%| <9SBRTZKGUs|CWnxiXBoRH>

assert_equal(2013, all_median(df_new)["Year"])
assert_equal(7, all_median(df_new)["Month"])

# |%%--%%| <CWnxiXBoRH|eNCzwVnEPV>
"""°°°
### Exercício 4

Quais são os atrasos médios (médios) de partida e chegada? Retorne uma tupla.
°°°"""
# |%%--%%| <eNCzwVnEPV|303mvZPsTc>


def delay(df) -> tuple:
    return df["DepDelay"].mean(), df["ArrDelay"].mean()


# |%%--%%| <303mvZPsTc|iERcG8E0WT>

assert_almost_equal(10.456614371849216, delay(df_new)[0])
assert_almost_equal(6.563286883449304, delay(df_new)[1])

# |%%--%%| <iERcG8E0WT|fD6qM8r8VN>
"""°°°
### Exercício 5

Indique qual rota tem o maior tempo de voo em MÉDIA. Use a coluna OriginAirportName e DestinationAirportName. Retorne uma tupla `(OriginAirportName, DestinationAirportName)`. Lembre-se de não considerar voos cancelados!
°°°"""
# |%%--%%| <fD6qM8r8VN|4wPKIstRkI>


def getMinutes(numTime: int, delay: int) -> int:
    """
    Calcule a diferença entre minutos dos tempos
    Não é necessário saber a diferença com uma estrutura de horário (eg, HH:MM)
    """
    minutes = int(numTime) % 100
    minutes += (int(numTime) // 100) * 60
    minutes += int(delay)
    return minutes


def difTime(
    arrTime: pd.Series, arrDelay: pd.Series, depTime: pd.Series, depDelay: pd.Series
) -> pd.Series:
    """
    Calcule a diferença de tempo fazendo a conversão necessária do formato esquisito de hora
    """
    timeArr = []
    for i, j, k, l in zip(
        arrTime.values, arrDelay.values, depTime.values, depDelay.values
    ):
        arrMin = getMinutes(int(i), int(j))
        depMin = getMinutes(int(k), int(l))
        # Ajuste se o tempo de chegada é maior que o tempo de partida
        # Ou seja, o dia "virou" (não considera o caso de um trecho maior que 24 horas)
        if arrMin > depMin:
            timeArr.append(arrMin - depMin)
        else:
            timeArr.append(24 * 60 - (depMin - arrMin))
    ser = pd.Series(timeArr)
    return ser


def high_delay(df: pd.DataFrame):
    not_canc = df[df["Cancelled"] == False]
    # Essa solução não considera o formato verdadeiro da hora
    arrTime = not_canc["CRSArrTime"] + not_canc["ArrDelay"]
    depTime = not_canc["CRSDepTime"] + not_canc["DepDelay"]
    idx_same_day = not_canc.CRSArrTime >= not_canc.CRSDepTime
    not_canc.loc[idx_same_day, "FT"] = arrTime - depTime
    not_canc.loc[~idx_same_day, "FT"] = 2400 - depTime + arrTime
    df_ready = not_canc[["OriginAirportName", "DestAirportName", "FT"]].copy()
    s = (
        df_ready.groupby(["OriginAirportName", "DestAirportName"])
        .mean()
        .sort_values(by="FT")
        .iloc[-1]
        .name
    )
    return s
    # Essa solução ajeita o formato da hora, mas não é aceita
    # time_of_flight = difTime(
    #     df_not_calc["CRSArrTime"],
    #     df_not_calc["ArrDelay"],
    #     df_not_calc["CRSDepTime"],
    #     df_not_calc["DepDelay"],
    # )
    # df_with_time = df_not_calc.assign(FlightTime=time_of_flight)
    # means = df_with_time.groupby(["OriginAirportName", "DestAirportName"]).mean()
    # rowMax = means.loc[means["FlightTime"].idxmax()]
    # return rowMax.name


high_delay(df_new)

# |%%--%%| <4wPKIstRkI|awEl8ueY1f>
"""°°°
### Exercício 6

Faça um boxplot dos atrasos de saída por dia da semana!

1. Dica, use `grid=False, showfliers=False` para o plot ficar mais limpo

*Saída esperada*

![](https://raw.githubusercontent.com/icd-ufmg/icd-ufmg.github.io/master/listas/l3/plot1.png)
°°°"""
# |%%--%%| <awEl8ueY1f|dR9Ywpjgz8>

df_new.boxplot(column="DepDelay", by="DayOfWeek", grid=False, showfliers=False)
plt.show()


# |%%--%%| <dR9Ywpjgz8|ENkBlGJYgl>
"""°°°
### Exercício 7

Correlacione o atraso de saída com o atraso de chegada!

1. Dica, remova os voos cancelados

*Saída esperada*

![](https://raw.githubusercontent.com/icd-ufmg/icd-ufmg.github.io/master/listas/l3/plot2.png)
°°°"""
# |%%--%%| <ENkBlGJYgl|htnnLgVlEj>

plt.scatter(df_new["DepDelay"], df_new["ArrDelay"], edgecolors="black", marker=".")
