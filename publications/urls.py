from django.urls import path
from .views import publication_list

urlpatterns = [
    path('', publication_list, name='publications'),
]