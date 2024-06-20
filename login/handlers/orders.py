import requests

API_BASE_URL = 'https://lhcapi.azurewebsites.net/api'

def get_all_dishes():
    url = API_BASE_URL + "/dishes"
    response = requests.get(url)
    print(f"GET {url}")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        try:
            dishes = response.json()
            for dish in dishes:
                print(f"Detalhes do Prato: {dish}")  # Processe cada prato aqui
            return dishes
        except Exception as e:
            print(f"Erro ao extrair dados dos pratos: {e}")
            return None
    else:
        print("Falha ao recuperar pratos.")
        return None

def get_dish_by_id(dish_id):
    url = f"{API_BASE_URL}/dishes/{dish_id}"
    response = requests.get(url)
    print(f"GET {url}")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        try:
            dish_details = response.json()
            return dish_details
        except Exception as e:
            print(f"Erro ao extrair detalhes do prato: {e}")
            return None
    else:
        print(f"Falha ao recuperar detalhes do prato {dish_id}.")
        return None

# Exemplo de uso
all_dishes = get_all_dishes()
if all_dishes:
    print("Todos os pratos:")
    for dish in all_dishes:
        print(dish)
else:
    print("Falha ao recuperar pratos.")

# Exemplo de uso para obter detalhes de um prato específico
dish_id = 123
dish_details = get_dish_by_id(dish_id)
if dish_details:
    print(f"Detalhes do prato {dish_id}:")
    print(dish_details)
else:
    print(f"Falha ao recuperar detalhes do prato {dish_id}.")
