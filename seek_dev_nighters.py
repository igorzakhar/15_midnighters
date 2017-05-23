from datetime import datetime

import requests
import pytz
import tqdm


def get_pages_count():
    url = 'https://devman.org/api/challenges/solution_attempts/'
    resp = requests.get(url)
    resp_dict = resp.json()
    page_count = resp_dict['number_of_pages']
    return page_count


def load_attempts(pages_count):
    url = 'https://devman.org/api/challenges/solution_attempts/'
    pages = pages_count
    pbar = tqdm.tqdm(range(1, pages + 1))
    for page in pbar:
    #for page in range(1, pages+1):
        query_str = '{}?page={}'.format(url, page)
        resp = requests.get(query_str)
        #print(resp.url)
        records = resp.json()['records']
        for record in records:
            yield record

"""
        # FIXME подключить загрузку данных из API

        yield {
            'username': 'bob',
            'timestamp': 0,
            'timezone': 'Europe/Moscow',
        }
"""
def get_midnighters():
    pages_count = get_pages_count()
    gen = load_attempts(pages_count)
    for item in gen:
        if item['timestamp']:
            time_zone = pytz.timezone(item['timezone'])
            date_time = datetime.fromtimestamp(item['timestamp'], time_zone)
            if (6 >= date_time.hour >= 0): 
                #print(date_time, item['username'])
                pass
           
if __name__ == '__main__':
        #pages_count = get_pages_count()
        #load_attempts(pages_count)
        print(get_midnighters())
