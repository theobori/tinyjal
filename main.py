"""main file"""

from typing import List
from sys import stderr, argv
from threading import Thread

from src.exception import JALError
from src.websites.jal import JAL
from src.tor import Tor

def check_args(ac: int, av: List[str]):
    """
        Handling CLI arguments
    """

    if ac != 2:
        raise JALError("Need only two arguments")
def main():

    av = argv[1:]
    ac = len(av)

    try:
        check_args(ac, av)

        circuit = Thread(target=Tor.daemon_circuit, args=(60 * 3,))
        circuit.start()

        jal = JAL(*av)
        jal.scrape()
    except JALError as error:
        print(error, file=stderr)

if __name__ == "__main__":
    main()
