# pyright: reportUnusedExpression=false

# |%%--%%| <XUzGohjHPb|xI5bKJ2VMm>
"""°°°
#Manipulando e limpando dados
Esta seção marca uma mudança sutil. Até agora, apresentamos ideias e técnicas para prepará-lo com uma caixa de ferramentas de técnicas para lidar com situações do mundo real. Agora vamos começar a usar algumas dessas ferramentas e, ao mesmo tempo, dar algumas idéias sobre como e quando usá-las em seu próprio trabalho com dados.

Os dados do mundo real são confusos. Provavelmente, você precisará combinar várias fontes de dados para obter os dados que realmente deseja. Os dados dessas fontes estarão incompletos. E provavelmente não será formatado exatamente da maneira que você deseja para realizar sua análise. É por esses motivos que a maioria dos cientistas de dados dirá que cerca de 80% de qualquer projeto é gasto apenas para colocar os dados em um formulário pronto para análise.

## Explorando informações do `DataFrame`

&gt; **Objetivo de aprendizagem:** Ao final desta subseção, você deve estar confortável para encontrar informações gerais sobre os dados armazenados nos DataFrames do pandas.

Depois de carregar seus dados no pandas, é mais provável que eles estejam em um `DataFrame`. No entanto, se o conjunto de dados em seu `DataFrame` tem 60.000 linhas e 400 colunas, como você começa a ter uma noção do que está trabalhando? Felizmente, o pandas fornece algumas ferramentas convenientes para examinar rapidamente informações gerais sobre um `DataFrame`, além das primeiras e últimas linhas.

Para explorar essa funcionalidade, importaremos a biblioteca Python scikit-learn e usaremos um conjunto de dados icônico que todo cientista de dados já viu centenas de vezes: o conjunto de dados * Iris * do biólogo britânico Ronald Fisher usado em seu artigo de 1936 "O uso de múltiplos medições em problemas taxonômicos ":
°°°"""
# |%%--%%| <xI5bKJ2VMm|ii85fxnbUA>

import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris["data"], columns=iris["feature_names"])

# |%%--%%| <ii85fxnbUA|9d2bHY06OR>
"""°°°
### `DataFrame.info`
Vamos dar uma olhada neste conjunto de dados para ver o que temos:
°°°"""
# |%%--%%| <9d2bHY06OR|FKdhXXrQWI>

iris_df.info()

# |%%--%%| <FKdhXXrQWI|1w9dxWQ0cj>
"""°°°
A partir disso, sabemos que o conjunto de dados * Iris * tem 150 entradas em quatro colunas. Todos os dados são armazenados como números de ponto flutuante de 64 bits.
°°°"""
# |%%--%%| <1w9dxWQ0cj|ez204jSUt6>
"""°°°
### `DataFrame.head`
A seguir, vamos ver como são as primeiras linhas do nosso `DataFrame`:
°°°"""
# |%%--%%| <ez204jSUt6|yud92TAQbU>

iris_df.head()

# |%%--%%| <yud92TAQbU|8mzpnTsoVy>
"""°°°
### `DataFrame.tail`
O outro lado de DataFrame.head é DataFrame.tail, que retorna as últimas cinco linhas de um DataFrame:
°°°"""
# |%%--%%| <8mzpnTsoVy|Ip5991de0t>

iris_df.tail()

# |%%--%%| <Ip5991de0t|pt9jB7iNYR>
"""°°°
Na prática, é útil examinar facilmente as primeiras linhas ou as últimas linhas de um DataFrame, principalmente quando você está procurando outliers em conjuntos de dados ordenados.

&gt; Conclusão: mesmo olhando para os metadados sobre as informações em um DataFrame ou os primeiros e os últimos valores em um, você pode ter uma ideia imediata sobre o tamanho, a forma e o conteúdo dos dados com os quais está lidando.
°°°"""
# |%%--%%| <pt9jB7iNYR|liIAVUn68U>
"""°°°
## Lidando com dados ausentes (missing data)

&gt; **Objetivo de aprendizagem:** Ao final desta subseção, você deve saber como substituir ou remover valores nulos de DataFrames.

Na maioria das vezes, os conjuntos de dados que você deseja usar (ou deve usar) têm valores ausentes. A maneira como os dados ausentes são tratados traz consigo compensações sutis que podem afetar sua análise final e os resultados do mundo real.

O Pandas lida com valores ausentes de duas maneiras. O primeiro que você viu antes nas seções anteriores: `NaN` ou Not a Number. Na verdade, este é um valor especial que faz parte da especificação de ponto flutuante IEEE e é usado apenas para indicar valores de ponto flutuante ausentes.

Para valores ausentes além de flutuantes, o pandas usa o objeto Python `Nenhum`. Embora possa parecer confuso encontrar dois tipos diferentes de valores que dizem essencialmente a mesma coisa, existem razões programáticas sólidas para essa escolha de design e, na prática, seguir esse caminho permite que os pandas forneçam um bom compromisso para a grande maioria dos casos. Não obstante, `Nenhum` e` NaN` trazem restrições que você precisa estar ciente sobre como eles podem ser usados.
°°°"""
# |%%--%%| <liIAVUn68U|KtcrgLLZzE>
"""°°°
### `None`: non-float missing data
Como `None` vem do Python, ele não pode ser usado em matrizes NumPy e pandas que não são do tipo de dados `'object'`. Lembre-se de que as matrizes NumPy (e as estruturas de dados nos pandas) podem conter apenas um tipo de dados. Isso é o que lhes dá um tremendo poder para dados em grande escala e trabalho computacional, mas também limita sua flexibilidade. Esses arrays precisam fazer upcast para o “menor denominador comum”, o tipo de dados que abrangerá tudo no array. Quando `None` está no array, significa que você está trabalhando com objetos Python.

Para ver isso em ação, considere o seguinte exemplo de array (observe o `dtype` para ele):
°°°"""
# |%%--%%| <KtcrgLLZzE|rmBBqDZkW9>

import numpy as np

example1 = np.array([2, None, 6, 8])
example1

# |%%--%%| <rmBBqDZkW9|CJCsb8lAca>
"""°°°
A realidade dos tipos de dados upcast traz dois efeitos colaterais. Primeiro, as operações serão realizadas no nível do código Python interpretado, em vez do código NumPy compilado. Essencialmente, isso significa que quaisquer operações envolvendo `Series` ou` DataFrames` com `None` neles serão mais lentas. Embora você provavelmente não notaria esse impacto no desempenho, para grandes conjuntos de dados ele pode se tornar um problema.

O segundo efeito colateral decorre do primeiro. Porque `None` essencialmente arrasta` Series` ou `DataFrames` de volta ao mundo do Python simples, usando agregações NumPy / pandas como` sum () `ou` min () `em matrizes que contêm um valor ``None`` geralmente produzirá um erro:
°°°"""
# |%%--%%| <CJCsb8lAca|LAl0rIGITo>

example1.sum()

# |%%--%%| <LAl0rIGITo|CiEGSvinGk>
"""°°°
### `NaN`: missing float values

Em contraste com `None`, NumPy (e, portanto, pandas) suporta `NaN` para suas operações e ufuncs vetorizadas rápidas. A má notícia é que qualquer aritmética realizada em `NaN` sempre resulta em `NaN`. Por exemplo:
°°°"""
# |%%--%%| <CiEGSvinGk|pKHiUvyydN>

np.nan + 1

# |%%--%%| <pKHiUvyydN|iOvgU3F8Pu>

np.nan * 0

# |%%--%%| <iOvgU3F8Pu|bgwKXsVYET>
"""°°°
A boa notícia: agregações executadas em arrays com `NaN` neles não apresentam erros. A má notícia: os resultados não são uniformemente úteis:
°°°"""
# |%%--%%| <bgwKXsVYET|DddWEiUvmW>

example2 = np.array([2, np.nan, 6, 8])
example2.sum(), example2.min(), example2.max()

# |%%--%%| <DddWEiUvmW|CyZOTUHYcv>
"""°°°
No processo de upcasting de tipos de dados para estabelecer homogeneidade de dados em `Series` e` DataFrames`, o pandas irá alternar voluntariamente os valores ausentes entre `None` e` NaN`. Por causa desse recurso de design, pode ser útil pensar em `None` e` NaN` como dois sabores diferentes de "nulo" em pandas. Na verdade, alguns dos métodos principais que você usará para lidar com os valores ausentes nos pandas refletem essa ideia em seus nomes:

- `isnull ()`: Gera uma máscara booleana indicando valores ausentes
- `notnull ()`: oposto de `isnull ()`
- `dropna ()`: Retorna uma versão filtrada dos dados
- `fillna ()`: retorna uma cópia dos dados com os valores ausentes preenchidos ou imputados

Esses são métodos importantes para dominar e se familiarizar com eles, portanto, vamos examiná-los com alguma profundidade.
°°°"""
# |%%--%%| <CyZOTUHYcv|4jDhYINf7e>
"""°°°
### Detectando valores nulos
Ambos `isnull ()` e `notnull ()` são seus métodos principais para detectar dados nulos. Ambos retornam máscaras booleanas sobre seus dados.
°°°"""
# |%%--%%| <4jDhYINf7e|RG9DyPXsO9>

example3 = pd.Series([0, np.nan, "", None])

# |%%--%%| <RG9DyPXsO9|Mnl1vC7Uer>

example3.isnull()

# |%%--%%| <Mnl1vC7Uer|NaoVFHrqK4>
"""°°°
Observe atentamente a saída. Alguma coisa disso te surpreende? Embora `0` seja um nulo aritmético, é um número inteiro perfeitamente bom e o pandas o considera como tal. `''` é um pouco mais sutil. Embora o tenhamos usado na Seção 1 para representar um valor de string vazio, ele é, no entanto, um objeto de string e não uma representação de nulo no que diz respeito aos pandas.

Agora, vamos virar isso e usar esses métodos de uma maneira mais parecida com a que você vai usar na prática. Você pode usar máscaras booleanas diretamente como um índice `` Series`` ou `` DataFrame``, que pode ser útil ao tentar trabalhar com valores ausentes (ou presentes) isolados.
°°°"""
# |%%--%%| <NaoVFHrqK4|bJJdLFOJFo>
"""°°°
** Conclusão importante **: os métodos `isnull ()` e `notnull ()` produzem resultados semelhantes quando você os usa em `DataFrame`s: eles mostram os resultados e o índice desses resultados, o que o ajudará enormemente enquanto você luta com seus dados.
°°°"""
# |%%--%%| <bJJdLFOJFo|JaSNGCyTBO>
"""°°°
### Eliminando valores nulos

Além de identificar valores ausentes, o pandas fornece um meio conveniente de remover valores nulos de `Series` e` DataFrame`s. (Particularmente em grandes conjuntos de dados, muitas vezes é mais aconselhável simplesmente remover os valores [NA] ausentes de sua análise do que lidar com eles de outras maneiras.) Para ver isso em ação, vamos voltar ao `exemplo3`:
°°°"""
# |%%--%%| <JaSNGCyTBO|tr1mcbm7v9>

example3 = example3.dropna()
example3

# |%%--%%| <tr1mcbm7v9|8x5RqROzGO>
"""°°°
Observe que isso deve ser parecido com a saída de `example3 [example3.notnull ()]`. A diferença aqui é que, em vez de apenas indexar os valores mascarados, `dropna` removeu esses valores ausentes do` Series` `example3`.

Como os `DataFrame`s têm duas dimensões, eles oferecem mais opções para descartar dados.
°°°"""
# |%%--%%| <8x5RqROzGO|VXtvslZvJ0>

example4 = pd.DataFrame([[1, np.nan, 7], [2, 5, 8], [np.nan, 6, 9]])
example4

# |%%--%%| <VXtvslZvJ0|JuB6e7JKvm>
"""°°°
(Você notou que os pandas transformam duas das colunas em flutuadores para acomodar os `NaN`s?)

Você não pode descartar um único valor de um `DataFrame`, então você deve descartar linhas ou colunas inteiras. Dependendo do que você está fazendo, você pode querer fazer um ou outro e, portanto, o pandas oferece opções para ambos. Como na ciência de dados, as colunas geralmente representam variáveis ​​e as linhas representam observações, é mais provável que você elimine linhas de dados; a configuração padrão para `dropna ()` é descartar todas as linhas que contenham quaisquer valores nulos:
°°°"""
# |%%--%%| <JuB6e7JKvm|UlOGL7UdBW>

example4.dropna()

# |%%--%%| <UlOGL7UdBW|ko3BOJZuXQ>
"""°°°
Se necessário, você pode eliminar os valores NA das colunas. Use `axis = 1` para fazer isso:
°°°"""
# |%%--%%| <ko3BOJZuXQ|wHX70h45R8>

example4.dropna(axis="columns")

# |%%--%%| <wHX70h45R8|WJaHHiIGpZ>
"""°°°
Observe que isso pode eliminar muitos dados que você pode querer manter, principalmente em conjuntos de dados menores. E se você apenas quiser descartar linhas ou colunas que contenham vários ou até mesmo todos os valores nulos? Você especifica essas configurações em `dropna` com os parâmetros` how` e `thresh`.

Por padrão, `how = 'any'` (se você gostaria de verificar por si mesmo ou ver quais outros parâmetros o método possui, execute` example4.dropna? `Em uma célula de código). Você pode, alternativamente, especificar `how = 'all'` de modo a descartar apenas linhas ou colunas que contenham todos os valores nulos. Vamos expandir nosso exemplo `DataFrame` para ver isso em ação.
°°°"""
# |%%--%%| <WJaHHiIGpZ|ueY8inNKsz>

example4[3] = np.nan
example4

# |%%--%%| <ueY8inNKsz|bOPC5QPFEk>
"""°°°
O parâmetro `thresh` oferece um controle mais refinado: você define o número de valores * não nulos * que uma linha ou coluna precisa ter para ser mantida:
°°°"""
# |%%--%%| <bOPC5QPFEk|CCaMi8hmjO>

example4.dropna(axis="rows", thresh=3)

# |%%--%%| <CCaMi8hmjO|je2WtNGeWE>
"""°°°
Aqui, a primeira e a última linha foram eliminadas, porque contêm apenas dois valores não nulos.
°°°"""
# |%%--%%| <je2WtNGeWE|KpKz6GpDkN>
"""°°°
### Preenchendo valores nulos

Dependendo do seu conjunto de dados, às vezes pode fazer mais sentido preencher valores nulos com valores válidos em vez de descartá-los. Você poderia usar `isnull` para fazer isso no lugar, mas pode ser trabalhoso, principalmente se você tiver muitos valores a preencher. Por ser uma tarefa comum em ciência de dados, o pandas fornece `fillna`, que retorna uma cópia do` Series` ou `DataFrame` com os valores ausentes substituídos por um de sua escolha. Vamos criar outro exemplo `Series` para ver como isso funciona na prática.
°°°"""
# |%%--%%| <KpKz6GpDkN|n0xp7epkJ3>

example5 = pd.Series([1, np.nan, 2, None, 3], index=list("abcde"))
example5

# |%%--%%| <n0xp7epkJ3|vUBMJKBrIy>
"""°°°
Você pode preencher todas as entradas nulas com um único valor, como `0`:
°°°"""
# |%%--%%| <vUBMJKBrIy|UZ66UGJLNu>

example5.fillna(0)

# |%%--%%| <UZ66UGJLNu|otweatGf5i>
"""°°°
Você pode ser criativo sobre como usar `fillna`. Por exemplo, vamos olhar para `example4` novamente, mas desta vez vamos preencher os valores ausentes com a média de todos os valores no` DataFrame`:
°°°"""
# |%%--%%| <otweatGf5i|9JNjw6pLkE>

example4.fillna(example4.mean())

# |%%--%%| <9JNjw6pLkE|76ftyg2pGi>
"""°°°
&gt; ** Takeaway: ** Existem várias maneiras de lidar com valores ausentes em seus conjuntos de dados. A estratégia específica que você usa (removê-los, substituí-los ou mesmo como você os substitui) deve ser ditada pelas particularidades desses dados. Você desenvolverá um senso melhor de como lidar com os valores ausentes quanto mais você manipular e interagir com os conjuntos de dados.
°°°"""
# |%%--%%| <76ftyg2pGi|MmucKtgyCm>
"""°°°
## Removendo dados duplicados

&gt; ** Objetivo de aprendizado: ** Ao final desta subseção, você deve estar confortável em identificar e remover valores duplicados de DataFrames.

Além de dados ausentes, você frequentemente encontrará dados duplicados em conjuntos de dados do mundo real. Felizmente, o pandas oferece um meio fácil de detectar e remover entradas duplicadas.
°°°"""
# |%%--%%| <MmucKtgyCm|9KZ2Ju94g1>
"""°°°
### Identificando duplicatas: `duplicated`

Você pode localizar facilmente valores duplicados usando o método `duplicated` em pandas, que retorna uma máscara booleana indicando se uma entrada em um` DataFrame` é uma duplicata de um ealier. Vamos criar outro exemplo de `DataFrame` para ver isso em ação.
°°°"""
# |%%--%%| <9KZ2Ju94g1|0fewtWLWs1>

example6 = pd.DataFrame({"letters": ["A", "B"] * 2 + ["B"], "numbers": [1, 2, 1, 3, 3]})
example6

# |%%--%%| <0fewtWLWs1|nTKgfoX0Lz>

example6.duplicated()

# |%%--%%| <nTKgfoX0Lz|YkdAuwkgRQ>
"""°°°
### Dropping duplicates: `drop_duplicates`
`drop_duplicates` simplesmente retorna uma cópia dos dados para os quais todos os valores `duplicados` são` False`:
°°°"""
# |%%--%%| <YkdAuwkgRQ|QE4cRyngID>

example6.drop_duplicates()

# |%%--%%| <QE4cRyngID|di39mskoNF>
"""°°°
Ambos `duplicated` e` drop_duplicates` consideram todas as colunas, mas você pode especificar que eles examinem apenas um subconjunto de colunas em seu `DataFrame`:
°°°"""
# |%%--%%| <di39mskoNF|nAslUUBxn0>

example6.drop_duplicates(["letters"])

# |%%--%%| <nAslUUBxn0|QPgL5nNwyN>

# example6.drop_duplicates?

# |%%--%%| <QPgL5nNwyN|0Hp0aYA3P2>
"""°°°
&gt; ** Conclusão: ** Remover dados duplicados é uma parte essencial de quase todos os projetos de ciência de dados. Dados duplicados podem alterar os resultados de suas análises e fornecer resultados espúrios!
°°°"""
# |%%--%%| <0Hp0aYA3P2|afLF94zhjI>
"""°°°
## Combinando conjuntos de dados: merge e join

&gt; ** Objetivo de aprendizagem: ** Ao final desta subseção, você deve ter um conhecimento geral das várias maneiras de combinar `DataFrame`s.

Suas análises mais interessantes geralmente virão de dados combinados de mais de uma fonte. Por causa disso, o pandas oferece vários métodos de mesclar e unir conjuntos de dados para facilitar esse trabalho necessário:
 - ** `pandas.merge` ** conecta linhas em` DataFrame`s com base em uma ou mais chaves.
 - ** `pandas.concat` ** concatena ou“ empilha ”objetos ao longo de um eixo.
 - O método de instância ** `combine_first` ** permite que você junte os dados sobrepostos para preencher os valores ausentes em um objeto com os valores de outro.

Vamos examinar a fusão de dados primeiro, porque será mais familiar para os participantes do curso que já estão familiarizados com SQL ou outros bancos de dados relacionais.
°°°"""
# |%%--%%| <afLF94zhjI|sfgWFPcyHk>
"""°°°
### Categorias de junções (joins)

`merge` realiza vários tipos de junções: * um-para-um *, * muitos-para-um * e * muitos-para-muitos *. Você usa a mesma chamada de função básica para implementar todos eles e examinaremos todos os três (porque você precisará de todos os três como algum ponto em sua pesquisa de dados, dependendo dos dados). Começaremos com junções de um para um porque geralmente são o exemplo mais simples.
°°°"""
# |%%--%%| <sfgWFPcyHk|IFvxNvLOHE>
"""°°°
#### Joins um a um

Considere combinar dois `DataFrame`s que contêm informações diferentes sobre os mesmos funcionários em uma empresa:
°°°"""
# |%%--%%| <IFvxNvLOHE|mzyseMZdxp>

df1 = pd.DataFrame(
    {
        "employee": ["Gary", "Stu", "Mary", "Sue"],
        "group": ["Accounting", "Marketing", "Marketing", "HR"],
    }
)
df1

# |%%--%%| <mzyseMZdxp|2zUIBMaxzW>

df2 = pd.DataFrame(
    {"employee": ["Mary", "Stu", "Gary", "Sue"], "hire_date": [2008, 2012, 2017, 2018]}
)
df2

# |%%--%%| <2zUIBMaxzW|Af2is0AaEb>
"""°°°
Combine essas informações em um único `DataFrame` usando a função` merge`:
°°°"""
# |%%--%%| <Af2is0AaEb|WbrYWCxgT6>

df3 = pd.merge(df1, df2)
df3

# |%%--%%| <WbrYWCxgT6|uV0p6GDXfg>
"""°°°
O Pandas fez a junção baseado na coluna `employee` porque era a única coluna comum a` df1` e `df2`. (Observe também que os índices originais de `df1` e` df2` foram descartados por `merge`; este é geralmente o caso com mesclagens, a menos que você conduza por índice, que discutiremos mais tarde.)
°°°"""
# |%%--%%| <uV0p6GDXfg|WLaFKwxX8b>
"""°°°
#### Joins muitos para um
Uma junção de muitos para um é como uma junção de um para um, exceto que uma das duas colunas principais contém entradas duplicadas. O DataFrame resultante de tal junção preservará essas entradas duplicadas conforme apropriado:
°°°"""
# |%%--%%| <WLaFKwxX8b|9jJkYyrSyx>

df4 = pd.DataFrame(
    {
        "group": ["Accounting", "Marketing", "HR"],
        "supervisor": ["Carlos", "Giada", "Stephanie"],
    }
)
df4

# |%%--%%| <9jJkYyrSyx|dZ7iuxNuhi>

pd.merge(df3, df4)

# |%%--%%| <dZ7iuxNuhi|D5QJSBEDWI>
"""°°°
O `DataFrame` resultante tem uma coluna adicional para` supervisor`; essa coluna tem uma ocorrência extra de 'Giada' que não ocorreu em `df4` porque mais de um funcionário no` DataFrame` mesclado trabalha no grupo 'Marketing'.

Observe que não especificamos em qual coluna juntar. Quando você não especifica essas informações, `merge` usa os nomes das colunas sobrepostas como as chaves. No entanto, isso pode ser ambíguo; várias colunas podem atender a essa condição. Por esse motivo, é uma boa prática especificar explicitamente em qual chave juntar. Você pode fazer isso com o parâmetro `on`:
°°°"""
# |%%--%%| <D5QJSBEDWI|fbJBryFOeA>

pd.merge(df3, df4, on="group")

# |%%--%%| <fbJBryFOeA|SlyBNGbve8>
"""°°°
#### Muitos para muitos joins
O que acontecerá se as colunas-chave em ambos os DataFrames que você está unindo contiverem duplicatas? Isso dá a você uma junção de muitos para muitos:
°°°"""
# |%%--%%| <SlyBNGbve8|rn7xejeNoL>

df5 = pd.DataFrame(
    {
        "group": ["Accounting", "Accounting", "Marketing", "Marketing", "HR", "HR"],
        "core_skills": [
            "math",
            "spreadsheets",
            "writing",
            "communication",
            "spreadsheets",
            "organization",
        ],
    }
)
df5

# |%%--%%| <rn7xejeNoL|xEhChwOvSC>

pd.merge(df1, df5, on="group")

# |%%--%%| <xEhChwOvSC|XTyO50H2jO>
"""°°°
Novamente, para evitar ambigüidade quanto a qual coluna unir, é uma boa idéia dizer explicitamente ao `merge` qual usar com o parâmetro` on`.
°°°"""
# |%%--%%| <XTyO50H2jO|KFUiQMw5Oq>
"""°°°
#### `left_on` and `right_on` keywords
E se você precisar mesclar dois conjuntos de dados sem nomes de coluna compartilhados? Por exemplo, e se você estiver usando um conjunto de dados em que o nome do funcionário é rotulado como 'nome' em vez de 'funcionário'? Nesses casos, você precisará usar as palavras-chave `left_on` e `right_on`
 para especificar os nomes das colunas nas quais unir:
°°°"""
# |%%--%%| <KFUiQMw5Oq|yTmdirGnsE>

df6 = pd.DataFrame(
    {"name": ["Gary", "Stu", "Mary", "Sue"], "salary": [70000, 80000, 120000, 90000]}
)
df6

# |%%--%%| <yTmdirGnsE|OnL9tanlhb>

pd.merge(df1, df6, left_on="employee", right_on="name")

# |%%--%%| <OnL9tanlhb|iMowluI3Qd>
"""°°°
### Concatenação em NumPy
A concatenação em pandas é construída a partir da funcionalidade de concatenação para matrizes NumPy. Esta é a aparência da concatenação NumPy:
 - Para matrizes unidimensionais:
°°°"""
# |%%--%%| <iMowluI3Qd|jD8Ge3t4vo>

x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
np.concatenate([x, y, z])

# |%%--%%| <jD8Ge3t4vo|72m6QwIm89>
"""°°°
 - Para matrizes bidimensionais:
°°°"""
# |%%--%%| <72m6QwIm89|uodA1Eigaz>

x = [[1, 2], [3, 4]]
np.concatenate([x, x], axis=1)

# |%%--%%| <uodA1Eigaz|vj2pF66QDE>
"""°°°
Observe que o parâmetro `axis = 1` faz com que a concatenação ocorra ao longo de colunas ao invés de linhas. A concatenação em pandas é semelhante a esta.
°°°"""
# |%%--%%| <vj2pF66QDE|EXPi8upGKM>
"""°°°
### Concatenação em pandas

Pandas tem uma função, `pd.concat ()` que pode ser usada para uma concatenação simples de objetos `Series` ou` DataFrame` de maneira semelhante a `np.concatenate ()` com ndarrays.
°°°"""
# |%%--%%| <EXPi8upGKM|AtdzMHYVUx>

ser1 = pd.Series(["a", "b", "c"], index=[1, 2, 3])
ser2 = pd.Series(["d", "e", "f"], index=[4, 5, 6])
pd.concat([ser1, ser2])

# |%%--%%| <AtdzMHYVUx|djn9tVfhaD>
"""°°°
Ele também concatena objetos de dimensões superiores, como `` DataFrame``s:
°°°"""
# |%%--%%| <djn9tVfhaD|HyvsLU6clV>

df9 = pd.DataFrame({"A": ["a", "c"], "B": ["b", "d"]})
df9

# |%%--%%| <HyvsLU6clV|zwsYa2A5AB>

pd.concat([df9, df9])

# |%%--%%| <zwsYa2A5AB|NnaEGFuvCG>
"""°°°
Observe que `pd.concat` preservou a indexação, embora isso signifique que ela foi duplicada. Você pode ter os resultados reindexados (e evitar possíveis confusões no caminho) assim:
°°°"""
# |%%--%%| <NnaEGFuvCG|s00xkAGHGI>

pd.concat([df9, df9], ignore_index=True)

# |%%--%%| <s00xkAGHGI|9cWWrpc1rQ>
"""°°°
Por padrão, `pd.concat` concatena a linha dentro do` DataFrame` (ou seja, `axis = 0` por padrão). Você pode especificar o eixo ao longo do qual concatenar:
°°°"""
# |%%--%%| <9cWWrpc1rQ|Qj1C9W15oO>

pd.concat([df9, df9], axis=1)

# |%%--%%| <Qj1C9W15oO|ILtPVGYHa9>
"""°°°
### Concatenação com junções
Assim como fez com a mesclagem acima, você pode usar junções internas e externas ao concatenar DataFrames com diferentes conjuntos de nomes de coluna.
°°°"""
# |%%--%%| <ILtPVGYHa9|DOGAK5dtkS>

df10 = pd.DataFrame({"A": ["a", "d"], "B": ["b", "e"], "C": ["c", "f"]})
df10

# |%%--%%| <DOGAK5dtkS|wPDc4LT0CY>

df11 = pd.DataFrame({"B": ["u", "x"], "C": ["v", "y"], "D": ["w", "z"]})
df11

# |%%--%%| <wPDc4LT0CY|38jEMTBGDq>

pd.concat([df10, df11])

# |%%--%%| <38jEMTBGDq|fpGiduHsJz>
"""°°°
Como vimos anteriormente, a junção padrão para isso é uma junção externa e as entradas para as quais nenhum dado está disponível são preenchidas com valores `NaN`. Você também pode fazer uma junção interna:
°°°"""
# |%%--%%| <fpGiduHsJz|USRa9PzIRp>

pd.concat([df10, df11], join="inner")

# |%%--%%| <USRa9PzIRp|k4jwivYK8u>
"""°°°
Outra opção é especificar diretamente o índice das colunas restantes usando o argumento `join_axes`, que obtém uma lista de objetos de índice. Aqui, especificaremos que as colunas retornadas devem ser as mesmas da primeira entrada (`df10`):
°°°"""
# |%%--%%| <k4jwivYK8u|vauB0jawD1>

pd.concat([df10, df11], join_axes=[df10.columns])

# |%%--%%| <vauB0jawD1|MVLF6S1TQ9>
"""°°°
#### `append()`

Como a concatenação direta de array é tão comum, os objetos `` Series`` e `` DataFrame`` têm um método `` append`` que pode realizar a mesma coisa em menos teclas. Por exemplo, em vez de chamar `` pd.concat ([df9, df9]) ``, você pode simplesmente chamar `` df9.append (df9) ``:
°°°"""
# |%%--%%| <MVLF6S1TQ9|0C7YHaT9it>

df9.append(df9)

# |%%--%%| <0C7YHaT9it|wMAFOB3vhz>
"""°°°
** Ponto importante **: Ao contrário dos métodos `append ()` e `extend ()` das listas Python, o método `append ()` no pandas não modifica o objeto original. Em vez disso, ele cria um novo objeto com os dados combinados.

&gt; ** Conclusão: ** uma grande parte do valor que você pode fornecer como cientista de dados vem da conexão de vários conjuntos de dados, muitas vezes díspares, para encontrar novos insights. Aprender como juntar e mesclar dados é, portanto, uma parte essencial do seu conjunto de habilidades.
°°°"""
# |%%--%%| <wMAFOB3vhz|YOxy0bQYD8>
"""°°°
## Estatísticas exploratórias e visualização

&gt; ** Objetivo de aprendizagem: ** Ao final desta subseção, você deve estar familiarizado com algumas das maneiras de explorar visualmente os dados armazenados em `DataFrame`s.

Freqüentemente, ao investigar um novo conjunto de dados, é inestimável obter informações de alto nível sobre o que o conjunto de dados contém. Anteriormente nesta seção, discutimos o uso de métodos como `DataFrame.info`,` DataFrame.head` e `DataFrame.tail` para examinar alguns aspectos de um` DataFrame`. Embora esses métodos sejam essenciais, eles são, por si próprios, muitas vezes insuficientes para obter informações suficientes para saber como abordar um novo conjunto de dados. É aqui que entram as estatísticas exploratórias e as visualizações dos conjuntos de dados.

Para ver o que queremos dizer em termos de obtenção de insights exploratórios (visual e numericamente), vamos nos aprofundar em um dos conjuntos de dados que vêm com a biblioteca scikit-learn, o Boston Housing Dataset:
°°°"""
# |%%--%%| <YOxy0bQYD8|1cp1XddAdx>

from sklearn.datasets import load_boston

boston_dataset = load_boston()
df = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
df["MEDV"] = boston_dataset.target

# |%%--%%| <1cp1XddAdx|9c8DsxICMU>

df.head()

# |%%--%%| <9c8DsxICMU|VlQFKyFkxd>
"""°°°
Este conjunto de dados contém informações coletadas do U.S Census Bureau sobre habitação na área de Boston, Massachusetts e foi publicado pela primeira vez em 1978. O conjunto de dados tem 14 colunas:
 - **CRIM**: Taxa de criminalidade per capita por cidade
 - **ZN**: Proporção de terrenos residenciais zoneados para lotes com mais de 25.000 pés quadrados
 - **INDUS**: Proporção de acres de negócios não varejistas por cidade
 - **CHAS**: variável dummy Charles River (= 1 se o trato limita o rio; 0 caso contrário)
 - **NOX**: concentração de óxidos nítricos (partes por 10 milhões)
 - **RM**: Número médio de quartos por habitação
 - **AGE**: Proporção de unidades ocupadas pelo proprietário construídas antes de 1940
 - **DIS**: distâncias ponderadas até cinco centros de empregos de Boston
 - **RAD**: Índice de acessibilidade às rodovias radiais
 - **TAX**: Taxa de imposto de propriedade de valor total por $ 10.000
 - **PTRATIO**: Proporção aluno-professor por cidade
 - **LSTAT**: Porcentagem da porção de status inferior da população
 - **MEDV**: valor médio das casas ocupadas pelo proprietário em $ 1.000
°°°"""
# |%%--%%| <VlQFKyFkxd|w6UYG11I5N>
"""°°°
Um dos primeiros métodos que podemos usar para entender melhor este conjunto de dados é `DataFrame.shape`:
°°°"""
# |%%--%%| <w6UYG11I5N|gBkFjntnN8>

df.shape

# |%%--%%| <gBkFjntnN8|ahcI9lUbuw>
"""°°°
O conjunto de dados possui 506 linhas e 13 colunas.

Para ter uma ideia melhor do conteúdo de cada coluna, podemos usar `DataFrame.describe`, que retorna o valor máximo, valor mínimo, média e desvio padrão dos valores numéricos em cada coluna, além dos quartis de cada coluna:
°°°"""
# |%%--%%| <ahcI9lUbuw|N24Z6idXz2>

df.describe()

# |%%--%%| <N24Z6idXz2|NMrsNjrV2w>
"""°°°
Como o conjunto de dados pode ter muitas colunas, muitas vezes pode ser útil transpor os resultados de `DataFrame.describe` para melhor usá-los:
°°°"""
# |%%--%%| <NMrsNjrV2w|GN6dt4GzE6>

df.describe().transpose()

# |%%--%%| <GN6dt4GzE6|86iewPkwym>
"""°°°
Observe que você também pode examinar estatísticas descritivas específicas para colunas sem ter que invocar `DataFrame.describe`:
°°°"""
# |%%--%%| <86iewPkwym|N34igk9bpA>

df["MEDV"].mean()

# |%%--%%| <N34igk9bpA|6fltUBVcAY>

df["MEDV"].max()

# |%%--%%| <6fltUBVcAY|vhQq1A3h5i>

df["AGE"].median()

# |%%--%%| <vhQq1A3h5i|QnkXshMnez>
"""°°°
### Exercicio 1:
°°°"""
# |%%--%%| <QnkXshMnez|2ynroILVGc>

# Encontre o valor máximo em df['AGE'].
df["AGE"].max()

# |%%--%%| <2ynroILVGc|77hsizO00T>
"""°°°
Outra informação que você frequentemente desejará ver é a relação entre as diferentes colunas. Você faz isso com o método `DataFrame.groupby`. Por exemplo, você pode examinar a MEDV média (valor médio das casas ocupadas pelo proprietário) para cada valor de AGE (proporção de unidades ocupadas pelo proprietário construídas antes de 1940):
°°°"""
# |%%--%%| <77hsizO00T|OPtoc39xlw>

df.groupby(["AGE"])["MEDV"].mean()

# |%%--%%| <OPtoc39xlw|4cKGwbKxHL>
"""°°°
### Exercício 2:
°°°"""
# |%%--%%| <4cKGwbKxHL|MQU60W4dgR>

# Agora tente encontrar o valor mediano de AGE para cada valor de MEDV.
df.groupby(["MEDV"])["AGE"].median()

# |%%--%%| <MQU60W4dgR|yMMrT0zmdQ>
"""°°°
Você também pode aplicar uma função lambda a cada elemento de uma coluna `DataFrame` usando o método `apply`. Por exemplo, digamos que você queira criar uma nova coluna que sinalize uma linha se mais de 50 por cento das casas ocupadas pelo proprietário forem construídas antes de 1940:
°°°"""
# |%%--%%| <yMMrT0zmdQ|lGXsZTMQZv>

df["AGE_50"] = df["AGE"].apply(lambda x: x > 50)

# |%%--%%| <lGXsZTMQZv|hfmEZZbMES>
"""°°°
Depois de aplicado, você também verá quantos valores retornaram verdadeiros e quantos falsos usando o método `value_counts`:
°°°"""
# |%%--%%| <hfmEZZbMES|k20kjJ13xQ>

df["AGE_50"].value_counts()

# |%%--%%| <k20kjJ13xQ|u1JZ7oNnxk>
"""°°°
Você também pode examinar os números da instrução groupby que criou anteriormente:
°°°"""
# |%%--%%| <u1JZ7oNnxk|CTSqOH9v57>

df.groupby(["AGE_50"])["MEDV"].mean()

# |%%--%%| <CTSqOH9v57|uAkjCluipp>
"""°°°
Você também pode agrupar por mais de uma variável, como AGE_50 (aquela que você acabou de criar), CHAS (se uma cidade está no rio Charles) e RAD (um índice que mede o acesso às rodovias radiais da área de Boston) e, em seguida, avalie cada grupo para o preço médio médio de uma casa nesse grupo:
°°°"""
# |%%--%%| <uAkjCluipp|zSEo0Omvhz>

groupby_twovar = df.groupby(["AGE_50", "RAD", "CHAS"])["MEDV"].mean()

# |%%--%%| <zSEo0Omvhz|VFzEhlPe22>

groupby_twovar

# |%%--%%| <VFzEhlPe22|HjEeqGQKbD>
"""°°°
Vamos analisar esses resultados com um pouco mais de profundidade. A primeira linha relata que as comunidades com menos da metade das casas construídas antes de 1940, com um índice de acesso à rodovia de 1, e que não estão situadas no rio Charles, têm um preço médio de casa de $ 24.667 (dólares dos anos 1970); a próxima linha mostra que para comunidades semelhantes à primeira linha, exceto por estarem localizadas no Charles River, o preço médio da casa é de $ 50.000.

Um insight que surge ao continuar a descer é que, se todo o resto for igual, estar localizado próximo ao rio Charles pode aumentar significativamente o valor do estoque de habitações mais recentes. A história é mais ambígua para comunidades dominadas por casas antigas: a proximidade com o Charles aumenta significativamente os preços das casas em uma comunidade (e presumivelmente mais longe da cidade); para todos os outros, estar situado às margens do rio proporcionou um aumento modesto no valor ou, na verdade, diminuiu os preços médios das residências.

Embora agrupamentos como este possam ser uma ótima maneira de começar a interrogar seus dados, você pode não se importar com o formato 'alto' que eles vêm. Nesse caso, você pode desempilhar os dados em um formato "amplo":
°°°"""
# |%%--%%| <HjEeqGQKbD|WC2VjG4wNu>

groupby_twovar.unstack()

# |%%--%%| <WC2VjG4wNu|17o8LAxG0Y>
"""°°°
### Exercício 3:
°°°"""
# |%%--%%| <17o8LAxG0Y|60mqD5SXeb>

# Como você poderia usar groupby para ter uma noção da proporção:
# do Nº de terrenos residenciais zoneados para lotes com mais de 25.000 pés quadrados,
df.groupby(["ZN"])["DIS"].mean()
# da proporção de acres de negócios não varejistas por cidade,
df.groupby(["INDUS"])["DIS"].mean()
# e, em seguida, avalie cada grupo para a distância das cidades dos centros de emprego em Boston?#

# |%%--%%| <60mqD5SXeb|n7RK42YFCe>
"""°°°
Também é frequentemente valioso saber quantos valores únicos uma coluna contém com o método `nunique`:
°°°"""
# |%%--%%| <n7RK42YFCe|5xKsiHO5y2>

df["CHAS"].nunique()

# |%%--%%| <5xKsiHO5y2|VdmBqqB2Bb>
"""°°°
Complementarmente, você provavelmente também desejará saber quais são esses valores exclusivos, que é onde o método `unique` ajuda:
°°°"""
# |%%--%%| <VdmBqqB2Bb|bqIuNTcajx>

df["CHAS"].unique()

# |%%--%%| <bqIuNTcajx|wRfR3jDg1S>
"""°°°
Você pode usar o método `value_counts` para ver quantos de cada valor único existem em uma coluna:
°°°"""
# |%%--%%| <wRfR3jDg1S|RIMB2kfTcd>

df["CHAS"].value_counts()

# |%%--%%| <RIMB2kfTcd|d47r3BIS86>
"""°°°
Ou você pode facilmente traçar um gráfico de barras para ver visualmente a divisão:
°°°"""
# |%%--%%| <d47r3BIS86|Vg6j3Asx8J>

import matplotlib.pyplot as plt

df["CHAS"].value_counts().plot(kind="bar")
plt.show()

# |%%--%%| <Vg6j3Asx8J|Oi94DLOOf1>
"""°°°
Observe que o comando mágico do IPython `% matplotlib inline` permite que você visualize o gráfico inline.

Vamos voltar ao conjunto de dados como um todo por um momento. Duas coisas importantes que você procurará em quase qualquer conjunto de dados são tendências e relacionamentos. Uma relação típica entre as variáveis ​​a explorar é a correlação de Pearson, ou a extensão na qual duas variáveis ​​estão linearmente relacionadas. O método `corr` mostrará isso em formato de tabela para todas as colunas em um` DataFrame`:
°°°"""
# |%%--%%| <Oi94DLOOf1|wE84fOcZ4E>

df.corr(method="pearson")

# |%%--%%| <wE84fOcZ4E|9wf5bCdfP7>
"""°°°
Suponha que você queira apenas examinar as correlações entre todas as colunas e apenas uma variável. Vamos examinar apenas a correlação entre todas as outras variáveis ​​e a porcentagem de casas ocupadas pelos proprietários construídas antes de 1940 (AGE). Faremos isso acessando a coluna por número de índice:
°°°"""
# |%%--%%| <9wf5bCdfP7|Q2AxIWubBH>

corr = df.corr(method="pearson")
corr_with_homevalue = corr.iloc[-1]
corr_with_homevalue[corr_with_homevalue.argsort()[::-1]]

# |%%--%%| <Q2AxIWubBH|i7oZbQhuRb>
"""°°°
Com as correlações organizadas em ordem decrescente, é fácil começar a ver alguns padrões. Correlacionar AGE com uma variável que criamos a partir de AGE é uma correlação trivial. No entanto, é interessante notar que a porcentagem do estoque de moradias mais antigas nas comunidades está fortemente correlacionada com a poluição do ar (NOX) e a proporção de acres de negócios não varejistas por cidade (INDUS); pelo menos em 1978 na área metropolitana de Boston, as cidades mais antigas são mais industriais.

Graficamente, podemos ver as correlações usando um mapa de calor da biblioteca Seaborn:
°°°"""
# |%%--%%| <i7oZbQhuRb|Yk6kTbO4cn>

import seaborn as sns

sns.heatmap(df.corr(), cmap=sns.cubehelix_palette(20, light=0.95, dark=0.15))

# |%%--%%| <Yk6kTbO4cn|IM5eekjLYl>
"""°°°
Os histogramas são outra ferramenta valiosa para investigar seus dados. Por exemplo, qual é a distribuição geral dos preços das casas ocupadas pelos proprietários na área de Boston?
°°°"""
# |%%--%%| <IM5eekjLYl|3zejViVZQY>

plt.hist(df["MEDV"])

# |%%--%%| <3zejViVZQY|sMRBq28Fga>
"""°°°
O tamanho do compartimento padrão para o histograma matplotlib (essencialmente grande de grupos de porcentagens que você inclui em cada barra de histograma, neste caso) é muito grande e pode mascarar detalhes menores. Para obter uma visão mais detalhada da coluna AGE, você pode aumentar manualmente o número de compartimentos no histograma:
°°°"""
# |%%--%%| <sMRBq28Fga|2BY73p5OAw>

plt.hist(df["MEDV"], bins=50)

# |%%--%%| <2BY73p5OAw|Pg9z1zm2gf>
"""°°°
Seaborn tem uma versão um pouco mais atraente do histograma matplotlib padrão: o gráfico de distribuição. Este é um gráfico de combinação de histograma e estimativa de densidade do kernel (KDE) (essencialmente um histograma suavizado):
°°°"""
# |%%--%%| <Pg9z1zm2gf|00FHmdam9c>

sns.distplot(df["MEDV"])

# |%%--%%| <00FHmdam9c|gakd9eWZ2u>
"""°°°
Outro gráfico comumente usado é o Seaborn jointplot, que combina histogramas para duas colunas junto com um gráfico de dispersão:
°°°"""
# |%%--%%| <gakd9eWZ2u|PbC279KG2M>

sns.jointplot(x=df["RM"], y=df["MEDV"], kind="scatter")

# |%%--%%| <PbC279KG2M|3YPBvGqKVa>
"""°°°
Infelizmente, muitos dos pontos são impressos uns sobre os outros. Você pode ajudar a resolver isso adicionando alguma mistura alfa, uma figura que define a transparência para os pontos de forma que as concentrações deles se sobrepondo sejam aparentes:
°°°"""
# |%%--%%| <3YPBvGqKVa|IK1cAlZKRl>

sns.jointplot(x=df["RM"], y=df["MEDV"], kind="scatter", alpha=0.3)

# |%%--%%| <IK1cAlZKRl|K47KXpH6Tu>
"""°°°
Outra maneira de ver os padrões em seus dados é com um gráfico bidimensional do KDE. As cores mais escuras aqui representam uma maior concentração de pontos de dados:
°°°"""
# |%%--%%| <K47KXpH6Tu|D24I0FF29c>

sns.kdeplot(x=df["RM"], y=df["MEDV"], shade=True)

# |%%--%%| <D24I0FF29c|kKbCSUZI1P>
"""°°°
Observe que, embora o gráfico do KDE seja muito bom em mostrar concentrações de pontos de dados, estruturas mais refinadas, como relações lineares (como a relação clara entre o número de quartos nas casas e o preço da casa), são perdidas no gráfico do KDE.

Finalmente, o gráfico de pares no Seaborn permite que você veja gráficos de dispersão e histogramas para várias colunas em uma tabela. Aqui, brincamos com algumas das palavras-chave para produzir um gráfico de par mais sofisticado e fácil de ler que incorpora tanto a combinação alfa quanto as linhas de regressão linear para os gráficos de dispersão.
°°°"""
# |%%--%%| <kKbCSUZI1P|WKhnAviKbN>

sns.pairplot(
    df[["RM", "AGE", "LSTAT", "DIS", "MEDV"]],
    kind="reg",
    plot_kws={"line_kws": {"color": "red"}, "scatter_kws": {"alpha": 0.1}},
)

# |%%--%%| <WKhnAviKbN|IN6CwjsXA3>
"""°°°
A visualização é o início da parte realmente legal e divertida da ciência de dados. Portanto, experimente essas ferramentas de visualização e veja o que você pode aprender com os dados!
°°°"""
# |%%--%%| <IN6CwjsXA3|JHdrsUQd66>
"""°°°
&gt; **Conclusão:** Uma velha piada diz: “O que um cientista de dados vê quando olha para um conjunto de dados? Um monte de números. ” Há mais do que um pouco de verdade nessa piada. A visualização geralmente é a chave para encontrar padrões e correlações em seus dados. Embora a visualização muitas vezes não possa fornecer resultados precisos, ela pode indicar a direção certa para fazer perguntas melhores e encontrar valor nos dados de maneira eficiente.
°°°"""
