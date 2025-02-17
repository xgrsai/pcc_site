"""Defines URL patterns for accounts."""
from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
 # Include default auth urls.
 path('', include('django.contrib.auth.urls')), #Django автоматично додає всі URL-адреси, які потрібні для роботи системи аутентифікації (напр вхід вихід забув_пароль тощо)
 # Registration page.
 path('register/', views.register, name='register'),
]