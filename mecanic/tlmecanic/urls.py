from django.urls import path
from .views import principal,regcliente

urlpatterns = [
    path('',principal,name='principal'),
    path('',principal,name='regcliente'),
]

