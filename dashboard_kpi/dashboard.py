import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from nltk.chat.util import Chat, reflections

# Load the data from a CSV file
data = pd.read_csv('supply_chain_data.csv')

# Define the KPIs
kpis = ['backorders', 'lead_times', 'fulfillment_rates', 'inventory_turnover']

# Create the layout for the dashboard
app = dash.Dash()
app.layout = html.Div([
    dcc.Dropdown(id='kpi-dropdown', options=[{'label': kpi, 'value': kpi} for kpi in kpis], value='backorders'),
    dcc.Graph(id='kpi-chart'),
    dcc.Input(id='query-input', type='text', placeholder='Ask a question...'),
    html.Div(id='response-text')
])

# Define the callback for the KPI dropdown
@app.callback(
    dash.dependencies.Output('kpi-chart', 'figure'),
    [dash.dependencies.Input('kpi-dropdown', 'value')]
)
def update_chart(kpi):
    # Create a line chart for the selected KPI
    chart_data = go.Scatter(
        x=data['date'],
        y=data[kpi],
        mode='lines',
        name=kpi
    )
    return {'data': [chart_data], 'layout': {'title': kpi}}

# Define the callback for the natural language query
@app.callback(
    dash.dependencies.Output('response-text', 'children'),
    [dash.dependencies.Input('query-input', 'value')]
)
def answer_query(query):
    # Define a set of rules for the natural language processing
    rules = [
        (r'how many backorders are there', 'There are currently {} backorders.'.format(data['backorders'].sum())),
        (r'what is the average lead time', 'The average lead time is {} days.'.format(data['lead_times'].mean())),
        (r'how well are we fulfilling orders', 'Our fulfillment rate is {}%.'.format(data['fulfillment_rates'].mean() * 100)),
        (r'how quickly are we turning over inventory', 'Our inventory turnover rate is {} times per year.'.format(data['inventory_turnover'].mean()))
    ]
    # Create a chat object with the rules
    chat = Chat(reflections, rules)
    # Generate a response to the query
    response = chat.respond(query)
    return response

# Run the dashboard
if __name__ == '__main__':
    app.run_server()
