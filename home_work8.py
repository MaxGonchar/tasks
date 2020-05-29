# coding: utf-8
import asyncio
import aiohttp
from time import time

URLS = ["http://docs.python-requests.org/",
        "https://httpbin.org/get",
        "https://httpbin.org/",
        "https://api.github.com/",
        "https://example.com/",
        "https://www.python.org/",
        "https://www.google.com.ua/",
        "https://regex101.com/",
        "https://docs.python.org/3/this-url-will-404.html",
        "https://www.nytimes.com/guides/",
        "https://www.mediamatters.org/",
        "https://1.1.1.1/",
        "https://www.politico.com/tipsheets/morning-money",
        "https://www.bloomberg.com/markets/economics",
        "https://www.ietf.org/rfc/rfc2616.txt"]


async def get_request(url: str) -> None:
    t = time()
    async with aiohttp.ClientSession() as session:
        # verify_ssl=False использую, т.к. имею конфликт с ssl
        async with session.get(url, verify_ssl=False) as response:
            print(f"Resource '{url}' "
                  f"request took some {'%.3f' % (time() - t)} sec,"
                  f" response status - {response.status}")


if __name__ == '__main__':

    start = time()

    loop = asyncio.get_event_loop()

    tasks = [get_request(url) for url in URLS]
    loop.run_until_complete(asyncio.gather(*tasks))

    print(f'\nFull fetching got {"%.3f" % (time() - start)} seconds.')
