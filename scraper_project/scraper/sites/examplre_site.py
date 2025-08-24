from scraper.base import BaseScraper
from utils.concurrency import fetch_all
from typing import List, Dict
import asyncio


class ExampleSiteScraper(BaseScraper):
    """
    Example scraper that fetches data from multiple URLs.
    """

    def __init__(self, urls: List[str]):
        self.urls = urls

    async def fetch_data(self) -> List[Dict]:
        """
        Uses the concurrency helper to fetch multiple URLs.
        """
        raw_data_list = await fetch_all(self.urls) #list of data of all urls
        return [self.parse_data(raw) for raw in raw_data_list]# making a list of
                        #parsed data of all urls

    def parse_data(self, raw_data: str) -> Dict:
        """
        Dummy parser - here we'll just count the number of words.
        """
        return {"file 1": raw_data}
