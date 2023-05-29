import requests


headers = {
    "ContentType": "application/json"
}

response_example = requests.get("https://swapi.dev/api/people/5", headers=headers)
api_json_example = response_example.json()
print(api_json_example)
