from urllib.parse import urlencode
from pprint import pprint
import requests

OAUTH_URL = 'https://oauth.vk.com/authorize'

OAUTH_PARAMS = {
    'client_id': 7515381,
    'display': 'page',
    'scope': 'video,status',
    'response_type': 'token',
    'v': 5.89
}

# # print('?'.join((OAUTH_URL, urlencode(OAUTH_PARAMS))))

TOKEN = 'b8ce66f61a311ddcf5fc4c24a186bc881a283a5ea0d14336c76781de224acb242ae3247830135a14c005c'

# params = {
#     'access_token': TOKEN,
#     'v': 5.89
# }

# response = requests.get('https://api.vk.com/method/status.get', params)

# pprint(response.json())

class User:
    def __init__(self, token: str) -> None:
        self.token = token

    
    def get_params(self):
        return {
            'access_token': self.token,
            'v': 5.89
        }

    def get_status(self) -> str:
        params = self.get_params()
        response = requests.get('https://api.vk.com/method/status.get', params)
        return response.json()['response']['text']

daria = User(TOKEN)
print(daria.get_status())