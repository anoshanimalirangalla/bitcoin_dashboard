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
