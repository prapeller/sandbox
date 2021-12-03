from django.http import HttpResponse
from django.shortcuts import render

from cookies_app.forms import ItemForm


def index(request):
    return render(request, 'cookies_app/index.html')


def index_with_counter(request):
    if 'count_cookie' in request.COOKIES:
        count = int(request.COOKIES.get('count_cookie')) + 1
    else:
        count = 1

    context = {
        'count': count
    }
    resp = render(request, 'cookies_app/index.html', context)
    resp.set_cookie('count_cookie', count)
    return resp


def set_test_cookie(request):
    request.session.set_test_cookie()
    return HttpResponse("<h2>Client browser just set test cookies to session. Go to \'get cookies\' page</h2>")


def get_test_cookie(request):
    if request.session.test_cookie_worked():
        print('cookies are enabled')
        request.session.delete_test_cookie()
    return HttpResponse('<h2>Check console to see if server sees test cookies in session dictionary!</h2>')


def shopping_cart(request):
    return render(request, 'cookies_app/shopping_cart.html')


def add_item(request):
    form = ItemForm()
    context = {
        'form': form
    }
    resp = render(request, 'cookies_app/add_item.html', context)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            qty = form.cleaned_data['qty']
            resp.set_cookie(name, qty , 5)

    return resp
