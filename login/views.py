from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            return render(request, 'orderTable.html')
        else:
            return HttpResponse('Nome ou Senha errados')


def pedidos(request):
    return render(request, 'orderTable.html')
