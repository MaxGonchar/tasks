import asyncio
import aiohttp
from time import time


async def get_request(url: str) -> None:
    t = time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Resource '{url}' request took some {'%.3f' % (time() - t)} sec,"
                  f" response status - {response.status}")


if __name__ == '__main__':

    with open('urls.txt', 'r') as file:
        urls = (line.strip('",\n') for line in file.readlines())

    start = time()

    loop = asyncio.get_event_loop()

    tasks = [get_request(url) for url in urls]
    loop.run_until_complete(asyncio.gather(*tasks))

    loop.close()

    print(f'\nFull fetching got {"%.3f" % (time() - start)} seconds.')
