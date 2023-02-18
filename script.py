import pandas as pd
from selenium import webdriver
from datetime import datetime, timedelta

# Define the list of hotel names to search for
names_path = pd.read_csv('competitors_names.csv')
hotel_names = names_path['competitors_names']

# Set up Selenium web driver
driver = webdriver.Chrome()

# Loop through each hotel name and extract its name and price for different occupancies
for name in hotel_names:
    # Create a list to store the search results
    search_results = []

    for occupancy in [2, 3, 4, 5, 6]:
        # Define the check in and out dates
        checkin_date = datetime.now().strftime("%Y-%m-%d")
        checkout_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

        # Construct the URL for the hotel page on Booking.com
        url = f'https://www.booking.com/searchresults.en-gb.html?checkin={checkin_date}&checkout={checkout_date}&ss={name}&group_adults={occupancy}'

        # Load the URL in the web driver
        driver.get(url)

        try:
            # Find the first hotel listing on the page
            hotel_listing = driver.find_element_by_xpath('//*[@id="hotellist_inner"]/div[1]/div[1]')

            # Extract the name and price of the hotel
            hotel_name = hotel_listing.find_element_by_class_name('sr-hotel__name').text.strip()
            hotel_price = hotel_listing.find_element_by_class_name('bui-price-display__value').text.strip()

            # Print the name, price and occupancy of the hotel
            print(f'Name: {hotel_name} | Occupancy:{occupancy} | Price: {hotel_price}')

            # Add the search results to the list
            search_results.append([hotel_name, occupancy, hotel_price])
        except:
            # If the price is not found, skip to the next one
            continue

    # Write the search results to a file
    with open(f'{name}_search_results.txt', 'x') as f:
        for result in search_results:
            f.write(f'Name: {result[0]} | Occupancy: {result[1]} | Price: {result[2]}\n')

    # Open the file to show the search results
    with open(f'{name}_search_results.txt', 'r') as f:
        print(f.read())

# Quit the web driver
driver.quit()
