from django.shortcuts import render, redirect

from session_app.forms import ItemForm


def index(request):
    raise Exception('message from raised exception')
    return render(request, 'session_app/index.html')


def index_with_counter(request):
    count = request.session.get('count', 0)
    count += 1
    request.session['count'] = count

    context = {
        'count': count
    }
    return render(request, 'session_app/index.html', context)


def shopping_cart(request):
    return render(request, 'session_app/shopping_cart.html')


def add_item(request):
    form = ItemForm()

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            qty = form.cleaned_data.get('qty')
            request.session[name] = qty
            return redirect('/add-item')

    context = {
        'form': form
    }
    return render(request, 'session_app/add_item.html', context)
