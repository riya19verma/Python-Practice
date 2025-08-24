# scraper/base.py

from abc import ABC, abstractmethod
from typing import List, Dict


class BaseScraper(ABC):
    # Abstract base class for all scrapers.
    @abstractmethod
    async def fetch_data(self) -> List[Dict]:
        # Abstract method to fetch data asynchronously
        pass

    @abstractmethod
    def parse_data(self, raw_data: str) -> Dict:
        # Abstract method to parse raw data.
        pass
