from product import Product
from g_sheets_auth import GoogleSheetsAuth
import datetime as dt
import os
from helper import get_id_from_whole_url_amazon

#FIRST CASE: product is not in google sheets
# 1. Create a class product that will be placed in the google sheets
# 2. I need check if its Amazon, what is the ID, shortcut link, name of product (URL), Amazon price, last checked(TODAY), notes(no)

def read_product_links(file_path):
   """
   Read product links from a file.

   Args:
   file_path (str): Path to the file containing product links.

   Returns:
   list: A list of product links.
   """
   try:
      with open(file_path) as file:
         return file.readlines()
   except IOError as e:
      print(f"Error reading file: {e}")
      return []

def find_first_empty_cell_in_column(worksheet, column_index=1):
   """
   Find the first empty cell in a specified column of a worksheet.

   Args:
   worksheet (Worksheet): A gspread Worksheet object.
   column_index (int): Index of the column to search. It would be 1 because this is the ID of the item

   Returns:
   int: The row index of the first empty cell.
   """
   col_values = worksheet.col_values(column_index)
   for i, cell in enumerate(col_values):
      if cell == '':
         return i
   return len(col_values)+1

def add_new_product_in_spreedsheet(worksheet, product, current_datetime):
   """
     Add a new product to the spreadsheet.

     Args:
     worksheet (Worksheet): A gspread Worksheet object where the product will be added.
     product (Product): A Product object containing product details.
     current_datetime (datetime): The current date and time.
     """
   last_empty_row = find_first_empty_cell_in_column(worksheet)
   row_data = [product.product_id, product.short_link, product.product_name,
               product.product_price, product.product_price,
               current_datetime.strftime('%d/%m/%Y')]
   worksheet.update( values=[row_data], range_name=f'A{last_empty_row}:F{last_empty_row}')
   print(f"Product{product.product_name} from {product.website} has been added into the google sheets.")

def product_already_exists(worksheet, product):
   id_list = worksheet.col_values(1)
   if product.product_id in id_list:
      return True

def main():
   """
   Main function to execute the script.

   This function handles the process of reading product links from a file, checking against
   a Google Sheets document to avoid duplicates, and adding new product information to the sheet.
   It establishes a connection to Google Sheets, reads product links, processes each product,
   and updates the spreadsheet with new products. After processing, the file containing the
   product links is cleared.

   Steps:
   1. Set up the Google Sheets client and open the spreadsheet.
   2. Read product links from 'raw_links.txt'.
   3. Cache the existing product IDs from the spreadsheet.
   4. Process each product link and add new products to the spreadsheet.
   5. Clear 'raw_links.txt' after processing.

   Raises:
       Exception: If any error occurs during the processing of products or updating the spreadsheet.
   """
   # Set up the Google Sheets client
   google_sheets_auth = GoogleSheetsAuth()
   client = google_sheets_auth.get_client()
   spreed_sheet_key = os.environ['SPREED_SHEET_KEY']
   spreadsheet_price_tracker = client.open_by_key(spreed_sheet_key)
   current_datetime = dt.datetime.now()

   # Read product links from the file
   links = read_product_links('raw_links.txt')
   new_products_to_add = [Product(link) for link in links]

   # Obtaining the current list of product and the list pass it
   id_list_cache = spreadsheet_price_tracker.worksheet("www.amazon.com.au").col_values(1)
   new_products_to_add_id_dic = {get_id_from_whole_url_amazon(link): link for link in links}

   for id, url in new_products_to_add_id_dic.items():
      try:
         # Check that it has not previously added
         if not id in id_list_cache:
            product = Product(url)
            worksheet = spreadsheet_price_tracker.worksheet(product.website)
            add_new_product_in_spreedsheet(worksheet, product, current_datetime)

      except Exception as e:
         print(f"Failed to add product {product.product_name}: {e}")

   #Clear the file with the links after adding the products
   with open('raw_links.txt', 'w'):
      pass

if __name__ == "__main__":
    main()

#TODO 1.1 Object is new -> I am going to add it to the spreadsheet based on the website that I found the product
#TODO 1.2 The object that has been added to the spreadsheets is deleted from the .txt file.
#TODO 1.3 Handle the case when an item already exists.
#TODO Second Feature: check the price of the product and compare to the one of the Excel, if its lower, send notification
#TODO 2.1 Iterate over each item of the spreadsheet
#TODO 2.2 Check the price of eah item, and compare it to the one expected.
#TODO 2.3.1 If Its lower, send a notification and update prices
#TODO 2.3.1 If Its not lower update the prices in the spreadhseet
#TODO 3. Handle different websites




