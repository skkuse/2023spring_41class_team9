from django.urls import path
from . import views

urlpatterns = [
    path('practice/', views.practice),
    path('real/', views.real),
    path('practice/practice_mode_start/<int:id>', views.practice_start, name='problem-view'),
]