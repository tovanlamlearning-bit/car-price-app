# 🚗 Car Price Predictor

An end-to-end machine learning application that predicts used car prices based on key features such as age, mileage, engine power, and weight.

👉 Live Demo: (add your Streamlit link here)

---

## 🎯 Project Objective

To build a predictive model that helps used car resellers:
- Set competitive prices
- Improve sales efficiency
- Reduce pricing risks

---

## 🧠 Machine Learning Approach

- Model: Linear Regression, Ridge, Lasso
- Target transformation: Log transformation (log1p)
- Feature engineering:
  - Handling categorical variables
  - Feature extraction from list-based columns
- Outlier treatment: IQR method
- Regularisation:
  - Ridge (L2)
  - Lasso (L1)

---

## 📊 Model Performance

| Model            | RMSE | R²   |
|------------------|------|------|
| Linear           | 0.14 | 0.87 |
| Clean Linear     | 0.15 | 0.85 |
| Ridge            | ~0.15 | ~0.85 |
| Lasso            | ~0.15 | ~0.85 |

👉 Insight:
- Regularisation improved model stability
- No significant overfitting observed
- Linear model is sufficient for this dataset

---

## ⚙️ Tech Stack

- Python
- Pandas / NumPy
- Scikit-learn
- Streamlit (for deployment)

---

## 🏗️ Project Structure
car-price-app/
│
├── app/ # Streamlit app
├── src/ # Prediction logic
├── models/ # Saved model files
├── notebook/ # Training notebook
├── data/ # Dataset
├── requirements.txt
└── README.md