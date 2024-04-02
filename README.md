# Bitcoin Dashboard with PyGal

## Objective 
The objective of the project is to create a dashboard for KPIs related to BITCOIN. 
I have selected 3 main KPIs for  the ease of the project and additionally added USD to CAD exchange rates as well. 
Each fetched KPI was introduced with a basic definition. 
The web application is powered with Flask.

The KPIS and data are fetched from NASDAQ API [https://data.nasdaq.com/databases/BCHAIN#anchor-metal-stocks-qdl-bchain-)for]

Each KPI is developed with related .py files. 

##  Chart 1 - Bitcoin trade vs transaction volume ratio

```python
import nasdaqdatalink
import pandas as pd
import pygal
import os

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 400)

# Define the static folder path
static = 'static'  # static folder path

nasdaqdatalink.ApiConfig.api_key = 'NASDAQ_API_KEY'
TVTVR_data = nasdaqdatalink.get_table('QDL/BCHAIN', code='TVTVR')

########################################################
# Chart 01 - Bitcoin trade vs transaction volume ratio
#########################################################
def chart_01():
# an empty list to store data
  TVTVR_list = []
  #loop through the data and append it to the list
  for index,row in TVTVR_data.iterrows():
    # convert the timestamp to date format as %Y-%m-%d.
    date = row[1].strftime('%Y-%m-%d')
    # append the list
    TVTVR_list.append((date, row[2]))

# extract and seperate lists from date and value
  dates,value = zip(*TVTVR_list)

  # create a line chart
  chart = pygal.Line()
  chart.title = "Bitcoin trade vs transaction volume ratio"
  chart.x_labels = dates
  chart.add('values', value)
  chart.render_to_file(os.path.join(static, 'Volume_ratio_chart.svg'))
  return "done" # to ensure the process is completed

print(chart_01())
```
## Chart 2 - Bitcoin Total Transaction Fees USD

```python
import nasdaqdatalink
import pandas as pd
import pygal
import os

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 400)

# Define the static folder path
static = 'static'  

nasdaqdatalink.ApiConfig.api_key = 'NASDAQ_API_KEY'
TRFUS_data = nasdaqdatalink.get_table('QDL/BCHAIN', code='TRFUS')

########################################################
# Chart 02 - Bitcoin Total Transaction Fees USD
########################################################
def chart_02():
# an empty list to store  data
  TRFUS_list = []
  #  loop through the data and append it to the list
  for index,row in TRFUS_data.iterrows():
    # convert the timestamp to date format as %Y-%m-%d.
    date = row[1].strftime('%Y-%m-%d')
    # append the list
    TRFUS_list.append((date, row[2]))

# extract and seperate lists from date and value
  dates,value = zip(*TRFUS_list)

  # create a line chart
  chart = pygal.Line()
  chart.title = "Bitcoin Total Transaction Fees USD"
  chart.x_labels = dates
  chart.add('values', value)
  chart.render_to_file(os.path.join(static, 'Transaction Fees_chart.svg'))
  return "done" # to ensure the process is completed

print(chart_02())
```
## Chart 3 - Bitcoin Cost Per Transaction

```python
import nasdaqdatalink
import pandas as pd
import pygal
import os

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_columns', 12)
pd.set_option('display.width', 400)

# Define the static folder path
static = 'static'  # folder path is added here.

nasdaqdatalink.ApiConfig.api_key = 'NASDAQ_API_KEY'
CPTRA_data = nasdaqdatalink.get_table('QDL/BCHAIN', code='CPTRA')

########################################################
# Chart 03 - Bitcoin Cost Per Transaction
#########################################################

def CPTRA_chart():

# an empty list to store data
  CPTRA_list = []
#  loop through the data and append it to the list
  for index,row in CPTRA_data.iterrows():
  # convert the timestamp to date format as %Y-%m-%d.
    date = row[1].strftime('%Y-%m-%d')
  # append the list
    CPTRA_list.append((date, row[2]))

# extract and seperate lists from date and value
  dates,value = zip(*CPTRA_list)

  # create a line chart
  chart = pygal.Bar()
  chart.title = "Bitcoin Cost Per Transaction"
  chart.x_labels = dates
  chart.add('values', value)
  chart.render_to_file(os.path.join(static, 'trans_chart.svg'))
 return "Done" #to ensure the process is completed

print(CPTRA_chart())
```
## Exchange rates -> USD to CAD for 7 days from 5th March 2024

```python
import urllib.request
import json
import pygal
import os

# Define the static folder path
static = 'static' 

def get_data():

# store the data
  data =[]

  for value in range(7):
# constructing API url to fetch data
    url = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@2024-03-0{2+value}/v1/currencies/usd.json'
    # data fetching from API
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())

# store the data
    data.append(result["usd"]["cad"])
    print(data)

# make the graph

  bar_chart = pygal.Line()
  bar_chart.title = 'currency rates within 7 days'
  bar_chart.add('CAD', data) #add some values

  bar_chart.render_to_file(os.path.join(static, 'exchange_rate_chart.svg')) #save the chart
  return "done" # this shows the process is completed

print(get_data())
```
## main.py - Flask powered web application 
```python
from flask import Flask, render_template
import nasdaqdatalink
import pandas as pd
import pygal
import os

# importing fucntions from other files
from exchange import get_data
from chart1 import chart_01
from chart2 import chart_02
from chart3 import CPTRA_chart


app = Flask(__name__) # flask application creation

@app.route('/', methods=['GET']) # route to the home page
def index():
  # call the functions 
  result_1 = get_data() 
  result_2 = chart_01()
  result_3 = chart_02()
  result_4 = CPTRA_chart()
  
  return render_template('index.html',result_1=result_1,result_2=result_2,result_3=result_3,result_4=result_4)

# run the flsk application
if __name__ == '__main__':
    app.run(debug=True)
```

## HTML page 

```html
<!DOCTYPE html>
<html>
<head>
    <title>Bitcoin Charts</title>

  <!-- <link rel="stylesheet" type="text/css" href="static/style.css"> -->
  <!--internal CSS styles -->
    
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #C8C0BD  ; /* Set background color  */
            text-align: center; /* Center align text */
        }
        .chart {
            margin-bottom: 20px auto; /* Center align charts */
            padding: 20px;
          
        }
        h1 {
          color: #FF4933; /* Set text color to orange */
        }
        h2 {
        color: #474544 ; /* Set text color to grey */
        }
        p {
          color: #080303; /* Set text color to black */
        }
        img {
          max-width: 70%; /* Making sure images don't exceed their container width */
          height: auto; /* Maintain aspect ratio */
          display: block; /* Center align images */
          margin: 0 auto; /* Center align images */
        }
    </style>
</head>
<body>
    <h1>Bitcoin Data Insights</h1>
  <br>
    <div class="chart">
        <h2>USD to CAD Exchange Rate</h2>
      <br>
      <p>This plot shows the USD to CAD exchange rate distribution within 7 days of a period starting from March 5th 2024.</p>
      <br>
        <img src="static/exchange_rate_chart.svg" alt="Exchange Rate Chart">
        
    </div>
  <br>
  <br>
    <div class="chart">
        <h2>Bitcoin Trade vs Transaction Volume Ratio</h2>
      <br>
      <p><b>The Bitcoin Trade vs Transaction Volume Ratio</b> is a metric used to compare the volume of Bitcoin traded on exchanges (trade volume) with the volume of Bitcoin transacted on the Bitcoin network (transaction volume).

      <b>Trade volume</b> refers to the total amount of Bitcoin traded on various exchanges within a specific period, typically measured in terms of Bitcoin (BTC) or its equivalent value in fiat currency (e.g., USD).

      <b>Transaction volume</b>, on the other hand, refers to the total amount of Bitcoin transacted on the Bitcoin network, which includes all transactions recorded on the blockchain.

      The ratio between these two volumes can provide insights into the <b>liquidity and market activity of Bitcoin</b>.</p>
      <br>
        <img src="static/Volume_ratio_chart.svg" alt="Trade vs Transaction Volume Ratio Chart">
        
    </div>
  <br>
  <br>
    <div class="chart">
        <h2>Bitcoin Total Transaction Fees USD</h2>
      <br>
      <p><b>Bitcoin Total Transaction Fees USD</b> refers to the total amount of fees paid by users for transactions on the Bitcoin network, calculated in US dollars.The total transaction fees in USD can vary depending on the number of transactions being processed on the network, the size of each transaction, and the current network congestion.</p>
      <br>
      <img src="static/Transaction Fees_chart.svg" alt="transaction_fees">
      
    </div>
  <br>
  <br>
    <div class="chart">
        <h2>Bitcoin Cost Per Transaction</h2>
      <br>
      <p><b>Bitcoin Cost Per Transaction </b>refers to the average cost incurred for each transaction on the Bitcoin network, typically measured in USD.The Bitcoin Cost Per Transaction is an important metric as it provides insight into the cost efficiency of using Bitcoin for transactions.</p>
      <br>
      <img src="static/trans_chart.svg" alt="Bitcoin Cost Per Transaction">
        
        
    </div>
</body>
</html>
```

Find the original work in [Replit](https://replit.com/@a00284480/A00284480-Assignment-7)






