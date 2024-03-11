import requests
import random

def fetch_random_workout_from_videos_database(notion_token, database_id):
    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Notion-Version": "2021-05-13",
    }
    response = requests.post(f'https://api.notion.com/v1/databases/{database_id}/query', headers=headers)
    if response.status_code == 200:
        results = response.json()["results"]
        if results:
            random_workout = random.choice(results)
            # Extract and return relevant details from random_workout
            print("Random workout fetched successfully!")
            return random_workout
        else:
            print("No workouts found.")
            return None
    else:
        print(f"Failed to fetch workouts. Status code: {response.status_code}")
        return None


def add_workout_to_videos_database(notion_token, database_id, name, tags, url, equipment):
    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Notion-Version": "2021-05-13",
        "Content-Type": "application/json",
    }
    data = {
        "parent": {"database_id": database_id},
        "properties": {
            "Name": {"title": [{"text": {"content": name}}]},
            "Tags": {"multi_select": [{"name": tag} for tag in tags]},
            "URL": {"url": url},
            "Equipment": {"rich_text": [{"text": {"content": equipment}}]}
        }
    }
    response = requests.post('https://api.notion.com/v1/pages', json=data, headers=headers)
    if response.status_code == 200:
        print("Workout added successfully!")
    else:
        print(f"Failed to add workout. Status code: {response.status_code}")

def log_completed_workout(notion_token, database_id, name, tags, date, heaviest_weight):
    headers = {
        "Authorization": f"Bearer {notion_token}",
        "Notion-Version": "2021-05-13",
        "Content-Type": "application/json",
    }
    data = {
        "parent": {"database_id": database_id},
        "properties": {
            "Name": {
                "title": [{"text": {"content": name}}]
            },
            "Tags": {
                "multi_select": [{"name": tag} for tag in tags]
            },
            "Date": {
                "date": {"start": date}
            },
            "HeaviestWeight": {
                "number": heaviest_weight
            }
        }
    }
    response = requests.post('https://api.notion.com/v1/pages', json=data, headers=headers)
    if response.status_code == 200:
        print("Workout logged successfully!")
        return response.json()
    else:
        print(f"Failed to log workout. Status code: {response.status_code}, response: {response.text}")
        return None

