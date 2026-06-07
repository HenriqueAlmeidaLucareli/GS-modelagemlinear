Análise Estatística de Dados de Satélites
Este repositório contém um script em Python desenvolvido para realizar a leitura, o tratamento e a análise estatística descritiva de uma base de dados sobre satélites. O projeto foi elaborado como parte das atividades da disciplina/curso (CCPQ).

Equipe
Luca Almeida Lucareli - RM: 569061

Henrique Almeida Lucareli - RM: 569183

Enzo Seiji Delgado Tabuchi - RM: 573156

Tecnologias e Dependências
Para que o código funcione corretamente, certifique-se de ter o Python 3.x instalado em sua máquina, juntamente com as seguintes bibliotecas:

Pandas (pip install pandas)

Matplotlib (pip install matplotlib)

Estrutura das Atividades
O script está dividido em quatro partes principais, correspondendo aos exercícios propostos:

Exercício 01: Carregamento da Base de Dados
Leitura do arquivo satellites.csv utilizando o Pandas.

Limpeza inicial dos dados através da remoção de colunas vazias sem nome (Unnamed).

Exercício 02: Tabelas de Frequências
Variável Quantitativa Discreta: Análise da variável Expected Lifetime (yrs.) (Tempo de vida esperado em anos). O script calcula e exibe as frequências absoluta, relativa (%), acumulada e relativa acumulada (%).

Variável Quantitativa Contínua: Análise da variável Perigee (km) (Perigeu em quilômetros). Os dados são agrupados em 10 classes (bins) para a geração da tabela completa de frequências.

Exercício 03: Visualização de Dados
Gráfico 1 (Histograma): Ilustra a distribuição do Perigeu dos satélites para visualização da concentração e dispersão dos dados.

Gráfico 2 (Barras): Destaca o "Top 10" de países proprietários ou operadores com a maior quantidade de satélites em órbita.

Exercício 04: Estatística Descritiva
Criação de uma função reutilizável para extrair e exibir métricas estatísticas essenciais de qualquer coluna numérica.

Métricas calculadas: Média, Mediana (Q2), Moda, Valores Máximo e Mínimo, Amplitude Total, Variância Amostral, Desvio Padrão, Coeficiente de Variação (CV), Primeiro Quartil (Q1) e Terceiro Quartil (Q3).

A função é aplicada e testada nas variáveis Expected Lifetime (yrs.) e Apogee (km).

Como Executar o Projeto
Certifique-se de que o arquivo de dados satellites.csv encontra-se no mesmo diretório do arquivo .py.

Instale as bibliotecas necessárias caso não as possua.

Execute o script utilizando a sua IDE favorita ou via terminal através do comando:
python nome_do_seu_arquivo.py
