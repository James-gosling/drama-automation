import requests
import json
from datetime import datetime, timedelta

# Constants
CHANNEL_ID = 'CelestialVisions'
URLS_FILE = 'urls.txt'

def get_latest_videos(channel_id):
    # Here you would add the actual API request to Dailymotion to get the latest videos
    response = requests.get(f'https://api.dailymotion.com/channel/{channel_id}/videos')
    return response.json()['list']

def update_urls_file(videos):
    with open(URLS_FILE, 'a') as file:
        for video in videos:
            file.write(video['url'] + '\n')

def main():
    today = datetime.utcnow()
    # Only run on Monday and Friday
    if today.weekday() not in [0, 4]:
        return

    latest_videos = get_latest_videos(CHANNEL_ID)
    update_urls_file(latest_videos)

if __name__ == '__main__':
    main()