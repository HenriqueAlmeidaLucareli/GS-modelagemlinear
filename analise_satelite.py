# Nome do Aluno e RM da CCPQ
# Luca Almeida Lucareli 569061 
# Henrique Almeida Lucareli 569183 
# Enzo Seiji Delgado Tabuchi 573156  

import pandas as pd
import matplotlib.pyplot as plt

# =============================================================================
# EXERCÍCIO 01 - CARREGAMENTO DA BASE DE DADOS
# =============================================================================
df = pd.read_csv('./satellites.csv', sep=';')
df = df.loc[:, ~df.columns.str.contains("^Unnamed")] # Remove colunas com valores totalmente vazios

print("Visualização inicial dos dados:")
print(df.head())

# =============================================================================
# EXERCÍCIO 02A - VARIÁVEL QUANTITATIVA DISCRETA
# Variável escolhida: Expected Lifetime (yrs.)
# =============================================================================

# Converter para numérico
df["Expected Lifetime (yrs.)"] = pd.to_numeric(
    df["Expected Lifetime (yrs.)"],
    errors="coerce"
)

dados_discreta = df["Expected Lifetime (yrs.)"].dropna()

# Cálculos de Frequência
freq_abs_disc = dados_discreta.value_counts().sort_index()
freq_rel_disc = (freq_abs_disc / len(dados_discreta)) * 100
freq_acum_disc = freq_abs_disc.cumsum()
freq_rel_acum_disc = freq_rel_disc.cumsum()

tabela_discreta = pd.DataFrame({
    "Expected Lifetime (Anos)": freq_abs_disc.index,
    "Frequência (fi)": freq_abs_disc.values,
    "Freq. Relativa (%)": freq_rel_disc.values.round(2),
    "Freq. Acumulada": freq_acum_disc.values,
    "Freq. Rel. Acum. (%)": freq_rel_acum_disc.values.round(2)
})

print("\n--- TABELA DE FREQUÊNCIAS: VARIÁVEL DISCRETA ---")
print(tabela_discreta)


# =============================================================================
# EXERCÍCIO 02B - VARIÁVEL QUANTITATIVA CONTÍNUA
# Variável escolhida: Perigee (km)
# =============================================================================

# Converter para numérico
df["Perigee (km)"] = pd.to_numeric(
    df["Perigee (km)"],
    errors="coerce"
)

dados_continua = df["Perigee (km)"].dropna()

# Criando as classes (10 bins)
classes = pd.cut(
    dados_continua,
    bins=10
)

# Cálculos de Frequência
freq_abs_cont = classes.value_counts().sort_index()
freq_rel_cont = (freq_abs_cont / len(dados_continua)) * 100
freq_acum_cont = freq_abs_cont.cumsum()
freq_rel_acum_cont = freq_rel_cont.cumsum()

tabela_continua = pd.DataFrame({
    "Classe": freq_abs_cont.index.astype(str),
    "Frequência (fi)": freq_abs_cont.values,
    "Freq. Relativa (%)": freq_rel_cont.values.round(2),
    "Freq. Acumulada": freq_acum_cont.values,
    "Freq. Rel. Acum. (%)": freq_rel_acum_cont.values.round(2)
})

print("\n--- TABELA DE FREQUÊNCIAS: VARIÁVEL CONTÍNUA ---")
print(tabela_continua)


# =============================================================================
# EXERCÍCIO 03 - DOIS GRÁFICOS DISTINTOS
# =============================================================================

# Gráfico 1 — Histograma
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

# Gráfico 2 — Barras
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


# =============================================================================
# EXERCÍCIO 04 — ESTATÍSTICA DESCRITIVA
# =============================================================================

def estatistica_descritiva(dataframe, coluna):
    # Isolando e limpando os dados da coluna específica
    dados_estatistica = pd.to_numeric(dataframe[coluna], errors="coerce").dropna()

    media = dados_estatistica.mean()
    mediana = dados_estatistica.median()
    moda = dados_estatistica.mode().iloc[0]

    maximo = dados_estatistica.max()
    minimo = dados_estatistica.min()
    amplitude = maximo - minimo

    variancia = dados_estatistica.var()
    desvio_padrao = dados_estatistica.std()
    coef_variacao = (desvio_padrao / media) * 100

    q1 = dados_estatistica.quantile(0.25)
    q2 = dados_estatistica.quantile(0.50)
    q3 = dados_estatistica.quantile(0.75)

    print(f"\n=--- ESTATÍSTICA DESCRITIVA: {coluna} ----")
    print(f"Média: {media:.2f}")
    print(f"Mediana (Q2): {mediana:.2f}")
    print(f"Moda: {moda:.2f}")
    print(f"Valor Máximo: {maximo:.2f}")
    print(f"Valor Mínimo: {minimo:.2f}")
    print(f"Amplitude Total: {amplitude:.2f}")
    print(f"Variância Amostral: {variancia:.2f}")
    print(f"Desvio Padrão: {desvio_padrao:.2f}")
    print(f"Coeficiente de Variação (CV): {coef_variacao:.2f}%")
    print(f"Primeiro Quartil (Q1): {q1:.2f}")
    print(f"Terceiro Quartil (Q3): {q3:.2f}")


# Executando a função para as variáveis
estatistica_descritiva(df, "Expected Lifetime (yrs.)")
estatistica_descritiva(df, "Apogee (km)")