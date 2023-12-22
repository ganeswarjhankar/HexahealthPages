import requests

endpoint = "https://api.openai.com/v1/chat/completions"
# Replace DEMO_KEY below with your own key if you generated one.
OPENAI_API_KEY = "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"

# Set up the headers with the authorization token
headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

# Example prompt for chat completion
prompt = "Translate the following English text to French:"

# Make a POST request with data in the body
data = {
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": prompt,
        }
    ]
}

response = requests.post(endpoint, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    print("Request successful!")
    print(response.json())
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
