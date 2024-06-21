from django.http.response import HttpResponse
from django.shortcuts import render
from .handlers.login import authHand
from .handlers.orders import order_list_view

def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authHand(login=username, password=senha)

        if user:
            return pedidos(request)
        else:
            return HttpResponse('Nome ou Senha errados')


def pedidos(request):
    orders = order_list_view(request)

    if orders is not None:  # Verifica se orders não é None ou vazio
        context = {
            'orders': orders,
        }
        return render(request, 'orderTable.html', context)
    else:
        return HttpResponse('Falha ao recuperar pedidos. Tente novamente mais tarde.')  
