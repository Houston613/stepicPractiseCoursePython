import json
import requests

with open('dataset_24476_3.txt') as file:
    for number in file:
        number = number.strip()
        params = {
            'default': 'Boring number is boring',
            'json': True
        }
        url = 'http://numbersapi.com/{}/math'.format(number)
        result = requests.get(url, params=params).text
        loaded = json.loads(result)
        if 'Boring' in loaded['text']:
            print('Boring')
        else:
            print('Interesting')
