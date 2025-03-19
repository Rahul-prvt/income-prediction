# Income Prediction App

## Overview

This is a Streamlit-based web application that predicts whether an individual's income is **<=50K or >50K** based on various personal attributes. The prediction is made using a **Decision Tree model** trained on labeled data.

## Features

- User-friendly **Streamlit UI** for inputting personal details.
- Uses a **pre-trained Decision Tree model** for predictions.
- Categorical variables are **encoded using Label Encoders**.
- Model and encoders are loaded using **joblib**.

## Dependencies

Make sure you have the following Python libraries installed:

```bash
pip install streamlit pandas numpy scikit-learn joblib
```

## How to Run

1. Clone the repository or copy the files to your system.
2. Ensure the **Decision Tree model (****`decision_tree_model.pkl`****)** and **label encoders** are in the same directory.
3. Run the Streamlit app using the command:

```bash
streamlit run app.py
```

## Input Features

- **Education** (Dropdown selection)
- **Marital Status** (Dropdown selection)
- **Occupation** (Dropdown selection)
- **Relationship** (Dropdown selection)
- **Native Country** (Dropdown selection)
- **Sex** (Dropdown selection)
- **Workclass** (Dropdown selection)
- **Hours per Week** (Slider input)
- **Capital Gain** (Number input)
- **Capital Loss** (Number input)

## Prediction Output

After submitting details, the app will predict the income category as:

- **<=50K** (Low Income)
- **>50K** (High Income)

## Model Training

The Decision Tree model was trained on structured data with **label-encoded categorical features** and numerical features like **capital gain/loss and hours worked per week**.

## Future Enhancements

- Deploying the model as an **API endpoint**.
- Improving accuracy with **Random Forest or XGBoost**.
- Adding **feature importance visualization**.

---

Developed using **Python, Streamlit, and Scikit-learn** 🚀

Thanks 
