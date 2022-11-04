import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

username = input('Digite o usuario para seguir: ')
token = ''

url = 'https://api.github.com/user/following/' + username
response = requests.put(url, auth=HTTPBasicAuth(username, token))

if response.status_code == 204:
    print('Usuario seguido com sucesso!')

