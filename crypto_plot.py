import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd

import plotly 
plotly.tools.set_credentials_file(username='kmr293', api_key='085yvDtcIGNTb6fFNIy0')

bitcoin_df = pd.read_csv('bitcoin.csv')
ether_df = pd.read_csv('ethereum.csv')


bitcoin_table = FF.create_table(bitcoin_df.head())
ether_tabe = FF.create_table(ether_df.head())



trace1 = go.Scatter(
                    x=bitcoin_df['day'], y=bitcoin_df['market_cap'], # Data
                    mode='lines', name='market cap'
                   )
				   
trace3 = go.Scatter( # Data
					x=['20170831', '20170523', '20170402', '20160802', '20170830', '20170716', '20170914', '20170901', '20170715', '20160619'],
					y=['35,701,500,000', '15,688,000,000', '4,582,700,000', '903,978,000', '34,848,400,000', '15,823,100,000', '26,166,100,000', '36,182,900,000', '18,630,200,000', '906,292,000'],
					mode='markers',
					text=['https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:08/24/2017,cd_max:08/30/2017', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:05/16/2017,cd_max:05/22/2017', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:03/26/2017,cd_max:04/01/2017', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:07/26/2016,cd_max:08/01/2016', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:08/23/2017,cd_max:08/29/2017', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:07/09/2017,cd_max:07/15/2017', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:09/07/2017,cd_max:09/13/2017', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:08/25/2017,cd_max:08/31/2017', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:07/08/2017,cd_max:07/14/2017', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:06/12/2016,cd_max:06/18/2016']# Additional options
					)
trace2 = go.Scatter(x=ether_df['day'], y=ether_df['market_cap'], mode='lines', name='ether_market_cap' )

layout = go.Layout(title='Simple Plot from csv data',
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

# Plot data in the notebook
py.iplot(fig, filename='simple-plot-from-csv')