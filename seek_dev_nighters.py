from datetime import datetime

import requests
import pytz

URL_API = 'https://devman.org/api/challenges/solution_attempts/'


def get_number_of_pages():
    resp = requests.get(URL_API)
    resp_dict = resp.json()
    page_count = resp_dict['number_of_pages']
    return page_count


def load_attempts(number_of_pages):
    for page in range(1, number_of_pages + 1):
        query_str = '{}?page={}'.format(URL_API, page)
        resp = requests.get(query_str)
        records = resp.json()['records']
        for record in records:
            yield record


def get_midnighters(load_attempts):
    midnighters = set()
    for item in load_attempts:
        time_zone = pytz.timezone(item['timezone'])
        local_datetime = datetime.fromtimestamp(item['timestamp'], time_zone)
        if (5 >= local_datetime.hour >= 0):
            midnighters.add(item['username'])
    return midnighters


def main():
    number_of_pages = get_number_of_pages()
    attempts = load_attempts(number_of_pages)
    midnighters = get_midnighters(attempts)
    print(midnighters)


if __name__ == '__main__':
    main()
