import requests
from getpass import getpass
import pandas as pd
import json
api_url = "https://suap.ifrn.edu.br/api/"

password = getpass("Senha: ")
user = '20191181110005'

data = {"username":user,"password":password}

response = requests.post(api_url+"v2/autenticacao/token/", json=data)
token = response.json()["access"]

headers = {
    
    "Authorization": f'Bearer {token}'
}
r = requests.get(api_url + "/v2/minhas-informacoes/boletim/2022/1/", json=data, headers=headers)

data = json.loads(r.text)
df = pd.DataFrame(data)

print(df)