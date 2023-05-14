#!/usr/bin/env python

"""Just Another Library scraping"""

import requests
import os
import re

from typing import List
from sys import stderr, argv
from threading import Thread
from time import sleep

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller

class Tor:
    """
        This class acts like a namespace for features
        that use the tor network
    """
    
    CONTROLLER_PORT = int(os.environ.get("CONTROLLER_PORT")) or 9051
    CONTROLLER_PASSWORD = os.environ.get("CONTROLLER_PASSWORD")

    PROXIES = {
        "http": "socks5h://localhost:9050",
        "https": "socks5h://localhost:9050"
    }

    def new_circuit():
        """
            Create a new circuit (new relays, exit and entry nodes)
        """

        with Controller.from_port(port=Tor.CONTROLLER_PORT) as controller:
            controller.authenticate(password=Tor.CONTROLLER_PASSWORD)
            controller.signal(Signal.NEWNYM)

            print("[+] Tor new circuit")

    def daemon_circuit(n: float):
        """
            New circuit every n seconds
        """

        while 1:
            Tor.new_circuit()
            sleep(n)

    def __request(_type: callable, *args, **kwargs) -> object:
        """
            HTTP requests throught Tor
        """

        headers = { "User-Agent": UserAgent().random }

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

        req = Tor.__request(requests.get, url=url)

        return req

class ScrapeError(Exception):
    """
        Exception raised for errors on the scraper
    """

    def __init__(self, message: str = ""):
        self.message = message

        super().__init__(self.message)

    def __str__(self):
        return self.message


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

        raise ScrapeError("Not implemented")


class JAL(Scrape):
    """
        This object manages the 'Just Another Library'
        hidden service
    """

    CATEGORY_RE = re.compile(r"(<a href.*>)(.*)(</a>)")
    SIZE_RE = re.compile(r"(<td class=\"size\">)(.*?)(</td>)")
    DATE_RE = re.compile(r"(<td class=\"date\">)(.*?)(</td>)")

    def __init__(self, url: str, localdir: str):
        super().__init__(url)

        self.localdir = localdir
    
    def __is_dir(self, name: str, size: str, date: str) -> bool:
        """
            Tells if the category is a directory
        """

        if len(name) == 0:
            return False
    
        return size == "-" and date != "-" and name[-1] == "/"

    def __is_file(self, name: str, size: str, date: str) -> bool:
        """
            Tells if the category is a file
        """

        if len(name) == 0:
            return False

        return size != "-" and date != "-" and name[-1] != "/"

    def download_file(self, url: str, path: str) -> bool:
        """
            Download a file
        """
    
        if os.path.exists(path):
            print("[Cache]", path, sep="    ")
            return False
        
        img = Tor.get_request(url)
        self.save_as(img.content, path)
        return True

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

            file_url = url + "/" + name
            dest_dir = self.localdir + "/" + endpoint_dir

            os.makedirs(dest_dir, exist_ok=True)
            if self.__is_dir(name, size, date):
                self.scrape(file_url)
    
            if self.__is_file(name, size, date):
                localpath = dest_dir + name
                if self.download_file(file_url, localpath):
                    print("[+]", endpoint_dir, name, size, sep="    ")

    def save_as(self, data: bytes, filepath: str):
        """
            Saving file
        """

        with open(filepath, "wb+") as f:
            f.write(data)

def check_args(ac: int, av: List[str]):
    """
        Handling CLI arguments
    """

    if ac != 2:
        raise ScrapeError("Need only two arguments")

def main():
    av = argv[1:]
    ac = len(av)

    try:
        check_args(ac, av)

        circuit = Thread(target=Tor.daemon_circuit, args=(60 * 10,))
        circuit.daemon = True
        circuit.start()

        jal = JAL(*av)
        jal.scrape()
    except ScrapeError as error:
        print(error, file=stderr)
        exit(1)

if __name__ == "__main__":
    main()
