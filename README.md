# 🎓 Student Score Predictor

> **End-to-end machine-learning application that predicts student exam scores from study-related inputs.**

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Joblib](https://img.shields.io/badge/Joblib-Model%20Persistence-green)](https://joblib.readthedocs.io/)

## Overview

Student Score Predictor demonstrates a complete supervised-learning workflow: inspect data, preprocess inputs, train a regression model, persist the trained model, and serve predictions through an interactive web interface.

## Features

- Student exam-score prediction
- Linear Regression model
- Dataset validation and preparation
- Model persistence with Joblib
- Interactive Streamlit interface

## ML Workflow

```text
Dataset
  ↓
Validate / Preprocess
  ↓
Train Linear Regression
  ↓
Evaluate
  ↓
Save Model
  ↓
Streamlit App
  ↓
Prediction
```

## Repository Structure

```text
Student-Score-Predictor/
├── dataset/
│   └── student_scores.csv
├── src/
│   ├── check_dataset.py
│   ├── data_preprocessing.py
│   ├── model_loader.py
│   ├── predict.py
│   ├── predictor.py
│   ├── train_model.py
│   └── utils.py
├── app.py
├── requirements.txt
└── README.md
```

## Tech Stack

Python · Pandas · NumPy · scikit-learn · Streamlit · Joblib

## Run Locally

```bash
git clone https://github.com/aizaz512/Student-Score-Predictor.git
cd Student-Score-Predictor
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/train_model.py
streamlit run app.py
```

## Portfolio Value

A focused demonstration of supervised ML engineering fundamentals, including data handling, training, model persistence, reusable Python modules, and user-facing inference.

## Roadmap

- [x] Dataset validation
- [x] Model training
- [x] Model persistence
- [x] Prediction application
- [ ] Automated tests
- [ ] Input validation improvements
- [ ] Evaluation metrics in UI
- [ ] Deployment
- [ ] Model monitoring

## Author

**Sahibzada Aizaz Ur Rahman**  
Python Developer | AI/ML Engineer

- GitHub: https://github.com/aizaz512
- Portfolio: https://github.com/aizaz512/sahibzada-portfolio

## License

MIT
