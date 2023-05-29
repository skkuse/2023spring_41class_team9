from django.urls import path
from . import views

urlpatterns = [
    path('practice/', views.practice),
    path('real/', views.real)
]