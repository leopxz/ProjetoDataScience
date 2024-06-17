import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
from flask import Flask
import io
import base64


# Iniciando o Flask e Dash
server = Flask(__name__)
app = dash.Dash(__name__, server=server)

# HTML do aplicativo
app.layout = html.Div([
    html.H1("Dashboard de Análise de Doenças Cardíacas"),
    dcc.Upload(
        id='upload-data',
        children=html.Button('Carregar Tabela', id='upload-button', style={'backgroundColor': 'green', 'color': 'white', 'fontWeight': 'bold'}),
        multiple=False
    ),

    html.Div(id='output-data-upload'),
    dcc.Graph(id='correlation-matrix'),
    dcc.Graph(id='scatter-matrix'),
    dcc.Graph(id='barplot-sex-heartdisease'),
    dcc.Graph(id='barplot-restingecg-sex-heartdisease'),
    dcc.Graph(id='stripplot-cholesterol'),
    dcc.Graph(id='boxplot-age'),
    dcc.Graph(id='histogram-age-heartdisease'),
    dcc.Graph(id='kdeplot-age-heartdisease'),
    dcc.Graph(id='scatter-age-maxhr'),
    dcc.Graph(id='stacked-bar-chestpaintype-sex')
])

# Função para parsear o conteúdo do arquivo carregado
def parse_contents(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    except Exception as e:
        print(f"Error parsing file: {e}")
        return None
    return df

# Callback para atualizar os gráficos com base no arquivo carregado
@app.callback(
    [Output('correlation-matrix', 'figure'),
     Output('scatter-matrix', 'figure'),
     Output('barplot-sex-heartdisease', 'figure'),
     Output('barplot-restingecg-sex-heartdisease', 'figure'),
     Output('stripplot-cholesterol', 'figure'),
     Output('boxplot-age', 'figure'),
     Output('histogram-age-heartdisease', 'figure'),
     Output('kdeplot-age-heartdisease', 'figure'),
     Output('scatter-age-maxhr', 'figure'),
     Output('stacked-bar-chestpaintype-sex', 'figure')],
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename')]
)
def update_graph(contents, filename):
    if contents is None:
        return [{}]*10
    
    # Parsear os dados carregados
    dados = parse_contents(contents)
    
    if dados is None:
        return [{}]*10


    print(dados.head())

    # Matriz de correlação (colunas numéricas)
    numeric_cols = dados.select_dtypes(include=['float64', 'int64']).columns
    correlation_matrix = dados[numeric_cols].corr()
    fig_corr = px.imshow(correlation_matrix, text_auto=True, aspect="auto", title="Matriz de Correlação")

    
    # Scatter matrix
    fig_scatter = px.scatter_matrix(dados, dimensions=['RestingECG', 'Cholesterol'],
                                    title="Scatter Matrix: RestingECG vs Cholesterol")

    # Taxa de Doenças Cardíacas por Sexo
    fig_bar_sex_hd = px.bar(dados, x='Sex', y='HeartDisease', title="Taxa de Doenças Cardíacas por Sexo", barmode='group')

    # Número de Cardíacos por EC em Repouso e Sexo
    grouped = dados.groupby(['RestingECG', 'Sex'])['HeartDisease'].sum().reset_index()
    fig_bar_restingecg_sex_hd = px.bar(grouped, x='RestingECG', y='HeartDisease', color='Sex', 
                                       title="Número de Cardíacos por EC em Repouso e Sexo", barmode='group')

    # Colesterol por EC em Repouso
    fig_strip = px.strip(dados, x='RestingECG', y='Cholesterol', title="Colesterol por EC em Repouso", stripmode="overlay")

    # Distribuição de Idade por EC em Repouso
    fig_box_age = px.box(dados, x='RestingECG', y='Age', title="Distribuição de Idade por EC em Repouso")

    # Histogram de Idade dos Cardíacos por RestingECG
    cardiacos = dados[dados['HeartDisease'] == 1]
    fig_hist_age = px.histogram(cardiacos, x='Age', color='RestingECG', 
                                title="Distribuição de Idade dos Cardíacos por EC em Repouso", nbins=30)

    # KDE plot de Idade dos Cardíacos por RestingECG
    fig_kde_age = px.density_contour(cardiacos, x='Age', color='RestingECG', 
                                     title="Distribuição de Densidade de Idades dos Cardíacos por EC em Repouso")

    # Scatter plot de Age vs MaxHR
    fig_scatter_age_maxhr = px.scatter(dados, x='Age', y='MaxHR', title="Idade vs MaxHR")

    # Stacked bar plot de ChestPainType por Sex
    fig_stacked_bar_cpt_sex = px.bar(dados, x='ChestPainType', y='HeartDisease', color='Sex', 
                                     title="Distribuição de ChestPainType por Sexo", barmode='stack')

    return (fig_corr, fig_scatter, fig_bar_sex_hd, fig_bar_restingecg_sex_hd, fig_strip, fig_box_age, 
            fig_hist_age, fig_kde_age, fig_scatter_age_maxhr, fig_stacked_bar_cpt_sex)

if __name__ == '__main__':
    app.run_server(debug=True)
