"""tor module"""

import requests

from time import sleep
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller

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

            print("Tor new circuit")

    def daemon_circuit(n: float):
        """
            New circuit every n seconds
        """

        while 1:
            Tor.new_circuit()
            sleep(n)

    def request(_type: callable, *args, **kwargs) -> object:
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

        req = Tor.request(requests.get, url=url)

        return req
