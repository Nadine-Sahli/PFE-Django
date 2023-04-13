from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('login/', views.logine, name="login"),
    path('maps/', views.add_node, name='add_node'),
    path('interface/', views.interface, name='interface'),
]
