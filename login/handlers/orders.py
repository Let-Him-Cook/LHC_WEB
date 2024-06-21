import requests
from django.shortcuts import render

API_BASE_URL = 'https://lhcapi.azurewebsites.net/api'

def get_all_orders():
    url = API_BASE_URL + "/orders"
    response = requests.get(url)

    if response:
        try:
            orders = response.json()
            # print(f"Orders from API: {orders}")  # Processe cada pedido aqui
            return orders
        except Exception as e:
            print(f"Erro ao extrair dados dos pedidos: {e}")
            return None
    else:
        print("Falha ao recuperar pedidos.")
        return None

def order_list_view(request):
    orders = get_all_orders()

    if orders:
        order_details = []
        for order in orders:
            order_info = {
                'id': order.get('id'),
                'idClient': order.get('idClient'),
                'totalPrice': order.get('totalPrice'),
                'status': order.get('status'),
                'tableNumber': order.get('tableNumber'),
                'createdAt': order.get('createdAt'),
                'updatedAt': order.get('updatedAt')
            }
            order_details.append(order_info)

        return order_details
    else:
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
