from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
