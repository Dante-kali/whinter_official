from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def views(request):
    print("-" * 100)
    print("-" * 100)
    print(request.method)
    date = {
        'date' : "Welcome to the Aplication 'Whinter'"
    }
    return render(request, 'template1.html', date)


def search(request, name):
    print("-" * 100)
    print("-" * 100)
    print(request.method)
    name = {
        'name' : name
    }
    return render(request, 'template2.html', name)


def selection(request):
    print("-" * 100)
    print("-" * 100)
    print(request.method)
    
    
    selection = {
        'players': [
            {"nombre": "Emiliano Martínez ", "rol": "arquero"},
            {"nombre": "Nicolas Otamendi ", "rol": "defensor"},
            {"nombre": "Nahuel Molina ", "rol": "defensor"},
            {"nombre": "Gonzalo Montiel ", "rol": "defensor"},
            {"nombre": "Lisando Martinez ", "rol": "defensor"},
            {"nombre": "Angel di maria", "rol": "mediocampista"},
            {"nombre": "Julián Álvarez", "rol": "delantero"},
        ]
    }
    return render(request, 'template3.html', selection)


from .models import Booking

def create(request, name, service):
    print("-" * 100)
    print("-" * 100)
    print(request.method)
    booking = Booking(name, service)
    return HttpResponse(f'the booking {booking}')