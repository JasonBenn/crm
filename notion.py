import json
import os
import requests
from dotenv import load_dotenv
from typing import Optional

load_dotenv()
NOTION_SECRET = os.getenv('NOTION_SECRET')
DB_ID = os.getenv('DATABASE_ID')

def list_people():
    return None


headers = {'Authorization': f'Bearer {NOTION_SECRET}', 'Notion-Version': '2021-08-16', 'Content-Type': 'application/json'}


def list_db(cursor: Optional[str]):
    data = {
      "sorts": [
        {
          "property": "Name",
          "direction": "ascending"
        }
      ],
      "page_size": 100
    }
    if cursor:
        data['start_cursor'] = cursor

    response = requests.post(f"https://api.notion.com/v1/databases/{DB_ID}/query", headers=headers, data=json.dumps(data))
    response.raise_for_status()
    return json.loads(response.text)


pages = list_db(None)
all_pages = pages['results']

while pages['has_more']:
    print(pages['next_cursor'])
    cursor = pages['next_cursor'] # '8fefddc1-0cb6-4f66-bb07-448073cde34b',
    pages = list_db(cursor)
    all_pages.extend(pages['results'])

print(len(all_pages))

import ipdb; ipdb.set_trace()
people_in_notion = {x['properties']['Name']['title'][0]['text']['content']: x for x in all_pages}