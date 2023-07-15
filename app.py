from flask import *
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/bmi', methods=["POST"])
def page():
    gen = eval(request.form.get("gen"))
    weight = eval(request.form.get("weight"))
    height = eval(request.form.get("height"))
    bmi = eval(request.form.get("bmi"))

    url = "BMI_Data.csv"

    data = pd.read_csv(url)
    health = data.values

    # Split the data
    x = health[:, :4]
    y = health[:, -1]

    model = RandomForestClassifier()
    model.fit(x, y)

    arr = model.predict([[gen, weight, height, bmi]])

    # Calculate accuracy
    accuracy = accuracy_score(y, model.predict(x))
    accuracy_percentage = accuracy * 100

    return render_template("index.html", data=str(arr[0]), accuracy=accuracy_percentage)


if __name__ == '__main__':
    app.run()
