import requests
from bs4 import BeautifulSoup
import os
import numpy as np

# Define the base URL of the website with pagination
site_url ='https://u-taste.com'
base_url = site_url+'/blogs/recipes?page='

# change the current directory to my working dir (OPTIONAL)
os.chdir('D:\\MYDOCS\\Nlp practice')

# Define the number of pages to crawl
num_pages = 22 

# use numpy to remove duplicates
def unique(list_dup):
    nplist_dup = np.array(list_dup)
    nplist_unique = np.unique(nplist_dup)
    return nplist_unique.tolist()

urls=[]
link= ""
# Loop through the specified number of pages
for page_number in range(1, num_pages + 1):
    # Construct the URL for the current page
    page_url = f'{base_url}{page_number}'
    print(page_url[-2])
    # Send an HTTP GET request to the current page
    response = requests.get(page_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the anchor tags (links) on the page
        links = soup.find_all('a',class_="full-unstyled-link")

        # Loop through the links and print them
        for link in links:
            # Get the href attribute, which contains the URL
            link_url = link.get('href')
            
            # Check if the link_url is not a full url and make it a full valid URL
            if link_url and not link_url.startswith('https'):
                link = site_url + link_url
                urls.append(link)
    else:
        print(f'Failed to retrieve page {page_number}. Status code: {response.status_code}')

#REMOVE DUPLICATES    
url_list=unique(urls)

#write the new list to a file sep by colon
with open('utasterecipelinks.txt', 'a') as file:
    for url in url_list:
        file.write(url+",")
