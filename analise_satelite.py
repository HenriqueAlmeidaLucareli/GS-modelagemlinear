# Nome do Aluno e RM da CCPQ
# Luca Almeida Lucareli 569061 
# Henrique Almeida Lucareli 569183 
# Enzo Seiji Delgado Tabuchi 573156  

import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('./satellites.csv', sep=';')
df = df.loc[:, ~df.columns.str.contains("^Unnamed")] #Remove colunas com valores totalmente vazios

print(df.head())

"""Exercício 02A - Variável Quantitativa Discreta

Uma boa escolha é:

Expected Lifetime (yrs.)

Ela é quantitativa discreta porque normalmente assume valores inteiros (5, 10, 15 anos etc.).
"""

# Converter para numérico
df["Expected Lifetime (yrs.)"] = pd.to_numeric(
    df["Expected Lifetime (yrs.)"],
    errors="coerce"
)

dados = df["Expected Lifetime (yrs.)"].dropna()

freq_abs = classes.value_counts().sort_index()

freq_rel = (freq_abs / len(dados)) * 100

freq_acum = freq_abs.cumsum()

freq_rel_acum = freq_rel.cumsum()

tabela_discreta = pd.DataFrame({
    "Massa de Lançamento (kg)": freq_abs.index,
    "Frequência (fi)": freq_abs.values,
    "Freq. Relativa (%)": freq_rel.values.round(2),
    "Freq. Acumulada": freq_acum.values,
    "Freq. Rel. Acum. (%)": freq_rel_acum.values.round(2)
})

print(tabela_discreta)

"""Exercício 02B - Variável Quantitativa Contínua

A melhor variável da base é:

Perigee (km)

Ela é contínua e tem muitos valores diferentes.
"""

df["Perigee (km)"] = pd.to_numeric(
    df["Perigee (km)"],
    errors="coerce"
)

dados = df["Perigee (km)"].dropna()

classes = pd.cut(
    dados,
    bins=10
)

freq_abs = classes.value_counts().sort_index()

freq_rel = (freq_abs / len(dados)) * 100

freq_acum = freq_abs.cumsum()

freq_rel_acum = freq_rel.cumsum()

tabela_continua = pd.DataFrame({
    "Classe": freq_abs.index.astype(str),
    "Frequência (fi)": freq_abs.values,
    "Freq. Relativa (%)": freq_rel.values.round(2),
    "Freq. Acumulada": freq_acum.values,
    "Freq. Rel. Acum. (%)": freq_rel_acum.values.round(2)
})

print(tabela_continua)

"""Gráfico 1 — Histograma

Variável: Perigee (km)

Objetivo:

Mostrar em quais altitudes os satélites estão concentrados.
Identificar se a maioria está em órbitas baixas (LEO).


Interpretação

Observa-se uma concentração significativa de satélites em baixas altitudes orbitais, indicando predominância de missões em órbita terrestre baixa (LEO), amplamente utilizadas para comunicação, observação terrestre e internet via satélite.
"""

plt.figure(figsize=(10,6))

plt.hist(
    df["Perigee (km)"].dropna(),
    bins=20,
    color='skyblue',
    edgecolor='black'
)

plt.title('Distribuição do Perigeu dos Satélites')
plt.xlabel('Perigee (km)')
plt.ylabel('Quantidade de Satélites')

plt.grid(True)

plt.show()

"""Gráfico 2 — Barras

Country of Operator/Owner

Objetivo:

Mostrar os principais tipos de missão.

Interpretação

Os resultados mostram forte concentração de satélites em poucos países, evidenciando a liderança tecnológica e econômica de determinadas nações na indústria espacial.
"""

plt.figure(figsize=(12,6))

df["Country of Operator/Owner"].value_counts().head(10).plot(
    kind='bar',
    color='green',
    edgecolor='black'
)

plt.title('Top 10 Países Operadores de Satélites')
plt.xlabel('País')
plt.ylabel('Quantidade de Satélites')

plt.xticks(rotation=45)

plt.show()

"""
Exercício 04 — Estatística Descritiva

Uma boa variável para analisar é:

Power (Watts)

ou

Expected Lifetime (Years)

Calcular:

Tendência Central
Média
Mediana
Moda
Dispersão
Máximo
Mínimo
Amplitude

Amplitude=Valor M
a
ˊ
ximo−Valor M
ı
ˊ
nimo

Variância
Desvio padrão

CV=
M
e
ˊ
dia
Desvio Padr
a
~
o
	​

×100

Coeficiente de variação
Separatrizes
Q1
Q2 (mediana)
Q3
"""
def estatistica_descritiva(df, coluna):

    dados = pd.to_numeric(df[coluna], errors="coerce").dropna()

    media = dados.mean()
    mediana = dados.median()
    moda = dados.mode().iloc[0]

    maximo = dados.max()
    minimo = dados.min()

    amplitude = maximo - minimo

    variancia = dados.var()
    desvio_padrao = dados.std()

    coef_variacao = (desvio_padrao / media) * 100

    q1 = dados.quantile(0.25)
    q2 = dados.quantile(0.50)
    q3 = dados.quantile(0.75)

    print(f"\nESTATÍSTICA DESCRITIVA - {coluna}")

    print(f"Média: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Moda: {moda:.2f}")

    print(f"Máximo: {maximo:.2f}")
    print(f"Mínimo: {minimo:.2f}")

    print(f"Amplitude: {amplitude:.2f}")

    print(f"Variância: {variancia:.2f}")
    print(f"Desvio Padrão: {desvio_padrao:.2f}")

    print(f"Coeficiente de Variação: {coef_variacao:.2f}%")

    print(f"Q1: {q1:.2f}")
    print(f"Q2: {q2:.2f}")
    print(f"Q3: {q3:.2f}")


estatistica_descritiva(df, "Expected Lifetime (yrs.)")
estatistica_descritiva(df, "Apogee (km)")