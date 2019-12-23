from django.shortcuts import render
from .models import Samsung, Apple, Phone


def show_catalog(request):
    template = 'catalog.html'
    items = []
    for phone in Samsung.objects.all().select_related('phone'):
        item = {
            'name': phone.phone.name,
            'price': phone.phone.price,
            'cpu': phone.phone.cpu,
            'ram': phone.phone.ram,
            'other': phone.other,
            'display': phone.phone.display
        }
        items.append(item)
    for phone in Apple.objects.all().select_related('phone'):
        item = {
            'name': phone.phone.name,
            'price': phone.phone.price,
            'cpu': phone.phone.cpu,
            'ram': phone.phone.ram,
            'other': phone.other,
            'display': phone.phone.display
        }
        items.append(item)
    context = {'items': items}
    return render(request, template, context)
