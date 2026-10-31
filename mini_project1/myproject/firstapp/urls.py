
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.all_project, name = "project"),
    path('projects/<int:id>/', views.get_project_detail, name='project_detail'),
    path('pricing/', views.pricing, name='pricing'),
    path('expirience/', views.expirience, name='expirience'),
    path('about/', views.about, name='about'),
    path('skill/', views.skill, name='skill'),
]

