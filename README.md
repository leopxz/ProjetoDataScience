# Projeto Data Science
## Painel de Análise de Doenças Cardíacas

Bem-vindo ao repositório do Painel de Análise de Doenças Cardíacas! Este painel é construído usando as bibliotecas Dash e Plotly em Python, com o objetivo de explorar e visualizar conjuntos de dados relacionados à análise de doenças cardíacas.

### Visão geral

Este aplicativo fornece visualizações interativas para analisar vários aspectos das doenças cardíacas com base nos dados de entrada. Inclui:

- **Matriz de Correlação**: Visualiza a correlação entre recursos numéricos do conjunto de dados.
- **Matriz de Dispersão**: Mostra relações entre pares de variáveis, com foco em RestingECG e Colesterol.
- **Gráficos de Barras**: Exibe gráficos de barras que ilustram as taxas de doenças cardíacas por sexo e outras variáveis categóricas.
- **Strip Plot**: Destaca os níveis de colesterol em diferentes valores de RestingECG.
- **Box Plot**: Analisa a distribuição da idade entre as categorias do RestingECG.
- **Histograma e Gráfico KDE**: Explora distribuições etárias de indivíduos com doenças cardíacas com base no RestingECG.
- **Gráfico de Dispersão**: Representa a relação entre idade e MaxHR (frequência cardíaca máxima alcançada).
- **Gráfico de Barras Empilhadas**: Mostra a distribuição de ChestPainType por gênero.

### Começando
Para executar este aplicativo localmente, siga os passos abaixo:

**Clone este repositório:**
git clone https://github.com/seu-usuario/nome-do-repositorio.git

**Navegue até o diretório do projeto**
cd nome-do-repositorio

**Instale as dependências necessárias:**
pip install -r requirements.txt

**Execute o aplicativo usando Python:**
python app.py

Após abrir a aplicação, importe o arquivo CSV fornecido como base de dados.

### Conjunto de Dados

Você pode obter o conjunto de dados necessário no [Kaggle Heart Failure Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction?phase=FinishSSORegistration&returnUrl=/datasets/fedesoriano/heart-failure-prediction/versions/1?resource=download&SSORegistrationToken=CfDJ8CHCUm6ypKVLpjizcZHPE71mLcSMss_OEFO2o5DsPbN5hgnDoDP9JfkCgHgOZJmyoplaw84Q5vH6EDekac95KQzZYWD9lrPuZQLaA6GQdmUs5gnQ5mKxYTRbqeXe7U1QQfjN39d9guiC_koXKWG19V2CdPmRuzQOyvilR0Vgt7plZPbgpdDX7CK0pzIrICLpubOqV5x9QDy6494gQi3pT2CNwAhaDoqnwK7IhAK9iBN6tmZXkpQYh-nW_3oJ7f6BZkE7oSQ_sBSvVDPMd8PqGz_gIo6q_yA9TcDlo0A1ABGssu931eowY_0CiElSYdAdeuo6p-aSR8kL1U8C24kLmD04m1E&DisplayName=leonardo%20paix%C3%A3o)

Clique em "Download" para baixar o arquivo CSV e utilize-o na aplicação para visualizar os gráficos.

