import requests
from pprint import pprint
from urllib.parse import urlencode

OAUTH_URL = 'https://oauth.vk.com/authorize'

OAUTH_PARAMS = {
    'client_id': 7515381,
    'display': 'page',
    'scope': 'video,status,friends',
    'response_type': 'token',
    'v': 5.89
}

# print('?'.join((OAUTH_URL, urlencode(OAUTH_PARAMS))))

TOKEN = 'a1bf69a83bfe3a7967c43bab8791cbea23809b8cb7657eecf52b7a79bd04fde51281b321ec8a3746b8bcc'
URL = 'https://vk.com/'


class User():
    def __init__(self, user, token: str) -> None:
        self.token = token
        self.user = user


    def get_uid(self, user):
        params = {
            'user_ids': user,
            'access_token': self.token,
            'v': 5.89
        }
        response = requests.get('https://api.vk.com/method/users.get', params)
        user_id = response.json()['response'][0]['id']
        return user_id


    def __and__(self, other_user):
        name_1 = self.__dict__['user']
        name_2 = other_user.__dict__['user']
        user_id_1 = self.get_uid(name_1)
        user_id_2 = self.get_uid(name_2)
        params = {
            'source_id': user_id_1,
            'target_uid': user_id_2,
            'access_token': self.token,
            'v': 5.89
        }
        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        uid_list = response.json()['response']
        friends_list = self.make_class(uid_list)
        return friends_list

    def make_class(self, uid_list):
        friends_list = []
        for uid in uid_list:
            uid = User(uid, TOKEN)
            friends_list.append(uid)
        return friends_list
    

    def make_url(self):
        uid = self.__dict__['user']
        url = ''.join((URL, uid))
        return url


user1 = User('hochufoamposite', TOKEN)
user2 = User('rozakutubaeva', TOKEN)

mutual = user1 & user2
print(mutual)
# print(user1.make_url())
