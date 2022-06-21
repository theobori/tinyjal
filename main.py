"""main file"""

from typing import List
from sys import stderr, argv
from bs4 import BeautifulSoup

from src.exception import JALError
from src.websites.jal import JAL

def check_args(ac: int, av: List[str]):
    """
        Handling CLI arguments
    """

    if ac != 1:
        raise JALError("Need only one argument")
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
