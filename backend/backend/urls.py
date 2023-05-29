from django.contrib import admin
from django.urls import include, path
from user.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('board/', include('board.urls')),
    path('', home)
]
