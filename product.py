from web_scraping import AmazonProductScraper

class Product:
    def __init__(self, full_url):
        """
        Initialize a Product object with details extracted from a URL.

        Parameters:
        full_url (str): The full URL of the Amazon product page.

        Attributes:
        website (str): The domain name of the website.
        product_name (str): The name of the product according to the website.
        product_id (str): The unique identifier of the product.
        short_link (str): A shortened URL to the product page.
        product_price (float): The current price of the product.
        """

        # Split the URL once and store the parts for further processing
        url_parts = full_url.split("/")

        # Basic validation for URL format
        if len(url_parts) < 6:
            raise ValueError("URL format is not as expected.")

        # Extract the website domain, product name, and product ID from the URL
        self.website = url_parts[2]
        self.product_name = url_parts[3]
        self.product_id = url_parts[5]

        # Construct a short link directly to the product page
        self.short_link = f"https://www.amazon.com.au/dp/{self.product_id}"

        # Use the AmazonProductScraper to fetch the current price of the product
        try:
            self.product_price = AmazonProductScraper(url=self.short_link).fetch_product_price()
        except Exception as e:
            # Handle exceptions related to price fetching and set price to None
            self.product_price = None
            print(f"Error fetching product price: {e}")