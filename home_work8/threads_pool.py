import concurrent.futures
import requests
from time import time


def get_request(url: str) -> None:
    t = time()
    response = requests.get(url)
    print(f"Resource '{url}' request took some {'%.3f' % (time() - t)} sec,"
          f" response status - {response.status_code}")


if __name__ == '__main__':
    with open('urls.txt', 'r') as file:
        urls = (line.strip('",\n') for line in file.readlines())

    start = time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as worker:
        worker.map(get_request, urls)

    print(f'\nFull fetching got {"%.3f" % (time() - start)} seconds.')
