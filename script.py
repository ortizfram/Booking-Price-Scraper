import pandas as pd
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Define the list of hotel names to search for
names_path = pd.read_csv('competitors_for_test.csv')
hotel_names = names_path['competitors_names']

# Set up Selenium web driver
driver = webdriver.Chrome()

# Create a list to store all search results
all_results = []

# Loop through each hotel name and extract its name and price for different occupancies
for name in hotel_names:
    for occupancy in [2, 3]:
        # Define the check in and out dates
        checkin_date = datetime.now().strftime("%Y-%m-%d")
        checkout_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

        # Construct the URL for the hotel page on Booking.com
        url = f'https://www.booking.com/searchresults.en-gb.html?ss={name}&checkin={checkin_date}&checkout={checkout_date}&group_adults={occupancy}&ssne_untouched={name}&src_elem=sb&src=searchresults'

        # Load the URL in the web driver
        driver.get(url)
        # add waiting time so elements charge
        driver.implicitly_wait(10)

        try:
            # Wait for the search button to become clickable to simulate human interaction
            button = driver.find_element_by_xpath('//*[@id="left_col_wrapper"]/div[1]/div/form/div/div[6]/div/button')

            button.click()

            # Find the first hotel listing on the page
            hotel_listing = driver.find_element_by_xpath('//*[@id="hotellist_inner"]/div[1]')

            # Extract the name and price of the hotel
            hotel_name = hotel_listing.find_element_by_xpath('//*[@id="search_results_table"]/div[2]/div/div/div[3]/div[3]/div[1]/div[2]/div/div[1]/div/div[1]/div/div[1]/div/h3/a/div[1]').text.strip()
            hotel_price = hotel_listing.find_element_by_xpath('//*[@id="search_results_table"]/div[2]/div/div/div[3]/div[3]/div[1]/div[2]/div/div[2]/div[2]/div/div[1]/span/div/span[2]').text.strip()

            # Print the name, price and occupancy of the hotel
            print(f'Name: {hotel_name} | Occupancy:{occupancy} | Price: {hotel_price}')

            # Add the search results to the list
            all_results.append([name, occupancy, hotel_name, hotel_price])
        except:
            # If the hotel is not found, skip to the next occupancy
            continue

# Write all search results to a single file
with open('search_results.txt', 'w') as f:
    for result in all_results:
        f.write(f'Hotel: {result[0]} | Occupancy: {result[1]} | Name: {result[2]} | Price: {result[3]}\n')

# Open the file to show the search results
with open('search_results.txt', 'r') as f:
    print(f.read())

# Quit the web driver
driver.quit()
