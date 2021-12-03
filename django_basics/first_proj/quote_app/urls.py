from django.urls import path
from quote_app.views import display_quote


urlpatterns = {
    path('quote/', display_quote),
}