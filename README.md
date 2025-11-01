# 🏠 House Price Predictor

A **machine learning web application** that predicts house prices in **Bangalore** based on features like location, square footage, number of bedrooms (BHK), and bathrooms.  
The app is built with **Flask**, styled using **Bootstrap**, and deployed on **Render**.

🔗 **Live Demo:** [House Price Predictor on Render](https://house-price-predictor-1-khif.onrender.com/)

---

## 🚀 Features

- Predicts the approximate house price instantly  
- Converts predicted value into Indian currency words  
- User-friendly and responsive web interface  
- Automatically reloads the same page with predictions (no redirect errors)  
- Model trained on real Bangalore housing dataset  

---

## 🧠 Tech Stack

**Frontend:**  
- HTML5  
- CSS3  
- Bootstrap 4  

**Backend:**  
- Flask (Python)  
- NumPy, Pandas, Scikit-learn  
- num2words for price in words  
- Pickle for loading trained ML model  

**Deployment:**  
- Render Cloud Platform  

---

## 📂 Project Structure

House-Price-Predictor/
│
├── app.py # Main Flask application
├── templates/
│ └── index.html # Webpage template
├── static/ # (Optional) CSS/JS files if added
├── House.pkl # Trained ML model file
├── Bangalore_dataset.csv # Dataset used for model training
├── requirements.txt # All dependencies
└── README.md # Project documentation


---

## ⚙️ How to Run Locally

1.Clone this repository
   git clone https://github.com/yourusername/House-Price-Predictor.git
   cd House-Price-Predictor

2.Create a virtual environment
    python -m venv venv
    venv\Scripts\activate       # For Windows
    source venv/bin/activate    # For Mac/Linux

3.Install dependencies
    pip install -r requirements.txt

4.Run the application
    python app.py

5.Open in browser
    http://127.0.0.1:5000/
    

## Model Description

Model Type: Regression (Linear/Polynomial/Ensemble)
Trained on: Bangalore_dataset.csv
Target variable: Price (in lakhs)
Features used:
    Location
    Total Square Feet
    Number of Bathrooms
    BHK

## Live App:https://house-price-predictor-1-khif.onrender.com/

