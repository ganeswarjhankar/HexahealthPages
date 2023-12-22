import requests
import json

# Replace with your own API key
API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"

# List of cities and business type
cities = ["City1", "City2", "City3"]
business_type = "Lawyers"

# Initialize an empty list to store extracted data
data_list = []

for city in cities:
    # Construct the URL for Google Places API
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={business_type}+in+{city}&key={API_KEY}"

    # Make a GET request to the API
    response = requests.get(url)
    data = response.json()

    # Extract relevant information from the response
    for result in data.get("results", []):
        business_name = result.get("name")
        phone_number = result.get("formatted_phone_number", "N/A")
        email = "N/A"  # You'll need more complex logic to extract emails
        google_reviews = result.get("rating", "N/A")

        # Append the extracted data to the list
        data_list.append({
            "Business Name": business_name,
            "Phone Number": phone_number,
            "Email": email,
            "Google Reviews": google_reviews
        })

# Export the data to a CSV file
import csv

csv_filename = "scraped_data.csv"
csv_fields = ["Business Name", "Phone Number", "Email", "Google Reviews"]

with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_fields)
    writer.writeheader()
    writer.writerows(data_list)

print(f"Data scraped and saved to {csv_filename}")
