from django.shortcuts import render


def index(request):
    return render(request, 'products_app/index.html')


def electronics(request):
    context = {
        'product1': 'mac',
        'product2': 'asus',
        'product3': 'dell',
        'product1_img':'images/electronics/1.jpg',
        'product2_img':'images/electronics/2.jpg',
        'product3_img':'images/electronics/3.jpg',
    }
    return render(request, 'products_app/products.html', context=context)


def toys(request):
    context = {
        'product1': 'Car',
        'product2': 'Drone',
        'product3': 'Rocket Launcher',
        'product1_img':'images/toys/1.jpg',
        'product2_img':'images/toys/2.jpg',
        'product3_img':'images/toys/3.jpg',
    }
    return render(request, 'products_app/products.html', context=context)


def shoes(request):
    context = {
        'product1': 'Nike',
        'product2': 'Adidas',
        'product3': 'Reebok',
        'product1_img':'images/shoes/1.jpg',
        'product2_img':'images/shoes/2.jpg',
        'product3_img':'images/shoes/3.jpg',
    }
    return render(request, 'products_app/products.html', context=context)
