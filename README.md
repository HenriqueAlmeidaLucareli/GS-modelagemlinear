# Análise Estatística de Dados de Satélites

Este repositório contém um script em Python desenvolvido para realizar a leitura, o tratamento e a análise estatística descritiva de uma base de dados sobre satélites. O projeto foi elaborado como parte das atividades da disciplina/curso (CCPQ).

## Equipe

- **Luca Almeida Lucareli** — RM: 569061
- **Henrique Almeida Lucareli** — RM: 569183
- **Enzo Seiji Delgado Tabuchi** — RM: 573156

## Tecnologias e Dependências

Para que o código funcione corretamente, certifique-se de ter o **Python 3.x** instalado em sua máquina, juntamente com as seguintes bibliotecas:

- **Pandas**
  ```bash
  pip install pandas
  ```

- **Matplotlib**
  ```bash
  pip install matplotlib
  ```

## Estrutura das Atividades

O script está dividido em quatro partes principais, correspondendo aos exercícios propostos.

### Exercício 01: Carregamento da Base de Dados

- Leitura do arquivo `satellites.csv` utilizando o Pandas.
- Limpeza inicial dos dados através da remoção de colunas vazias sem nome (`Unnamed`).

### Exercício 02: Tabelas de Frequências

#### Variável Quantitativa Discreta

Análise da variável **Expected Lifetime (yrs.)** (Tempo de vida esperado em anos).

O script calcula e exibe:

- Frequência absoluta
- Frequência relativa (%)
- Frequência acumulada
- Frequência relativa acumulada (%)

#### Variável Quantitativa Contínua

Análise da variável **Perigee (km)** (Perigeu em quilômetros).

Os dados são agrupados em **10 classes (bins)** para a geração da tabela completa de frequências.

### Exercício 03: Visualização de Dados

#### Gráfico 1 — Histograma

Ilustra a distribuição do **Perigee (km)** dos satélites, permitindo visualizar a concentração e a dispersão dos dados.

#### Gráfico 2 — Gráfico de Barras

Destaca o **Top 10** de países proprietários ou operadores com a maior quantidade de satélites em órbita.

### Exercício 04: Estatística Descritiva

Criação de uma função reutilizável para extrair e exibir métricas estatísticas essenciais de qualquer coluna numérica.

#### Métricas Calculadas

- Média
- Mediana (Q2)
- Moda
- Valor máximo
- Valor mínimo
- Amplitude total
- Variância amostral
- Desvio padrão
- Coeficiente de variação (CV)
- Primeiro quartil (Q1)
- Terceiro quartil (Q3)

A função é aplicada e testada nas variáveis:

- `Expected Lifetime (yrs.)`
- `Apogee (km)`

## Como Executar o Projeto

1. Certifique-se de que o arquivo de dados `satellites.csv` encontra-se no mesmo diretório do arquivo `.py`.
2. Instale as bibliotecas necessárias, caso ainda não as possua.
3. Execute o script utilizando sua IDE favorita ou pelo terminal:

```bash
python nome_do_seu_arquivo.py
```

## Objetivo

O objetivo deste projeto é aplicar conceitos de:

- Manipulação e tratamento de dados com Pandas;
- Estatística descritiva;
- Construção de tabelas de frequência;
- Visualização de dados com Matplotlib;
- Análise exploratória de dados reais relacionados a satélites artificiais.

---
**Projeto desenvolvido para fins acadêmicos.**
