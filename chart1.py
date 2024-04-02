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
