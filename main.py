from web_scraping import AmazonProductScraper
from product import Product
from g_sheets_auth import GoogleSheetsAuth
import os

#FIRST CASE: product is not in google sheets
# 1. Create a class product that will be placed in the google sheets
# 2. I need check if its Amazon, what is the ID, shortcut link, name of product (URL), Amazon price, last checked(TODAY), notes(no)


with open('raw_links.txt') as file:
   links = file.readlines()

for link in links:
   product = Product(link)
   print(product.product_price)
#TODO 1.1 Object is new -> I am going to add it to the spreadsheet based on the website that I found the product
#TODO 1.2 The object that has been added to the spreadsheets is deleted from the .txt file.
#TODO

# robot_vacuum = AmazonProductScraper(url="https://www.amazon.com.au/dp/B08YY4ZPNB")
#
# print(robot_vacuum.price)
#
# google_sheets_auth = GoogleSheetsAuth()
#
# client = google_sheets_auth.get_client()
#
# spreed_sheet_key = os.environ['SPREED_SHEET_KEY']
#
# spreadsheet = client.open_by_key(spreed_sheet_key)
# worksheet = spreadsheet.get_worksheet(0)
# print(worksheet.acell('A1').value)




