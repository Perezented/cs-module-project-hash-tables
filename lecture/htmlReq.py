"""Command line program that repeatedly accepts URL as input, and prints out the HTML data as output.
 """
import datetime
import urllib.request


class CacheEntry:
    def __init__(self, url, data):
        self.url = url
        self.data = data
        self.timestamp = datetime.datetime.now().timestamp()


cache = {}
TIMEOUT_SECONDS = 15
while True:
    url = input(('Enter a URL: '))
    if url == 'exit':
        break

    needs_refresh = False

    cur_time = datetime.datetime.now().timestamp()

    if url not in cache:
        print('CACHE MISS')
        needs_refresh = True

    else:
        cur_time = datetime.datetime.now().timestamp()
        diff_time = cur_time - cache[url].timestamp

        # if diff_time > TIMEOUT_SECONDS:
        #     needs_refresh = True
        needs_refresh = diff_time > TIMEOUT_SECONDS

    if needs_refresh:

        resp = urllib.request.urlopen(url)

        data = resp.read()

        cache[url] = CacheEntry(url, data)
    else:
        print('CACHE HIT')
    print(cache[url])
