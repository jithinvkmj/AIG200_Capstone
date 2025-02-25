import requests
import json

scoring_uri = "http://14009f86-7433-4e80-b294-623aa1fc1973.eastus2.azurecontainer.io/score"
data = {
    "data": [[1, 89, 66, 23, 94, 28.1, 0.167, 30]]
}
headers = {"Content-Type": "application/json"}
response = requests.post(scoring_uri, json=data, headers=headers)
print(response.json())