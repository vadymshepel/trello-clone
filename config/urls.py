from django.contrib import admin
from django.urls import path, include
from importlib import import_module
from boards.views import home_view

try:
    jwt_views = import_module('rest_framework_simplejwt.views')
except ImportError:
    jwt_views = None

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('boards.urls')),
    
]

if jwt_views is not None:
    urlpatterns += [
        path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    ]
