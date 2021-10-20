




import csv
import plotly_express as px
import numpy as np


def getDataSource(data_path):
    x=[]
    y=[]
    with open(data_path) as f:
        reader=csv.DictReader(f)
        for row in reader:
            y.append(float(row["Days Present"]))
            x.append(float(row["Marks In Percentage"]))
    return{"x":x,"y":y}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print('The correlation between these two is: ' ,correlation[0,1])    

def setup():
    data_path="./Student Marks vs Days Present.csv"     
    datasource=getDataSource(data_path)       
    findCorrelation(datasource)           

setup()