import requests
import os

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
DISC_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
TOKEN = 'AgAAAAAknGUZAADLW-vBDmDdu09ji0Q-K9B-UiI'


def readfile(filename):
    with open(os.path.join('input', filename), 'r', encoding='utf-8') as readfile:
        text = readfile.readlines()
    return text


def writefile(filename, text):
    with open(os.path.join('output', filename), 'w') as writefile:
        for line in text:
            writefile.write(line)
    return None


def yadiskupload(output_filename, text):
    path = os.path.join('/translate', output_filename)
    params = {
        'path': path,
        'overwrite': True
    }
    headers = {
        'Authorization': TOKEN
    }
    response = requests.get(DISC_URL, headers=headers, params=params)
    json_ = response.json()
    href = json_['href']
    response = requests.put(href, text)
    return None


def translate_it(from_lang, input_filename, output_filename, to_lang='ru', yadisk=False):
    text = readfile(input_filename)
    lang = f'{from_lang}-{to_lang}'

    params = {
        'key': API_KEY,
        'text': text,
        'lang': lang
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    text = ''.join(json_['text'])
    if yadisk:
        text_to_send = text.encode('utf-8')
        yadiskupload(output_filename, text_to_send)
    else:
        writefile(output_filename,text)
    return None

if __name__ == '__main__':
    print(translate_it('fr', 'FR.txt', 'translated.txt'))
