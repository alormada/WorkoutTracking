import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 85
HEIGHT_CM = 190
AGE = 23

APP_ID_Nurtritions = os.environ["APP_ID_Nurtritions"]
API_KEY = os.environ["API_KEY"]
TOKEN = os.environ["TOKEN"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
endpoint_name = SHEETY_ENDPOINT.split("/")[-1].replace("s", "")

# print(TOKEN)

host_domain = "https://trackapi.nutritionix.com"
exercise_nurtrition_endpoint = f"{host_domain}/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID_Nurtritions,
    "x-app-key": API_KEY,
}

query = input("Tell me which exercise you did: ")

parameters = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

nurtritions_response = requests.post(url=exercise_nurtrition_endpoint, headers=headers, json=parameters)
result = nurtritions_response.json()
print(result)

duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]
exercise = result["exercises"][0]["name"]

date = str(datetime.now().strftime("%d/%m/%Y"))
time = str(datetime.now()).split(" ")[1].split(".")[0]

# print(date, time)
# print(duration, calories, exercise)

sheety_params = {
    f"{endpoint_name}": {
        "date": date,
        "time": time,
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories,
    }
}

sheety_headers = {
    "Authorization": f"Bearer {TOKEN}"
}
# print(sheety_headers)
# print(sheety_params)

sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=sheety_headers)
sheety_result = sheety_response.json()
print(sheety_result)