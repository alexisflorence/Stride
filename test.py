import requests
print(requests) 
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

notion_token = os.getenv('NOTION_SECRET')
database_id_logged = os.getenv('LOGGED_DB')
database_id_video = os.getenv('VIDEO_DB')

headers = {
    "Authorization": f"Bearer {notion_token}",
    "Notion-Version": "2021-05-13",
    "Content-Type": "application/json",
}

# TESTING LOGGED DATABASE CONNECTION
response = requests.post(f'https://api.notion.com/v1/databases/{database_id_logged}/query', headers=headers)
print("Testing Video Database Connection: ")

# Check if the request was successful
if response.status_code == 200:
    print("Success! Connected to Notion API and database found.")
    # Print out a part of the response content
    print(response.json())
else:
    print("Failed to connect. Status code:", response.status_code)
    print("Response:", response.text)

# TESTING VIDEO DATABASE CONNECTION
response = requests.post(f'https://api.notion.com/v1/databases/{database_id_video}/query', headers=headers)
print("Testing Video Database Connection: ")

# Check if the request was successful
if response.status_code == 200:
    print("Success! Connected to Notion API and database found.")
    # Print out a part of the response content
    print(response.json())
else:
    print("Failed to connect. Status code:", response.status_code)
    print("Response:", response.text)
