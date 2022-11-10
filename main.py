import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

username = 'maikerosa'
token = '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'

response = requests.get(f'https://api.github.com/users/maikerosa/following/maikerosa', auth=HTTPBasicAuth(username, token))


print(response.status_code)