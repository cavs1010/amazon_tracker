import requests
from bs4 import BeautifulSoup

class AmazonProductScraper:
    def __init__(self, url):
        """Initialize the scraper with a product URL.

           Args:
               url (str): URL of the Amazon product page to scrape.
        """
        self.url_product = url
        self.price_product = self.fetch_product_data(self.url_product)

    def fetch_product_data(self, url):
        """Fetch and return the product price from the given URL.

        Args:
            url (str): URL of the Amazon product page to scrape.

        Returns:
            float: The price of the product.

        Raises:
            Exception: If the request fails, the price element is not found, or price conversion fails.
        """

        # User-Agent string for Google Chrome
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        # Perform a GET request with the specified headers
        try:
            response = requests.get(url, headers=headers)
            # Raises an HTTPError for unsuccessful status codes
            response.raise_for_status()
        except requests.RequestException as e:
            raise Exception(f"Request failed: {e}")


        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the price element using its HTML class
        price_element = soup.find(name="span", class_="a-offscreen")
        if price_element:
            try:
                # Extract the text from the price element and convert it to a float
                return float(price_element.getText().replace("$", ""))
            except ValueError:
                # Handle cases where the text cannot be converted to float
                raise Exception("Failed to convert price to float")
        else:
            # Raise an exception if the price element is not found in the HTML
            raise Exception("Price element not found")

