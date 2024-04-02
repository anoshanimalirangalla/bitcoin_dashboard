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
