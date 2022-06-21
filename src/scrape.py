"""scrape module"""

from src.exception import JALError

class Scrape:
    """
        Model for the class that are used to scrape
    """

    def __init__(self, url: str):
        self.url = url
    
    def scrape(self):
        """
            function that start the scrapipg
        """
        raise JALError("Not implemented")
