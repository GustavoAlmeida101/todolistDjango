from django.contrib import admin
from django.urls import path
from .views import home,salvar,excluir

urlpatterns = [
    path('',home),
    path('salvar/',salvar ,name='salvar'),
    path('excluir/<int:id>',excluir ,name='excluir')
]
