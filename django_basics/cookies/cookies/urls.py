"""cookies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from cookies_app.views import set_test_cookie, get_test_cookie, index, index_with_counter, shopping_cart, add_item

urlpatterns = [
    path('admin/', admin.site.urls),

    path('set_test_cookie/', set_test_cookie),
    path('get_test_cookie/', get_test_cookie),

    path('', index),
    path('counter/', index_with_counter),

    path('shopping-cart/', shopping_cart),
    path('add-item/', add_item),
]
