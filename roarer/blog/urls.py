from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    url(r'^register/', views.register, name='register'),
]