import requests
from bs4 import BeautifulSoup

# Define the list of hotel names to search for
hotel_names = ['Hotel A', 'Hotel B', 'Hotel C']

# Loop through each hotel name and extract its name and price
for name in hotel_names:
    # Construct the URL for the hotel page on Booking.com
    url = f'https://www.booking.com/searchresults.en-gb.html?ss={name}'

    # Send a GET request to the URL and get the HTML content of the page
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the first hotel listing on the page
    hotel_listing = soup.find('div', {'class': 'sr_item_content'})

    # Extract the name and price of the hotel
    hotel_name = hotel_listing.find('span', {'class': 'sr-hotel__name'}).text.strip()
    hotel_price = hotel_listing.find('div', {'class': 'bui-price-display__value'}).text.strip()

    # Print the name and price of the hotel
    print(f'Name: {hotel_name} | Price: {hotel_price}')
