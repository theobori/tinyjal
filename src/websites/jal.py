"""jal module"""

from src.tor import Tor
from src.scrape import Scrape

class JAL(Scrape):
    """
        This object manages the 'Just Another Library'
        category scraping
    """

    def __init__(self, url: str):
        super().__init__(url)
    
    def scrape(self):
        """
            It will scrape a category in the archives
        """

        req = Tor.get_request(self.url)
        print(req.content)

    def save_as(self, data: bytes, filepath: str):
        """
            Saving file
        """

        with open(filepath, "w") as f:
            f.write(data)
