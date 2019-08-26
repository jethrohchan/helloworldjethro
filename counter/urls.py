from django.urls import path
from . import views

urlpatterns = [
    path('', views.counter_home, name='counter_home'),
]
