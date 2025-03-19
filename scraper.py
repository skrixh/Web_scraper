import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

#Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['web_scraper']
collection = db['quotes']

#Make a request to the webpage
url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#Find all the quotes on the webpage
quotes = []
for quote in soup.find_all("span", class_="text"):
    quotes.append({"quote": quote.text})

#Save the quotes to MongoDB
collection.insert_many(quotes)  # Insert the quotes into the collection
print("Scraped and stored quotes in MongoDB!")