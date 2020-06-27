import requests
import time
from pprint import pprint

TOKEN = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'


class User:
    def __init__(self, user, token: str =TOKEN) -> None:
        self.token = token
        self.user = user


    def get_uid(self):
        user = self.user
        params = {
            'user_ids': user,
            'access_token': self.token,
            'v': 5.89
        }
        response = requests.get('https://api.vk.com/method/users.get', params)
        user_id = response.json()['response'][0]['id']
        return user_id 


    def get_groups(self):
        user = self.get_uid()
        time.sleep(0.34)
        params = {
            'user_id': user,
            'access_token': self.token,
            'v': 5.89
        }
        response = requests.get('https://api.vk.com/method/users.getSubscriptions', params)
        json_ = response.json()
        # print(json_)
        list_of_groups = []
        try:
            list_of_groups = response.json()['response']['groups']['items']
        except KeyError as e:
            print(f'У пользователя {user} скрыт, заблокирован или удален профиль')
        return list_of_groups


    def get_friends(self):
        user = self.get_uid()
        params = {
            'user_id': user,
            'access_token': self.token,
            'v': 5.89
        }
        response = requests.get('https://api.vk.com/method/friends.get', params)
        # print(response.json())
        list_of_friends = response.json()['response']['items']
        friends = []
        for uid in list_of_friends:
            uid = User(uid, TOKEN)
            friends.append(uid)
        return friends


    def make_set_of_friends_groups(self):
        friends = self.get_friends()
        list_of_groups = []
        for friend in friends:
            time.sleep(0.34)
            print('.')
            friend_groups = friend.get_groups()
            list_of_groups.extend(friend_groups)
        groups = set(list_of_groups)
        return groups


    def compare_groups(self):
        user_groups = self.get_groups()
        user_groups = set(user_groups)
        friends_groups = self.make_set_of_friends_groups()
        spy_groups = user_groups.difference(friends_groups)
        return spy_groups


    def get_spy_groups(self):
        groups = self.compare_groups()
        time.sleep(0.34)
        groups = list(groups)
        for i, item in enumerate(groups):
            groups[i] = str(item)
        print(groups)
        groups = ','.join(groups)
        # print(groups)
        params = {
            'group_ids': groups,
            'fields': 'members_count',
            'access_token': self.token,
            'v': 5.89
        }
        print('.')
        response = requests.get('https://api.vk.com/method/groups.getById', params)
        json_ = response.json()
        group_info_list = []
        for item in json_['response']:
            # pprint(item)
            group_info = {}
            group_info['name'] = item['name']
            group_info['gid'] = item['id']
            group_info['members_count'] = item['members_count']
            group_info_list.append(group_info)
        pprint(group_info_list)
        return group_info_list

            
                
user1 = User('eshmargunov')
user1.get_spy_groups()

