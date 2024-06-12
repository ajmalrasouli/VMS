# visitor_management/urls.py

from django.contrib import admin
from django.urls import path, include
from visitors.views import home, CustomLoginView, user_logout, RegisterView, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', user_logout, name='logout'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),  # Add this line
    path('visitors/', include('visitors.urls')),
]
