from urllib.parse import urlencode
import requests
from pprint import pprint

# APP_ID = 7055854
# AUTH_URL = 'https://oauth.vk.com/authorize'
# AUTH_DATA = {
#     "client_id": APP_ID,
#     "display":'page',
#     "scope":'friends',
#     "response_type":'token'
# }
#
#
# print('?'.join((AUTH_URL, urlencode(AUTH_DATA))))
TOKEN = 'b004d77e0349a7b4c800b2b0b9f7472fe51c5f7ff9f3f26748c1f47c59c1e0246c8579e93dd094eb6c9a2'
ID_leysan = '4529854'
ID_vova = '663564'


class VK_user:
    def __init__(self,token,ID):
        self.token=token
        self.ID=ID

    def get_params(self):
        return{
            'access_token':self.token,
            'v':'5.52',
            'user_id': self.ID,
            'order':'hints',
            'name_case' :'nom',
            'ref' :'255',
            'fields' :'nickname'
        }

    def request(self,method,params):
        response = requests.get(
            'https://api.vk.com/method/'+method,
            params=params
        )
        return(response)
    def get_friends(self):
        params=self.get_params()
        response=self.request(
            'friends.get',
            params=params
        )
        dict_of_friends=response.json()['response']['items']
        list_of_friends=[]
        for friend in dict_of_friends:
            list_of_friends.append(friend['id'])
        return set(list_of_friends)

    def get_mutual_friends(self,ID):
        response = self.request('friends.getMutual',
                                params={
                                    'access_token':self.token,
                                    'v':'5.52',
                                    'source_uid':self.ID,
                                    'target_uid': ID})
        return(response.json())



leysan = VK_user(TOKEN,ID_leysan)
vova = VK_user(TOKEN,ID_vova)

pprint(vova.get_mutual_friends(leysan.ID))

mutual_friend_list=[]
for mutual_friend_ID in vova.get_friends()&leysan.get_friends():
   mutual_friend_list.append(VK_user(TOKEN, mutual_friend_ID))
pprint(mutual_friend_list)

def print(user):
    pprint('https://vk.com/id'+user.ID)

print(leysan)