import requests


def get_pages_count():
    url = 'https://devman.org/api/challenges/solution_attempts/'
    resp = requests.get(url)
    resp_dict = resp.json()
    page_count = resp_dict['number_of_pages']
    return page_count


def load_attempts(pages_count):
    url = 'https://devman.org/api/challenges/solution_attempts/'
    pages = pages_count
    for page in range(1, pages+1):
        query_str = '{}?page={}'.format(url, page)
        resp = requests.get(query_str)
        print(resp.url)
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
    pass

if __name__ == '__main__':
        pages_count = get_pages_count()
        load_attempts(pages_count)
