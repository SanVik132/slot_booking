from django.urls import path,include
from api.views import get_slot


urlpatterns = [
    path('get_slot/', get_slot, name="get_slot"),
    
]