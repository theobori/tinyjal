"""main file"""

import requests

from typing import List
from stem import Signal
from sys import stderr, argv
from stem.control import Controller
from bs4 import BeautifulSoup

from fake_useragent import UserAgent

from exception import JALError

def check_args(ac: int, av: List[str]):
    """
        Handling CLI arguments
    """

    if ac != 1:
        raise JALError("Need only one argument")

class Tor:
    """
        This class acts like a namespace for features
        that use the tor network
    """

    PROXIES = {
        "http": "socks5h://localhost:9050",
        "https": "socks5h://localhost:9050"
    }

    def new_circuit():
        """
            Create a new circuit (new relays, exit and entry nodes)
        """

        with Controller.from_port(port = 9051) as controller:
            controller.authenticate(password="sh33sh")
            controller.signal(Signal.NEWNYM)

    def request(_type: callable, *args, **kwargs) -> object:
        """
            HTTP requests throught Tor
        """

        headers = { "User-Agent": UserAgent().random }

        print(headers)

        try:
            req = _type(
                *args, **kwargs,
                proxies=Tor.PROXIES,
                headers=headers
            )
            
            return req
        except:
            return None

    def get_request(url: str) -> str:
        """
            Simplest get request model
        """

        req = Tor.request(requests.get, url=url)

        return req

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

def main():

    av = argv[1:]
    ac = len(av)

    try:
        check_args(ac, av)
        jal = JAL(av[0])
        jal.scrape()
    except JALError as error:
        print(error, file=stderr)

if __name__ == "__main__":
    main()
