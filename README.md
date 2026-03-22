### Docker Assignment Project

BMW Global Sales Prediction Web Application
This project is a machine learning web application developed using Flask and Docker.
The system predicts BMW global sales performance based on the selected BMW model, year, and region.
The prediction result is classified into two categories:

-High Sales
-Low Sales

---

Features

Web-based user interface built with Flask
Machine learning model for sales level prediction
Dockerized application for easy deployment
Simple and intuitive user interaction

---

Machine Learning Overview
The prediction model was trained using historical BMW global sales data (2018–2025).
Relevant features such as vehicle model, year, and sales region are used as input to predict the expected sales level.

---

## How to Run

```bash
docker build -t bmw-app .
docker run -p 5000:5000 bmw-app
```

Open: http://localhost:5000

---

How to Use the Website

1.Select a BMW Model from the dropdown list
2.Select a Year
3.Select a Region
4.Click the Predict button
5.The prediction result (High Sales / Low Sales) will be displayed on the right side of the page

---

## Project Structure

```
.
├── app.py
├── templates/
│   └── index.html
├── model.pkl
├── bmw_global_sales_2018_2025.csv
├── bmw_modified_prediction.ipynb
├── Dockerfile
├── requirements.txt
├── Demo_Assignment_Video.mp4
└── README.md


```


**File Descriptions
app.py
Main Flask backend application.

Loads the trained machine learning model
Handles user input from the web interface
Performs prediction
Sends prediction results back to the frontend

templates/index.html
Frontend web page of the application.

Provides dropdown selections for BMW model, year, and region
Displays the prediction result in a user-friendly format

model.pkl
Serialized machine learning model trained for predicting BMW global sales levels.
bmw_global_sales_2018_2025.csv
Dataset containing historical BMW global sales data used for training and analysis.
bmw_modified_prediction.ipynb
Jupyter Notebook used for:

Data preprocessing
Feature engineering
Model training and evaluation

Dockerfile
Defines the Docker image configuration for running the Flask application.
requirements.txt
Lists all Python dependencies required to run the project.
Demo_Assignment_Video.mp4
Demonstration video showing how the application works and how to use it.
README.md
Project documentation explaining setup, usage, and structure.


---

## Authors
Natthanon Narongsaksakul (st126113)
GitHub: https://github.com/st126113-hash

Waranon Neamtuptim (st125934)
GitHub: https://github.com/Waranon021
