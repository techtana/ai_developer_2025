import json
import requests
# Load data from JSON file
with open('solutions.json', 'r') as f:
    emotional_wellness_solutions = json.load(f)

# Your code to work with the data goes here

# Post the file to /items/create
url = "http://localhost:8000/items/create"  # Change to your actual endpoint if different
files = {'file': open('solution_building/solutions.py', 'rb')}
response = requests.post(url, files=files)
print(f"POST status: {response.status_code}")
print(f"Response: {response.text}")
