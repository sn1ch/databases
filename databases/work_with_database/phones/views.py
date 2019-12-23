from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    template = 'catalog.html'
    land = request.GET.get('sort')
    items = []
    print(land)
    if land == 'min_price':
        for phone in Phone.objects.order_by('price'):
            item = {
                'name': phone.name,
                'price': phone.price,
                'img': phone.image,
                'slug': phone.slug
            }
            items.append(item)
    elif land == 'max_price':
        for phone in Phone.objects.order_by('-price'):
            item = {
                'name': phone.name,
                'price': phone.price,
                'img': phone.image,
                'slug': phone.slug
            }
            items.append(item)
    else:
        for phone in Phone.objects.all():
            item = {
                'name': phone.name,
                'price': phone.price,
                'img': phone.image,
                'slug': phone.slug
            }
            items.append(item)

    context = {'items': items}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug=slug)
    for phone in phones:
        item = {
            'name': phone.name,
            'price': phone.price,
            'img': phone.image,
            'releases_date': phone.releases_date,
            'lte_exists': phone.lte_exists
        }

    context = {'item': item}
    return render(request, template, context)
