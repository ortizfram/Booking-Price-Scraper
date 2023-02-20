import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


# Define the list of hotel names to search for
names_path = pd.read_csv('competitors_for_test.csv')
hotel_names = names_path['competitors_names']

# Set up Selenium web driver
driver = webdriver.Chrome()

# Set up an explicit wait for locating the search results
wait = WebDriverWait(driver, 15)

# Create a list to store all search results
all_results = []

# Loop through each hotel name and extract its name and price for different occupancies
for name in hotel_names:
    for occupancy in [2, 3]:
        # Define the check in and out dates
        checkin_date = (pd.Timestamp.now() + pd.Timedelta('1D')).strftime('%Y-%m-%d')
        checkout_date = (pd.Timestamp.now() + pd.Timedelta('2D')).strftime('%Y-%m-%d')

        # Construct the URL for the hotel page on Booking.com
        url = 'https://www.booking.com'
        driver.get(url)

        # Find the search bar element and send the hotel name
        search_bar = wait.until(presence_of_element_located((By.XPATH, "//input[@type='search']")))
        search_bar.send_keys(name)

        # Wait for a bit to allow the search results to appear
        time.sleep(1)

        # Send the Enter key to execute the search
        search_bar.send_keys(Keys.RETURN)
#-----------------------------------------------------------------
# ADD check in out dates, and occupancy

#-----------------------------------------------------------------
        try:
            # Wait for the search results to appear
            hotel_listings = wait.until(presence_of_element_located((By.XPATH, "//div[@id='hotellist_inner']/div")))

            # Find the first hotel listing on the page
            hotel_listing = hotel_listings.find_element_by_xpath("./*[contains(@class, 'sr_item')][1]")

            # Extract the name and price of the hotel
            hotel_name = hotel_listing.find_element_by_xpath(".//span[contains(@class, 'sr-hotel__name')]").text.strip()
            hotel_price = hotel_listing.find_element_by_xpath(".//div[contains(@class, 'bui-price-display__value')]").text.strip()

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