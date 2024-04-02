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
