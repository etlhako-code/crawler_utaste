import requests
from bs4 import BeautifulSoup

# Define the base URL of the website with pagination
base_url = 'https://u-taste.com/blogs/recipes?page='

# Define the number of pages to crawl
num_pages = 3  # Change this to the desired number of pages

# Loop through the specified number of pages
for page_number in range(1, num_pages + 1):
    # Construct the URL for the current page
    page_url = f'{base_url}{page_number}'

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

            # Check if the link_url is not None and is a valid URL
            if link_url and link_url.startswith('http'):
                print(link_url)
    else:
        print(f'Failed to retrieve page {page_number}. Status code: {response.status_code}')
