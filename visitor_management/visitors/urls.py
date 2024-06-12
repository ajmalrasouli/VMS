# visitors/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.visitor_list, name='visitor_list'),
    path('sign_out/<int:visitor_id>/', views.sign_out_visitor, name='sign_out_visitor'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('profile/', views.profile, name='profile'),# Add this line
]

