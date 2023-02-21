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

soup = BeautifulSoup(page2.content, 'html.parser')
print(soup)
