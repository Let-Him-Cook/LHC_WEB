import requests

# Link para API
API_BASE_URL = 'https://lhcapi.azurewebsites.net/api'

def get_all_clients():
    url = API_BASE_URL + "/clients"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_client_by_id(client_id):
    url = f"{API_BASE_URL}/clients/{client_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

# Testando as funções
if __name__ == "__main__":
    # Obtendo todos os clientes
    clients = get_all_clients()
    print("Todos os clientes:", clients)

    # Obtendo um cliente pelo ID (substitua 'client_id' pelo ID real de um cliente)
    client_id = '1f078e5b-48a6-46f6-a5b6-35c6cb7a38cf'
    client = get_client_by_id(client_id)
    print(f"Cliente com ID {client_id}:", client)
