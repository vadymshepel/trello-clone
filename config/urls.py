from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('admin/', permanent=False)),  # Временно перенаправляем корень на админку
]
