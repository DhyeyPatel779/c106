import csv
import plotly_express as px
import numpy as np


def getDataSource(data_path):
    x=[]
    y=[]
    with open(data_path) as f:
        reader=csv.DictReader(f)
        for row in reader:
            x.append(float(row["Size of TV"]))
            y.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return{"x":x,"y":y}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print('The correlation between these two is: ' ,correlation)    

def setup():
    data_path="./tvsizevstime.csv"     
    datasource=getDataSource(data_path)       
    findCorrelation(datasource)           

setup()