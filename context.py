import contextlib
import datetime
import os
from os.path import join

def transform_file_in_dicts(file_path):
    olympic_countries = {}
    with open(file_path) as file:
        olympic_cities_list = []
        country_list = []
        temp_list = []
        for line in file:
            city_dict = {}
            line = line.strip()
            game = line.split('\t')
            # print(game)
            city_dict['страна'] = game[1]
            city_dict['город'] = game[0]
            city_dict['год'] = game[7]
            city_dict['тип игр'] = game[6]
            olympic_cities_list.append(city_dict)
            city_dict = {}
        for city in olympic_cities_list:
            country = city['страна']
            del city['страна']
            if country not in temp_list:
                olympic_countries[country] = [city]
            else:
                olympic_countries[country] = olympic_countries[country] + [city]
            temp_list.append(country)
    print(olympic_countries)
    return olympic_countries

def olympics_in_country(country_input, type):
    olympic_countries = transform_file_in_dicts(join('input', 'olympic_games'))
    type = type.capitalize()
    counter = 0
    for country, game in olympic_countries.items():
        # print(country)
        if country == country_input:
            for i in game:
                if i['тип игр'] == type:
                    counter += 1
    if counter > 0:
        print(f'{type} олимпийские игры проходили в {country_input} {counter} раз с 1980 года')
    else:
        print(f'{type} олимпийские игры не проходили в {country_input} с 1980 года')


@contextlib.contextmanager
def start_code():
    try:
        start_time = datetime.datetime.now()
        yield
    finally:
        close_time = datetime.datetime.now()
        execution_time = close_time - start_time
        print(f'Время начала выполнения: {start_time}')
        print(f'Время завершения выполнения: {close_time}')
        print(f'Время выполнения программы: {execution_time}')


if __name__ == '__main__':
    with start_code():
        olympics_in_country('США', 'Зимние')


# Словарь со структурой: {США:[{'город': , 'год': ,'тип игр': }]}
# Сколько зимних олимпийских игр проходило в США?





