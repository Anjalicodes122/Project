
from django.contrib import admin
from django.urls import path
from .views import registration,login,dashboard,all_user

urlpatterns = [
    path('', all_user),
    path('registration/', registration),
    path('login/', login),
    path('dashboard/', dashboard)
]
