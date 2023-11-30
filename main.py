from web_scraping import AmazonProductScraper
from g_sheets_auth import GoogleSheetsAuth
import os



robot_vacuum = AmazonProductScraper(url="https://www.amazon.com.au/dp/B08YY4ZPNB")

print(robot_vacuum.price_product)

google_sheets_auth = GoogleSheetsAuth()

client = google_sheets_auth.get_client()

spreed_sheet_key = os.environ['SPREED_SHEET_KEY']

spreadsheet = client.open_by_key(spreed_sheet_key)
worksheet = spreadsheet.get_worksheet(0)
print(worksheet.acell('A1').value)




