from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('callapi/', views.callApi, name="callapi"),
    path('students/', views.ListStudents.as_view(), name="student"),

]

























  # path('home/', views.home, name="home"),
    # path('case1/', views.case1_func, name="case1"),
    # path('case2/', views.case2_func, name="case2"),
    # path('case2_2/', views.case2_func_part2, name="case2_2"),
    # path('case3/', views.case3_func, name="case3"),
    # path('case4/', views.case4_func, name="case4"),
    # path('case6/', views.case6_func, name="case6"),
    # path('case7/', views.case7_func, name="case7"),
    # path('case9/', views.case9_func, name="case9"),
    # path('case10/', views.case10_func, name="case10"),

    # path('race/', views.database_race, name="race"),