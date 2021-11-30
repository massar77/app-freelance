from . import views
from django.urls import path, include

urlpatterns = [
    path('login', views.login, name='login'),
    path('signin', views.signin, name='signin'),
]