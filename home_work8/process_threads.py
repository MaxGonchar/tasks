import concurrent.futures
import threading
import requests
from time import time
from math import ceil


def get_request(url: str) -> None:
    t = time()
    response = requests.get(url)
    print(f"Resource '{url}' request took some {'%.3f' % (time() - t)} sec,"
          f" response status - {response.status_code}")


def threads_pac(urls: list) -> None:
    threads = []
    for url in urls:
        thread = threading.Thread(target=get_request, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    with open('urls.txt', 'r') as file:
        urls = [line.strip('",\n') for line in file.readlines()]

    proc_numb = 4

    url_pacs = [urls[i * (ceil(len(urls) / proc_numb)):
                     (i + 1) * ceil((len(urls) / proc_numb))]
                for i in range(proc_numb)]

    start = time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=proc_numb) as worker:
        worker.map(threads_pac, url_pacs)

    print(f'\nFull fetching got {"%.3f" % (time() - start)} seconds.')
