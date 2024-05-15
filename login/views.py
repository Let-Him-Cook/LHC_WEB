from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def pedidos(request):
    return render(request, 'orderTable.html')
