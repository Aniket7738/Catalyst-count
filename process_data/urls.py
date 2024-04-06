from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login, name="login"),
    path("upload", views.upload, name="upload"),
    path('count-records', views.count_records, name='count_records'),
    path('user_list', views.user_list, name='user_list'),
    path('logout', views.logout, name='logout'),
]
