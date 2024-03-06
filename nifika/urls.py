from django.urls import path
from . import views

urlpatterns = [
    path('', views.nifika, name='nifika'),
]
