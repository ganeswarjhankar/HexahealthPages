from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# open each URL with Selenium and run code for it
S = Service("D:\\chromedriver.exe")
driver = webdriver.Chrome(service=S)
driver.maximize_window()

import pandas as pd

# Read LinkedIn job data from Excel/CSV file
job_data = pd.read_csv('D:\\upwork\\linkedin_jobs.csv')

# Use LinkedIn API or other methods to extract detailed job information
# (Please replace this comment with your specific code for LinkedIn API integration)



import openai

# OpenAI API key
#Authorization: Bearer OPENAI_API_KEY
openai.api_key = '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'

# Analyze job role using GPT-3.5
job_role = "Software Engineer"  # Example job role, replace it with your actual job role
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"Analyse the job role: {job_role}.",
    max_tokens=1  # Adjust the token limit as per your requirement
)

mpc_pitch = response.choices[0].text.strip()





#point 3
# Read contact list
contact_list = pd.read_csv('contacts.csv')

# Match job roles with contacts
matching_contacts = []
for _, contact in contact_list.iterrows():
    if contact['job_role'] == job_role:
        matching_contacts.append(contact)

# Now, `matching_contacts` contains the contacts with the specified job role



