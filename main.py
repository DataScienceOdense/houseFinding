from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import requests
import os
url = 'https://www.nybolig.dk/soegeresultat-boliger?isRental=false&postalCodes=5210'

#session = requests.Session()

raw_html = requests.get(url)
soup = bs(raw_html.text, 'html.parser')
price = []
address = []
info = []
eRating = []

print(soup.find_all('div', class_="tile__info"))
