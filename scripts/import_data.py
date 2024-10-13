import requests

# Correct API endpoint for ClinicalTrials.gov v2
url = "https://clinicaltrials.gov/api/v2/studies"

# Define query parameters (adjust fields as needed)
params = {
    "format": "json",  # Response format
    "pageSize": 10,    # Number of trials to fetch
}

# Send the request
response = requests.get(url, params=params)

# Check for a successful response
if response.status_code == 200:
    with open("data/clinical_trials.json", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("✅ Clinical trial data downloaded successfully!")
else:
    print(f"❌ Failed to fetch data. Status code: {response.status_code}, Response: {response.text}")
