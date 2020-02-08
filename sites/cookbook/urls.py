from django.urls import path

from .views import CookView


app_name = 'cookbook'
urlpatterns = [
    path('what_can_i_cook/', CookView.as_view(), name='what-can-i-cook'),
]
