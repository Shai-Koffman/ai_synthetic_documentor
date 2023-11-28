# filename: web_search_urls.py
from urllib.parse import quote

def construct_search_url(query):
    # Encode the search query for use in a URL
    encoded_query = quote(query)
    # Construct the search URL for DuckDuckGo
    search_url = f"https://duckduckgo.com/?q={encoded_query}&ia=web"
    return search_url

# Market information on the Lidar industry
lidar_market_url = construct_search_url("Lidar industry market report")

# Market information on the car industry
car_market_url = construct_search_url("Car industry market report")

# Historical RFQs by car companies to Lidar providers
rfqs_url = construct_search_url("Car company RFQs to Lidar providers")

# Print the search URLs
print("Lidar Industry Market Report URL:")
print(lidar_market_url)
print("\nCar Industry Market Report URL:")
print(car_market_url)
print("\nCar Company RFQs to Lidar Providers URL:")
print(rfqs_url)