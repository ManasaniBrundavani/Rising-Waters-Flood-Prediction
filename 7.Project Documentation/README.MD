# Project Documentation

# Rising Waters – Machine Learning Based Flood Prediction System

---

# 1. Introduction

Floods are among the most devastating natural disasters, causing severe damage to human lives, infrastructure, agriculture, and the environment. Accurate flood prediction enables governments and disaster management authorities to take preventive measures and reduce the impact of floods.

The **Rising Waters – Flood Prediction System** uses Machine Learning algorithms to analyze environmental and geographical parameters and predict whether a region is at **High Flood Risk** or **Low Flood Risk**. The trained XGBoost model is integrated into a Flask web application that provides an easy-to-use interface for flood risk prediction.

---

# 2. Problem Statement

Traditional flood forecasting methods often depend on manual observations and historical records, making early prediction difficult.

This project aims to develop an intelligent Machine Learning-based flood prediction system capable of providing quick and reliable flood risk predictions using environmental data.

---

# 3. Objectives

- Develop a Machine Learning-based flood prediction model.
- Analyze environmental factors affecting floods.
- Compare multiple Machine Learning algorithms.
- Select the best-performing model.
- Deploy the trained model using Flask.
- Provide an easy-to-use web application for flood prediction.

---

# 4. Technologies Used

## Programming Language

- Python

## Frontend

- HTML5
- CSS3

## Backend

- Flask

## Machine Learning

- Scikit-learn
- XGBoost
- Pandas
- NumPy
- Joblib

## Deployment

- GitHub
- Render

---

# 5. Dataset

The project uses the **Flood Prediction Dataset** obtained from Kaggle.

Dataset Link:

https://www.kaggle.com/datasets/naiyakhalid/flood-prediction-dataset

The dataset contains the following environmental features:

- Monsoon Intensity
- Topography Drainage
- River Management
- Deforestation
- Urbanization
- Climate Change
- Dams Quality
- Siltation
- Agricultural Practices
- Encroachments
- Disaster Preparedness
- Drainage Systems
- Coastal Vulnerability
- Landslides
- Watersheds
- Deteriorating Infrastructure
- Population Score
- Wetland Loss
- Inadequate Planning
- Political Factors

Target Variable:

- Flood Probability

---

# 6. Machine Learning Workflow

1. Dataset Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Data Preprocessing
5. Feature Scaling
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Comparison
10. Model Deployment using Flask

---

# 7. Models Implemented

The following Machine Learning models were trained and evaluated:

- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- XGBoost

## Model Accuracy

| Model | Accuracy |
|--------|----------|
| Decision Tree | 69.94% |
| Random Forest | 90.28% |
| KNN | 84.57% |
| XGBoost | **93.24%** |

The XGBoost model achieved the highest accuracy and was selected for deployment.

---

# 8. Application Features

- User-friendly web interface
- Accepts environmental input parameters
- Predicts flood risk instantly
- Displays High Flood Risk or Low Flood Risk
- Responsive design
- Live deployment using Render

---

# 9. System Architecture

```
User
   │
   ▼
Flask Web Application
   │
   ▼
Input Validation
   │
   ▼
Feature Scaling
   │
   ▼
XGBoost Model
   │
   ▼
Flood Risk Prediction
   │
   ▼
Prediction Result
```

---

# 10. Results

The application successfully predicts flood risk based on user-provided environmental parameters.

The deployed web application:

- Accepts valid user inputs
- Performs feature scaling
- Uses the trained XGBoost model
- Predicts High Flood Risk or Low Flood Risk
- Generates results within a few seconds

The application was successfully deployed using Render.

---

# 11. Future Enhancements

- Integration with Live Weather APIs
- Real-Time Rainfall Monitoring
- SMS and Email Alert System
- Interactive GIS Maps
- Mobile Application
- Cloud-based Data Storage
- District-wise Flood Prediction

---

# 12. Conclusion

The **Rising Waters – Machine Learning Based Flood Prediction System** demonstrates how Machine Learning can assist in early flood risk prediction. By analyzing multiple environmental parameters using the XGBoost algorithm, the application provides quick and reliable flood risk predictions through a simple Flask web interface. The project showcases the practical application of Machine Learning in disaster management and can be further enhanced by integrating real-time weather data and advanced visualization techniques.

---

# Project Repository

GitHub Repository:

https://github.com/ManasaniBrundavani/Rising-Waters-Flood-Prediction

---

# Live Demo

Deployment Link:

https://rising-waters-flood-prediction-sxaw.onrender.com