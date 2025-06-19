# 🩺 Disease Classification 

This project is a **Streamlit-based web app** that classifies diseases based on user-reported symptoms. It leverages machine learning to provide fast and accurate predictions across a wide range of common illnesses.
URL : https://disease-classification-by-saket.streamlit.app/

---

## 🚀 Features

* 🔍 **Predicts from 112 unique symptoms**
* 🧠 **Classifies among 50 unique diseases**
* 🤖 **Machine Learning model: Bernoulli Naive Bayes**
* 📈 **Model accuracy: 95%+**
* 💻 **Interactive Streamlit web interface**
* 🧾 **Downloadable PDF report of predictions**
* ⚙️ **Custom feature engineering for better accuracy**

---

## 🧠 How It Works

* The user inputs:

  * Age and sex
  * Minimum 3 symptoms (up to 17 supported)
* The symptoms are vectorized using `TfidfVectorizer`
* The processed features are passed through a trained **BernoulliNB** model
* The model outputs the **predicted disease**
* The app also provides:

  * Suggested precautions
  * Risk assessment
  * Treatment guidance (medications or surgery if applicable)

---

## 🛠 Tech Stack

* **Frontend:** Streamlit
* **ML Model:** Scikit-learn (`BernoulliNB`)
* **Vectorization:** TF-IDF (`TfidfVectorizer`)
* **Model Persistence:** Joblib
* **Report Generation:** FPDF

---

## 🧬 Model Performance

* **Accuracy:** 95%+
* **Algorithm:** Bernoulli Naive Bayes
* **Training Data:** Cleaned dataset of symptoms mapped to diseases
* **Evaluation:** Stratified train-test split with performance validation

---

## 🧠 Future Enhancements

* Add confidence scores for predictions
* Expand to support multiple languages
* Connect to electronic health record (EHR) systems
* Improve visualization and user dashboard

---
