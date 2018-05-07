import datetime
import json
import random

import requests


class Transaction:
    def __init__(self, source:str, source_username:str,  dest:str, dest_username:str, message:str, time_created:str):
        self.source = source
        self.source_username = source_username
        self.dest = dest
        self.dest_username = dest_username
        self.message = message
        self.time_create = time_created


def add_data(records_to_add: list, data: dict) -> dict:
    for item in records_to_add:
        source_id = item['actor']['id']
        source_username = item['actor']['username']
        message = item['message']
        time_created = item['created_time']
        for transaction in item['transactions']:
            if 'target' not in transaction:
                continue
            if 'id' not in transaction['target']:
                continue
            target_id = transaction['target']['id']
            target_username = transaction['target']['username']

            trans = Transaction(source_id, source_username, target_id, target_username, message, time_created)

            if source_id in data:
                data[source_id].append(trans.__dict__)
            else:
                data[source_id] = [trans.__dict__]

    return data


def save_data(data, itteration):
    with open('data_{}.json'.format(itteration), 'w') as f:
        json.dump(data, f, indent=4)
    return


def collect_hour_of_data(time: datetime):
    data = {}
    unix_time = int(time.timestamp())
    url = 'https://venmo.com/api/v5/public?until={}'.format(unix_time)

    for i in range(30):
        print("collecting batch: {}".format(i))
        r = requests.get(url)
        values = r.json()
        add_data(values.get('data'), data)

        url = values.get('paging').get('next')

    with open('data-{}.json'.format(time.strftime('%Y-%m-%dT%X')), 'w') as f:
        json.dump(data, f, indent=4)


def sample_time() -> int:
    return random.randint(8, 23)


def get_hour_per_day(day):
    return datetime.datetime(2018, 4, day, hour=sample_time())


def collect_lots_of_data():
    for day in range(1, 31):
        time = get_hour_per_day(day)
        collect_hour_of_data(time)


def collect_data():
    data = {}
    url = 'https://venmo.com/api/v5/public?since=1525132800'
    may1 = 1525132800
    april1 = 1525132680

    for i in range(21600):
        print("collecting batch: {}".format(i))
        # url = base_url.format(since, until)
        r = requests.get(url)
        values = r.json()
        add_data(values.get('data'), data)

        url = values.get('paging').get('next')
        # until -= 120
        # since -= 120

        if i % 1000 == 0:
            save_data(data, i)

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    # collect_data()
    collect_lots_of_data()
