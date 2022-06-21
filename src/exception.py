"""exceptions system"""

class JALError(Exception):
    """
        Exception raised for errors on the scraper
    """

    def __init__(self, message: str = ""):
        self.message = message

        super().__init__(self.message)

    def __str__(self):
        return self.message
