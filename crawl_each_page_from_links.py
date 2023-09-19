import requests
from bs4 import BeautifulSoup
import os
import numpy as np


#dictionary to hold recipe
doc={"title":"","recipe":""}
recipes=[]

# read urls from file
with open('utasterecipelinks.txt') as rfile:
    crawl_urls=rfile.read().split(',')
    
crawl_urls

# Loop through the urls from file
for url in crawl_urls:
    
    # Construct the URL for the current page
    page_url = url
    print(page_url)
    if not page_url and not page_url.startswith('https://'):
        break
    # Send an HTTP GET request to the current page
    response = requests.get(page_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find title and body of recipe on the page
        heading = soup.find('h1',class_="article-template__title")
        body= soup.find('div',class_="article-template__content")
        doc={"title":heading.text,"recipe":body.text.replace(u'\xa0', u' ')}
        recipes.append(doc)
        
        
    else:
        print(f'Failed to retrieve page {page_number}. Status code: {response.status_code}')

with open("recipes.json",'a') as rec:
    json.dump(recipes,rec)
