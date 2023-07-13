from flask import *
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression


app=Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/bmi', methods=["POST"])
def page():
  gen=eval(request.form.get("gen"))
  weight=eval(request.form.get("weight"))
  height=eval(request.form.get("height"))
  bmi=eval(request.form.get("bmi"))
  
  url="BMI_Data.csv"
  
  data=pd.read_csv(url)
  health=data.values
  
  #Split
  x=health[:,:4]
  y=health[:,-1]
  
  model=LogisticRegression()
  model.fit(x,y)
  
  arr=model.predict([[gen,weight,height,bmi]])

  return render_template("index.html", data=str(arr[0]))


if __name__ == '__main__':
  app.run()