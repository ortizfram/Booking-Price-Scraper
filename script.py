from bs4 import BeautifulSoup
import requests

'''go to booking.com, put desired location,occupancy quantity, and dates. Then press enter and 
paste those lnks here '''


# Paste the URL here
url = "https://www.booking.com/searchresults.en-gb.html?ss=Mendoza&ssne=Mendoza&ssne_untouched=Mendoza&label=gen173nr-1FCAEoggI46AdIM1gEaAyIAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4Au3_0p8GwAIB0gIkNDA3M2Q2ZjMtZjZjOC00ZWNjLWFmNjQtZWFlZDlmYjVjMTc22AIG4AIB&sid=d8b713e5b1e956005a30a6976b1dc703&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-1003869&dest_type=city&checkin=2023-02-21&checkout=2023-02-22&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure"

# Fetch the page
page = requests.get(url)

# Initialize html parser
soup = BeautifulSoup(page.content, "html.parser")

# Find all property cards
property_cards = soup.find_all("div", class_="a826ba81c4 fe821aea6c fa2f36ad22 afd256fc79 d08f526e0d ed11e24d01 ef9845d4b3 da89aeb942")

# Print title of each property
for card in property_cards:
    title_element = card.find('div', class_='fcab3ed991 a23c043802')
    title = title_element.get_text()
    price_element = card.find('span', class_="fcab3ed991 fbd1d3018c e729ed5ab6")
    price = price_element.get_text()
    occupancy_element = card.find('div', class_="d8eab2cf7f c90c0a70d3")
    occupancy = occupancy_element.get_text()
    info = [title, price, occupancy]
    print(info)
