import pandas as pd
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests
# pip install lxml 

# Define the list of hotel names to search for
names_path = pd.read_csv('competitors_test.csv')
hotel_names = names_path['competitors_names']
location = names_path['location']
checkin_date =   pd.Timestamp.now().strftime('%Y-%m-%d')
checkout_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

# Create a list to store all search results
all_results = []

# Loop through each hotel name and extract its name and price for different occupancies

for occupancy in [2, 3]:

        # Construct the URL for the hotel page on Booking.com
        url = 'https://www.booking.com/searchresults.en-gb.html?ss={location}&ssne={location}&ssne_untouched={location}&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin={checkin_date}&checkout={checkout_date}&group_adults={occupancy}&no_rooms=1&group_children=0&sb_travel_purpose=leisure'    
        # define headers
        response = requests.get(url)
        headers = response.headers
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.content,'lxml')

        # Select Property block
        for item in soup.select('.property-card'):
                print(item)
                print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
#---------------------------------------------
# SAVE TO A FILE

# # Write all search results to a single file
# with open('search_results.txt', 'w') as f:
#     for result in all_results:
#         f.write(f'Hotel: {result[0]} | Occupancy: {result[1]} | Name: {result[2]} | Price: {result[3]}\n')

# # Open the file to show the search results
# with open('search_results.txt', 'r') as f:
#     print(f.read())

# # Quit the web driver
# driver.quit()
