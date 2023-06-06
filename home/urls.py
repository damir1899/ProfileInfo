from django.urls import path
from .views import index, add_index


urlpatterns = [
    path('', index, name = 'index'),
    path('add/', add_index)
]
