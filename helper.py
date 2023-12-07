import re

def get_id_from_whole_url_amazon(url):
    """
        Extracts and returns the product ID from a given URL.

        Args:
            url (str): The URL to extract the product ID from.

        Returns:
            str: The extracted product ID.

        Raises:
            ValueError: If the product ID is not found in the URL.
    """
    match = re.search(r'\/B\w{9}', url)
    if match:
        return match.group()[1:]
    else:
        raise ValueError("Product ID not found in the URL")