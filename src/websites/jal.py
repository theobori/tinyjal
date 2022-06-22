"""jal module"""

from concurrent.futures import thread
from threading import Thread
import requests
import re
import os

from src.tor import Tor
from src.scrape import Scrape

from bs4 import BeautifulSoup

class JAL(Scrape):
    """
        This object manages the 'Just Another Library'
        category scraping
    """

    CATEGORY_RE = re.compile(r"(<a href.*>)(.*)(</a>)")
    SIZE_RE = re.compile(r"(<td class=\"size\">)(.*?)(</td>)")
    DATE_RE = re.compile(r"(<td class=\"date\">)(.*?)(</td>)")

    def __init__(self, url: str, localdir: str):
        super().__init__(url)

        self.localdir = localdir
    
    def is_dir(self, name: str, size: str, date: str) -> bool:
        """
            Tells if the category is a directory
        """

        if len(name) == 0:
            return False

        return size == "-" \
            and date != "-" \
            and name[-1] == "/"

    def is_file(self, name: str, size: str, date: str) -> bool:
        """
            Tells if the category is a file
        """

        if len(name) == 0:
            return False

        return size != "-" \
            and date != "-" \
            and name[-1] != "/"
    

    def scrape(self, url: str = None):
        """
            It will scrape a category in the archives
        """

        url = url or self.url

        req = Tor.get_request(url)
        soup = BeautifulSoup(req.content, "html.parser")

        endpoint_dir = url.split("/")[3:]
        endpoint_dir = "/".join(endpoint_dir).replace("//", "/")

        for category in soup.find_all("tr"):
            category = str(category)

            try:
                name = JAL.CATEGORY_RE.findall(category)[0][1]
                size = JAL.SIZE_RE.findall(category)[0][1]
                date = JAL.DATE_RE.findall(category)[0][1]
            except:
                continue

            file = url + "/" + name

            os.makedirs(self.localdir + endpoint_dir, exist_ok=True)
            if self.is_dir(name, size, date):
                self.scrape(file)
    
            if self.is_file(name, size, date):
                img = Tor.get_request(file)
                self.save_as(img.content, self.localdir + endpoint_dir + name)
                print("[+]", endpoint_dir, name, size, sep="    ")

    def save_as(self, data: bytes, filepath: str):
        """
            Saving file
        """

        with open(filepath, "wb+") as f:
            f.write(data)
