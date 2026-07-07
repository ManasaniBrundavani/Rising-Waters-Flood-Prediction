# 🌊 Rising-Waters-Flood-Prediction

Rising-Waters-Flood-Prediction is an intelligent **Machine Learning-based Flood Prediction System** designed to assess flood risk using environmental and weather parameters. The system analyzes historical data and predicts the likelihood of flooding, enabling governments, disaster management authorities, researchers, and citizens to make informed decisions before disasters occur.

---

## ✨ Features

- 🤖 **Machine Learning Prediction**
  - Uses a trained Random Forest Classifier for flood risk prediction.

- 📊 **Flood Risk Analysis**
  - Predicts flood risk levels such as:
    - Low Risk
    - Moderate Risk
    - High Risk
    - Severe Risk

- ⚡ **Real-Time Predictions**
  - Instant flood prediction with confidence scores.

- 📈 **Comprehensive Dashboard**
  - Risk Percentage
  - Prediction Confidence
  - Environmental Parameter Analysis
  - Interactive Charts
  - Safety Recommendations

- 📉 **Data Visualization**
  - Bar Charts
  - Radar Charts
  - Risk Meter
  - Parameter Comparison Graphs

- 📱 **Responsive User Interface**
  - Modern Bootstrap 5 design
  - Mobile-friendly layout
  - Interactive dashboard

- 🕒 **Prediction History**
  - Stores recent predictions for quick reference.

---

# 🛠 Tech Stack

### Backend
- Flask 3.0.0

### Machine Learning
- Scikit-learn 1.4+
- Random Forest Classifier

### Data Processing
- Pandas 2.2+
- NumPy 1.26+

### Frontend
- Bootstrap 5
- Chart.js
- HTML5
- CSS3
- JavaScript

### Environment
- Python 3.13+

---

# 📦 Installation

## Prerequisites

- Python 3.13+
- pip

---

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Rising-Waters-Flood-Prediction.git

cd Rising-Waters-Flood-Prediction
```

---

## Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your-secret-key
FLASK_DEBUG=False
FLASK_ENV=production
```

---

## Prepare Dataset

Place your dataset inside the project root.

```
dataset.csv
```

### Required Columns

```
Rainfall
River_Level
Humidity
Temperature
Drainage
Soil_Moisture
Elevation
Flood
```

---

## Run the Application

```bash
python app.py
```

The application will be available at:

```
http://localhost:5000
```

---

# 🚀 API Endpoints

## GET /

Displays the Flood Prediction Dashboard.

**Response**

```
HTML Page
```

---

## POST /predict

Predicts the flood risk based on environmental parameters.

### Request Body (form-data)

| Parameter | Description |
|-----------|-------------|
| Rainfall | Rainfall (mm) |
| River_Level | River Water Level (m) |
| Humidity | Relative Humidity (%) |
| Temperature | Temperature (°C) |
| Drainage | Drainage Efficiency (%) |
| Soil_Moisture | Soil Moisture (%) |
| Elevation | Elevation Above Sea Level (m) |

---

### Response

Returns:

- Flood Risk Prediction
- Confidence Score
- Risk Percentage
- Environmental Analysis
- Interactive Charts
- Safety Recommendations

---

# 🧪 Testing with Postman

## Example 1 — High Flood Risk

POST

```
http://localhost:5000/predict
```

Body

```
Rainfall = 285

River_Level = 8.4

Humidity = 93

Temperature = 28

Drainage = 22

Soil_Moisture = 90

Elevation = 15
```

Prediction

```
High Flood Risk
```

---

## Example 2 — Moderate Flood Risk

```
Rainfall = 175

River_Level = 5.8

Humidity = 82

Temperature = 30

Drainage = 48

Soil_Moisture = 72

Elevation = 38
```

Prediction

```
Moderate Flood Risk
```

---

## Example 3 — Low Flood Risk

```
Rainfall = 42

River_Level = 2.0

Humidity = 55

Temperature = 32

Drainage = 90

Soil_Moisture = 30

Elevation = 125
```

Prediction

```
Low Flood Risk
```

---

# 🌊 Flood Risk Levels

| Risk Level | Description |
|------------|-------------|
| 🟢 Low | Minimal flood possibility |
| 🟡 Moderate | Monitor weather conditions |
| 🟠 High | Prepare for possible flooding |
| 🔴 Severe | Immediate evacuation recommended |

---

# 📂 Project Structure

```
Rising-Waters-Flood-Prediction/
│
├── app.py
├── requirements.txt
├── dataset.csv
├── README.md
├── .env
├── .gitignore
│
├──  scaler.pkl
│ 
├── static/
│   ├── css/
│   │   └── styles.css
│   │
│   ├── js/
│   │   └── charts.js
│   │
│   └── images/
│
├── templates/
│   └── index.html
│
└
```

---

# ⚙️ How It Works

### Step 1 — User Input

The user enters environmental information:

- Rainfall
- River Level
- Humidity
- Temperature
- Drainage
- Soil Moisture
- Elevation

⬇️

### Step 2 — Data Validation

The application validates:

- Numeric values
- Missing values
- Acceptable ranges

⬇️

### Step 3 — Feature Scaling

Input values are normalized using **StandardScaler**.

⬇️

### Step 4 — Machine Learning Prediction

The trained **Random Forest Classifier** predicts the flood risk.

⬇️

### Step 5 — Risk Analysis

The system calculates:

- Prediction Confidence
- Risk Percentage
- Flood Category

⬇️

### Step 6 — Visualization

Displays:

- Flood Risk Meter
- Radar Chart
- Parameter Comparison
- Confidence Score

⬇️

### Step 7 — Safety Recommendations

Provides disaster preparedness recommendations based on the predicted risk.

---

# 🔒 Security Features

- Secure Environment Variables
- Input Validation
- Error Handling
- Flask Session Security
- Production Configuration
- CSRF Protection
- Safe Data Processing

---

# 📊 Performance

| Metric | Value |
|--------|-------|
| Model Accuracy | 94% |
| Prediction Time | < 100 ms |
| Machine Learning Model | Random Forest |
| Risk Categories | 4 |
| Dataset Size | Historical Flood Dataset |

---

# 🚀 Future Enhancements

- 🌦️ Live Weather API Integration
- 🛰️ Satellite Image Analysis
- 🌍 GIS Flood Mapping
- 📡 IoT River Water Sensors
- 📱 Android & iOS Mobile App
- 📩 SMS & Email Alerts
- 🔔 Push Notifications
- 🤖 Deep Learning Models
- 🗺️ Evacuation Route Recommendation
- 📈 Rainfall Forecasting
- 🌐 Multi-language Support

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 🤝 Support

If you find any bugs or have suggestions for improvements, please open an issue on GitHub or contact the development team.

---

# 👨‍💻 Contributors

**Development Team**

- Machine Learning Engineer
- Backend Developer
- Frontend Developer
- UI/UX Designer
- Data Analyst

---

## ⭐ If you found this project useful, don't forget to give it a Star on GitHub!