from datetime import time, datetime

import requests
import pytz


def load_attempts(url_api):
    page_number = 1
    while True:
        payload = {'page': page_number}
        response = requests.get(url_api, params=payload)
        records = response.json()['records']
        for record in records:
            yield record

        page_number += 1
        if page_number > response.json()['number_of_pages']:
            break


def get_midnighters(attempts):
    start_time = time(0, 0)
    end_time = time(6, 0)
    midnighters = set()
    for attempt in attempts:
        time_zone = pytz.timezone(attempt['timezone'])
        local_datetime = datetime.fromtimestamp(
            attempt['timestamp'],
            time_zone
        )
        if (end_time >= local_datetime.time() >= start_time):
            midnighters.add(attempt['username'])
    return midnighters


def print_output(midnighters):
    print("Users, who have sent a solution after 00-00:")
    for midnighter in midnighters:
        print(midnighter)


def main():
    url_api = 'https://devman.org/api/challenges/solution_attempts/'
    attempts = load_attempts(url_api)
    midnighters = get_midnighters(attempts)
    print_output(midnighters)


if __name__ == '__main__':
    main()
