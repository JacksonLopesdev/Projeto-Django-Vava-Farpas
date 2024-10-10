from django.urls import path
from .views import gerar_arte

urlpatterns = [
    path('', gerar_arte, name='gerar_arte'),
]