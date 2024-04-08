import requests
from bs4 import BeautifulSoup
import json
from json import *
from datetime import datetime, timedelta

url = 'https://www.republika.co.id/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

news_items = []

# Find all article elements
articles = soup.select('li.list-group-item.list-border.conten1')

for article in articles:
    if article.select_one('a.adv-eksternal') is not None:
        continue
    
    # Judul
    title = article.select_one('h3 > span').text.strip()

    # Kategori
    category = article.select_one('span.kanal-info').text.strip()

    # Mengambil teks dari tag <div class="date">
    date_text = article.select_one('div.date').get_text(strip=True)

    # Memisahkan teks untuk mendapatkan hanya tanggal dan waktu
    publish_time = date_text.split('-')[-1].strip()
    if "detik" in publish_time:
        publish_time = datetime.now() - timedelta(seconds=int(publish_time.split()[0]))
        publish_time = publish_time.strftime("%d-%m-%Y %H:%M")
    if "menit" in publish_time:
        publish_time = datetime.now() - timedelta(minutes=int(publish_time.split()[0]))
        publish_time = publish_time.strftime("%d-%m-%Y %H:%M")
    if "jam" in publish_time:
        publish_time = datetime.now() - timedelta(hours=int(publish_time.split()[0]))
        publish_time = publish_time.strftime("%d-%m-%Y %H:%M")
        
    news_link = article.select_one('a').get('href')

    # Create a dictionary for the news item
    news_item = {
        "title": title,
        "category": category,
        "publish_time": publish_time,
        "news_link": news_link,
    }

    # Append the news item to the list
    news_items.append(news_item)

# Write the news items to a JSON file
with open('Scrap_Berita/republika.json', 'w') as json_file:
    json.dump(news_items, json_file, indent=4)

# Waktu scrapping
scrap_time = datetime.now().strftime("%d-%m-%Y %H:%M")

with open('Scrap_Berita/Scrap_Time.json', 'w') as json_file:
    json.dump(scrap_time, json_file, indent=4) 