import requests
import json

# Get the authentication key for the deployed service
key, _ = service.get_keys()

# One sample patient. Features: age, prevalentHyp, sysBP, diaBP, glucose
sample_input = {
    "data": [[40, 1, 20, 94, 66]]
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {key}'
}

json_data = json.dumps(sample_input)

response = requests.post(
    service.scoring_uri,
    data=json_data,
    headers=headers
)

print("Response:")
print(response.json())
