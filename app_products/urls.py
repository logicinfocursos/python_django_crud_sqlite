#from django.contrib import admin
from django.urls import path, include
from .views import home, add, edit, update, delete

urlpatterns = [
    path('', home),
    path('add/', add, name='add'),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]
