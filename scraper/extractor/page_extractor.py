from abc import ABC, abstractmethod

class PageExtractor(ABC):
    def __init__(self, year: int, period: int, url: str):
        self.year = year
        self.period = period
        self.url = url

    @abstractmethod
    def extract(self):
        pass