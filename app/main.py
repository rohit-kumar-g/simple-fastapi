from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import requests
import json

app = FastAPI()

# Define the public folder path
PUBLIC_FOLDER = "./app/media"
app.mount("/media", StaticFiles(directory=PUBLIC_FOLDER), name="fsdf")


class FetchDetailsRequest(BaseModel):
    title: str  # For fetching YouTube data


@app.get("/")
async def root():
    return {"message": "Hello World"}

import requests

def fetchdetailshelper():
    req_url = "https://newapp-1-my0o.onrender.com/media"
    
    response = requests.get(req_url)
    
    # Check if the response contains valid JSON
    if response.status_code == 200:
        try:
            data = response.json()  # Parse the JSON response
            media_links = data.get("media_links", [])  # Get the media_link field
            if isinstance(media_links, list):
                print(f"Number of media links: {len(media_links)}")
            else:
                print("media_link is not a list.")
        except ValueError:
            print("Failed to parse JSON.")
    else:
        print(f"Request failed with status code: {response.status_code}")


@app.get("/fetch/")
async def get_details(background_tasks: BackgroundTasks):
    # Add the task to fetch details in the background
    background_tasks.add_task(fetchdetailshelper)
    return {"message": "Description download started"}