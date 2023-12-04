import requests
from bs4 import BeautifulSoup

class AmazonProductScraper:
    def __init__(self, url):
        """Initialize the scraper with a product URL.

           Args:
               url (str): URL of the Amazon product page to scrape.
        """
        self.url_product = url
        self.soup = self.get_website_and_parse_it()

    def get_website_and_parse_it(self):
        # User-Agent string for Google Chrome
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        # Perform a GET request with the specified headers
        try:
            response = requests.get(self.url_product, headers=headers)
            # Raises an HTTPError for unsuccessful status codes
            response.raise_for_status()
        except requests.RequestException as e:
            raise Exception(f"Request failed: {e}")

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def fetch_product_name(self):
        name_element = self.soup.find(name="span", id="productTitle").getText().strip()
        if name_element:
            return name_element
        else:
            # Raise an exception if the price element is not found in the HTML
            raise Exception(f"Name element with link {self.url} not found")


    def fetch_product_price(self):
        """Fetch and return the product price from the given URL.

        Args:
            url (str): URL of the Amazon product page to scrape.

        Returns:
            float: The price of the product.

        Raises:
            Exception: If the request fails, the price element is not found, or price conversion fails.
        """



        # Find the price element using its HTML class
        price_whole = self.soup.find(name="span", class_="a-price-whole").getText()
        price_fraction = self.soup.find(name="span", class_="a-price-fraction").getText()
        if price_whole and price_fraction:
            try:
                # Extract the text from the price element and convert it to a float
                full_price = price_whole+price_fraction
                return float(full_price)
            except ValueError:
                # Handle cases where the text cannot be converted to float
                raise Exception("Failed to convert price to float")
        else:
            # Raise an exception if the price element is not found in the HTML
            raise Exception("Price element not found")

