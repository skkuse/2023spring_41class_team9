from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [


    path('problems', ProblemAPI.as_view()),

]