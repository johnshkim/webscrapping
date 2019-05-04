from django.urls import path
from .views import home
from .views import add

urlpatterns = [
    path('', home),
    path('add', add),
]