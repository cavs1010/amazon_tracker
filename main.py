import requests
from bs4 import BeautifulSoup

# Retrieving the website
#URL = "https://www.amazon.com.au/dp/B09R51WRV4"
URL = "https://www.amazon.com.au/dp/B08YY4ZPNB"
response = requests.get(URL)
if response.status_code != 200:
    raise Exception("Failed to retrieve data from the website")

# Fetch the data using beautiful soup
soup =BeautifulSoup(response.text, 'html.parser')
price_product = float(soup.find(name="span", class_="a-offscreen").getText().replace("$",""))
print(price_product)

