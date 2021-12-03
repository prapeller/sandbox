from django.urls import path

from first_app.views import display, display_datetime

urlpatterns = {
    path('hello/', display),
    path('datetime/', display_datetime),
}
