import requests

API_BASE_URL = 'https://lhcapi.azurewebsites.net/api'

def authHand(login, password):
    url = API_BASE_URL + "/users/auth/web"
    payload = {
        'login': login,
        'password':  password
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        print("Erro:", response.status_code)

