from datetime import time, datetime

import requests
import pytz

URL_API = 'https://devman.org/api/challenges/solution_attempts/'


def get_number_of_pages():
    resp = requests.get(URL_API)
    resp_dict = resp.json()
    number_of_pages = resp_dict['number_of_pages']
    return number_of_pages


def load_attempts(number_of_pages):
    for page_number in range(1, number_of_pages + 1):
        payload = {'page': str(page_number)}
        resp = requests.get(URL_API, params=payload)
        records = resp.json()['records']
        for record in records:
            yield record


def get_midnighters(records):
    start_time = time(0, 0)
    end_time = time(6, 0)
    midnighters = set()
    for item in records:
        time_zone = pytz.timezone(item['timezone'])
        local_datetime = datetime.fromtimestamp(item['timestamp'], time_zone)
        if (end_time >= local_datetime.time() >= start_time):
            midnighters.add(item['username'])
    return midnighters


def print_output(content):
    print("Users, who have sent a solution after 00-00:")
    for item in content:
        print(item)


def main():
    number_of_pages = get_number_of_pages()
    content = load_attempts(number_of_pages)
    midnighters = get_midnighters(content)
    print_output(midnighters)


if __name__ == '__main__':
    main()
