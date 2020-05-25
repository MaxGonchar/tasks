Сделать скрипт, который будет делать GET запросы на следующие ресурсы:
"http://docs.python-requests.org/",
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
"https://www.ietf.org/rfc/rfc2616.txt"

Для каждого запроса должен быть вывод по примеру: "Resource 'google.com.ua', request took 0.23 sec, response status - 200."
В реализации нет ограничений - можно использовать процессы, потоки, асинхронность. Любые вспомагательные механизмы типа Lock, Semaphore, пулы для тредов и потоков.

Главная цель - сделать чтобы код максимально быстро выполнился.

Пример листинга вывода программы:
Resource 'https://1.1.1.1/', request took some 0.039 sec, response status - 200
Resource 'https://www.politico.com/tipsheets/morning-money', request took some 0.072 sec, response status - 200
Resource 'https://www.ietf.org/rfc/rfc2616.txt', request took some 0.083 sec, response status - 200
Resource 'https://docs.python.org/3/this-url-will-404.html', request took some 0.100 sec, response status - 404
Resource 'https://www.python.org/', request took some 0.120 sec, response status - 200
Resource 'https://api.github.com/', request took some 0.144 sec, response status - 200
Resource 'https://www.google.com.ua/', request took some 0.155 sec, response status - 200
Resource 'https://www.mediamatters.org/', request took some 0.169 sec, response status - 200
Resource 'https://regex101.com/', request took some 0.213 sec, response status - 200
Resource 'https://www.nytimes.com/guides/', request took some 0.295 sec, response status - 200
Resource 'https://www.bloomberg.com/markets/economics', request took some 0.397 sec, response status - 200
Resource 'http://docs.python-requests.org/', request took some 0.470 sec, response status - 200
Resource 'https://example.com/', request took some 0.490 sec, response status - 200
Resource 'https://httpbin.org/get', request took some 0.543 sec, response status - 200
Resource 'https://httpbin.org/', request took some 0.560 sec, response status - 200

Full fetching got 0.564 seconds.

Process finished with exit code 0