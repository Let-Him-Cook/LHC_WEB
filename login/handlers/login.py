import requests

#Link para APIimport requests

API_BASE_URL = 'https://lhcapi.azurewebsites.net/api'

def get_all_orders():
    url = API_BASE_URL + "/orders"
    response = requests.get(url)
    print(f"GET {url}")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        try:
            orders = response.json()
            for order in orders:
                print(f"Detalhes do Pedido: {order}")  # Processe cada pedido aqui
            return orders
        except Exception as e:
            print(f"Erro ao extrair dados dos pedidos: {e}")
            return None
    else:
        print("Falha ao recuperar pedidos.")
        return None

def get_order_by_id(order_id):
    url = f"{API_BASE_URL}/orders/{order_id}"
    response = requests.get(url)
    print(f"GET {url}")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        try:
            order_details = response.json()
            return order_details
        except Exception as e:
            print(f"Erro ao extrair detalhes do pedido: {e}")
            return None
    else:
        print(f"Falha ao recuperar detalhes do pedido {order_id}.")
        return None

# Exemplo de uso
all_orders = get_all_orders()
if all_orders:
    print("Todos os pedidos:")
    for order in all_orders:
        print(order)
else:
    print("Falha ao recuperar pedidos.")

# Exemplo de uso para obter detalhes de um pedido específico
order_id = 123
order_details = get_order_by_id(order_id)
if order_details:
    print(f"Detalhes do pedido {order_id}:")
    print(order_details)
else:
    print(f"Falha ao recuperar detalhes do pedido {order_id}.")

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

