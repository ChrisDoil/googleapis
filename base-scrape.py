import re
import requests
from bs4 import BeautifulSoup


base_loc_req = requests.get('https://en.wikipedia.org/wiki/List_of_United_States_Air_Force_installations')
soup = BeautifulSoup(base_loc_req.text, 'html.parser')

for tr in soup.find_all('tr'):
    print(tr)


