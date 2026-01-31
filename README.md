# 🏠 California Housing Price Prediction App

This project is an end-to-end Machine Learning web application that predicts the median house value in California based on housing and location-related features. The model is trained using scikit-learn Pipelines and deployed as a live application using Streamlit.

🔗 Live App:  
https://housing-price-california.streamlit.app/

---

## 📌 Project Overview

- Dataset: California Housing Dataset  
- Objective: Predict median house value  
- Approach:
  - Data preprocessing using Pipeline and ColumnTransformer
  - Handling missing values, feature scaling, and categorical encoding
  - Training a regression model
  - Deploying the trained model as a web application using Streamlit Cloud

This project follows real-world ML development and deployment practices, including strict library version control.

---

## ⚙️ Tech Stack

- Python  
- scikit-learn  
- pandas  
- numpy  
- joblib  
- Streamlit  

---

## 🧠 Machine Learning Pipeline

The complete preprocessing and model training are handled using a single scikit-learn pipeline:

- Numerical features:
  - Missing value imputation using SimpleImputer  
  - Feature scaling using StandardScaler  
- Categorical features:
  - One-hot encoding using OneHotEncoder  
- Model:
  - Regression model trained on processed features  

The same pipeline is used during training and prediction, ensuring consistency and preventing data leakage.

---

## 🖥️ Web Application Features

- Interactive sliders for numerical inputs  
- Dropdown menu for categorical feature (Ocean Proximity)  
- Real-time prediction of median house price  
- Simple and user-friendly interface  

---

## 🚀 Deployment

The application is deployed using Streamlit Community Cloud.

Important deployment consideration:
- The model was retrained and serialized using a fixed scikit-learn version.
- The same version is pinned in the requirements file to avoid compatibility issues during deployment.

---

## 📁 Project Structure

```bash
  housing-price-streamlit/
├── app.py
├── housing_price_model.pkl
├── requirements.txt
└── README.md
```


---

## 📦 Requirements

- streamlit
- pandas
- numpy
- scikit-learn==1.3.2
- joblib


---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```



---

## 📈 Example Use Case

Users can input housing details such as location, population, households, median income, and ocean proximity. The application then predicts the median house value instantly, making it useful for real estate analysis and machine learning demonstrations.

---

## 🧪 Key Learning Outcomes

- Building robust ML pipelines using scikit-learn  
- Handling numerical and categorical data correctly  
- Model serialization with version safety  
- Deploying machine learning models using Streamlit  
- Debugging real-world ML deployment issues  

---

## 👨‍💻 Author

**Krishna Bedi**
Data Science & Machine Learning Practitioner
📍 India

* LinkedIn: https://www.linkedin.com/in/krishna-bediofficial/
* GitHub: https://github.com/KrishnaJiii

---


## 📜 License

This project is intended for educational and demonstration purposes.


---

⭐ If you found this project useful, feel free to star the repository!
