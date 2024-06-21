import requests
from django.shortcuts import render
from datetime import datetime, timedelta

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

from datetime import datetime

def order_list_view(request):
    orders = get_all_orders()

    if orders:
        order_details = []
        current_datetime = datetime.now()

        for order in orders:
            # Converter createdAt para datetime
            created_at = order.get('createdAt')
            created_at_datetime = datetime.fromisoformat(created_at)

            # Calcular a diferença de tempo
            time_difference = current_datetime - created_at_datetime

            # Formatar a diferença para horas e minutos
            hours = time_difference // timedelta(hours=1)
            minutes = (time_difference // timedelta(minutes=1)) % 60

            # Montar o dicionário com os detalhes do pedido
            order_info = {
                'id': order.get('id'),
                'idClient': order.get('idClient'),
                'totalPrice': order.get('totalPrice'),
                'status': order.get('status'),
                'tableNumber': order.get('tableNumber'),
                'createdAt': created_at_datetime,  # Manter o objeto datetime para outros usos
                'updatedAt': order.get('updatedAt'),
                'timeDifference': f"{hours:02}h{minutes:02}min"  # Formatar horas e minutos
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
