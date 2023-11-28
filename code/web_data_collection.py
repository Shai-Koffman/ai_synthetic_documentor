# filename: web_data_collection.py
import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup

def search_for_information(query):
    # Encode the search query for use in a URL
    encoded_query = quote(query)
    # Search query on DuckDuckGo (as Google may block automated searches)
    search_url = f"https://duckduckgo.com/html/?q={encoded_query}"
    # Perform the HTTP request to get the search results page
    response = urllib.request.urlopen(search_url)
    # Read the response and convert it to a BeautifulSoup object for parsing
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    # Find all search result links
    links = soup.find_all('a', class_='result__a')
    # Print the URLs of the search results
    for link in links:
        print(link.get('href'))

# Market information on the Lidar industry
search_for_information("Lidar industry market report")

# Market information on the car industry
search_for_information("Car industry market report")

# Historical RFQs by car companies to Lidar providers
search_for_information("Car company RFQs to Lidar providers")