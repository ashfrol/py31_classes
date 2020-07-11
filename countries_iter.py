import requests
from os.path import join
import json

URL = "https://en.wikipedia.org/w/api.php"

class Wiki_Countries:

    def __init__(self, filename):
        self.country_list = self.get_countries_list(filename)
        self.end = len(self.country_list)
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start >= self.end:
            raise StopIteration
        country = self.country_list[self.start]
        link = self.get_url(country)
        pair = str(f'{country} - {link}')
        return pair

    def get_countries_list(self, filename):
        country_list = []
        with open(join('input', filename), 'r', encoding='utf-8') as file_read:
            countries_json = json.load(file_read)
            for item in countries_json:
                country_name = item['name']['common']
                country_name.lower()
                country_list.append(country_name)
        return country_list

    def get_url(self, country):
        params = {
            'action': 'opensearch',
            'search': country
        }
        response = requests.get(URL, params)
        url = response.json()[3][0]
        return url


def write_countries_in_file(filename, countries):
    with open(join('output', filename), 'w', encoding='utf-8') as file_write:
        for pair in countries:
            file_write.write(pair)
            file_write.write('\n')

write_countries_in_file('countrylink.txt', Wiki_Countries('countries.json'))