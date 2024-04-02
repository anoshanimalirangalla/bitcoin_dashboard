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
