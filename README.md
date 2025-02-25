## AIG200_Capstone
# Machine Learning Deployment Report

## Project Overview
The goal of this project is to deploy a machine learning model on Azure Machine Learning (Azure ML) and make it accessible via an API endpoint. The model predicts whether a person has diabetes based on features such as glucose level, BMI, age, etc. This project demonstrates the end-to-end process of developing, deploying, and testing a machine learning model in the cloud.

## Architecture
The deployment architecture consists of the following components:

### Model Development:
- Data preprocessing, model training, and evaluation were performed locally using Python and Scikit-Learn.
- The trained model was saved as a .pkl file using joblib.

### Cloud Deployment:
- The model was deployed on Azure Machine Learning.
- The deployment involved:
  - Registering the model in the Azure ML workspace.
  - Creating an inference configuration with a scoring script (score.py).

Deploying the model as a web service using Azure Container Instance (ACI).

API Configuration:

- An API endpoint was created to receive input data and return predictions.

- The API is accessible via a scoring URI.

3. Data Used
Dataset: Pima Indians Diabetes Dataset.

Source: UCI Machine Learning Repository.

Features:

Pregnancies

Glucose

BloodPressure

SkinThickness

Insulin

BMI

DiabetesPedigreeFunction

Age

Target Variable: Outcome (1 = Diabetes, 0 = No Diabetes).

4. Model Development
Algorithm: Random Forest Classifier.

Framework: Scikit-Learn.

Training:

The dataset was split into training (80%) and testing (20%) sets.

The model was trained on the training set and evaluated on the test set.

Performance Metrics:

Accuracy: XX%

Precision: XX%

Recall: XX%

F1-Score: XX%

5. Cloud Infrastructure
Azure Machine Learning:

Used for model registration, deployment, and management.

Azure Container Instance (ACI):

Used to host the deployed model as a web service.

Azure Storage:

Used to store the trained model (diabetes_model.pkl).

6. How It Works
API Endpoint:

The deployed model is accessible via a scoring URI.

Users can send HTTP POST requests with input data to the API endpoint.

Input Format:

The API expects input data in JSON format:

json
Copy
{
  "data": [[6, 148, 72, 35, 0, 33.6, 0.627, 50]]
}
Output Format:

The API returns predictions in JSON format:

json
Copy
[1]
7. Code and Resources
Files Included
Model Development:

train_model.py: Script for data preprocessing, model training, and saving the model.

diabetes_model.pkl: Trained Random Forest model.

Model Deployment:

deploy_model.py: Script for deploying the model on Azure ML.

score.py: Scoring script for handling API requests and generating predictions.

Testing:

test_api.py: Script for testing the API endpoint.

8. Access Instructions
API Endpoint:

Scoring URI: http://<your-service>.azurecontainer.io/score

Request Type: POST

Input Format: JSON

json
Copy
{
  "data": [[6, 148, 72, 35, 0, 33.6, 0.627, 50]]
}
Output Format: JSON

json
Copy
[1]
Testing the API:

Use the provided test_api.py script or tools like Postman to send requests to the API.

9. Evaluation and Conclusion
Model Performance
Accuracy: The model achieved an accuracy of XX% on the test dataset.

Evaluation Metrics:

Precision: XX%

Recall: XX%

F1-Score: XX%

Deployment Challenges
Deprecation Warnings:

The deployment used Azure ML SDK v1, which is being deprecated. Migrating to SDK v2 is recommended for future-proofing.

API Testing:

Initial testing revealed syntax errors in the score.py file, which were resolved by ensuring proper JSON handling and error logging.

10. Future Improvements
Model Enhancements:

Experiment with other algorithms (e.g., Gradient Boosting, Neural Networks) to improve accuracy.

Perform hyperparameter tuning for better performance.

Deployment Enhancements:

Migrate to Azure ML SDK v2 for better features and long-term support.

Use Azure Kubernetes Service (AKS) for scalable deployments.

API Security:

Add authentication (e.g., API keys) to secure the API endpoint.

11. Example API Request and Response
Request:
json
Copy
{
  "data": [[6, 148, 72, 35, 0, 33.6, 0.627, 50]]
}
Response:
json
Copy
[1]
12. Screenshots
Azure ML Workspace:
Azure ML Workspace (Add screenshot of your Azure ML workspace)

Deployed Service:
Deployed Service (Add screenshot of the deployed service in Azure ML)

API Testing:
API Testing (Add screenshot of API testing using Postman or Python)

13. References
Azure Machine Learning Documentation

Scikit-Learn Documentation

Pima Indians Diabetes Dataset

Repository Structure
Copy
DiabetesML/
├── train_model.py
├── diabetes_model.pkl
├── deploy_model.py
├── score.py
├── test_api.py
├── README.md
