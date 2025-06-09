
# ⚖️ BMI Health Status Predictor

A simple Flask web app that predicts health status based on BMI data using a Random Forest Classifier.

## 🚀 Screenshot

![image](https://github.com/user-attachments/assets/8d8a86a4-a0e3-48ad-82f6-124dab1d6969)


## 🚀 Features

- Input: Gender, Weight, Height, BMI
- Output: Predicted Health Status
- Model: Random Forest Classifier (from `scikit-learn`)
- Live Accuracy Calculation

## 📁 Project Structure

```

.
├── app.py              # Main Flask app
├── BMI\_Data.csv        # Dataset for training
├── templates/
│   └── index.html      # HTML form and result display
└── README.md           # Project info

````

## 💻 How to Run

1. **Install dependencies:**

```bash
pip install flask pandas scikit-learn
````

2. **Run the Flask app:**

```bash
python app.py
```

3. **Open in Browser:**

```
http://127.0.0.1:5000
```

## 🧠 Model Info

* **Algorithm**: RandomForestClassifier
* **Training**: Done at runtime using `BMI_Data.csv`
* **Accuracy**: Displayed dynamically after prediction

## 📄 Sample Inputs (index.html)

* Gender: `0 = Female`, `1 = Male`
* Weight: in kilograms
* Height: in centimeters
* BMI: Body Mass Index

## 📜 License

MIT License. Free to use and modify.

