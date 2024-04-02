from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def selection(request):
    print("-" * 100)
    print("-" * 100)
    print(request.method)
    
    selection = {
        'players': [
            "Emiliano Martínez - Arquero",
            "Nicolas Otamendi - Defensor",
            "Nahuel Molina - Defensor",
            "Gonzalo Montiel - Defensor",
            "Lisando Martinez - Defensor",
            "Angel di maria - Mediocampista"
        ]
    }
    return render(request, 'template.html', selection)
    
def views(request):
    print("-" * 100)
    print("-" * 100)
    print(request.method)
    return HttpResponse("<h1>Hello, welcome to the aplication 'whinter'<h1>")

def search(request, name):
    print("-" * 100)
    print("-" * 100)
    print(request.method)
    return HttpResponse(f'<h3>searching information for the user: {name}</h3>') 