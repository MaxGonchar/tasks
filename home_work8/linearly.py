import requests
from time import time


with open('urls.txt', 'r') as file:
    urls = (line.strip('",\n') for line in file.readlines())
    total_time = 0
    for url in urls:
        t1 = time()
        response = requests.get(url)
        t2 = time()
        print(f"Resource '{url}' request took some {'%.3f' %(t2 - t1)} sec,"
              f" response status - {response.status_code}")
        total_time += (t2 - t1)

    print(f'\nFull fetching got {"%.3f" %total_time} seconds.')