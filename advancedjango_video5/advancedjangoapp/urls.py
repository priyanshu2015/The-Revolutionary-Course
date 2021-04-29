from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('callapi/', views.callApi, name="callapi"),
    path('students/', views.ListStudents.as_view(), name="student"),
    path('run/', views.runafterresponse, name="run"),

]


















