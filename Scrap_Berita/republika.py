import requests
from bs4 import BeautifulSoup
import json
from json import *
from datetime import datetime, timedelta

url = 'https://www.republika.co.id/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

news_items = []

def get_publish_time(publish_time):
    if 'detik' in publish_time:
        return datetime.now() - timedelta(seconds=int(publish_time.split()[0]))
    elif 'menit' in publish_time:
        return datetime.now() - timedelta(minutes=int(publish_time.split()[0]))
    elif 'jam' in publish_time:
        return datetime.now() - timedelta(hours=int(publish_time.split()[0]))
    elif 'hari' in publish_time:
        return datetime.now() - timedelta(days=int(publish_time.split()[0]))
    elif 'minggu' in publish_time:
        return datetime.now() - timedelta(weeks=int(publish_time.split()[0]))
    elif 'bulan' in publish_time:
        return datetime.now() - timedelta(weeks=int(publish_time.split()[0])*4)
    elif 'tahun' in publish_time:
        return datetime.now() - timedelta(weeks=int(publish_time.split()[0])*52)
    else:
        if 'minutes' in publish_time:
            minutes_ago = int(publish_time.split()[0])
            return datetime.now() - timedelta(minutes=minutes_ago)
        elif 'hours' in publish_time:
            hours_ago = int(publish_time.split()[0])
            return datetime.now() - timedelta(hours=hours_ago)
        else:
            raise ValueError("Unknown time format: " + publish_time)
# Find all article elements
articles = soup.select('li.list-group-item.list-border.conten1')

for article in articles:
    if article.select_one('a.adv-eksternal') is not None:
        continue
    
    # Extract the title
    title = article.select_one('h3 > span').text.strip()

    # Extract the category
    category = article.select_one('span.kanal-info').text.strip()

    # Extract the publish time dengan get_publish_time
    publish_time = get_publish_time(article.select_one('div.date').text.strip().split('-')[-1].strip())

    # Format the publish time as string
    publish_time_str = publish_time.strftime("%d-%m-%Y %H:%M")

    # Create a dictionary for the news item
    news_item = {
        "title": title,
        "category": category,
        "publish_time": publish_time_str,  # Use the formatted string
    }

    # Append the news item to the list
    news_items.append(news_item)

# Write the news items to a JSON file
with open('Scrap_Berita/republika.json', 'w') as json_file:
    json.dump(news_items, json_file, indent=4)

