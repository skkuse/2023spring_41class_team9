from django.urls import path
from . import views
# app_name = 'board'


urlpatterns = [
    path('practice/', views.practice),
    path('real/', views.real),
    path('practice/practice_mode_start/<int:id>', views.practice_start, name='problem-view'),
    path('real/real_mode_start/<int:id>', views.real_start, name='problem-view2'),
    path('review/', views.review),
    path('review_mode/', views.review_mode),
    
]
