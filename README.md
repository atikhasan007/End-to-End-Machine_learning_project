# End-to-End-Machine_learning_project

## Workflow
1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity
5. update the configuration manger is src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the app.py



## project pipeline
1. Data ingestion component --> github
2. Data validation
3. Data Transformation ->preprocessing train, test 
4. model trainer component
5. model Evaluation component
6. prediction pipeline
7. user app with flask



```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```
```bash
pip install -r requirements.txt

```


```bash
1. notebook expriment
2. project utility - > logging, exceptions, utils, module
3. project workflow
```

# 🍷 Wine Quality Prediction - End-to-End Machine Learning Project

## 📌 Project Overview
This project is an end-to-end Machine Learning system that predicts wine quality based on physicochemical properties. It includes a full ML pipeline (data ingestion, validation, transformation, model training, evaluation) and a Flask web application for real-time predictions.

---

## 🎯 Business Objectives
- Predict wine quality using chemical features
- Build an automated end-to-end ML pipeline
- Provide a user-friendly web interface
- Enable model retraining using Flask `/train` endpoint

---

## 📊 Data Sources
Dataset: Wine Quality Dataset

### Features:
- fixed acidity
- volatile acidity
- citric acid
- residual sugar
- chlorides
- free sulfur dioxide
- total sulfur dioxide
- density
- pH
- sulphates
- alcohol

### Target:
- quality (wine rating)

---

## 🔍 Exploratory Data Analysis (EDA)
- Feature distribution analysis
- Correlation heatmap
- Outlier detection
- Relationship between alcohol and wine quality

---

## 🤖 Models Used
- ElasticNet Regression

### ⚙️ Hyperparameters:
- alpha: Regularization strength
- l1_ratio: Balance between L1 and L2 penalty

## 📈 Evaluation Metrics
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² Score

---

## 🌐 End-to-End Application
This project includes a Flask web application.

### Routes:
- `/` → Home page (input form)
- `/predict` → Make predictions
- `/train` → Train the ML pipeline

---

## 📁 user interface 
<img width="963" height="622" alt="Screenshot 2026-04-25 110403" src="https://github.com/user-attachments/assets/44443c67-d30b-49ea-bf1d-b7df320e4ec8" />
and after click button 
<img width="1012" height="589" alt="Screenshot 2026-04-25 110538" src="https://github.com/user-attachments/assets/67fb46d5-15d6-4bd8-bd7b-66ae6f376405" />


