import requests
import os

# resp = requests.get("http://httpbin.org/get", params={'foo': 'bar'}, headers={'X-Test-Header': '100'})

url = 'https://reddit.com/r/gifs/top.json'
params = {"t": "day"}
headers = {'User-Agent': 'Netcourse'}

resp = requests.get(url, params=params, headers=headers)

resp_json = resp.json()
resp_data = resp_json["data"]
resp_children = resp_data["children"]

# print(resp)
# print(resp.status_code)
# print(resp.headers)
# print(resp.json())
# print(resp.text)

# print(resp_children)

total_len = len(resp_children)

for index, child in enumerate(resp_children, 1):
    print(f'Processing {index} / {total_len}')
    data = child["data"]
    filename = os.path.join("gifs_reddit", f'{data["name"]}.mp4')
    url = data["url"]
    if 'imgur' not in url:
        continue
    url = url.replace('.gifv', '.mp4')
    with open(filename, 'wb') as fw:
        file_resp = requests.get(url, stream=True)
        for chunk in file_resp:
            fw.write(chunk)
    # print(data["name"], data["url"])
    print(f'Saved {filename}')