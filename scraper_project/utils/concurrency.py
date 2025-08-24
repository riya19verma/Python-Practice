# utils/concurrency.py

import asyncio
import aiohttp
from typing import List


async def fetch(session: aiohttp.ClientSession, url: str) -> str:
    """
    Fetches a single URL asynchronously.
    """
    async with session.get(url) as response:
        return await response.text()


async def fetch_all(urls: List[str]) -> List[str]:
    """
    Fetches multiple URLs concurrently.
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)
