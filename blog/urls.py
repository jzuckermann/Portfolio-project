"""Portfolio URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('<int:entry_id>/', views.detailentry, name='detailentry'),
    path('possiblechange/', views.possiblechange, name='possiblechange'),
    path('About-Jonas-Zuckerman/', views.Aboutpage, name='Aboutpage'),
]
