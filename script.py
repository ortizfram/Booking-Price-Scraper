import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


# Define the list of hotel names to search for
names_path = pd.read_csv('competitors_test.csv')
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

        # ADD CHECK IN/OUT DATES AND OCCUPANCY
        # Choose check-in date

        # Split checkin_date into year, month, and day components
        year, month, day = checkin_date.split('-')

        # Find and click on the check-in date box
        checkin_box = wait.until(presence_of_element_located((By.XPATH, '//*[@id="frm"]/div[1]/div[2]/div[1]/div[2]/div/div')))
        checkin_box.click()

        # Select the check-in date by clicking on the corresponding day element in the calendar
        checkin_day_element = wait.until(presence_of_element_located((By.XPATH, f'//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[1]/table/tbody/tr/td[@data-date="{year}-{month}-{day}"]')))                                                   
        checkin_day_element.click()

        # Choose check-out date

        # Find and click on the check-out date box
        checkout_box = wait.until(presence_of_element_located((By.XPATH, '//*[@id="frm"]/div[1]/div[2]/div[1]/div[3]/div/div')))
        checkout_box.click()

        # Select the check-out date by clicking on the corresponding day element in the calendar
        checkout_day_element = wait.until(presence_of_element_located((By.XPATH, f'//*[@id="frm"]/div[1]/div[2]/div[2]/div/div/div[2]/table/tbody/tr/td[@data-date="{year}-{month}-{int(day)+1}"]')))
        checkout_day_element.click()
#------------------------------------------
# OCCUPANCY

        # Choose occupancy

        # Find and click on the occupancy selection box
        occupancy_box = wait.until(presence_of_element_located((By.XPATH, '//*[@id="xp__guests__toggle"]')))
        occupancy_box.click()

        # Select the occupancy by clicking on the corresponding option element in the occupancy menu
        occupancy_option = wait.until(presence_of_element_located((By.XPATH, f'//*[@id="frm"]/div[1]/div[4]/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div/div/div[1]/div/span[1]')))
        occupancy_option.click()

                # Find the occupancy dropdown element
        occupancy_dropdown = wait.until(presence_of_element_located((By.ID, "xp__guests__toggle")))

        # Click on the occupancy dropdown to expand it
        occupancy_dropdown.click()

        # Find the occupancy option for the desired number of guests
        occupancy_option = wait.until(presence_of_element_located((By.XPATH, f"//select[@id='no_rooms']/option[@value='1']//following::option[@value='{occupancy}']")))
        
        # Select the occupancy option
        occupancy_option.click()
#------------------------------------------
# SEARCH EXTRACT

        # Find and click the search button
        search_button = wait.until(presence_of_element_located((By.XPATH, "//button[@data-sb-id='main']")))
        search_button.click()

        # Wait for the search results to load
        hotel_listings = wait.until(presence_of_element_located((By.ID, "hotellist_inner")))

        # Find the first hotel listing on the page
        hotel_listing = hotel_listings.find_element_by_xpath(".//div[@class='sr_item'][1]")

        # Extract the name and price of the hotel
        hotel_name = hotel_listing.find_element_by_xpath(".//span[@class='sr-hotel__name']").text
        hotel_price = hotel_listing.find_element_by_xpath(".//div[@class='bui-price-display__value prco-inline-block-maker-helper']").text

        # Print the name, price, and occupancy of the hotel
        print(f"Name: {hotel_name} | Occupancy: {occupancy} | Price: {hotel_price}")

        # Add the search results to the list
        all_results.append([name, occupancy, hotel_name, hotel_price])

# Write all search results to a single file
with open('search_results.txt', 'w') as f:
    for result in all_results:
        f.write(f'Hotel: {result[0]} | Occupancy: {result[1]} | Name: {result[2]} | Price: {result[3]}\n')

# Open the file to show the search results
with open('search_results.txt', 'r') as f:
    print(f.read())

# Quit the web driver
driver.quit()
