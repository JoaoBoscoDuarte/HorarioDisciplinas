from abc import ABC, abstractclassmethod

class PageExtractor(ABC):
    def __init__(self, year, period, url):
        self.year = year
        self.period = period
        self.url = url
    
    @abstractclassmethod
    def extract(self):
        pass