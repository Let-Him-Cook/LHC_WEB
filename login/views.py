from django.http.response import HttpResponse
from django.shortcuts import render
from .handlers.login import authHand

def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authHand(login=username, password=senha)

        if user:
            return render(request, 'orderTable.html')
        else:
            return HttpResponse('Nome ou Senha errados')


def pedidos(request):
    return render(request, 'orderTable.html')
