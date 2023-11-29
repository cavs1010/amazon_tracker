import json
import os
from google.oauth2.service_account import Credentials
import requests
from bs4 import BeautifulSoup

#TODO Create google sheets
#TODO Create google sheets connection

# Retrieving the website
#URL = "https://www.amazon.com.au/dp/B09R51WRV4"
URL = "https://www.amazon.com.au/dp/B08YY4ZPNB"
response = requests.get(URL)
if response.status_code != 200:
    raise Exception("Failed to retrieve data from the website")

# Fetch the data using beautiful soup
soup =BeautifulSoup(response.text, 'html.parser')
price_product = float(soup.find(name="span", class_="a-offscreen").getText().replace("$",""))


# Load credentials from the environmental variable
creds_json = json.loads(os.environ['GOOGLE_APPLICATION_CREDENTIALS_JSON'])
creds = Credentials.from_service_account_info(creds_json)

