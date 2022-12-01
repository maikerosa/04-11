import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

username = 'maikerosa'
token = ''

response = requests.get(f'https://api.github.com/users/maikerosa/following/maikerosa', auth=HTTPBasicAuth(username, token))


print(response.status_code)
