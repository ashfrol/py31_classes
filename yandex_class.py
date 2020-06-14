import requests

url = "https://translate.yandex.net/api/v1/tr.json/translate"
params = {
    "id": "5fa92573.5ee51c02.ca901fc8-7-0",
    "srv": "tr-text",
    "lang": "ru-en"
}

text = "Во имя света!"

resp = requests.post(url, data={"text": text}, params=params)
print(resp)
print(resp.json())