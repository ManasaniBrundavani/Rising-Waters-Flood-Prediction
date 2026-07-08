# Project Testing

## Objective

The objective of testing is to verify that the **Rising Waters: Flood Prediction System** performs correctly, accepts valid user input, predicts flood risk accurately using the trained XGBoost model, and provides reliable results through a user-friendly Flask web application.

---

## Testing Environment

| Component | Details |
|-----------|---------|
| Operating System | Windows 11 |
| Programming Language | Python 3.10 |
| Framework | Flask |
| IDE | Visual Studio Code |
| Browser | Google Chrome / Microsoft Edge |
| Machine Learning Library | Scikit-learn, XGBoost |
| Dataset | Flood Prediction Dataset (Kaggle) |

---

# Functional Test Cases

| Test Case | Description | Expected Result | Status |
|-----------|-------------|-----------------|--------|
| TC-01 | Launch the application | Home page loads successfully | ✅ Pass |
| TC-02 | Enter valid feature values | Prediction result is displayed | ✅ Pass |
| TC-03 | Enter low-risk values | Low Flood Risk is displayed | ✅ Pass |
| TC-04 | Enter high-risk values | High Flood Risk is displayed | ✅ Pass |
| TC-05 | Submit incomplete form | Browser validation prevents submission | ✅ Pass |
| TC-06 | Click Predict Flood Risk | Model predicts flood risk successfully | ✅ Pass |

---

# Validation Testing

| Input Condition | Result |
|-----------------|--------|
| Valid numerical values | Accepted |
| Empty input fields | Validation message displayed |
| Decimal values | Accepted |
| Values within dataset range | Processed successfully |
| Invalid text input | Rejected by browser validation |

---

# Performance Testing

- Application starts successfully.
- Model loads without errors.
- Prediction is generated within a few seconds.
- User interface remains responsive during prediction.

---

# Compatibility Testing

| Browser | Result |
|----------|--------|
| Google Chrome | ✅ Pass |
| Microsoft Edge | ✅ Pass |

---

# Model Testing

| Machine Learning Model | Accuracy |
|------------------------|----------|
| Decision Tree | 69.94% |
| Random Forest | 90.28% |
| K-Nearest Neighbors | 84.57% |
| XGBoost | **93.24%** |

The XGBoost model achieved the highest accuracy and was selected for deployment in the Flask web application.

---

# Testing Summary

The application was tested for functionality, input validation, prediction accuracy, and browser compatibility. All modules performed as expected. The trained XGBoost model successfully predicts flood risk based on user-provided environmental parameters. The web interface is responsive, easy to use, and successfully deployed on Render.

---

# Overall Status

## ✅ Project Testing Successfully Completed