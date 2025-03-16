import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "age": 30,
    "extraversion": 5,
    "independ": 6,
    "selfcontrol": 7,
    "anxiety": 4,
    "novator": 8,
    "stag": 10,
    "industry": "Retail",
    "profession": "Sales",
    "traffic": "rabrecNErab",
    "coach": "no",
    "way": "car",
    "gender": "m",
    "head_gender": "f",
    "greywage": "white"
}

response = requests.post(url, json=data)
print(response.json())  # Expected: {"turnover_prediction": 0} or 1
