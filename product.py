from web_scraping import AmazonProductScraper

class Product:
    def __init__(self, full_url):
        self.website = full_url.split("/")[2]
        self.product_name = full_url.split("/")[3]
        self.product_id = full_url.split("/")[5]
        self.short_link = f"https://www.amazon.com.au/dp/{self.product_id}"
        self.product_price = AmazonProductScraper(url=self.short_link).fetch_product_price()