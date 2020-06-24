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

TOKEN = 'df8c9d215dcd6dd0f01b44682ed1e42f3adea31af3b19f32d73f309fc85b97b8a96fb71457f9a6b4191a9'
URL = 'https://vk.com/'


class User():
    def __init__(self, user, token: str) -> None:
        self.token = token
        self.user = user

    def __str__(self):
        user = self.__dict__['user']
        if user.isdigit():
            shortname = self.get_shortname(user)
            url = ''.join((URL, shortname))
        else:
            shortname = self.__dict__['user']
            url = ''.join((URL, shortname))
        return url

    def get_uid(self, user):
        params = {
            'user_ids': user,
            'access_token': self.token,
            'v': 5.89
        }
        response = requests.get('https://api.vk.com/method/users.get', params)
        json_ = response.json()
        user_id = json_['response'][0]['id']
        return user_id

    def get_shortname(self, user):
        params = {
            'user_ids': user,
            'fields': 'screen_name',
            'access_token': self.token,
            'v': 5.89
        }
        response = requests.get('https://api.vk.com/method/users.get', params)
        json_ = response.json()
        shortname = json_['response'][0]['screen_name']
        return shortname


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

user1 = User('hochufoamposite', TOKEN)
user2 = User('rozakutubaeva', TOKEN)

mutual = user1 & user2
print(mutual)
print(user1)
print(user2)
