## AIG200_Capstone
# Machine Learning Deployment Report
1. Project Overview
The goal of this project is to deploy a machine learning model on Azure Machine Learning (Azure ML) and make it accessible via an API endpoint. The model predicts whether a person has diabetes based on features such as glucose level, BMI, age, etc. This project demonstrates the end-to-end process of developing, deploying, and testing a machine learning model in the cloud.
2. Architecture
The deployment architecture consists of the following components:

Model Development:
Data preprocessing, model training, and evaluation were performed locally using Python and Scikit-Learn.

The trained model was saved as a .pkl file using joblib.

Cloud Deployment:

The model was deployed on Azure Machine Learning.

The deployment involved:

Registering the model in the Azure ML workspace.

Creating an inference configuration with a scoring script (score.py).

Deploying the model as a web service using Azure Container Instance (ACI).

API Configuration:

- An API endpoint was created to receive input data and return predictions.

- The API is accessible via a scoring URI.
