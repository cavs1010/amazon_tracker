
from product import Product
from g_sheets_auth import GoogleSheetsAuth
import datetime as dt
import os

#FIRST CASE: product is not in google sheets
# 1. Create a class product that will be placed in the google sheets
# 2. I need check if its Amazon, what is the ID, shortcut link, name of product (URL), Amazon price, last checked(TODAY), notes(no)
google_sheets_auth = GoogleSheetsAuth()
client = google_sheets_auth.get_client()
current_datetime = dt.datetime.now()

with open('raw_links.txt') as file:
   links = file.readlines()

new_products_to_add = []
for link in links:
   product = Product(link)
   new_products_to_add.append(product)

spreed_sheet_key = os.environ['SPREED_SHEET_KEY']
spreadsheet_price_tracker = client.open_by_key(spreed_sheet_key)

def find_first_empty_cell_in_column(worksheet, column_index=1):
   col_values = worksheet.col_values(column_index)
   for i, cell in enumerate(col_values):
      if cell == '':
         return i
   return len(col_values)+1

def add_new_product_in_spreedsheet(product):
   worksheet = spreadsheet_price_tracker.worksheet(product.website)
   last_empty_row = find_first_empty_cell_in_column(worksheet)
   worksheet.update_cell(last_empty_row, 1, product.product_id)
   worksheet.update_cell(last_empty_row, 2, product.short_link)
   worksheet.update_cell(last_empty_row, 3, product.product_name)
   worksheet.update_cell(last_empty_row, 4, product.product_price)
   worksheet.update_cell(last_empty_row, 5, product.product_price)
   worksheet.update_cell(last_empty_row, 6, current_datetime.strftime('%d/%m/%Y'))
   print('Product has been added to the spreedsheet!')

for product in new_products_to_add:
   add_new_product_in_spreedsheet(product)



#TODO 1.1 Object is new -> I am going to add it to the spreadsheet based on the website that I found the product
#TODO 1.2 The object that has been added to the spreadsheets is deleted from the .txt file.
#TODO 1.3 Handle the case when an item already exists.
#TODO Second Feature: check the price of the product and compare to the one of the Excel, if its lower, send notification
#TODO 2.1 Iterate over each item of the spreadsheet
#TODO 2.2 Check the price of eah item, and compare it to the one expected.
#TODO 2.3.1 If Its lower, send a notification and update prices
#TODO 2.3.1 If Its not lower update the prices in the spreadhseet
#TODO 3. Handle different websites

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




