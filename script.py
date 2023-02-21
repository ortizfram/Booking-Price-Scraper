from bs4 import BeautifulSoup 
import requests

'''go to booking.com, put desired location,occupancy quantity, and dates. Then press enter and 
paste those lnks here '''

url_2pax = "https://www.booking.com/searchresults.en-gb.html?ss=Mendoza&ssne=Mendoza&ssne_untouched=Mendoza&label=gen173nr-1FCAEoggI46AdIM1gEaAyIAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4Au3_0p8GwAIB0gIkNDA3M2Q2ZjMtZjZjOC00ZWNjLWFmNjQtZWFlZDlmYjVjMTc22AIG4AIB&sid=d8b713e5b1e956005a30a6976b1dc703&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-1003869&dest_type=city&checkin=2023-02-21&checkout=2023-02-22&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure"
page2= requests.get(url_2pax)
# url3=
# url4=
# url5=
# url6=

# Initialize html parser page2
soup = BeautifulSoup(page2.content, 'html.parser')
lists = soup.find_all('div', class_="a826ba81c4 fe821aea6c fa2f36ad22 afd256fc79 d08f526e0d ed11e24d01 ef9845d4b3 da89aeb942") # property-card

for list in lists:
        title = lists.find('a', class_="fcab3ed991 a23c043802") #title in every section 
        price = lists.find('span', class_="fcab3ed991 fbd1d3018c e729ed5ab6") #price in every section
        info = [title, price]
        print(info)